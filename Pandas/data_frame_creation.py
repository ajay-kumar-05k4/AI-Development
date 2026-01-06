import pandas as pd

# Creating a DataFrame from a dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'London', 'Tokyo']
}
df = pd.DataFrame(data)
print("DataFrame created from dictionary:")
print(df)

# Creating a DataFrame from a list of lists
data_list = [
    ['Alice', 25, 'New York'],
    ['Bob', 30, 'London'],
    ['Charlie', 35, 'Tokyo']
]
df_list = pd.DataFrame(data_list, columns=['Name', 'Age', 'City'])
print("\nDataFrame created from list of lists:")
print(df_list)
