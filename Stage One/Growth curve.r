# Generate time points
time_points <- seq(0, 150, by = 1)  # Extended time to include decline
# Simulate a single growth curve
single_growth_curve <- simulate_growth_with_decline(time_points)
growth_curve_example <- simulate_growth_with_decline(time_points)  # Simulate one curve
# Plot example
plot(time_points, growth_curve_example, type="l", col="blue", lwd=2,
     xlab="Time", ylab="Population Size", main="Bacterial Growth Curve with Decline Phase")
# Generate 100 different growth curves
time_points <- seq(0, 150, by=1)  # Extended time to include decline
growth_data <- data.frame(Time=rep(time_points, 100),
                          Curve=rep(1:100, each=length(time_points)),
                          Population=unlist(lapply(1:100, function(x) simulate_growth_with_decline(time_points))))
# Plot the growth curve
ggplot(growth_data, aes(x = Time, y = Population)) +
  geom_line(color = "blue") +
  labs(title = "Bacterial Growth Curve with Decline Phase",
       x = "Time",
       y = "Population Size") +
  theme_minimal()
# Function to determine time to reach 80% of carrying capacity (K)
time_to_80_percent <- function(time, population, K=1) {
  threshold <- 0.8 * K
  return(min(time[population >= threshold]))
}
# Time to 80% for first curve
curve_1_time <- growth_data$Time[growth_data$Curve == 1]
curve_1_population <- growth_data$Population[growth_data$Curve == 1]
t80 <- time_to_80_percent(curve_1_time, curve_1_population)
print(paste ("Time to 80% of carrying capacity:", t80))
