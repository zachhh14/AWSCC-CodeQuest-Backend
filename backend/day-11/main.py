sortedLines = []
with open('./backend/day-11/students.txt', 'r') as file:
    lines = file.readlines()

for line in sorted(lines):
    sortedLines.append(f"{line.strip()}\n")

with open('./backend/day-11/students.txt', 'w') as file:
    file.writelines(sortedLines)

    