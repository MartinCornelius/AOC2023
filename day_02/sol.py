file = open("sample.txt", "r")
lines = file.read().split("\n")

rules = {"red": 12, "green": 13, "blue": 14}
possible_games = []

for line in lines:
    totals = {"red": 0, "green": 0, "blue": 0}
    line_split = line.split(":")
    game_id = line_split[0].split(" ")[1]
    
    subsets = line_split[1].split(";")

    possible = True
    for sub in subsets:
        sub = sub.strip().split(",")
        for draw in sub:
            balls = draw.strip().split(" ")
            if rules[balls[1]] < int(balls[0]): possible = False
            totals[balls[1]] += int(balls[0])

    if possible:
        possible_games.append(game_id)        

result = 0
for x in possible_games:
    result += int(x)

print(result)
