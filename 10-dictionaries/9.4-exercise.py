# Open the file mbox-short.txt and read it line by line. When you find a line that starts with 'From ' like the following line:
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

# fileName = input("Enter file name: ")
fileName = "./10-dictionaries/" + "mbox-short.txt"

fileHandle = open(fileName)

countStore = {}

for line in fileHandle:
    if line.startswith("From "):
        words = line.split()
        email = words[1]

        countStore[email] = countStore.get(email, 0) + 1

highEmail = None
highCount = None

for email, count in countStore.items():
    if highCount == None or highCount < count:
        highEmail = email
        highCount = count

print(highEmail, highCount)
