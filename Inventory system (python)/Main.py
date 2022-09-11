houses = [
    {
        "number":1,
        "house":"Self contain",
        "wood":50,
        "rod":50,
        "cement":50,
        "price":2500
    },
    {
        "number": 2,
        "house": "Bungalow",
        "wood": 120,
        "rod": 70,
        "cement": 200,
        "price":5000
    },
    {
        "number": 3,
        "house": "Palace",
        "wood": 500,
        "rod": 270,
        "cement": 580,
        "price":15000
    },]


def Inventory_system():
    try:
        name = input("Name: ").lower()
        if name.isdigit() or name.isnumeric():
            raise Exception("Name should be a string")
        money = int(input("Input budget: "));wood = int(input("Wood: "));rod = int(input("rod: "))
        cement = int(input("cement: "))
    except Exception as err:
        print(err)
        Inventory_system()

    def choice_():
        choice = int(input(f"You have {wood}xwoods, {rod}xrods and {cement}xcements\n1.\
Self contain\n2. Bungalow\n3. Palace\nWhich do you want to build? "))

    choice = int(input(f"You have {wood}xwoods, {rod}xrods and {cement}xcements\n1.\
Self contain\n2. Bungalow\n3. Palace\nWhich do you want to build? "))

    for item in houses:
        if choice == item["number"]:
            house = item["house"]
            required_wood = item["wood"];required_rod = item["rod"];required_cement = item["cement"]
            house_price = item["price"]
    if not(choice in range(1,len(houses))):
        print("Invalid input");quit()

    try:
        if wood >= required_wood:
            if rod >= required_rod:
                if cement >= required_cement:
                    if money >= house_price:
                        print(f"You have built a {house}")
                    else:
                        print("Insufficient funding")
                else:
                    print(f"Cement is not enough for a {house}")
            else:
                print(f"Rod is not enough for a {house}")
        else:
            print(f"Wood is not enough for a {house}")

    except ValueError:
        print("An error occurred")
        if input("Do you want to try again? ") == 'yes':
            Inventory_system()
        else:
            print("Okay");quit()

Inventory_system()
