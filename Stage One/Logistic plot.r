#Task 2 and 3 of 4
# Load ggplot package
library(ggplot2)
# Function to simulate growth with decline phase
simulate_growth_with_decline <- function(time, K = 1, r = 0.5, initial_population = 0.01) {
  lag_phase <- runif(1, 5, 15)   # Random lag phase
  exp_phase <- runif(1, 10, 30)  # Random exponential phase
  stat_phase <- runif(1, 10, 20) # Random stationary phase
  death_rate <- runif(1, 0.02, 0.1) # Random decline rate
  # Adjusted times for each phase
  adjusted_exp_time <- pmax(time - lag_phase, 0)
  adjusted_decline_time <- pmax(time - (lag_phase + exp_phase + stat_phase), 0)
  # Calculate growth curve
  growth_curve <- ifelse(
    time < lag_phase,
    initial_population,  # Lag phase
    ifelse(
      time < lag_phase + exp_phase,
      K / (1 + ((K - initial_population) / initial_population) * exp(-r * adjusted_exp_time)),  # Exponential phase
      ifelse(
        time < lag_phase + exp_phase + stat_phase,
        K,  # Stationary phase
        K * exp(-death_rate * adjusted_decline_time)  # Decline phase
      )
    )
  )
  return(growth_curve)
}
