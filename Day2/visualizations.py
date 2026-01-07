import matplotlib.pyplot as plt
import seaborn as sns

def visualize_distributions(data):
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

def correlation_analysis(data):
    # Correlation analysis for numerical variables
    numerical_cols = ['gpa', 'gmat', 'work_exp']
    plt.figure(figsize=(10, 8))
    correlation_matrix = data[numerical_cols].corr()
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
    plt.title('Correlation Matrix of Numerical Variables')
    plt.savefig('correlation_matrix.png')
    plt.close()

def explore_relationships(data):
    # Explore relationships with admission status
    numerical_cols = ['gpa', 'gmat', 'work_exp']
    categorical_cols = ['gender', 'international', 'major', 'race', 'work_industry', 'admission']

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
