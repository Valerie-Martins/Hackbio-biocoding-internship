#Task 2.1_Py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import math
from scipy import stats
# Load dataset
data_source = "https://raw.githubusercontent.com/HackBio-Internship/2025_project_collection/refs/heads/main/Python/Dataset/mcgc.tsv"
df = pd.read_csv(data_source, sep='\t')
# Define strains and their respective wild-type (WT) and mutant (MUT) groups
strain_groups = {
    "Strain 1": {"WT (+)": ["A1", "A3", "B1", "B3", "C1", "C3"], "MUT (-)": ["A2", "A4", "B2", "B4", "C2", "C4"]},
    "Strain 2": {"WT (+)": ["A5", "A7", "B5", "B7", "C5", "C7"], "MUT (-)": ["A6", "A8", "B6", "B8", "C6", "C8"]},
    "Strain 3": {"WT (+)": ["A9", "A11", "B9", "B11", "C9", "C11"], "MUT (-)": ["A10", "A12", "B10", "B12", "C10", "C12"]}
}
strain_data = []# Initialize an empty list to store reformatted data
# Loop through each strain and its associated WT/MUT groups
for strain, types in strain_groups.items():
    for strain_type, cols in types.items():# Iterate through WT and MUT categories
        for col in cols:# Iterate through column names in each category
            for i in range(len(df)):  # Loop through each row of the dataset to unpack values
                strain_data.append({
                    "Time": df.loc[i, "time"], # Extract time value
                    "OD600": df.loc[i, col], # Extract OD600 measurement
                    "Strain": strain, # Assign strain label
                    "Type": strain_type # Assign WT or MUT label
                })
# Convert the collected data into a DataFrame for easier analysis
df_new = pd.DataFrame(strain_data)
#theformula i used in stage1 to determine the time to reach carrying capacity. didnt work in this task.So i had to redefine it
# Create a scatter plot to visualize OD600 values over time
sns.scatterplot(data=df_new, x="Time", y="OD600", hue="Strain", style="Type")
# Create a box plot to visualize OD600 values over time
sns.boxplot(data=df_new, x="Strain", y="OD600", hue="Type")
carrying_capacity_times = {"WT (+)": [], "MUT (-)": []}
# Find carrying capacity time for each strain and type
for strain, types in strain_groups.items():
    for strain_type, cols in types.items():
        for col in cols:
            max_od600 = max(df[col])  # Find max OD600 value
            for i in range(len(df)):  # Loop through rows to find first occurrence of max OD600
                if df[col][i] == max_od600:
                    carrying_capacity_times[strain_type].append(df["time"][i])  # Store time value
                    break  # Stop once first max value is found
# Extract times for t-test
wt_times = carrying_capacity_times["WT (+)"]
mut_times = carrying_capacity_times["MUT (-)"]
# Perform independent t-test
t_stat, p_value = stats.ttest_ind(wt_times, mut_times, equal_var=False)  # Welch's t-test (unequal variance)
# Print results
print(f"T-statistic: {t_stat:.4f}")
print(f"P-value: {p_value:.4f}")
# Interpretation
alpha = 0.05
if p_value < alpha:
    print("Significant difference in carrying capacity times between WT and MUT strains.")
else:
    print("No significant difference in carrying capacity times between WT and MUT strains.")
# ---------------------- Observations ---------------------- #
# 1. The wild-type (WT) strains generally reach carrying capacity faster than the mutant (MUT) strains.
# 2. Some mutant (MUT) strains take a longer time to reach their maximum OD600, suggesting a potential
#    growth defect caused by the mutation.
# 3. In certain cases, the WT and MUT strains reach their carrying capacity at similar times, indicating
#    that the mutation does not always affect growth duration.
# 4. The t-test results show that there is no significant difference in carrying capacity times between WT and MUT strains.
