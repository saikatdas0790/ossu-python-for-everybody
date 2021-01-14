# Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

# fileName = input("Enter file name: ")
fileName = "./10-dictionaries/" + "mbox-short.txt"

fileHandle = open(fileName)

timeDictionary = {}

for line in fileHandle:
    if line.startswith("From "):
        words = line.split()
        time = words[5]

        hour = time.split(":")[0]

        timeDictionary[hour] = timeDictionary.get(hour, 0) + 1

for key in sorted(timeDictionary.keys()):
    print(key, timeDictionary[key])
