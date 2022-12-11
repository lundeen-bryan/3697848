# %% [markdown]
# # Types of Data Supported by NumPy

# %%
import numpy as np

# %%
array1 = np.array([[1, 2, 3], [4, 5, 6]])
print(array1)

# %% [markdown]
# The default data type (dtype) is set to None on
# ndarrays. So on the next line add "dtype = int" to see each element
# stored as an int %%

# %%
array1 = np.array([[1, 2, 3], [4, 5, 6]], dtype="int")
array1

# %% [markdown]
# Now change the type to float32
# %%
array1 = np.array([[1, 2, 3], [4, 5, 6]], dtype="float32")
array1

# %% [markdown]
# NumPy added a "." after the number because floats have a decimal place

# %% [markdown]
# We can also change the data type by adding it to the beginningZZ