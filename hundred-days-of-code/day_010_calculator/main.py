#* Calculator
from art import logo
# Add
def add(n1, n2):
    return n1 + n2

# Subtract 
def subtract(n1, n2):
    return n1 - n2 

# Multiply
def multiply(n1, n2):
    return n1 * n2 

# Divide
def divide(n1, n2):
    return n1 / n2

#* You can assign function names to variables and then call the function using the variable and passing arguments with it
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    print(logo)
    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)
        
    quit_calculator = False
    while not quit_calculator:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number: "))
        function = operations[operation_symbol]
        answer = function(num1, num2)
        
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        
        carry_on = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation.: ").lower()
        if carry_on == 'n':
            quit_calculator = True
            calculator()
        else:
            num1 = answer
    
calculator()