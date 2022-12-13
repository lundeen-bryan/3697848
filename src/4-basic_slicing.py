# %% [markdown]
# # Working with Arrays
# %%
import numpy as np

# %% [markdown]
# ## Slicing

# %%
matrix_A = np.array(
    [
        [1, 2, 3],
        [4, 5, 6],
    ]
)
matrix_A
# %%
matrix_A[:]
# %%
matrix_A[0:0]

# %%
matrix_A[0:1]


# %%
matrix_A[0:2]

# %%
matrix_A[
    :,
]

# %% [markdown]
# ### Compare indexing vs slicing
#
# Notice that the slicing adds an extra bracket
# %%
matrix_A[0]  # indexing
# %%
matrix_A[:1]  # slicing

# %% [markdown]
# What if we print these values are they different?
# %%
print(f"Indexing: {matrix_A[0]}")

# %%
print(f"Slicing: {matrix_A[:1]}")

# %% [markdown]
# ### Slicing a column
# %%
print(f"Slicing a column: {matrix_A[:,0]}")

# %%
print(f"Slicing a column: {matrix_A[:-1]}")

# %%
print(f"Slicing a column: {matrix_A[:,0]}")

# %% [markdown]
# ## Stepwise Slicing
#
# from a new
# %%
matrix_B = np.array(
    [
        [1, 1, 1, 2, 0],
        [3, 6, 6, 7, 4],
        [4, 5, 3, 8, 0],
    ]
)
# %%
matrix_B[::, ::]
# %%
print(f"Stepwise Slicing: \n{matrix_B}")

# %% [markdown]
# ## Conditional Slicing


# %%
matrix_C = np.array(
    [
        [1, 1, 1, 2, 0],
        [3, 6, 6, 7, 4],
        [4, 5, 3, 8, 0],
    ]
)

# %%
matrix_C[:, 0]

# %% [markdown]
# ## Dimensions and the Squeeze Function
# %%
matrix_D = np.array(
    [
        [1, 1, 1, 2, 0],
        [3, 6, 6, 7, 4],
        [4, 5, 3, 8, 0],
    ]
)
# %%
print(matrix_D)
# %%
type(matrix_D[0,0])
# %%
type(matrix_D[0,0:1])
# %%
print(matrix_D[0:1,0:1])
# %%
matrix_D[0:1,0:1].squeeze()
# %%
