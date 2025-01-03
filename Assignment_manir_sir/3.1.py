import pandas as pd

# Load the dataset
data = pd.DataFrame({
    'Patient ID': range(1, 21),
    'Survival Time': [15, 28, 10, 22, 35, 8, 18, 32, 12, 25, 16, 30, 9, 21, 38, 6, 19, 33, 13, 27],
    'Censor Status': [1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0],
    'Treatment Group': ['B', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'A'],
    'Age': [62, 55, 45, 60, 70, 40, 58, 65, 48, 57, 52, 68, 43, 59, 72, 38, 56, 66, 49, 61],
    'Sex': [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
})

# Compute mean survival time by treatment group
mean_survival = data.groupby('Treatment Group')['Survival Time'].mean()

# Compute the percentage of censored patients by treatment group
censored_percentage = data[data['Censor Status'] == 0].groupby('Treatment Group').size() / data.groupby('Treatment Group').size() * 100

print("Mean Survival Time:")
print(mean_survival)
print("\nPercentage of Censored Patients:")
print(censored_percentage)
