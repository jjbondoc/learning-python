from sys import argv
#
script, first, second, third = argv

print("The first script is called:", script)
print("Your first variable is:", first)
print("Your second variable:", second)
print("Your third variable:", third)

extra = input("Extra variable please: ")

print(f"Here's your extra variable: {extra}")
print(f"And here they all are: {first}, {second}, {third} and {extra}.")