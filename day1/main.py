"""
twolnine - iterate and find the first substring which matches our pars - iterate and find the first substring which matches our parserr

for reverse, we reverse the solution matches and do the same thing
"""

matches = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

numbers = [str(num) for num in range(1, 10)]


def getForwardCode(input_line):
    for i in range(len(input_line)):
        for match in matches:
            if input_line[i:].startswith(match):
                return str(matches[match])
            elif input_line[i].isdigit():
                return input_line[i]


def getBackwardCode(input_line):
    for i in range(len(input_line) - 1, -1, -1):
        for match in matches:
            if input_line[i:].startswith(match):
                return str(matches[match])
            elif input_line[i].isdigit():
                return input_line[i]


def parseFile(path):
    cum = 0
    with open(path, "r") as file:
        lines = file.readlines()
        for line in lines:
            f_code = getForwardCode(line)
            b_code = getBackwardCode(line)
            assert f_code is not None and b_code is not None
            cum += int(f_code + b_code)
    print(cum)


if __name__ == "__main__":
    parseFile("data.txt")
