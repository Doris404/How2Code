""" player.py """
import numpy as np
import random

class Role():
    def __init__(self, role):
        """ Role
        SB (Small Blind) BB (Big Blind) T (Trigger) O (Other players) D (Dealer)
        """
        self.role = role
class Robot():
    def __init__(self, robot):
        """
        True (is robot) False (not robot)
        """
        self.robot = robot
class Player():
    def __init__(self, card1, card2, robot=True, role=None, idx=None, name='Robot'):
        self.card1 = card1
        self.card2 = card2
        self.robot = robot
        self.role = role
        self.idx = idx
        self.name = name
    def show(self):
        print(self.idx, self.name, self.card1, self.card2, self.role)
    def is_robot(self):
        return self.robot
    def bet(self): # need strategy here
        if self.robot:
            return 10
        else:
            bet = input("Please bet: ")
            return bet
class Players():
    def __init__(self, config):
        self.config = config
        self.player_num = self.config['player_num']
    def deliver(self, player_cards):
        self.player_cards = player_cards
        self.deliver_player_cards = np.array(player_cards).reshape((-1,2))
        self.deliver_player_cards = list(self.deliver_player_cards)
        self.player_list = []
        for i in range(self.player_num):
            player = Player(idx=i, card1=self.deliver_player_cards[i][0], card2=self.deliver_player_cards[i][1])
            if i == 0:
                player.role = 'SB'
            elif i == 1:
                player.role = 'BB'
            elif i == 2:
                player.role = 'T'
            elif i == self.player_num - 1:
                player.role = 'D'
            else:
                player.role = 'O'
            self.player_list.append(player)
        if self.config['my_role'] == 'SB':
            self.player_list[0].name = 'You'
            self.player_list[0].robot = False
        elif self.config['my_role'] == 'BB':
            self.player_list[1].name = 'You'
            self.player_list[1].robot = False 
        elif self.config['my_role'] == 'T':
            self.player_list[2].name = 'You'
            self.player_list[2].robot = False
        elif self.config['my_role'] == 'D':
            self.player_list[self.player_num-1].name = 'You'
            self.player_list[self.player_num-1].robot = False
        elif self.config['my_role'] == 'O':
            idx = random.randint(3, self.player_num-2)
            self.player_list[idx].name = 'You'
            self.player_list[idx].robot = False
        else:
            raise ValueError("config setting error: my_role should be one of SB/BB/T/D/O")
    def show(self):
        print('player_num: ', self.player_num)
        print('play_list: ')
        for i in range(self.player_num):
            self.player_list[i].show()
class Deal():
    def __init__(self, price, player):
        self.price = price
        self.player = player
    def show(self):
        print(self.player.idx, self.player.name, self.player.role, self.price)
class Deals():
    def __init__(self, turn):
        self.turn = turn
        self.deal_list = []
    def show(self):
        for i in range(len(self.deal_list)):
            self.deal_list[i].show()    