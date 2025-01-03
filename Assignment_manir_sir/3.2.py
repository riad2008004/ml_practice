import pandas as pd
import matplotlib.pyplot as plt
from lifelines import KaplanMeierFitter
from lifelines.statistics import logrank_test
from lifelines import CoxPHFitter

# Step 1: Define the dataset
data = pd.DataFrame({
    'Patient ID': range(1, 21),
    'Survival Time': [15, 28, 10, 22, 35, 8, 18, 32, 12, 25, 16, 30, 9, 21, 38, 6, 19, 33, 13, 27],
    'Censor Status': [1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0],
    'Treatment Group': ['B', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'A'],
    'Age': [62, 55, 45, 60, 70, 40, 58, 65, 48, 57, 52, 68, 43, 59, 72, 38, 56, 66, 49, 61],
    'Sex': [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
})

# Step 2: Descriptive Analysis - Mean Survival Time for Treatment A and B
mean_survival_A = data[data['Treatment Group'] == 'A']['Survival Time'].mean()
mean_survival_B = data[data['Treatment Group'] == 'B']['Survival Time'].mean()

print(f"Mean survival time for Treatment A: {mean_survival_A:.2f} months")
print(f"Mean survival time for Treatment B: {mean_survival_B:.2f} months")

# Percentage of censored patients in each group
percent_censored_A = data[(data['Treatment Group'] == 'A') & (data['Censor Status'] == 0)].shape[0] / data[data['Treatment Group'] == 'A'].shape[0] * 100
percent_censored_B = data[(data['Treatment Group'] == 'B') & (data['Censor Status'] == 0)].shape[0] / data[data['Treatment Group'] == 'B'].shape[0] * 100

print(f"Percentage of censored patients in Treatment A: {percent_censored_A:.2f}%")
print(f"Percentage of censored patients in Treatment B: {percent_censored_B:.2f}%")

# Step 3: Kaplan-Meier Survival Curves
kmf = KaplanMeierFitter()

plt.figure(figsize=(10, 6))

# Plot Kaplan-Meier for Treatment A
kmf.fit(data[data['Treatment Group'] == 'A']['Survival Time'], event_observed=data[data['Treatment Group'] == 'A']['Censor Status'], label='Treatment A')
kmf.plot()

# Plot Kaplan-Meier for Treatment B
kmf.fit(data[data['Treatment Group'] == 'B']['Survival Time'], event_observed=data[data['Treatment Group'] == 'B']['Censor Status'], label='Treatment B')
kmf.plot()

plt.title("Kaplan-Meier Survival Curves")
plt.xlabel("Time (Months)")
plt.ylabel("Survival Probability")
plt.legend()
plt.show()

# Step 4: Log-Rank Test to Compare Survival Distributions
results = logrank_test(data[data['Treatment Group'] == 'A']['Survival Time'],
                       data[data['Treatment Group'] == 'B']['Survival Time'],
                       event_observed_A=data[data['Treatment Group'] == 'A']['Censor Status'],
                       event_observed_B=data[data['Treatment Group'] == 'B']['Censor Status'])

print(f"Log-Rank Test p-value: {results.p_value:.4f}")

# Step 5: Cox Proportional Hazards Model
cph = CoxPHFitter()
data['Treatment Group'] = data['Treatment Group'].apply(lambda x: 1 if x == 'A' else 0)  # Convert A to 1, B to 0
cph.fit(data[['Survival Time', 'Censor Status', 'Treatment Group']], duration_col='Survival Time', event_col='Censor Status')

print("Cox Proportional Hazards Model Summary:")
cph.print_summary()

# Step 6: Conclusion
# Interpret results based on Kaplan-Meier, Log-rank test, and Cox model.
