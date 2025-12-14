#%%
def rotate(dir_move: str, curr_num: int) -> tuple[int, int]:
    # dir_move is like 'L10' or 'R25'
    dir = dir_move[0]
    move_num = int(dir_move[1:].strip())
    start_num = curr_num
    dirSign = -1 if dir == 'L' else 1
    curr_num += dirSign * move_num
    # Count how many times we went through zero, and if ew landed up on zero.
    zero_count = \
        abs(curr_num) // 100 \
        + (1 if start_num>0 and curr_num < 0 else 0) \
        + (1 if start_num!=0 and curr_num == 0 else 0)
    return (curr_num % 100, zero_count)

#%%
def process_file(filename="input.txt",debug=False):
    start_num = 50
    zero_count_total = 0
    with open(filename, "r") as file:
        for dir_move in file:
            dir_move = dir_move.strip() # Get rid of newline
            # Read the first character of the line and print it
            curr_num, zero_count = rotate(dir_move, start_num)
            if debug:
                print(f"{dir_move=}, {start_num=}, {curr_num=}, {zero_count=}")
            start_num = curr_num
            zero_count_total += zero_count
    print(f"{zero_count_total=}")

#%%
# Runs some tests, zero_count_total should be 6!
process_file("test.txt", debug=True)
# zero_count_total=6

#%%
process_file()
# zero_count_total=6175

# %%
(curr_nam,zero_count) = rotate('L150', 50)
assert ((curr_nam, zero_count) == (0, 2))

(curr_nam,zero_count) = rotate('L5', 0)
assert ((curr_nam, zero_count) == (95, 0))

(curr_nam,zero_count) = rotate('R5', 99)
assert ((curr_nam, zero_count) == (4, 1))

(curr_nam,zero_count) = rotate('L2', 1)
assert ((curr_nam, zero_count) == (99, 1))

(curr_nam,zero_count) = rotate('L1', 0)
assert ((curr_nam, zero_count) == (99, 0))

(curr_nam,zero_count) = rotate("R48", 50)
assert ((curr_nam, zero_count) == (98, 0))

# %%
