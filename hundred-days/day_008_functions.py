#Write your code below this line 👇
import math
def prime_checker(number):
    max_number = math.ceil(number/2)
    for _ in range(2, max_number):
        print(_)
        if number % _ == 0:
            print("It's not a prime number.")
            break
    else:
        print("It's a prime number.")
    




#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)