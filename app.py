import pandas as pd

# Creating a DataFrame
data = {
    'Name': ['John', 'Anna', 'Peter', 'Linda'],
    'Age': [28, 24, 35, 32],
    'City': ['New York', 'Paris', 'London', 'Berlin']
}

df = pd.DataFrame(data)

# Display the DataFrame
print("Original DataFrame:")
print(df)

# Adding a new column
df['Salary'] = [50000, 62000, 48000, 54000]

# Displaying the DataFrame with the new column
print("\nDataFrame after adding Salary column:")
print(df)

# Filtering data
filtered_df = df[df['Age'] > 30]

# Displaying the filtered DataFrame
print("Filtered Data\n", filtered_df)
