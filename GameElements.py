from CardExceptions import SuitException, RankException, InvalidArgumentException

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
