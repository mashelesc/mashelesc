"""
A program that replaces each space in a sentence with ...
"""

def playback(string: str) -> str:
    return string.replace(" ", "...")

userInput: str = str(input("Please enter a sentence: "))
newString: str = playback(userInput)

print(newString)