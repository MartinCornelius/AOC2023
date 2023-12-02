file = open("input.txt", "r")
lines = file.read().split("\n")

print(lines)

def is_integer(n):
    try:
        int(n)
    except ValueError:
        return False
    else:
        return True

result = 0
for line in lines:
    number = []

    for x in line:
        if is_integer(x):
            number.append(x)

    answer = ""
    if len(number) > 1:
        answer += number[0]
        answer += number[len(number) - 1]

    if len(number) == 1:
        answer += number[0]
        answer += number[0]

    if not answer == "":
        result += int(answer)

print(result)