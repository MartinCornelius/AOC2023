file = open("input.txt")
lines = file.read().splitlines()


def generate_new_seq(seq):
    result = []
    for num in range(0, len(seq)-1):
        result.append((seq[num+1]-seq[num]))
    return result


def extrapolate(history):
    history[len(history)-1].append(0)
    tmp = history[-1][-1]
    for x in range(len(history)-2, -1, -1):
        num = history[x][-1] + tmp
        tmp = num
        history[x].append(num)


result = 0
for line in lines:
    history = []
    history.append(list(map(int, line.split())))

    while [idx for idx, val in enumerate(history[len(history)-1]) if val != 0]:
        history.append(generate_new_seq(history[len(history)-1]))

    extrapolate(history)
    result += history[0][-1]

print(result)
