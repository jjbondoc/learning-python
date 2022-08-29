# importing an object from the sys module
# argv = argument variable
# it is a list that contains all the command-line arguments passed to the script
from sys import argv
# unpacking argv, so that instead of holding all of the arguments,
# each one is assigned to its own variable
script, first, second, third = argv

print("The first script is called:", script)
print("Your first variable is:", first)
print("Your second variable:", second)
print("Your third variable:", third)

extra = input("Extra variable please: ")

print(f"Here's your extra variable: {extra}")
print(f"And here they all are: {first}, {second}, {third} and {extra}.")