def num_adj_rolls_at_loc(map:list[str], at_loc:tuple[int,int]) -> int:
    count_adj_rolls = 0
    L = len(map)
    for x in range(-1,2):
        for y in range(-1,2):
            check_loc = (at_loc[0]+x, at_loc[1]+y)
            if x==0 and y==0: # Skip self
                continue
            if check_loc[0]<0 or check_loc[1]<0 or check_loc[0]>L-1 or check_loc[1]>L-1: # Out of bounds
                continue
            if map[check_loc[1]][check_loc[0]]=="@":
                count_adj_rolls += 1
    return count_adj_rolls

def scan_map_adj_rolls(map:list[str]) -> int:
    total_adj_rolls = 0
    Y = len(map);
    for y in range(Y):
        X = len(map[y])
        for x in range(X):
            if map[y][x]=="@" and num_adj_rolls_at_loc(map, (x,y)) < 4:
                total_adj_rolls += 1
    return total_adj_rolls

def process_file(filename,debug=False) -> int:
    total_adj_rolls = 0
    with open(filename, 'r') as file:
        map = file.readlines()
    total_adj_rolls = scan_map_adj_rolls(map)
    print(f"{total_adj_rolls=}")
    return total_adj_rolls