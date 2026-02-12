import numpy as np
from scipy import stats

# Conversion rates from two versions (sample data)
version_A = np.random.normal(loc=5.0, scale=1.0, size=50)  # old design
version_B = np.random.normal(loc=5.5, scale=1.0, size=50)  # new design

# Perform two-sample t-test
t_stat, p_value = stats.ttest_ind(version_A, version_B)

print("Average Conversion A:", np.mean(version_A))
print("Average Conversion B:", np.mean(version_B))
print("P-value:", p_value)

# Decision
if p_value < 0.05:
    print("New design significantly improves performance")
else:
    print("No significant difference between designs")
