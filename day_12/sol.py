import itertools

file = open("input.txt")
lines = file.read().splitlines()
 
allowedChars = [".", "#"]

def isAllowedArrangement(springs, groups):
    s = list(filter(None, ''.join(map(str, springs)).split(".")))
    if len(s) == len(groups):
        for x in range(len(groups)):
            if len(s[x]) != groups[x]:
                return False
        return True
    return False

def trySpringArrangement(springs, arrangement):
    result = []
    idx = 0
    for x in range(len(springs)):
        if springs[x] == "?":
            result.append(arrangement[idx])
            idx += 1
        else:
            result.append(springs[x])
    return result

result = 0
for line in lines:
    line = line.split()
    springs = list(line[0])
    groups = list(map(int, line[1].split(",")))

    arrangements = []
    unknowns = springs.count("?")

    for arrangement in itertools.product(allowedChars, repeat=unknowns):
        arrangements.append(arrangement)

    for arrangement in arrangements:
        newArrangement = trySpringArrangement(springs, arrangement)
        if isAllowedArrangement(newArrangement, groups):
            result += 1

print("result:", result)
