from collections import defaultdict

"""
Map each seed to a location, and in the end take the lowest one.
First parse,
the generate mapping functions.
then traverse the map"""


class Main:
    def __init__(self):
        self.parse()
        self.traverse_map()
        print(self.result)

    def mapping(
        self, source_num, destination_range_start, source_range_start, range_len
    ):
        print(
            "Using mapping",
            destination_range_start,
            source_range_start,
            range_len,
        )
        if (
            source_range_start <= source_num <= source_range_start + range_len
        ):  # e.g, 50 <= x <= 52
            diff = source_num - source_range_start  # e.g, 51-50
            return destination_range_start + diff  # e.g, 100 + 1
        else:
            return source_num

    def get_next_val(self, curr_val, maps):
        # print(maps)
        for mapping_params in maps:
            # print("mapping_params", mapping_params)
            candidate = self.mapping(curr_val, *mapping_params)
            if candidate != curr_val:
                break  # found a mapping, otherwise will apply identity mapping
        assert candidate is not None
        return candidate

    def traverse_helper(self, seed):
        print("SEED", seed)
        curr_val = seed
        for maps in self.maps.values():
            print("maps", maps)
            curr_val = self.get_next_val(curr_val, maps)
            print("curr_val", curr_val)
        print("Final Location", curr_val)
        return curr_val

    def traverse_map(self):
        locations = [self.traverse_helper(seed) for seed in self.seeds]
        self.result = min(locations)

    def parse(self):
        with open("data.txt") as f:
            self.seeds = [int(num) for num in f.readline().strip().split(" ")[1:]]
            self.maps = defaultdict(list)  # ordered list of maps

            # print(self.seeds)
            current_key = None
            for line in f:
                line = line.strip().split(" ")
                # print(line)
                if len(line) == 1:  # empty line
                    pass
                elif len(line) == 2:  # Map titles
                    # print("line", line)
                    current_key = line[0]
                elif len(line) == 3:
                    line = [int(num) for num in line]
                    destination_range_start = line[0]
                    source_range_start = line[1]
                    range_len = line[2]
                    # print("Adding mapping", destination_range_start, source_range_start)

                    assert current_key is not None
                    # print("current_key", current_key)
                    # print("mapping", mapping)
                    self.maps[current_key].append(
                        (destination_range_start, source_range_start, range_len)
                    )
                    # print("mapping", self.maps.keys())


if __name__ == "__main__":
    Main()
