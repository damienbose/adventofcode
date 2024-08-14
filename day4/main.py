class Main:
    def __init__(self) -> None:
        self.win_nums, self.curr_nums = self.parse_data()
        result = self.calculate_score(self.win_nums, self.curr_nums)
        print(result)

    def parse_data(self):
        win_nums_arr = []
        my_nums_arr = []
        with open("data.txt", "r") as f:
            for line in f:
                line = line.split()[2:]  # Remove the first two words
                num_win_numbers = 10
                win_nums = [int(num) for num in line[:num_win_numbers]]
                my_nums = [int(num) for num in line[num_win_numbers + 1 :]]  # Skip '|'
                win_nums_arr.append(win_nums)
                my_nums_arr.append(my_nums)
        return win_nums_arr, my_nums_arr

    def calculate_score(self, win_nums, my_nums):
        score = 0
        for win_num, my_num in zip(win_nums, my_nums):
            matches = set(win_num).intersection(set(my_num))
            if len(matches) == 0:
                score += 0
            else:
                score += 2 ** (len(matches) - 1)
            print(matches, score)
        return int(score)


if __name__ == "__main__":
    Main()
