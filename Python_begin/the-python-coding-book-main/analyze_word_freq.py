import string

with open("pride_and_prejudice.txt") as file:
    text = file.read()

# Clean data by removing capitalization and punctuation marks
text = text.lower()

for punctuation_mark in ".,?!;:-":
    text = text.replace(punctuation_mark, " ")

# Split string into a list of strings containing all words
words = text.split()

# Look at the first word. Add number 1 to it to show it's the first time and found it

# Move to the next word. Has this world already been encountered?
word_frequencies = {}

for word in words:
    if word not in word_frequencies.keys():
        word_frequencies[word] = 1
    else:
        word_frequencies[word] = word_frequencies[word] + 1

print(len(word_frequencies))

# Exports words and frequencies to a CSV spreadsheet
with open("words in Pride and Prejudice.csv", "w") as file:
    # Write header line 
    file.write("Word,Frequency\n")

    # Loop through dictionary and write key-value pairs to csv
    for word, frequency in word_frequencies.items():
        file.write(f"{word},{frequency}\n")

# file2 = open("test_write.txt", "w")
# file2.write("I'm miserable. But not really.\n Im learning mindfulness, specifically vipissanna.")
# file2.close()
