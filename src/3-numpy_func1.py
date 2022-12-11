# %% [markdown]
# # Characteristics of NumPy Functions

# %%
import numpy as np

# %%
array_a = np.array([1,2,3])
array_a
# %%
array_b = np.array([[1],[2]])
array_b
# %%
matrix_C = np.array([[1,2,3],[4, 5, 6]])
matrix_C
# %%
np.add(array_a, matrix_C)

# %% [markdown]
# ## Broadcasting Rules
#
# 1. The arrays  have the same shape
# 2. The arrays have the same number of dimensions, and the length of each dimension is either common or 1
# 3. The arrays  have too few dimensions can have their shapes altered with a dimension1, to satisfy the second rule.
#
# %% [markdown]
# ## Type Casting

# %%
np.add(array_b, matrix_C, dtype=np.float64)
# %%
np.mean(matrix_C, axis=0)
# %%
matrix_C
# %%
## >>> (1 + 4) / 2
## 2.5
##
