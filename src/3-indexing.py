# %% [markdown]
# # Numpy Fundamentals
# %%
import numpy as np
# %% [markdown]
# ## Indexing
# %%
array_a = np.array([[1,2,3], [4,5,6]])
array_a

# %%
print(array_a)

# %% [markdown]
# ### Specific Values
# %%
array_a[0]

# %%
array_a[1]

# %% [markdown]
# we want to retrieve the 2nd element of the 1st row
# %%
array_a[0][1]
# %% [markdown]
# we want the 1st element of the 2nd row
#
# we reference 1 instead of 0 for the 2nd row
# %%
array_a[1][0]

# %% [markdown]
# An equivalent method for getting the answer above
# is to use a comma to separate row and column references.
#
# This is the approach used in this course.
# %%
array_a[1,0]

# %% [markdown]
# get an entire column, substitute row index with colon
# %%
print(array_a[:,0])

# %% [markdown]
# note that it returns [1 4] these are the values
# found in the first column separated by a space

# %% [markdown]
# ### Negative Indices

# %% [markdown]
# A negative index can be used to retrieve the last element of the 1st row.

# %%
array_b = np.array([1,2,3])
print(array_b)

# %% [markdown]
# Now call the index -1 from the array_b
# %%
print(array_b[-1])

# %% [markdown]
# Using a negative number returns the value from the end of
# the array
# %%
print(array_a)
# %%
print(array_a[-1])
# %%
