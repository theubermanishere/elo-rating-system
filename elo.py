#!/usr/bin/python3

""" An implementation of the Elo rating system to be used for ranking during 
competitions
"""

from math import pow, floor, ceil

WIN = 1
LOSS = 0
DRAW = 0.5

class Elo:
    """ Creates a object that contains a particular participants information
    and other related methods.

    usage: obj = Elo(rank=1400,k=32)
    """

    game = 0

    def __init__(self, rank=1400, k=32):
        self.rank = rank
        self.k = k

    def expectancy(self, b):
        """ Calculate self win expectancy against an opponent. """
        exp = 1 / (1 + pow(10, (b - self.rank) / 400))
        return exp

    def winsAgainst(self, b):
        """ Calculates and changes rank of both self and opponent 
        if self wins. """
        self.game = self.game + 1
        b.game = b.game + 1
        self.rank = self.rank + int(round(self.k * (WIN 
            - self.expectancy(b.rank))))
        b.rank = b.rank + int(round(self.k * (LOSS - b.expectancy(self.rank))))

    def loseAgainst(self, b):
        """ Calculates and changes rank of both self and opponent
        if self loses. """
        self.game = self.game + 1
        b.game = b.game + 1
        self.rank = self.rank + int(round(self.k * (LOSS 
            - self.expectancy(b.rank))))
        b.rank = b.rank + int(round(self.k * (WIN - b.expectancy(self.rank))))

    def drawAgainst(self, b):
        """ Calculates and changes rank of both self and opponent
        if the match is a draw. """
        self.game = self.game + 1
        b.game = b.game + 1
        self.rank = self.rank + int(round(self.k * (DRAW 
            - self.expectancy(b.rank))))
        b.rank = b.rank + int(round(self.k * (DRAW - b.expectancy(self.rank))))

    def games(self):
        return (self.games)

# Sample Implementation
if __name__ == "__main__":
    a = Elo(1300)
    b = Elo(1500)
    print(a.rank)
    a.winsAgainst(b)
    print(a.rank)
    print(b.rank)
    a.loseAgainst(b)
    print(a.rank)
    print(b.rank)
    a.drawAgainst(b)
    print(a.rank)
    print(b.rank)

