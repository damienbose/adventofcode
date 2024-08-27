import math

"""
LLR
a 223, 246, 270.
lcm(223, 246, 270) = 14910

"""


def lcm_of_array(arr):
    result = arr[0]
    for number in arr[1:]:
        result = math.lcm(result, number)
    return result


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
    nodes = [k for k in nav_map.keys() if k[-1] == "A"]
    print(nodes)

    counts = []
    for node in nodes:
        count = 0
        while True:
            node = nav_map[node][pattern[count % len(pattern)]]
            count += 1
            if node[-1] == "Z":
                counts.append(count)
                break

    print(counts)

    lcm = lcm_of_array(counts + [len(pattern)])

    return lcm


if __name__ == "__main__":
    Main()
