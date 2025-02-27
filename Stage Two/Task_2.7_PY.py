#Task 2.7_Py
import pandas as pd
import seaborn as sns
from scipy.stats import ttest_ind
# Load dataset from the given URL
df = pd.read_csv("https://raw.githubusercontent.com/HackBio-Internship/public_datasets/main/R/nhanes.csv")
# Convert weight from kilograms to pounds
df['Weight_pounds'] = df['Weight'] * 2.2
df.replace("NA", pd.NA, inplace=True)  # Convert "NA" to NaN
# Replace fully empty rows and columns with 0
df.fillna(0, inplace=True)
df_cleaned = df
# Convert weight from kilograms to pounds
df_cleaned['Weight_pounds'] = df_cleaned ['Weight'] * 2.2
# Create histograms for BMI, Weight, Weight in pounds, and Age
sns.histplot(df_cleaned, x="BMI")
sns.histplot(df_cleaned, x="Weight")
sns.histplot(df_cleaned, x="Weight_pounds")
sns.histplot(df_cleaned, x="Age")
# Calculate and print the mean 60-second pulse rate
mean_pulse = df_cleaned['Pulse'].mean()
print(f"Mean 60-second pulse rate: {mean_pulse:.2f}")
# Determine and print the range (minimum and maximum) of diastolic blood pressure
bp_min = df_cleaned['BPDia'].min()
bp_max = df_cleaned['BPDia'].max()
print(f"Diastolic BP Range: {bp_min}-{bp_max}")
# Compute and print the variance and standard deviation of income
income_variance = df_cleaned['Income'].var()
income_std = df_cleaned['Income'].std()
print(f"Variance of Income: {income_variance:.2f}")
print(f"Standard Deviation of Income: {income_std:.2f}")
# Histogram for Weight vs Height, colored by Gender
sns.histplot(df_cleaned, x="Height", y="Weight", hue="Gender", bins=30)
# Histogram for Weight vs Height, colored by Diabetes
sns.histplot(df_cleaned, x="Height", y="Weight", hue="Diabetes", bins=30)
# Histogram for Weight vs Height, colored by Smoking Status
sns.histplot(df_cleaned, x="Height", y="Weight", hue="SmokingStatus", bins=30)
# Function to perform a t-test between two groups of a categorical variable
def perform_ttest(group_col, var_name):
    """
    Conducts an independent t-test between two groups of a categorical variable.
    - group_col: The categorical variable used for grouping.
    - var_name: The numerical variable to compare between the two groups.
    """
    # Get unique values in the categorical column
    unique_values = df_cleaned[group_col].unique()
    # Ensure it's a binary variable
    if len(unique_values) != 2:
        print(f"T-test for {var_name} between {group_col} groups: Not a binary categorical variable. Found {len(unique_values)} groups.")
        return
    # Extract data for each group
    group0 = df_cleaned[df_cleaned[group_col] == unique_values[0]][var_name]
    group1 = df_cleaned[df_cleaned[group_col] == unique_values[1]][var_name]
    # Remove zero or NaN values
    group0 = group0[group0 > 0]
    group1 = group1[group1 > 0]
    # Ensure each group has at least two valid data points
    if len(group0) < 2 or len(group1) < 2:
        print(f"T-test for {var_name} between {group_col} groups: Not enough valid data points.")
        return
    # Perform independent t-test assuming unequal variance
    t_stat, p_val = ttest_ind(group0, group1, equal_var=False)
    print(f"T-test for {var_name} between {group_col} groups: p-value = {p_val:.3f}")
    # Interpretation
    if p_val < 0.05:
        print(f"The difference in {var_name} between {group_col} groups is statistically significant.\n")
    else:
        print(f"The difference in {var_name} between {group_col} groups is not statistically significant.\n")
# Conduct t-tests for specified variable pairs
perform_ttest('Gender', 'Age')
perform_ttest('BMI', 'Diabetes')
perform_ttest('AlcoholYear', 'RelationshipStatus')
