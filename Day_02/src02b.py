def check_id_range(id_range:str) -> tuple[int,int, int]:
    id_parts = id_range.split("-")
    if len(id_parts) != 2 or any([len(part)==0 for part in id_parts]):
        return (0,0,0)

    start_id,end_id = map(int, id_parts[:2])
    id_validity = [(is_valid_id(id),id) for id in range(start_id, end_id+1)]
    # Return (Number of Ids, Number of valid Ids, Sum of invalid Ids)
    return (len(id_validity), sum([not x[0] for x in id_validity]), sum([x[1] for x in id_validity if not x[0]]))

def is_valid_id(id:int) -> bool:
    id_s = str(id)
    L = len(id_s)
    if L == 0: # Empty string is not good!
        return False
    for split_num in range(1,L):
        id_groups = [id_s[i:i+split_num] for i in range(0,L,split_num)]
        if all([id_groups[0] == group for group in id_groups]):
            return False
    return True

def process_file(filename:str, debug:bool = False):
    total_sum_invalid = 0
    with open(filename, "r") as file:
        if debug:
            print(f"{"id_range":<30}| {"num_ids":<7} | {"num_valid":<9} | {"sum_invalid":<11}")
        for id_range in file.read().split(","):
            (num_ids,num_valid,sum_invalid) = check_id_range(id_range)
            total_sum_invalid += sum_invalid
            if debug:
                print(f"{id_range:<30}| {num_ids:<7} | {num_valid:<9} | {sum_invalid:<11}")
    print(f"{total_sum_invalid=}")