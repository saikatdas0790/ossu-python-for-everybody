# Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
# X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.
# You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.

# fileName = "./08-files/" + "mbox-short.txt"
fileName = input("Enter file name: ")
fileHandle = open(fileName)

allFloats = []

for line in fileHandle:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue

    parsedValue = float(line.split(" ")[-1])
    allFloats.append(parsedValue)

allFloatsSum = 0

for member in allFloats:
    allFloatsSum += member

average = allFloatsSum/len(allFloats)

print("Average spam confidence:", average)
