"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730466575"

word: str = input("Enter a 5-character word: ")
if len(word) != 5:
    print("Error: Word must contain 5 characters")
    exit()
letter: str = input("Enter a single character: ")
if len(letter) != 1:
    print("Error: Character must be a single character.")
    exit()
print("Searching for " + letter + " in " + word + ".")

i: int = 0
counter: int = 0

while i < len(word):
    if word[i] == letter:
        counter += 1
        print(letter + " found at index " + str(i) + ".")
        i += 1
    else:
        i += 1

if counter == 1: 
    print(str(counter) + " instance of " + letter + " found in " + word + ".")
elif counter <= 0:
    print("No instances of " + letter + " found in " + word + ".")
else:
    print(str(counter) + " instances of " + letter + " found in " + word + ".")