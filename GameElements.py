from CardExceptions import SuitException, RankException, InvalidArgumentException, InvalidHandException, IncompleteHandException

RANK_ORDER = "23456789TJQKA"
SUITS = "SCHD"

HIGH_CARD,PAIR,TWO_PAIR,TRIPS,STRAIGHT,FLUSH,FULL_HOUSE,QUADS,STRAIGHT_FLUSH,ROYAL_FLUSH = range(10)

def rank_to_str(rank:int) -> str:
    return RANK_ORDER[rank]

def str_to_rank(s:str) -> int:
    return RANK_ORDER.index(s)
class Card:
    def __init__(self, rank, suit):
        if not rank or not suit or len(rank) != 1 or len(suit) != 1:
            raise InvalidArgumentException()
        
        rank = rank.upper()
        suit = suit.upper()

        if rank not in RANK_ORDER:
            raise RankException()
        
        if suit not in SUITS:
            raise SuitException()

        self.rank = RANK_ORDER.index(rank)
        self.suit = suit

class Hand:
    def __init__(self, *args):
        if not args or 2 < len(args) < 5:
            raise IncompleteHandException()

        if len(args) > 5:
            raise InvalidHandException()
        
        self.hand = sorted(args, key=lambda x: x.rank, reverse=True)

    def rank(self):
        ranks = {}
        suits = set()

        for card in self.hand:
            ranks[card.rank] = ranks.get(card.rank,0) + 1
            suits.add(card.suit)
        
        sorted_ranks = sorted(ranks.items(), key = lambda item: (-item[1], -item[0]))

        rank_keys, rank_counts = [], []
        for key, value in sorted_ranks:
            rank_keys.append(key)
            rank_counts.append(value)
            

        is_flush = len(suits) == 1
        unique_ranks = sorted(set(card.rank for card in self.hand), reverse=True)

        is_straight = len(unique_ranks) == 5 and unique_ranks[0] - unique_ranks[4] == 4


        # wheel case
        if unique_ranks == [12,3,2,1,0]:
            is_straight = True
            unique_ranks = [3,2,1,0,-1]
        
        if is_straight and is_flush:
            if unique_ranks[0] == 12:
                return (ROYAL_FLUSH,)   
            return (STRAIGHT_FLUSH, unique_ranks[0])
        
        if rank_counts == [4,1]:
            return (QUADS, (rank_keys[0], rank_keys[1]))

        if rank_counts == [3,2]:
            return (FULL_HOUSE, (rank_keys[0], rank_keys[1]))

        if is_flush:
            return (FLUSH, *rank_keys)
        
        if is_straight:
            return (STRAIGHT, unique_ranks[0])

        if rank_counts == [3,1,1]:
            return (TRIPS, (rank_keys[0], rank_keys[1], rank_keys[2]))
        
        if rank_counts == [2,2,1]:
            return (TWO_PAIR, (rank_keys[0], rank_keys[1], rank_keys[2]))

        if rank_counts == [2,1,1,1]:
            return (PAIR, (rank_keys[0], rank_keys[1], rank_keys[2], rank_keys[3]))

        return (HIGH_CARD, *rank_keys)



        






        
    


        
        


