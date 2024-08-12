"""The data is of the form:

467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..

"""

import numpy as np


def check_surrounding(data, i, j):
    deltas = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    n, m = data.shape
    for delta in deltas:
        x, y = i + delta[0], j + delta[1]
        if x > n - 1 or x < 0 or y > m - 1 or y < 0:
            continue
        if data[x, y] == "." or data[x, y].isdigit():
            continue
        else:
            return True
    return False


if __name__ == "__main__":
    results = []
    # Read the input file
    with open("data.txt", "r") as f:
        # Load the data into a numpy array
        data = np.array([[c for c in line.strip()] for line in f])
        print(data)

        # Iterate char by char, if char is a digit, then check the delta regions (adding to a buffer), if none of the chars have met the criteria then abandon that one.
        curr_num_buffer = []
        is_next_symbol = False
        n, m = data.shape
        for i in range(n):
            if is_next_symbol:
                results.append(int("".join(curr_num_buffer)))
            curr_num_buffer = []
            is_next_symbol = False

            for j in range(m):
                if len(curr_num_buffer) > 0:
                    # We are currently parsing a number
                    if data[i, j].isdigit():
                        curr_num_buffer.append(data[i, j])
                        is_next_symbol = is_next_symbol or check_surrounding(
                            data, i, j
                        )  # does not evaluate if we already found around the number
                    else:
                        # we have reached the end of the number
                        if is_next_symbol:
                            results.append(int("".join(curr_num_buffer)))
                            # flush the buffer
                        curr_num_buffer = []
                        is_next_symbol = False

                else:
                    # We are just moving along a file till we find a number.
                    if not data[i, j].isdigit():
                        continue
                    if data[i, j].isdigit():
                        curr_num_buffer.append(data[i, j])
                        is_next_symbol = check_surrounding(data, i, j)
                        continue
    print(sum(results))
