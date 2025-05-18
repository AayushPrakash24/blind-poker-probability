from CardExceptions import SuitException, RankException, InvalidArgumentException, InvalidHandException

class Card:
    def __init__(self, rank, suit):
        if not rank or not suit or len(rank) != 1 or len(suit) != 1:
            raise InvalidArgumentException()
        
        self.rank = rank.upper()
        self.suit = suit.upper()

        if self.rank not in "23456789TJQKA":
            raise RankException()
        
        if self.suit not in "SCHD":
            raise SuitException()

class Hand:
    def __init__(self, *args):
        if not args or 2 < len(args) < 5:
            raise InvalidHandException("Incomplete hand.")

        if len(args) > 5:
            raise InvalidHandException("Too many cards.")
        
        self.hand = sorted(*args, key=lambda x: x.rank)
        

        
    


        
        


