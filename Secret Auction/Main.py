from Class import Bidder,Item

# No draws, the first person to bid the highest amount wins.
# it does not change even if another person placed the same value as the person with the highest bid
# The program can take any amount of bidders 0 - ~


def Num_of_bidders():
    """
    This function collects an int as number of bidders,

    it prompts user to add a name and bid amount repeatedly until the num of bidders is met
    :returns Number of bidders as an integer:
    """
    while True:
        try:
            N_bidders = int(input("How many bidders are there?: "))
            break
        except ValueError:
            print("Invalid input")
    return int(N_bidders)


def validation(bidder_name):
    """
    checks for the validity of a bidder name
    it does not allow symbols,whitespaces or numbers in bidder's name
    :param bidder_name:
    """
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    symbols = ['!', '@', '$', '%', '^', '&', '*',' ', '(', ')', '_', '-', '+', '=', '}', ']', '{', '[', '|', '\\', ':', ';',
               '/', '?', '.', '>', ',', '<', '`', '~', ']', '}']
    for char in bidder_name:
        if char in numbers:
            raise TypeError("Invalid name. Name cannot contain numbers")
        if char in symbols:
            raise TypeError("Invalid name. Name cannot contain symbol(s)")


def list_bidders():
    """
    This function does not allow for invalid names as well
    str-name and int-bid amount
    :returns Lists of bidders:
    """
    list_of_bidders_ = []
    for index in range(Num_of_bidders()):
        while True:
            try:
                bidder_name = input(f"{index + 1}. Bidder's name: ").lower()
                validation(bidder_name)
                bidder_bid = int(input("Bid amount: "))
                break
            except TypeError as err:
                print(err)
            except ValueError:
                print("Invalid bid amount")

        bidder = Bidder(name=bidder_name, bid=bidder_bid)
        list_of_bidders_.append(bidder)
        print("Bid has been placed")
    return list_of_bidders_

list_of_bidders = list_bidders()


def bid_winner():
    """
    heavy liftings: This functions determines the winner and then prints it out to the console

    responsible for adding a new bidder or changing an old bidder's bid

    it does not return anything
    """
    try:
        list_of_bidders.append(Item(name="Item_for_sale",bid=0))
        # Length of the list will always be > 1, since an Item is automatically appended to it
        if len(list_of_bidders) > 0:
            winning_bid = list_of_bidders[0].bid
            for bidder in list_of_bidders:
                if bidder.bid >= winning_bid:
                    winning_bid = bidder.bid
                    winner = bidder
        ask_ = input("(n) To add/change a bidder's bid.\n(y) To show highest bid\n>>> ")
        if ask_ == 'y':
            if len(list_of_bidders) <= 1:
                raise UnboundLocalError("No bid has been made")
            else:
                print(f"The highest bid is N{winner.bid}\n{winner.name.title()} won the bid.")
        elif ask_ == 'n':
            try:
                while True:
                    name = input("Name: ").lower()
                    validation(name)
                    bid = int(input("Bid amount: "))
                    break
            except ValueError:
                print("Invalid bid amount")
            list_of_bidders.append(Bidder(name=name, bid=bid))
            bid_winner()
        else:
            print("Invalid input")
            bid_winner()
    except UnboundLocalError as err:
        print(err)


bid_winner()

# phewwww....aswear nor be small work be dis
