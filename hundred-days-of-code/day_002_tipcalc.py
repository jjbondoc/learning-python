print("Welcome to the tip calculator!")

total_bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))/100 + 1
people = int(input("How many people to split the bill? "))

cost = round(total_bill/people*tip, 2)
# a formatted string that forces to print to 2 decimal places
cost = "{:.2f}".format(cost)

message = f"Each person should pay: ${cost}"

print(message)