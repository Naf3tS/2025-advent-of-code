def max_joltage(bank:str) -> int:
    battery_joltage = [int(battery) for battery in bank]
    tens_index, tens_value = max(enumerate(battery_joltage[0:-1]), key=lambda x: x[1])
    ones_value = max(battery_joltage[tens_index+1:])
    return tens_value * 10 + ones_value

def process_file(filename,debug=False) -> int:
    total_joltage = 0
    with open(filename, 'r') as file:
        for line in file:
            bank = line.strip()
            bank_max_joltage = max_joltage(bank)
            if debug:
                print(f"{bank}: {bank_max_joltage}")
            total_joltage += bank_max_joltage
    print(f"{total_joltage=}")
    return total_joltage