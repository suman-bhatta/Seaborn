import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style="white")

# Generate a random univariate dataset
rs = np.random.RandomState(10)
d = rs.normal(size=100)

# Define the colors to use
colors = ["r", "g", "b"]

# Plot a histogram with multiple colors
sns.distplot(d, kde=True, hist=True, bins=10,
             rug=True,hist_kws={"alpha": 0.3,
                                "color": colors[0]},
             kde_kws={"color": colors[1], "lw": 2},
             rug_kws={"color": colors[2]})


# Show the plot
plt.show()