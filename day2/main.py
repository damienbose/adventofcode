import numpy as np


config = (12, 13, 14)


def getGameOutcomes(line):
    line = line.split(": ")[1]
    result = []
    for segment in line.split(";"):
        r, g, b = 0, 0, 0  # Initialize red, green, blue counts
        for color in segment.split(","):
            count, color_name = color.strip().split()
            if color_name == "red":
                r = int(count)
            elif color_name == "green":
                g = int(count)
            elif color_name == "blue":
                b = int(count)
        result.append((r, g, b))
    return result


def isValidGame(game_res):
    # Iterate through each game
    for res in game_res:
        r, g, b = res
        # Check if the game is valid
        if r <= 12 and g <= 13 and b <= 14 and r + g + b <= sum(config):
            pass
        else:
            return False
    return True


def getFestNum(game_res):
    # Iterate through each game
    # convert to numpu array
    game_res = np.array(game_res)
    # print(game_res)
    min_red = np.max(game_res[:, 0])
    min_green = np.max(game_res[:, 1])
    min_blue = np.max(game_res[:, 2])
    return min_red * min_green * min_blue


if __name__ == "__main__":
    valid_games = []
    # iterate line by line
    # parse the inputs, create function which returns [(r,g,b), ...], a lise of rgb for each game (line)
    counter = 0
    for line in open("data.txt", "r"):
        counter += 1
        game_res = getGameOutcomes(line)
        print(game_res)
        # for each game fewest number of cubes of each color
        fewest_num = getFestNum(game_res)
        print("hello", fewest_num)
        valid_games.append(fewest_num)

    print("The final result is: ", sum(valid_games))
