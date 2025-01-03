from scipy.stats import poisson

# Parameters
lambda_poisson = 4  # Average unresolved calls per hour
k_poisson = 6       # Target unresolved calls

# Probability of 6 or more unresolved calls
prob_poisson = 1 - poisson.cdf(k_poisson - 1, lambda_poisson)
print(f"Probability of 6 or more unresolved calls: {prob_poisson:.4f}")