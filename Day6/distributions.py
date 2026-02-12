import numpy as np

# 1. Uniform Distribution
uniform_data = np.random.uniform(low=0, high=10, size=10)
print("Uniform Distribution:")
print(uniform_data)
print()

# 2. Normal Distribution
normal_data = np.random.normal(loc=50, scale=10, size=10)
print("Normal Distribution:")
print(normal_data)
print()

# 3. Binomial Distribution
binomial_data = np.random.binomial(n=10, p=0.5, size=10)
print("Binomial Distribution:")
print(binomial_data)
print()

# 4. Poisson Distribution
poisson_data = np.random.poisson(lam=5, size=10)
print("Poisson Distribution:")
print(poisson_data)
print()
