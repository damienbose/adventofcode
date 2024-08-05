def getCodeForLine(input_line):
    n = len(input_line)
    c1 = None
    for i in range(n):
        c = input_line[i]
        if c.isdigit():
            c1 = c
            break
    c2 = None
    for i in range(n - 1, -1, -1):
        c = input_line[i]
        if c.isdigit():
            c2 = c
            break
    assert c1 is not None and c2 is not None, "Invalid Number of digits"
    return int(c1 + c2)


def parseFile(path):
    cum = 0
    with open(path, "r") as file:
        lines = file.readlines()
        for line in lines:
            code = getCodeForLine(line)
            cum += code
    print(cum)


if __name__ == "__main__":
    parseFile("data.txt")
