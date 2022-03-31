def while_count(a, b):
    i = 0
    numbers = []
    while i < a:
        print(f"At the top i is {i}")
        numbers.append(i)

        i = i + b
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")
    return numbers

def for_count(a, b, c):
    numbers = []
    for i in range(a, b, c):
        print(f"At the top i is {i}")
        numbers.append(i)

        print("Numbers now: ", numbers)
        print(f"At the bottom i is still {i}")
    return numbers
        
# numbers = while_count(11, 2)
numbers = for_count(0, 11, 2)

print("The numbers: ")

for num in numbers:
    print(num)