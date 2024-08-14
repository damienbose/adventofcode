"""
We first parse data as before.
Then we iterate num by num, and add more cards based on needs.
so initailly populate with 1 of each and then add more as we move down
"""

import numpy as np


class Main:
    def __init__(self) -> None:
        self.win_nums, self.curr_nums = self.parse_data()
        cards_count = self.calculate_score(self.win_nums, self.curr_nums)
        print(sum(cards_count))

    def calculate_score(self, win_nums, my_nums):
        num_cards, _ = my_nums.shape
        cards_count = np.ones(num_cards, dtype=int)
        # TODO: Vim for rename symbole

        for card_idx in range(num_cards):
            print(card_idx)
            for _ in range(cards_count[card_idx]):
                matches = set(win_nums[card_idx]).intersection(set(my_nums[card_idx]))
                num_matches = len(matches)

                # print(cards_count[card_idx + 1 : card_idx + 1 + num_matches])
                cards_count[card_idx + 1 : card_idx + 1 + num_matches] += 1
        return cards_count

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
        return np.array(win_nums_arr), np.array(my_nums_arr)


if __name__ == "__main__":
    Main()
