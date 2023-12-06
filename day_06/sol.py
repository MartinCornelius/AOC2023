file = open("input.txt", "r")
lines = file.read().split("\n")

times = lines[0].split()[1:]
t = ""
for time in times:
    t += time
times = [int(t)]

distances = lines[1].split()[1:]
d = ""
for dis in distances:
    d += dis
distances = [int(d)]

results = []
for x in range(len(times)):
    counter = 0
    for i in range(times[x] + 1):
        a = i * (times[x] - i)
        if a > distances[x]:
            counter += 1
    results.append(counter)

result = 1
for res in results:
    result *= res
print("RESULT:", result)
