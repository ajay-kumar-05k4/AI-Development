import seaborn as sns
import matplotlib.pyplot as plt


df = sns.load_dataset('iris')

sns.scatterplot(data=df, x='sepal_length', y='sepal_width', hue='species')
plt.title("Sepal Length vs Width")
plt.show()
 # Histogram of sepal_length
sns.histplot(df['sepal_length'], bins=10, color='skyblue')
plt.title("Distribution of Sepal Length")
plt.show()
 # Boxplot of petal_length for each species
sns.boxplot(x='species', y='petal_length', data=df)
plt.title("Petal Length by Species")
plt.show()
# Correlation heatmap
corr = df.corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title("Feature Correlation")
plt.show()
