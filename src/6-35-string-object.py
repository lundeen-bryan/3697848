# %% [markdown]
# # String vs Object vs Numbers
# %%
import numpy as np
# %%
# genfromtxt lending_data_lt headers are LoanID to TotalPrice
lending_data_lt = np.genfromtxt(
    "./data/lending-co-LT.csv",
    delimiter=",",
)
print(f"Lending Data:\n{lending_data_lt}")

# %% [markdown]
# *When we see scientific notation (1.043e+03) then...*
#
# Can do exponent right here:
# 1.660e+04=16600
# 1.043e+03=1043
#
# we use dtype=np.int32 to convert those notations to integers
# %%
# genfromtxt lending_data_lt headers are LoanID to TotalPrice
lending_data_lt = np.genfromtxt(
    "./data/lending-co-LT.csv",
    delimiter=",",
    dtype=np.int32,
)
print(f"Lending Data:\n{lending_data_lt}")

# %% [markdown]
# * We can also import the whole dataset as text *
#
# > dtype=np.str_
#
# _Note that "np.str" is deprecated and can also use just "str" inplace_
# %%
# genfromtxt lending_data_lt headers are LoanID to TotalPrice
lending_data_lt = np.genfromtxt(
    "./data/lending-co-LT.csv",
    delimiter=",",
    dtype=np.str_,
)
print(f"Lending Data:\n{lending_data_lt}")

# %% [markdown]
# if we use object as dtype then...
# %%
# genfromtxt lending_data_lt headers are LoanID to TotalPrice
lending_data_lt = np.genfromtxt(
    "./data/lending-co-LT.csv",
    delimiter=",",
    dtype=np.object_,
)
print(f"Lending Data:\n{lending_data_lt}")

# %%
