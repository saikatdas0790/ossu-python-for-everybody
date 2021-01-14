import re

# fileName = "./12-regular-expressions/" + "regex_sum_42.txt"
fileName = "./12-regular-expressions/" + "regex_sum_1129224.txt"
fileHandle = open(fileName)

allOccurrences = []

for line in fileHandle:
    findResult = re.findall("[0-9]+", line)
    if len(findResult) != 0:
        allOccurrences += findResult


total = sum(map(lambda i: int(i), allOccurrences))

print(total)
