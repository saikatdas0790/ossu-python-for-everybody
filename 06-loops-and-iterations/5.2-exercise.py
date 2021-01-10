# Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. Once 'done' is entered, print out the largest and smallest of the numbers. If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. Enter 7, 2, bob, 10, and 4 and match the output below.

largestNumber = None
smallestNumber = None

counter = 0

while True:
    num = input("Enter a number: ")
    if num == "done":
        break

    try:
        parsedNum = int(num)

        if counter == 0:
            smallestNumber = parsedNum
            largestNumber = parsedNum

        if (parsedNum < smallestNumber):
            smallestNumber = parsedNum

        if (parsedNum > largestNumber):
            largestNumber = parsedNum

        counter = counter + 1
    except:
        print("Invalid input")

print("Maximum is", largestNumber)
print("Minimum is", smallestNumber)
