import re
from functools import reduce

file = open("input.txt", "r")
lines = file.read().split("\n")

digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

help_dict = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

def is_integer(n):
    try:
        int(n)
    except ValueError:
        return False
    else:
        return True

result = 0
for line in lines:
    d_in_word = {}
    for d in digits:
        occurrences = re.finditer(d, line)
        res = reduce(lambda x, y: x + [y.start()], occurrences, [])

        if len(res) > 1:
            if is_integer(d):
                n = d
            else:
                n = help_dict[d]

            for x in res:
                d_in_word[x] = n #line.find(d)
        elif len(res) == 1:
            if is_integer(d):
                n = d
            else:
                n = help_dict[d]
            d_in_word[res[0]] = n

    d_in_word = dict(sorted(d_in_word.items(), key=lambda item: item[0]))
    answer = ""

    if len(d_in_word) > 1:
        first, *_, last = d_in_word.items()
        answer += first[1]
        answer += last[1]

    if len(d_in_word) == 1:
        first, *_ = d_in_word.items()
        answer += first[1]
        answer += first[1]

    result += int(answer)
    print(answer)

print(result)