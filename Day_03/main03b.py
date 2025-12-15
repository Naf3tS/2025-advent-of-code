#%%
from src03b import process_file

#%%
total_max_joltage = process_file("test.txt",debug=True)
assert total_max_joltage == 3121910778619

# %%
process_file("input.txt");
# total_joltage=168575096286051