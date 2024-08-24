"""
Five of a kind, where all five cards have the same label: AAAAA
Four of a kind, where four cards have the same label and one card has a different label: AA8AA
Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
High card, where all cards' labels are distinct: 23456


base 13 then?

AAAAA is the highest number
23456 is the lowest number

7 buckets it can go into
if bucket are same we have to check which 5 digit base 13 number is bigger

We can make the bucket the 6th digit?


5, 4, 3, 2, 1, 0

"""

from collections import Counter
from functools import cache


def main():
    # parse the data from the input file [(hand, bid)])
    data = parseData("day7/data.txt")
    print(data)

    # sort this array based on the hand strength custom function
    data.sort(key=lambda x: hand_score(x[0]))
    print(data)

    # multiply by the bid amount and the ranking
    result = sum([x[1] * i for i, x in enumerate(data, start=1)])
    print(result)


def get_type_num(hand):
    char_counter = sorted(Counter(hand).values(), reverse=True)
    if char_counter[0] == 5:
        # five of a kind
        return 6
    if char_counter[0] == 4:
        # four of a kind
        return 5
    if char_counter[0] == 3 and char_counter[1] == 2:
        # full house
        return 4
    if char_counter[0] == 3 and char_counter[1] == 1 and char_counter[2] == 1:
        # three of a kind
        return 3
    if char_counter[0] == 2 and char_counter[1] == 2 and char_counter[2] == 1:
        # two pair
        return 2
    if (
        char_counter[0] == 2
        and char_counter[1] == 1
        and char_counter[2] == 1
        and char_counter[3] == 1
    ):
        # one pair
        return 1
    # high card
    return 0


@cache
def hand_score(hand):
    """formula = type * 13^5 + n[0] * 13^4 + n[1]^3 + ..."""
    maps = {
        "2": 0,
        "3": 1,
        "4": 2,
        "5": 3,
        "6": 4,
        "7": 5,
        "8": 6,
        "9": 7,
        "T": 8,
        "J": 9,
        "Q": 10,
        "K": 11,
        "A": 12,
    }

    highest_digit = get_type_num(hand)

    return highest_digit * 13**5 + sum(
        [maps[card] * 13 ** (4 - i) for i, card in enumerate(hand)]
    )


def parseData(filename):
    data = []
    with open(filename) as f:
        for line in f:
            hand, bid = line.strip().split(" ")
            data.append((hand, int(bid)))
    return data


if __name__ == "__main__":
    main()
