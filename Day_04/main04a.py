#%%
from src04a import process_file

#%%
total_adj_rolls = process_file("test.txt",debug=True)
assert total_adj_rolls == 13

# %%
process_file("input.txt");
# total_adj_rolls=1428