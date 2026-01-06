import pandas as pd

# Creating a Series from a list
data = [10, 20, 30, 40, 50]
series = pd.Series(data)
print("Series created from list:")
print(series)

# Creating a Series with custom index
data_index = [10, 20, 30, 40, 50]
index = ['a', 'b', 'c', 'd', 'e']
series_index = pd.Series(data_index, index=index)
print("\nSeries with custom index:")
print(series_index)

# Basic operations on Series
print("\nSum of series:", series.sum())
print("Mean of series:", series.mean())
print("Maximum value:", series.max())
print("Minimum value:", series.min())
