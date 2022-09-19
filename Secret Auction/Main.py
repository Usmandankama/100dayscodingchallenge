from Class import Bidder,Item
# No draws, the first person to bid the highest amount wins.
# it does not change even if another person placed the same value as the person with the highest bid
# The program can take any amount of bidders 0 - ~

items = [
    {"number":'1',"alpha_num":"one","price":20000},
    {"number":'2',"alpha_num":"two","price":30000},
    {"number":'3',"alpha_num":"three",'price':1000}
]


def auction():
    try:
        print("Choose item to start bidding on.\n1.Sarcophagus\n2.King Richard the second's Bugatti\n3.War helmet ")
        chose_item = input(">>>> ")
        # You can input any of the following list items, and it'll work
        if not(chose_item in ['1','2','3','one','two','three']):
            print("Invalid item number")
            auction()
        for item in items:
            if chose_item == item["number"]:
                item_price = item["price"]
            elif chose_item.lower() == item["alpha_num"]:
                item_price = item["price"]

        def Num_of_bidders():
            """
            This function collects an int as number of bidders,

            it prompts user to add a name and bid amount repeatedly until the num of bidders is met
            :returns Number of bidders as an integer:
            """
            while True:
                try:
                    N_bidders = int(input(f"Bids cannot be less than N{item_price}\nHow many bidders are there?: "))
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
                    raise Exception("Invalid name. Name cannot contain numbers")
                if char in symbols:
                    raise Exception(f"Invalid name. Name cannot contain '{char}'")

        def bidder_details_(index):
            """
            Takes an index as a parameter and returns the name of the bidder and also the bid amount
            :param index:
            :return bidder_name, bidder_bid:
            """
            while True:
                try:
                    bidder_name = input(f"{index + 1}. Bidder's name: ").lower()
                    validation(bidder_name)
                    bidder_bid = int(input("Bid amount: "))
                    if bidder_bid < item_price:
                        raise Exception(f"Amount cannot be less than item price (N{item_price})")
                    break
                except ValueError:
                    print("Invalid bid amount")
                except Exception as error:
                    print(error)
            return bidder_bid,bidder_name

        def list_bidders():
            """
            This function does not allow for invalid names as well
            str-name and int-bid amount
            :returns Lists of bidders:
            """
            list_of_bidders_ = []
            for index in range(Num_of_bidders()):
                while True:
                    bidder_details = bidder_details_(index)
                    bidder_bid = bidder_details[0]
                    bidder_name = bidder_details[1]

                    break
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
            list_of_bidders.append(Item(name="Item_for_sale",bid=0))
            index = 0
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
                    raise Exception("No bid has been made")
                elif len(list_of_bidders) > 1 and (winner.name != 'Item_for_sale'):
                    print(f"The highest bid is N{winner.bid}\n{winner.name.title()} won the bid.")
                else:
                    print("No bid has been made.")
            elif ask_ == 'n':

                while True:
                    bidder_details = bidder_details_(index)
                    bidder_name = bidder_details[1]
                    bidder_bid = bidder_details[0]

                    break

                list_of_bidders.append(Bidder(name=bidder_name, bid=bidder_bid))
                bid_winner()
            else:
                print("Invalid input")
                bid_winner()

        bid_winner()
    except ValueError:
        print("invalid input")
        auction()
    except NameError:
        pass
    except Exception as err:
        print(err)


auction()
# phewwww....aswear nor be small work be dis
