import matplotlib.pyplot as plt
import seaborn as sns

# Create a list of data
data = [0, 1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4]

# Create a distplot
sns.distplot(data, kde=False)

# Show the plot
plt.show()