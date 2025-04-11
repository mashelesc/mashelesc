"""
A program that prompts the user for mass as an integer and then outputs the equivalent number of joules
"""

c: float = 3 * (10**8)
def einstein(mass: int) -> int:
    return mass * (c ** 2)

mass: int = int(input("Please enter the mass(kg) of the object: "))
print(einstein(mass))