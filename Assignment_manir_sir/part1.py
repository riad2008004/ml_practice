from scipy.stats import binom

# Parameters
p_binomial = 0.02  # Probability of unresolved call
n_binomial = 200  # Total calls
k_binomial = 5    # Target unresolved calls

# Probability of exactly 5 unresolved calls
prob_binomial = binom.pmf(k_binomial, n_binomial, p_binomial)
print(f"Probability of exactly 5 unresolved calls: {prob_binomial:.4f}")