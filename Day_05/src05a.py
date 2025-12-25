
def load_file(filename,debug=False) -> int:
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if debug:
                print(f"Loaded line: {line}")
            return int(line)
