import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

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

# Visualize distributions for numerical variables
numerical_cols = ['gpa', 'gmat', 'work_exp']
for col in numerical_cols:
    plt.figure(figsize=(8, 6))
    sns.histplot(data[col], kde=True)
    plt.title(f'Distribution of {col}')
    plt.savefig(f'{col}_distribution.png')
    plt.close()

# Visualize distributions for categorical variables
categorical_cols = ['gender', 'international', 'major', 'race', 'work_industry', 'admission']
for col in categorical_cols:
    plt.figure(figsize=(8, 6))
    sns.countplot(data=data, x=col)
    plt.title(f'Count of {col}')
    plt.xticks(rotation=45)
    plt.savefig(f'{col}_count.png')
    plt.close()

# Correlation analysis for numerical variables
plt.figure(figsize=(10, 8))
correlation_matrix = data[numerical_cols].corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix of Numerical Variables')
plt.show()

# Explore relationships with admission status
# Box plots for numerical variables vs admission
for col in numerical_cols:
    plt.figure(figsize=(8, 6))
    sns.boxplot(data=data, x='admission', y=col)
    plt.title(f'{col} vs Admission')
    plt.savefig(f'{col}_vs_admission_box.png')
    plt.close()

# Count plots for categorical variables vs admission
for col in categorical_cols[:-1]:  # Exclude 'admission' itself
    plt.figure(figsize=(10, 6))
    sns.countplot(data=data, x=col, hue='admission')
    plt.title(f'{col} vs Admission')
    plt.xticks(rotation=45)
    plt.savefig(f'{col}_vs_admission_count.png')
    plt.close()
