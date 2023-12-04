with open("input.txt", "r") as f:
    lines = f.readlines()
    lines = [entry.strip() for entry in lines]

result = 0
scratch_cards = []
for line in lines:
    counter = 0
    game_id = line.split(":")[0].strip().split(" ")
    game_id = game_id[len(game_id) - 1]
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

    for num in my_nums:
        if num in win_nums:
            counter += 1

    scratch_cards.append(game_id)
    for y in range(scratch_cards.count(game_id)):
        for x in range(counter):
            scratch_cards.append(str(int(game_id) + 1 + x))

print("result:", len(scratch_cards))
