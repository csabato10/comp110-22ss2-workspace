"""One Shot Wordle."""

author = 730466575

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
secret_word: str = "python"
guess = input(f"What is your {len(secret_word)}-letter guess? ")

while len(guess) != len(secret_word):
    guess = input("That was not 6 letters! Try again: ")

image: str = ""
i: int = 0

while i < len(guess):
    if secret_word[i] == guess[i]:
        image += GREEN_BOX
    else:
        truth: bool = False
        x: int = 0
        while not truth and x < len(secret_word):
            if secret_word[x] == guess[i]:
                truth = True
            x += 1
        if truth:
            image += YELLOW_BOX
        else:
            image += WHITE_BOX

    i += 1

print(image)
if guess == secret_word:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")