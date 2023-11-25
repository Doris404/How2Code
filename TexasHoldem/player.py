""" player.py """
import numpy as np

class Player():
    def __init__(self, card1, card2):
        self.card1 = card1
        self.card2 = card2
    def show(self):
        print(self.card1, self.card2)
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
            player = Player(self.deliver_player_cards[i][0], self.deliver_player_cards[i][1])
            self.player_list.append(player)
    def show(self):
        print('player_num: ', self.player_num)
        print('play_list: ')
        for i in range(self.player_num):
            self.player_list[i].show()
        