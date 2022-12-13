# %% [markdown]
# # Partial Cleaning While Importing

# %%
# import numpy
import numpy as np

# %%
# read Lending-Company-Numeric-Data-NAN.csv
lending_data = np.genfromtxt(
    "./data/Lending-Company-Numeric-Data-NAN.csv",
    delimiter=";",
)
print(f"Lending Data Shape: {lending_data.shape}")
print(f"Lending Data:\n{lending_data}\n")
# %%
# Same as above but skip top 2 rows
lending_data = np.genfromtxt(
    "./data/Lending-Company-Numeric-Data-NAN.csv",
    delimiter=";",
    skip_header=2,
)
print(f"Lending Data Shape: {lending_data.shape}")
print(f"Lending Data:\n{lending_data}\n")
# %%
# Same as above but skip bottom 2 rows
lending_data = np.genfromtxt(
    "./data/Lending-Company-Numeric-Data-NAN.csv",
    delimiter=";",
    skip_footer=2,
)
print(f"Lending Data Shape: {lending_data.shape}")
print(f"Lending Data:\n{lending_data}\n")
# %%
# Same as above but show only col 1, 2, and last
lending_data = np.genfromtxt(
    "./data/Lending-Company-Numeric-Data-NAN.csv",
    delimiter=";",
    usecols=(0, 1, 5),
)
print(f"Lending Data Shape: {lending_data.shape}")
print(f"Lending Data:\n{lending_data}\n")
# %%
# Same as above but combine modifications
lending_data = np.genfromtxt(
    "./data/Lending-Company-Numeric-Data-NAN.csv",
    delimiter=";",
    usecols=(0, 1, 5),
    skip_footer=2,
    skip_header=2,
)
print(f"Lending Data Shape: {lending_data.shape}")
print(f"Lending Data:\n{lending_data}\n")

# %%
# Same as above but combine modifications
lending_data5, lending_data0, lending_data1 = np.genfromtxt(
    "./data/Lending-Company-Numeric-Data-NAN.csv",
    delimiter=";",
    usecols=(5, 0, 1),
    skip_footer=2,
    skip_header=2,
    unpack=True,
)
print(f"Lending Data column 4:\n{lending_data5}\n")
print(f"Lending Data column 1:\n{lending_data0}\n")
print(f"Lending Data column 2:\n{lending_data1}\n")

# %%
