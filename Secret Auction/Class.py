class Bidder:

    def __init__(self,name,bid):
        self.name = name
        self.bid = bid


class Item(Bidder):

    def __int__(self,name,bid):
        super().__init__(name,bid)
