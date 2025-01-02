import matplotlib.pyplot as plt
import seaborn as sns

# Create a list of data
sns.distplot([0, 1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4], hist=False)

# Show the plot
plt.show()