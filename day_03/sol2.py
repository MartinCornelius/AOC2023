file = open("input.txt", "r")
lines = file.read().split("\n")


def get_number(row, col):
    number = lines[row][col]
    lcol = col
    rcol = col
    while lcol-1 >= 0:
        lcol -= 1
        if lines[row][lcol].isdigit():
            number = lines[row][lcol] + number
        else:
            break
    while rcol+1 < len(lines[0]):
        rcol += 1
        if lines[row][rcol].isdigit():
            number = number + lines[row][rcol]
        else:
            break
    return number


result = 0

for line_idx, line in enumerate(lines):
    for ch_idx, ch in enumerate(line):
        numbers = []
        if ch == "*":
            if lines[line_idx][ch_idx - 1].isdigit():
                numbers.append(get_number(line_idx, ch_idx - 1))
            if lines[line_idx][ch_idx + 1].isdigit():
                numbers.append(get_number(line_idx, ch_idx + 1))

            if lines[line_idx - 1][ch_idx].isdigit():
                numbers.append(get_number(line_idx - 1, ch_idx))
            else:
                if lines[line_idx - 1][ch_idx - 1].isdigit():
                    numbers.append(get_number(line_idx - 1, ch_idx - 1))
                if lines[line_idx - 1][ch_idx + 1].isdigit():
                    numbers.append(get_number(line_idx - 1, ch_idx + 1))

            if lines[line_idx + 1][ch_idx].isdigit():
                numbers.append(get_number(line_idx + 1, ch_idx))
            else:
                if lines[line_idx + 1][ch_idx - 1].isdigit():
                    numbers.append(get_number(line_idx + 1, ch_idx - 1))
                if lines[line_idx + 1][ch_idx + 1].isdigit():
                    numbers.append(get_number(line_idx + 1, ch_idx + 1))

        if len(numbers) > 0:
            print("NUMBERS:", numbers)
        if len(numbers) == 2:
            result += int(numbers[0]) * int(numbers[1])
            print("Result:", result)

print(result)
