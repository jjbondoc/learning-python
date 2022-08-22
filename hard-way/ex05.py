name = 'Joselito Bondoc'
age = 24 # not a lie
height = 172 # cm
height_inches = round(height / 2.54)
weight = 70 # kg
weight_pounds = round(weight * 2.20462)
eyes = 'Dark-brown'
teeth = 'White'
hair = 'Black'

print(f"Let's talk about {name}.")
print(f"He's {height} centimetres or {height_inches} inches tall.")
print(f"He's {weight} kilograms or {weight_pounds} lbs heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")