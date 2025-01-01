from scipy.stats import poisson

# Parameters
lambda_ = 4  # Average number of unresolved calls per hour
k = 6  # Minimum number of unresolved calls

# Calculate the probability of encountering 6 or more unresolved calls
probability = 1 - poisson.cdf(k - 1, lambda_)
print(probability)
