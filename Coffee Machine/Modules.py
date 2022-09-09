DRINKS = {
    'espresso':
        {
            'price':200,
            'water':80,
            'milk':10,
            'coffee':5,
            'amount_of_water':80,
            'amount_of_milk':10,
            'amount_of_coffee':5
        },
    'latte':
        {
            'price':300,
            'water':160,
            'milk':90,
            'coffee':30,
            'amount_of_water':160,
            'amount_of_milk':90,
            'amount_of_coffee':30
        },
    'cappucino':
        {
            'price':500,
            'water':250,
            'milk':100,
            'coffee':60,
            'amount_of_water':250,
            'amount_of_milk':120,
            'amount_of_coffee':60
        }
}


def Transaction():
    try:
        MONEY = 0
        if MONEY >= 200:
            pass
        else:
            Twenty_naira = int(input('How many N20? ')) * 20
            Fifty_naira= int(input('How many N50? ')) * 50
            Hundred_naira = int(input('How many N100? ')) * 100
            MONEY = (Twenty_naira + Fifty_naira + Hundred_naira)
        return MONEY
    except ValueError:
        print("Input a valid money.")
        func = Transaction()

def change(REFUND):
    try:
        Twenty_naira = int(input('How many N20? ')) * 20
        Fifty_naira= int(input('How many N50? ')) * 50
        Hundred_naira = int(input('How many N100? ')) * 100
        REFUND += (Twenty_naira + Fifty_naira + Hundred_naira)
        return REFUND
    except ValueError:
        print("Input a valid money.")
        change(REFUND)



