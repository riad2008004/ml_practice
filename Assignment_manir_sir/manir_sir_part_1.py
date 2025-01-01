from scipy.stats import binom

# Parameters
n = 200  # Number of trials (calls)
p = 0.02  # Probability of success (call unresolved)
k = 5  # Number of unresolved calls

# Calculate probability
probability = binom.pmf(k, n, p)
print(probability)
