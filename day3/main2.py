"""
Parsing
iterate char by char parsing the numbers. 
Check the surrounding of the number, for each * found, add update has map to number. Hash map *idx -> [number] 

Iterate through has map. If 2 numbers, multiply them and add to the results.
"""

from collections import defaultdict
import numpy as np


class Main:
    def __init__(self) -> None:
        print("Running...")
        self.char_ptr = 0
        self.run()

    def check_surrounding(self, data, i, j):
        gears = []
        deltas = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        n, m = data.shape
        for delta in deltas:
            x, y = i + delta[0], j + delta[1]
            if x > n - 1 or x < 0 or y > m - 1 or y < 0:
                continue
            if data[(x, y)] == "*":
                # print("Found a gear at", x, y)
                gears.append((x, y))
        return gears

    def parse_data(self):
        with open("data.txt", "r") as f:
            data = np.array([[c for c in line.strip()] for line in f])

        gears_map = defaultdict(list)

        while self.char_ptr < data.shape[0] * data.shape[1]:
            i = self.char_ptr // data.shape[0]
            j = self.char_ptr % data.shape[0]
            c = data[i, j]
            if not c.isdigit():
                self.char_ptr += 1
                continue
            else:
                number = self.parse_digit(data, i, j)
                len_digit = len(str(number))
                nearby_gears = set()
                for dig_pos_delta in range(len_digit):
                    nearby_gears.update(
                        self.check_surrounding(data, i, j + dig_pos_delta)
                    )
                for gear_idx in nearby_gears:
                    gears_map[gear_idx].append(number)
        return gears_map

    def parse_digit(self, data, i, j):
        buffer = []
        n, m = data.shape
        while True:
            i = self.char_ptr // n
            j = self.char_ptr % n
            c = data[i, j]
            if c.isdigit():
                buffer.append(c)
                self.char_ptr += 1
                if self.char_ptr % n == 0:
                    break  # end of line
            else:  # end of number
                self.char_ptr += 1
                break
        return int("".join(buffer))

    def get_gear_ratio(self, gears):
        result = 0
        for gear, numbers in gears.items():
            if len(numbers) == 2:
                result += numbers[0] * numbers[1]
        return result

    def run(self):
        # Parse the data
        gears = self.parse_data()
        result = self.get_gear_ratio(gears)
        print(result)


if __name__ == "__main__":
    Main()
