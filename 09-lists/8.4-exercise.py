# Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method. The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it to the list. When the program completes, sort and print the resulting words in alphabetical order.

# fileName = input("Enter file name: ")
fileName = "./09-lists/" + "romeo.txt"
fileHandle = open(fileName)

listOfWords = []

for line in fileHandle:
    for word in line.split():
        if word not in listOfWords:
            listOfWords.append(word)

listOfWords.sort()

print(listOfWords)
