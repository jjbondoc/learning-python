types_of_people = 10
x = f"There are {types_of_people} types of people."

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

# printing the strings stored in variables x, y
print(x)
print(y)

# using an f-string
print(f"I said: {x}")
print(f"I also said: '{y}'")

# the {} brackets allows the use of .format()
# because there is only one {}, you can only pass
# one argument in the .format() method
hilarious = True
joke_evaluation = "Isn't that joke so funny?! {}"

print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

# concatenation of strings
print(w + e)