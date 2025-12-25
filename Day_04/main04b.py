#%%
from src04b import process_file

#%%
total_num_removed = process_file("test.txt",debug=True)
assert total_num_removed == 43

# %%
process_file("input.txt");
# total_adj_rolls=8936