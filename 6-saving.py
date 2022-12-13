# %% [markdown]
# # Saving Files with NumPy

# %%
import numpy as np

# %%
# get data from Lending-Company-Saving.csv
task_file = "./data/Lending-Company-Saving.csv"
lending_co = np.genfromtxt(
    task_file,
    delimiter=",",
    dtype=np.str_,
)
print(f"Lending Data:\n{lending_co}")
# %%
# save the data as an npy file
np.save("Lending-Company-Saving", lending_co)
# %%
# load the data and view it from the npy file (looks same as str)
lending_co_saved = np.load(
    "./data/Lending-Company-Saving.npy",
)
print(f"Lending Data from npy file:\n{lending_co_saved}")
# %%
# check if npy data is same as data from the str
np.array_equal(lending_co, lending_co_saved)
# %%
np.savez("Lending-Company-Saving", lending_co, lending_co_saved)

# %%
# lending_co_npz_file to variable then load first dataset
lending_co_npz_file = np.load("./data/Lending-Company-Saving.npz")
first_recordz = lending_co_npz_file["arr_0"]
print(f"First Record:\n{first_recordz}")
# %%
# lending_co_npz_file to variable then load first dataset
lending_co_npz_file = np.load("./data/Lending-Company-Saving.npz")
second_recordz = lending_co_npz_file["arr_1"]
print(f"Lending Savez:\n{first_recordz}")

# %%
lending_co_npz_file.files
# %%
np.savez(
    "./data/Lending-Company-Saving.npz",
    company=lending_co,
    data_save=lending_co_saved,
)
# %%
lending_data_savez = np.load("./data/Lending-Company-Saving.npz")

# %%
lending_data_savez.files
# %%
company_data = lending_data_savez["company"]
print(f"Lending Savez:\n{company_data}")
# %%
data_save_data = lending_data_savez["data_save"]
print(f"Lending Savez:\n{data_save_data}")
# %%
# check that company and data_save are the same data
np.array_equal(data_save_data, company_data)

# %% [markdown]
# ## np.savetxt() Function
# %%
# get data from Lending-Company-Saving.csv
task_file = "./data/Lending-Company-Saving.csv"
lending_co = np.genfromtxt(
    task_file,
    delimiter=",",
    dtype=np.str_,
)
print(f"Lending Data:\n{lending_co}")

# %%
np.savetxt(
    "Lending-Company-Saving.txt",
    lending_co,
    fmt = "%s",
    delimiter=",",
)
# %%
## use genfromtxt to get the string values
lending_data_savetext = np.genfromtxt(
    "Lending-Company-Saving.txt",
    delimiter=",",
    dtype = np.str_,
)
print(f"Lending Data:\n{lending_data_savetext}")

# %%
lending_data_save = np.load(
    "./data/Lending-Company-Saving.npy",
)
# %%
np.array_equal(lending_data_save , lending_data_savetext)
# %%
