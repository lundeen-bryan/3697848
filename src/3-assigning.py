# %% [markdown]
# # Assigning Values
#
# Discuss different options for assigning values to an array.

# %%
import numpy as np

# %% [markdown]
# Start by defining an array variable and display it
# %%
arraya = np.array([[1, 2, 3], [4, 5,6]])
print(arraya)

# %% [markdown]
# Change the 3rd row 1st column value to 9
# %%
arraya[0, 2] = 9
print(arraya)

# %% [markdown]
# Set value for entire rows (vector) within array
# %%
arraya[0] = 9
print(arraya)

# %% [markdown]
# Change entire 1st column value to 9
# by using a colon indicating no row index

# %%
arraya[:,0] = 9
print(arraya)

# %% [markdown]
# Assign different values to an array
# %%
lista = [8,7,8]
arraya[0] = lista
arraya

# %% [markdown]
# The code above says that we want to replace
# the first row with 8,7,8

# %% [markdown]
# Check that the value is still an array
# %%
print(type(arraya[0]))

# %% [markdown]
# Replace every value in the array with 9
# %%
arraya[:] = 9
print(arraya)
# %%
