from scipy.stats import chisquare

# Observed unresolved calls
observed = [100, 80, 50, 70]

# Expected unresolved calls (uniform distribution)
total_calls = sum(observed)
expected = [total_calls / 4] * 4

# Perform chi-square test
chi2_stat, p_value = chisquare(observed, expected)

print(chi2_stat)
print(p_value)
