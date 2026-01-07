import pandas as pd
import numpy as np
from visualizations import visualize_distributions, correlation_analysis, explore_relationships

# Load the data
data = pd.read_csv('Day2/MBA.csv')

# Display basic information
print("Dataset Shape:", data.shape)
print("\nData Types:")
print(data.dtypes)
print("\nSummary Statistics:")
print(data.describe(include='all'))

# Check for missing values
print("\nMissing Values:")
print(data.isnull().sum())

# Call visualization functions
visualize_distributions(data)
correlation_analysis(data)
explore_relationships(data)
