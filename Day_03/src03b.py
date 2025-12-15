def max_joltage(bank:str, num_batteries:int = 2) -> int:
    battery_joltage = [int(battery) for battery in bank]
    B = len(battery_joltage)
    assert B >= num_batteries

    joltage = 0
    search_from_index = 0
    for i in range(0,num_batteries):
        search_to_index = B - (num_batteries - i)
        search_batteries = enumerate(battery_joltage[search_from_index:search_to_index+1])
        loop_index, loop_value = max(search_batteries, key=lambda x: x[1])
        search_from_index += loop_index+1
        joltage += loop_value*(10**(num_batteries-i-1))
    return joltage

def process_file(filename,debug=False) -> int:
    total_joltage = 0
    with open(filename, 'r') as file:
        for line in file:
            bank = line.strip()
            bank_max_joltage = max_joltage(bank, 12)
            if debug:
                print(f"{bank}: {bank_max_joltage}")
            total_joltage += bank_max_joltage
    print(f"{total_joltage=}")
    return total_joltage