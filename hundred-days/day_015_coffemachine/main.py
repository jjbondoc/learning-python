MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def get_requirements(drink):
    """Obtain the requirements of a drink"""
    requirements = {}
    drink_ingredients = MENU[drink]['ingredients']
    requirements['cost'] = MENU[drink]['cost']
    requirements['water'] = drink_ingredients['water']
    if drink != 'espresso':
        requirements['milk'] = drink_ingredients['milk']
    else:
        requirements['milk'] = 0
    requirements['coffee'] = drink_ingredients['coffee']
    
    return requirements

#TODO 3. Print Report
def print_report(water_supply, milk_supply, coffee_supply, wallet):
    """Output the status of the coffee machine resources."""
    print(f"Water: {water_supply}ml")
    print(f"Milk: {milk_supply}ml")
    print(f"Coffee: {coffee_supply}g")
    print(f"Money: ${wallet:.2f}")

#TODO 4. Check resources sufficient to make drink order
def sufficient_resources(water_supply, milk_supply, coffee_supply, drink):
    """Check whether the coffee machine has enough resources for the drink ordered."""
    if water_supply < get_requirements(drink)['water']:
        print("Sorry there is not enough water.")
        return False
    elif milk_supply < get_requirements(drink)['milk']:
        print("Sorry there is not enough milk.")
        return False
    elif coffee_supply < get_requirements(drink)['coffee']:
        print("Sorry there is not enough coffee.")
        return False
    else:
        return True

#TODO 6. Check transaction is successful
def successful_transaction(money_given, drink):
    """Check whether the customer has inserted enough coins for the drink ordered."""
    change = round(money_given - get_requirements(drink)['cost'], 2)
    if money_given < get_requirements(drink)['cost']:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        print(f"Here is ${change:.2f} in change.")
        return True

#TODO 7. Make coffee and update resources
def update_resources(water_supply, milk_supply, coffee_supply, wallet, drink):
    """Update the coffee machine's resources after a successful order."""
    water_supply = water_supply - get_requirements(drink)['water']
    milk_supply = milk_supply - get_requirements(drink)['milk']
    coffee_supply = coffee_supply - get_requirements(drink)['coffee']
    wallet = wallet + get_requirements(drink)['cost']
    return water_supply, milk_supply, coffee_supply, wallet 
    

#TODO 1. Prompt user asking: "What would you like?"
def coffee_machine():
    turned_off = False
    water = resources['water']
    milk = resources['milk']
    coffee = resources['coffee']
    money = 0
    
    while not turned_off:
        drink_order = input("   What would you like? (espresso/latte/cappuccino): ")
        if drink_order in ['espresso', 'latte', 'cappuccino']:
            
            if sufficient_resources(water, milk, coffee, drink_order):
                #TODO 5. Process coins
                print("Please insert coins.")
                quarters = int(input("How many quarters?: ")) * 0.25
                dimes = int(input("How many dimes?: ")) * 0.10
                nickles = int(input("How many nickles?: ")) * 0.05
                pennies = int(input("How many pennies?: ")) * 0.01
                total = quarters + dimes + nickles + pennies
                
                if successful_transaction(total, drink_order):
                    print(f"Here is your {drink_order} ☕. Enjoy!")
                    water, milk, coffee, money = update_resources(water, milk, coffee, money, drink_order)
        
        elif drink_order == 'report':
            print_report(water, milk, coffee, money)
            
        #TODO 2. Turn off the coffee machine 
        elif drink_order == 'off':
            turned_off = True
            
        else:
            print("Sorry, that's not a valid order.")

coffee_machine()