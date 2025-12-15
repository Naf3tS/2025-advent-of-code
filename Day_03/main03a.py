#%%
from src03a import process_file

#%%
total_max_joltage = process_file("test.txt",debug=True)
assert total_max_joltage == 357

# %%
process_file("input.txt");
# total_joltage=17031