"""Structured wordle."""

__author__ = "730466575"


def input_guess(expected_length: int) -> str:
    """Get input."""
    guess: str = input(f"Enter a {expected_length} character word: ")
    while len(guess) != expected_length:
        guess = input(f"That wasn't {expected_length} chars! Try again: ")
    return guess
    

def contains_char(word: str, letter: str) -> bool:
    """Search for character in word."""
    assert len(letter) == 1
    i: int = 0
    while i < len(word):
        if word[i] == letter:
            return True
        i += 1
    return False


def emojified(guess: str, secret: str) -> str:
    """Create emoji."""
    assert len(guess) == len(secret)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    i: int = 0
    emoji: str = ""
    while i < len(secret):
        if guess[i] == secret[i]:
            emoji += GREEN_BOX
        else:
            if contains_char(secret, guess[i]):
                emoji += YELLOW_BOX
            else:
                emoji += WHITE_BOX
        i += 1
    return emoji


def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret_word: str = "codes"
    guess: str = ""
    i: int = 1
    while i <= 6 and guess != secret_word:
        print(f"=== Turn {i}/6 ===")
        guess = input_guess(len(secret_word))
        print(emojified(guess, secret_word))
        if guess == secret_word:
            print(f"You won in {i}/6 turns!")
        i += 1
    if guess != secret_word:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()
