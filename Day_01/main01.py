#%%
def rotate(dir, move_num, curr_num):
    if dir == 'L':
        curr_num -= move_num
    elif dir == 'R':
        curr_num += move_num
    return curr_num % 100

#%%
def process_file(filename='input.txt',debug=False):
    curr_num = 50
    num_zero = 0
    with open(filename, 'r') as file:
        for line in file:
            # Read the first character of the line and print it
            dir = line[0]
            move_num = int(line[1:].strip())
            curr_num = rotate(dir, move_num, curr_num)
            if debug:
                print(f"{dir=}, {move_num=}, {curr_num=}")
            if curr_num == 0:
                num_zero += 1
    print(f"{num_zero=}")

#%%
# Runs some tests, should return 3!
process_file("test.txt", debug=True)

#%%
process_file()
# num_zero=1102

# %%
rotate('L', 0, 100)