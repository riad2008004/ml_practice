from statsmodels.stats.proportion import proportions_ztest

# Given data
n_new = 5500  # Total sample size after training
x_new = 85    # Number of unresolved calls in the sample
p0 = 0.02     # Historical unresolved rate (null hypothesis proportion)
alpha = 0.05  # Significance level

# Perform the z-test for proportions
statistic, p_value = proportions_ztest(count=x_new, nobs=n_new, value=p0, alternative='smaller')

# Determine rejection of null hypothesis
reject_null = p_value < alpha

print(statistic, p_value, reject_null)
