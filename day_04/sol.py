with open("input.txt", "r") as f:
    lines = f.readlines()
    lines = [entry.strip() for entry in lines]

result = 0
for line in lines:
    points = 0
    game = line.split(":")[1].strip().split("|")
    game = [entry.strip() for entry in game]

    my_nums = game[1].split(" ")
    for x in my_nums:
        if x == "": my_nums.remove(x)
    my_nums = [int(entry) for entry in my_nums]

    win_nums = game[0].split(" ")
    for x in win_nums:
        if x == "": win_nums.remove(x)
    win_nums = [int(entry) for entry in win_nums]

    for x in win_nums:
        if x in my_nums:
            if points == 0:
                points += 1
            elif points > 0:
                points *= 2

    result += points
print(result)
