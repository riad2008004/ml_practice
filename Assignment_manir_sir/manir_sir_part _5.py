from scipy.stats import norm

# Parameters
n = 400  # Total sample size
x = 15   # Number of unresolved calls
p_hat = x / n  # Sample proportion
confidence_level = 0.95
z = norm.ppf(1 - (1 - confidence_level) / 2)  # Z-value for 95% confidence

# Standard error
se = (p_hat * (1 - p_hat) / n) ** 0.5

# Confidence interval
lower_bound = p_hat - z * se
upper_bound = p_hat + z * se

print(lower_bound, upper_bound)
