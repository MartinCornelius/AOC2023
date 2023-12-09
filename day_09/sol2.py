file = open("input.txt")
lines = file.read().splitlines()


def generate_new_seq(seq):
    result = []
    for num in range(0, len(seq)-1):
        result.append((seq[num+1]-seq[num]))
    return result


def extrapolate(history):
    history[-1] = [0] + history[-1]
    tmp = history[-1][0]
    for x in range(len(history)-2, -1, -1):
        num = history[x][0] - tmp
        tmp = num
        history[x] = [num] + history[x]


result = 0
for line in lines:
    history = []
    history.append(list(map(int, line.split())))
    while [idx for idx, val in enumerate(history[len(history)-1]) if val != 0]:
        history.append(generate_new_seq(history[len(history)-1]))

    extrapolate(history)
    result += history[0][0]

print(result)
