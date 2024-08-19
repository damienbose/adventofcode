"""
We want > max_dis for each

per race bf: input: (time = 7, max_dis=9)
t in [0, 7] # where t is discrete
- hold down for 0, travel 0
- hold down for 1, s = d/t, d = s*t, t = 1 * (7-1) = 6
- hold down for 2, s = d/t, d = s*t, t = 2 * (7-2) = 10 > max_dis
- we want range of t, s.t d = t * (max_t-t) > max_dis
- t * max_t - t^2 > max_dis
- -t^2 + max_t * t - max_dis > 0


"""

import math


class Main:
    def __init__(self):
        self.filePath = "main.txt"
        self.parseFile()
        self.run()
        print("Final:")
        print(self.result)

    def parseFile(self):
        with open(self.filePath) as f:
            self.times = f.readline().strip().split()[1:]
            # self.times = [int(t) for t in self.times]
            # print(self.times)

            self.distances = f.readline().strip().split()[1:]
            # self.distances = [int(d) for d in self.distances]
            # print(self.distances)

            self.time = int("".join(self.times))
            self.distance = int("".join(self.distances))

            self.races = [(self.time, self.distance)]
            print(self.races)

    def getNumTimes(self, max_t, max_d):
        bottom_range = -(max_t) - math.sqrt(max_t**2 - 4 * -1 * -max_d)
        bottom_range = bottom_range / (2 * -1)

        top_range = -(max_t) + math.sqrt(max_t**2 - 4 * -1 * -max_d)
        top_range = top_range / (2 * -1)

        print(f"{top_range} < t < {bottom_range}")

        bottom_range = (
            math.floor(bottom_range)
            if not bottom_range.is_integer()
            else int(bottom_range) - 1
        )
        top_range = (
            math.ceil(top_range) if not top_range.is_integer() else int(top_range) + 1
        )
        print(
            f"{top_range} <= t <= {bottom_range}"
        )  # bug in case when wither roots are integer valued

        num_times = bottom_range - top_range + 1
        return num_times

    def run(self):
        self.result = 1
        for max_t, max_d in self.races:
            print("running", max_t, max_d)
            num_times = self.getNumTimes(max_t, max_d)
            print(num_times)
            self.result *= num_times
        return self.result


if __name__ == "__main__":
    Main()
