"""
A program that takes user input and converts it to a lowercase string
"""

def toLower(string: str) -> str:
    return string.lower()

userString: str = str(input("Enter a string: "))
newString = toLower(userString)

print(newString)