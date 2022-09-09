# About to add a payment system
# Ask the user to either pay with a card or cash
# Collect the card if its valid and account balance is sufficient


from Modules import *

print('Espresso is N200, Latte is N300, Cappucino is N500.')
# Global Variables 
WATER,MILK,COFFEE,DRINKS = 700,500,300,DRINKS
MONEY = Transaction()
try:
    def Coffee_machine():
        """ This is a coffee machine function,
        
            Based off of the resources at stock, products are produced.
            When money is not sufficient it asks for more.
            Returns excess money as well
            
        """
        
        def Inventory_stuff(product):
            """Shows and sorts out stuffs we have in inventory,
            
                To determine the possibility of producing a product.
            """
            global WATER;global MILK;global COFFEE;global DRINKS
            if product != 'report':
                _D = DRINKS[product]
                amount_water, amount_milk, amount_coffee = \
                    _D['amount_of_water'], _D['amount_of_milk'], _D['amount_of_coffee']
                if WATER >= amount_water and MILK >= amount_milk and COFFEE >= amount_coffee:
                    for key in DRINKS:
                        if key == product:
                            WATER -= amount_water
                            MILK -= amount_milk
                            COFFEE -= amount_coffee
                else:
                    print(f"Sorry Insuficient resources for a {product}")
                    print(f"Here is your money N{MONEY}")
                    quit()
        def Money_back(refund):
            print(f"Here is your change N{refund}")
            quit()
    
        def Logicals():
            """This is where all the reasoning and conditons are sorted.
            
                Function that checks for all the logicals and provides feedback..
                It also returns the product chosen by the customer

            """
            try:
                global MONEY
                global DRINKS  
                Drink= input('What would you like? (espresso,latte,cappucino): ').lower()
                Inventory_stuff(Drink)   
                if Drink == 'report':
                    print(f'Water = {WATER}ml\nMilk = {MILK}ml\nCoffee = {COFFEE}ml')
                    Coffee_machine()
                # Using for loop to check through all the items in DRINKS for a match with the Drink provided by the customer
                for key in DRINKS:  
                    product = key
                    if Drink == product:
                        if  MONEY >= DRINKS[product]['price']:
                            REFUND = MONEY - DRINKS[product]['price']
                            print(f"Enjoy your drink\nYour change is N{REFUND}")
                            break
                        else:
                            print(f"Sorry {product} costs N{DRINKS[product]['price']}")
                            __ = input('Do you which to add more money? ').lower()
                            if __ == 'yes':
                                MONEY = change(MONEY)
                                Coffee_machine()
                                break
                            else:
                                Money_back(MONEY)
                                
            
                # Prompts the user to choose between purchasing and quiting
                while True:       
                    __= input('Continue purchasing?').lower()
                    if __ == 'yes':
                        if  REFUND >= 200:
                            MONEY = REFUND
                            Coffee_machine()
                            break
                        else:
                            print("Currect balance can not purchase any item.")
                            __ = input('Do you which to add more money? ').lower()
                            if __ == 'yes':
                                MONEY = change(REFUND)
                                Coffee_machine()
                                break
                            elif __ == 'no':
                                if REFUND > 0:
                                    Money_back(REFUND)
                                
                                
                    elif __ == 'no':
                        if  REFUND > 0: 
                            Money_back(REFUND)
                    else:
                        print('Input a yes or no answer please.')
                        
                        continue
                    return Drink
            except KeyError:
                print(f"{Drink} is not a valid input")
                Coffee_machine()
                
        Logicals()
        

    Coffee_machine()

except TypeError:  # This is a bug i could not fix so i caught it and just end the program.
    print("An error occured please try again later.")

finally:
    print("Thank you for shopping with us.")
