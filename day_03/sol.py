file = open("input.txt", "r")
lines = file.read().split("\n")

result = 0
for line_idx, line in enumerate(lines):
    cleared = False
    current = ""
    for ch_idx, ch in enumerate(line):
        if ch.isdigit():
            current += ch
            # Above number
            if line_idx > 0:
                if lines[line_idx - 1][ch_idx] != ".": 
                    cleared = True
            # Left number
            if ch_idx > 0:
                if lines[line_idx][ch_idx - 1] != ".":
                    if lines[line_idx][ch_idx - 1].isdigit() == False: 
                        cleared = True
            # Below number
            if line_idx < len(lines) - 2:
                if lines[line_idx + 1][ch_idx] != ".":
                    cleared = True

            # Right number
            if ch_idx < len(lines[0]) - 2:
                if lines[line_idx][ch_idx + 1] != ".":
                    if lines[line_idx][ch_idx + 1].isdigit() == False:
                        cleared = True
            # Top left
            if line_idx > 0 and ch_idx > 0:
                if lines[line_idx - 1][ch_idx - 1] != ".":
                    if lines[line_idx - 1][ch_idx - 1].isdigit() == False:
                        cleared = True

            # Bottom left
            if line_idx < len(lines) - 2 and ch_idx > 0:
                if lines[line_idx + 1][ch_idx - 1] != ".":
                    if lines[line_idx + 1][ch_idx - 1].isdigit() == False:
                        cleared = True

            # Top right
            if line_idx > 0 and ch_idx < len(lines[0]) - 2:
                if lines[line_idx - 1][ch_idx + 1] != ".":
                    if lines[line_idx - 1][ch_idx + 1].isdigit() == False:
                        cleared = True

            # Bottom right
            if line_idx < len(lines) - 2 and ch_idx < len(lines[0]) - 2:
                if lines[line_idx + 1][ch_idx + 1] != ".":
                    if lines[line_idx + 1][ch_idx + 1].isdigit() == False:
                        cleared = True
            
            if ch_idx == len(line)-1:
                if cleared:
                    print(current)
                    result += int(current)
                    current = ""
                    cleared = False
        elif ch.isdigit() == False or ch_idx == len(line) - 1:
            if cleared:
                print(current)
                result += int(current)
            current = ""
            cleared = False

print("result:", result)

