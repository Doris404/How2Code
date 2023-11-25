""" card.py """
import random

class Suit():
    """ Suit 
    H (Heart), D(diamond), C (club), S (spade)
    """
    def __init__(self, suit):
        self.suit = suit
class Point():
    """ Point
    A, 2, 3, 4, 5, 6, 7, 8, 9, T, J, Q, K
    """
    def __init__(self, point):
        self.point = point
class Card():
    def __init__(self, suit, point):
        self.suit = suit
        self.point = point

class Pattern():
    def __init__(self, card1, card2, card3, card4, card5, card6, card7):
        self.card1 = card1
        self.card2 = card2
        self.card3 = card3
        self.card4 = card4
        self.card5 = card5
        self.card6 = card6
        self.card7 = card7
    def pattern(self):
        # Need to summary pattern types
        if True:
            pattern = 'Royal Flush'
        self.pattern = pattern
class Decision():
    def __init__(self, pattern1, pattern2):
        self.pattern1 = pattern1
        self.pattern2 = pattern2
    def compare(self):
        if self.pattern1 > self.pattern2:
            return self.pattern1
        elif self.pattern2 > self.pattern1:
            return self.pattern2
        else:
            return 1
class Cards():
    def __init__(self, config):
        self.config = config
        self.full_cards = self.config['full_cards']
        card_num = 2 * self.config['player_num'] + 3 + 1 + 1
        self.card_num = card_num
    def deliver(self):
        random.shuffle(self.full_cards)
        shuffled_cards = self.full_cards
        chosen_cards = shuffled_cards[:self.card_num]
        player_flag = 2 * self.config['player_num']
        player_cards = chosen_cards[:player_flag]
        flop_cards = chosen_cards[player_flag:player_flag+3]
        turn_card = chosen_cards[player_flag + 3]
        river_card = chosen_cards[player_flag + 4]
        self.chosen_cards = chosen_cards
        self.player_cards = player_cards
        self.flop_cards = flop_cards
        self.turn_card = turn_card
        self.river_card = river_card