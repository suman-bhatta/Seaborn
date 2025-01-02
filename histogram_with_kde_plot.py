import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style="whitegrid")

# Generate random data
rs = np.random.RandomState(9)
d = rs.normal(size=100)

# Create histogram with KDE
sns.histplot(d, kde=True, color="b", bins=20)

plt.show()
