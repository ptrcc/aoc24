with open("input.txt", "r") as f:
    data = f.read().splitlines()

left = []
right = []
for entry in data:
    entry = entry.split("   ")
    left.append(int(entry[0]))
    right.append(int(entry[1]))

left.sort()
right.sort()

diff = 0 
for i in range(len(left)):
    diff = diff + abs(int(left[i]) - int(right[i]))

print(diff)

def count_occurrences_in_list(list, value: int) -> int:
    count = 0
    for element in list:
        if element == value:
            count += 1
    return count

score = 0
for item in left:
    occurences = count_occurrences_in_list(right, item)
    score += (occurences*item)

print(score)