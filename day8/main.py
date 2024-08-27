def Main():
    data = parse_input("day8/data.txt")
    print(data)
    count = calculate(*data)
    print(count)


def parse_input(filename):
    with open(filename) as file:
        pattern = file.readline().strip()
        pattern = [0 if c == "L" else 1 for c in pattern]

        nav_map = {}  # char to (x, y)

        for line in file:
            if line == "\n":
                continue
            line = line.strip().split()
            from_char = line[0][0:3]

            L_char = line[2][1:4]
            R_char = line[3][0:3]

            nav_map[from_char] = (L_char, R_char)
    return pattern, nav_map


def calculate(pattern, nav_map):
    count = 0
    curr_char = "AAA"
    while True:
        curr_char = nav_map[curr_char][pattern[count % len(pattern)]]
        count += 1
        if curr_char == "ZZZ":
            break
    return count


if __name__ == "__main__":
    Main()
