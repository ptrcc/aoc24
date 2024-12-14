import re

with open('input.txt', 'r') as file:
    text = file.read()

regex = r"mul\((\d+),(\d+)\)"

matches = re.findall(regex, text)

result = 0
for match in matches:
    result += int(match[0]) * int(match[1])

print(result)

regex = r"(do\(\))|(don't\(\))|mul\((\d+),(\d+)\)"
matches = re.findall(regex, text)

result = 0
do_calculate = True

for match in matches:
    if match[0] == 'do()' or match[1] == "don't()":
        if match[0] == 'do()':
            do_calculate = True
        elif match[1] == "don't()":
            do_calculate = False
        continue
    
    if do_calculate:
        numbers = [group for group in match if group.isdigit()]
        if len(numbers) == 2:
            result += int(numbers[0]) * int(numbers[1])

print(result)
