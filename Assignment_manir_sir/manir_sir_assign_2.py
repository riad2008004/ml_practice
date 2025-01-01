import pandas as pd
from scipy.stats import ttest_rel
import numpy as np

# Sample data
data = {
    "Before": [165, 145, 160, 155, 162, 148, 152, 159, 151, 157],
    "After": [140, 133, 144, 142, 148, 137, 140, 145, 139, 143],
}
df = pd.DataFrame(data)

# Calculate differences
df["Difference"] = df["Before"] - df["After"]

# Descriptive Statistics
mean_diff = df["Difference"].mean()
std_diff = df["Difference"].std()
var_diff = df["Difference"].var()
print("Mean:", mean_diff, "Std Dev:", std_diff, "Variance:", var_diff)

# Paired t-test
t_stat, p_value = ttest_rel(df["Before"], df["After"])
print("t-statistic:", t_stat, "p-value:", p_value)

# Confidence Interval
n = len(df)
conf_interval = (mean_diff - 1.96 * (std_diff / np.sqrt(n)),
                 mean_diff + 1.96 * (std_diff / np.sqrt(n)))
print("95% Confidence Interval:", conf_interval)

# Effect Size (Cohen's d)
cohens_d = mean_diff / std_diff
print("Cohen's d:", cohens_d)