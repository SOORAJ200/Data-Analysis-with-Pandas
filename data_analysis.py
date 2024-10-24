import pandas as pd

# Load the CSV file
df = pd.read_csv('student-dataset.csv')

# Display the first few rows
print("First few rows:")
print(df.head())
# Calculate the average of a column
average_age = df['age'].mean()
print(f'Average Age: {average_age}')

# Display summary statistics
print("\nSummary statistics:")
print(df.describe())

# Count unique values in a column
print("\nUnique counts in 'age':")
unique_counts = df['age'].value_counts()
print(unique_counts)

# Check for missing values
print("\nMissing values in each column:")
missing_values = df.isnull().sum()
print(missing_values)
