#Task 2.1_R
# Load necessary libraries
library(ggplot2)
library(dplyr)
library(tidyr)
# Read the data
data <- read.table("microbiology.txt", header = TRUE, sep = "\t")
# Read the strain description
strain_description <- read.table("microbiology description.txt", header = TRUE, sep = "\t")
# Reshape the strain description into long format
strain_description_long <- strain_description %>%
  pivot_longer(cols = -Strain, names_to = "Type", values_to = "Well")
# Add strain and type information to the main data
data_long <- data %>%
  pivot_longer(cols = -time, names_to = "Well", values_to = "OD600") %>%
  left_join(strain_description_long, by = "Well") %>%
  separate(Strain, into = c("Strain", "Replicate"), sep = "_") %>%
  mutate(Type = ifelse(Type == "WT", "Knock-in (+)", "Knock-out (-)"))
# Average of replicates for each strain and type
data_avg <- data_long %>%
  group_by(Strain, Type, time) %>%
  summarize(OD600_avg = mean(OD600, na.rm = TRUE), .groups = 'drop')
# Plot averaged growth curves for each strain, with knock-ins and knock-outs together
ggplot(data_avg, aes(x = time, y = OD600_avg, color = Type, group = interaction(Strain, Type))) +
  geom_line(linewidth = 1, alpha = 0.8) +  # Use `linewidth` instead of `size`
  facet_wrap(~Strain, scales = "free_y") +
  labs(title = "Averaged Growth Curves of OD600 vs Time for Different Strains",
       x = "Time (minutes)",
       y = "OD600 (Averaged)",
       color = "Strain Type") +
  theme_minimal()
# make carrying capacity 85% of max OD600
carrying_capacity_threshold <- max(data_avg$OD600_avg, na.rm = TRUE) * 0.80
# Time to reach carrying capacity for each strain and type
carrying_times <- data_avg %>%
  group_by(Strain, Type) %>%
  filter(OD600_avg >= carrying_capacity_threshold) %>%
  summarize(Time_to_Carrying_Capacity = min(time), .groups = 'drop')
# Scatterplot of time to reach carrying capacity
ggplot(carrying_times, aes(x = Strain, y = Time_to_Carrying_Capacity, color = Type)) +
  geom_jitter(width = 0.2, alpha = 0.6) +
  labs(title = "Time to Reach Carrying Capacity (Averaged)",
       x = "Strain",
       y = "Time to Reach Carrying Capacity (minutes)",
       color = "Strain Type") +
  theme_minimal()
# Box plot for carrying capacity times
ggplot(carrying_times, aes(x = Type, y = Time_to_Carrying_Capacity, fill = Type)) +
  geom_boxplot(alpha = 0.6) +
  labs(title = "Comparison of Time to Carrying Capacity (Averaged)",
       x = "Strain Type",
       y = "Time to Reach Carrying Capacity (minutes)") +
  theme_minimal()
# Statistical test (t-test) to check if there is a significant difference
t_test_result <- t.test(Time_to_Carrying_Capacity ~ Type, data = carrying_times)
print(t_test_result)
# Observations:
# p-value < 0.05 indicates a significant difference in growth between knock-out and knock-in strains.
# Boxplots and scatterplots provide visual evidence of distribution differences.
