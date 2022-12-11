# %% [markdown]
# ### List vs Array
# %%
import numpy as np
# %%
list_a = [[1,2,3],[4,5,6]]
# %%
len(list_a)
# %%
array_a = np.array(list_a)
# %%
type(array_a)
# %%
print(list_a)
# %%
print(array_a)
# %%
array_a.shape
# %%
len(list_a)
# %%
list_b = list_a[0] + list_a[1]
array_b = array_a[0] + array_a[1]
# %%
np.sqrt(array_a)
# %%
