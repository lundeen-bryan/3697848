# %% [markdown]
# # Elementwise Properties
#
# This notebook shows how to use Elementwise properties of arrays
# %%
import numpy as np

# %%
array1 = np.array([7,8,9])
array1
# %%
array2 = np.array([[7,8,9], [4,5,6]])
array2
# %%
array2[0:] = [1,2,3]
array2
# %%
array2[1:] = [4,5,6]
array2

# %% [markdown]
# Add 2 to each number in array1
# %%
array1 = array1 + 2
print(array1)

# %%
type(array1)

# %% [markdown]
# ## Lists Vs Arrays
#
# - Lists and arrays serve different purposes
# - The main pupose for lists is to store data
# - The main purpose of arrays is to compute mathematical operations
#
# ### Find the sum off array1

# %%
print(f"Array1: {array1}")
print(f"\nArray2: {array2}")
# %%
array1 + array2[0]

# %% [markdown]
# > Each element in array1 is matched with array2 and added together
#
# This is called "Elementwise addition" when they can be matched with cooresponding elements in another array it's called "elementwise"
#
# Test this by adding array1 with the 2nd row of array2

# %%
array1 + array2[1]
# %%
array1 * array2[1]

# %% [markdown]
# We can also do math across arrays of different dimensions
# %%
array1 + array2
# %%
array1 * array2

# %% [markdown]
# The whole time the original array values didn't change
# %%
print(f"Array1: {array1}")
print(f"\nArray2: {array2}")

# %%
