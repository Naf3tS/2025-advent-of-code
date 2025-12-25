def num_adj_rolls_at_loc(map:list[list[str]], at_loc:tuple[int,int]) -> int:
    count_adj_rolls = 0
    L = len(map)
    for row in range(-1,2):
        for col in range(-1,2):
            check_loc = (at_loc[0]+row, at_loc[1]+col)
            if row==0 and col==0: # Skip self
                continue
            if check_loc[0]<0 or check_loc[1]<0 or check_loc[0]>L-1 or check_loc[1]>L-1: # Out of bounds
                continue
            if map[check_loc[0]][check_loc[1]]=="@":
                count_adj_rolls += 1
    return count_adj_rolls

def scan_map_adj_rolls(map:list[list[str]]) -> int:
    total_rolls_removed = 0
    L = len(map);
    num_rolls_removed = None
    while num_rolls_removed is None or num_rolls_removed > 0:
        num_rolls_removed = 0 # Reset!
        remove_roll_at_loc = []
        for row in range(L):
            for col in range(L):
                if map[row][col]=="@" and num_adj_rolls_at_loc(map, (row,col)) < 4:
                    num_rolls_removed += 1
                    remove_roll_at_loc.append((row,col))
        for loc in remove_roll_at_loc:
            map[loc[0]][loc[1]] = "X"
        total_rolls_removed += num_rolls_removed
    return total_rolls_removed

def load_map_from_str_lines(map:list[str]) -> list[list[str]]:
    L = len(map[0]);
    out = [["."] * L for _ in range(L)]
    for row in range(L):
        for col in range(L):
            out[row][col] = map[row][col]
    return out

def process_file(filename,debug=False) -> int:
    total_adj_rolls = 0
    with open(filename, 'r') as file:
        map_lines = file.read().splitlines()
    map = load_map_from_str_lines(map_lines)
    total_adj_rolls = scan_map_adj_rolls(map)
    print(f"{total_adj_rolls=}")
    return total_adj_rolls