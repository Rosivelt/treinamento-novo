#_*_ coding: utf-8 _*_

import collections
Card = collections.namedtuple('Carta',['ranking','naipe'])
class Buraco(object):
    ranks = [str(n) for n in range(2,11)]+list('JQKA')
    suits = 'espada ouros copas paus'.split()

    def __init__(self):
    # Construtor da classe 
        self._cards = [Card(ranking,naipe) for naipe in self.suits
                                           for ranking in self.ranks]
    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]
