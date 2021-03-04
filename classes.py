import random

suits = ('hearts', 'diamonds', 'spades', 'clubs')
ranks = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace')
values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
          '9': 9, '10': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}


class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
        self.name = self.rank + ' of ' + self.suit

    def __str__(self):
        return self.rank + ' of ' + self.suit


class Deck:

    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.all_cards)
        random.shuffle(self.all_cards)

    def deal(self, number):
        cards_being_dealt = []
        for each in range(0, number):
            cards_being_dealt.append(self.all_cards.pop(0))

        return cards_being_dealt


class Chips:

    def __init__(self, number):
        self.number = number


class Player:

    def __init__(self, name, index):
        self.name = name
        self.index = index
        self.cards = []
        self.cards2 = []
        self.cards_sets = []
        self.chips = Chips(10)

    def place_bet(self):
        print(f'{self.name} has {self.chips.number} chips')
        chips = 'sjdnkfsdf'

        while chips.isdigit() == False or int(chips) not in range(1, self.chips.number+1):
            chips = input("Place your bet in chips[you can't go over your your current balance and minimum is 1 chip]: ")

        print(f'{self.name} has placed a bet of {chips} chips')
        return int(chips)

    def play(self):
        choice = 'dfsgsdg'
        while choice not in ['H', 'S', 'D']:
            choice = input(f'{self.name} choose to Hit[H], Stay[S] or Double Down[D]: ')
        return choice

    def __str__(self):
        return f'{str(self.name)} has {str(len(self.cards))} cards and {str(self.chips.number)} chips'

