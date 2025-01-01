from scipy.stats import norm

# Parameters
n = 10000  # Total number of calls per month
p = 0.02  # Probability of an unresolved call

# Mean and standard deviation for normal approximation
mean = n * p
std_dev = (n * p * (1 - p))**0.5

# Question (c): Probability that unresolved calls are between 180 and 220
lower_bound = 180
upper_bound = 220
prob_between = norm.cdf(upper_bound, mean, std_dev) - norm.cdf(lower_bound, mean, std_dev)

# Question (d): Probability that unresolved calls exceed 230
exceed_bound = 230
prob_exceed = 1 - norm.cdf(exceed_bound, mean, std_dev)

print(prob_between)
print(prob_exceed)
