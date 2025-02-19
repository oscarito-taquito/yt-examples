# %%
import os
import sys
from itertools import combinations

# %% set directories
try:
    parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
except NameError:
    current_dir = os.getcwd()
    parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

# %% import customer data
from data.datagenerator import DataGen

datagen = DataGen()
dataset = datagen.generate_ecomm_data()

# List all attribute combinations
attributes = dataset.columns.tolist()

# %% List the combination of attributes
for i in range(1, len(attributes) + 1):
    print(list(combinations(attributes, i)), "\n")
