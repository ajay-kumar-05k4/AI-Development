import plotly.express as px
df = px.data.iris()
fig = px.scatter(df, x="sepal_length", y="sepal_width", 
                 color="species", size="petal_length",
                 hover_data=['petal_width'], 
                 title="Iris Sepal Scatter Plot")
fig.show()

fig = px.histogram(df, x="sepal_length", nbins=10, color="species", 
                   title="Sepal Length Distribution by Species")
fig.show()
fig = px.box(df, x="species", y="petal_length", color="species", 
             title="Petal Length Boxplot by Species")
fig.show()

# 3D scatter plot
fig = px.scatter_3d(df, x='sepal_length', y='sepal_width', z='petal_length', 
                    color='species', size='petal_width', 
                    title="3D Scatter Plot of Iris Dataset")
fig.show()
