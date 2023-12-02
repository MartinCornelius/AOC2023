file = open("input.txt", "r")
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
            if int(balls[0]) > totals[balls[1]]:
                totals[balls[1]] = int(balls[0])

    print(totals)
    answer = 1
    for total in totals:
        answer *= totals[total]

    possible_games.append(answer)

result = 0
for res in possible_games:
    result += res
print(result)

