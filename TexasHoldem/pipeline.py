""" pipeline.py """
from player import Player, Players
from card import Cards
import os
import json
import datetime
from datetime import timezone, timedelta
import argparse

timestamp = datetime.datetime.now().astimezone(timezone(timedelta(hours=8))).strftime("%Y%m%d")
id_ = datetime.datetime.now().astimezone(timezone(timedelta(hours=8))).strftime("%Y%m%d-%H%M%S")
try:
    os.mkdir("../{}".format(timestamp))
except:
    pass

parser = argparse.ArgumentParser()
parser.add_argument("--config_file", type=str, default='config.json')
args = parser.parse_args()
config_file = args.config_file
config = json.load(open("{}".format(config_file)))

if __name__ == "__main__":
    print("Hello, this is a Texas Holdem game with {} players!".format(str(config['player_num'])))
    print("Your role is: {}".format(config['my_role']))
    """ First Deal: 2 cards for each player """
    # cards
    cards = Cards(config)
    cards.deliver()
    players = Players(config)
    players.deliver(cards.player_cards)
    
    # deal
    for player in players.player_list:
        price = player.bet()
        # print(price)
    players.show()    
    """ Second Deal:  """
    # cards
    flop_cards = cards.flop_cards
    # print('flop cards: ', flop_cards)
    # deal
    """ Third Deal: """
    # cards
    turn_card = cards.turn_card
    # print('turn_card: ', turn_card)
    # deal
    """ Fourth Deal """
    # cards
    river_card = cards.river_card
    # print('river card: ', river_card)
    # deal
    """ Show Time: """
    # winner decision