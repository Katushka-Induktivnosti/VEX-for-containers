import pandas as pd
import numpy as np

# Example matrices as DataFrames
df1 = pd.DataFrame([[1, 0.71, 0.161, 0.34, 0.4, 0.06, 0.018],
[0.71, 1, 0.155, 0.304, 0.355, 0.004, 0],
[0.161, 0.155, 1, 0.062, 0.12, 0.010, 0.004],
[0.34, 0.304, 0.062, 1, 0.332, 0.129, 0.041],
[0.4, 0.355, 0.12, 0.332, 1, 0.003, 0],
[0.06, 0.004, 0.010, 0.129, 0.003, 1, 0.095],
[0.018, 0, 0.004, 0.041, 0, 0.095, 1]])
df2 = pd.DataFrame([[1, 0.12, 0.105, 0.27, 0.25, 0.15, 0],
[0.12, 1, 0.133, 0.178, 0.105, 0.04, 0],
[0.105, 0.133, 1, 0.08, 0.27, 0.08, 0.16],
[0.27, 0.178, 0.08, 1, 0.15, 0.28, 0],
[0.25, 0.105, 0.27, 0.15, 1, 0.2, 0.1],
[0.15, 0.04, 0.08, 0.28, 0.2, 1, 0],
[0, 0, 0.16, 0, 0.1, 0, 1]])

# Flatten the DataFrames into 1D arrays
vec1 = df1.to_numpy().ravel()
vec2 = df2.to_numpy().ravel()

# Calculate correlation using NumPy
correlation = np.corrcoef(vec1, vec2)[0, 1]

print("Correlation:", correlation)
