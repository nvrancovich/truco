import time
import random

from cards import CARDS

def shuffle(deck, hand):
    print('shuffling.')
    time.sleep(1)
    print('shuffling..')
    time.sleep(1)
    print('shuffling...')
    time.sleep(1)
    print(random.sample(deck, hand))

def score(player_score, oponent_score):
    player_score_list = list()
    oponent_score_list = list()
    for i in range (0, player_score):
        player_score_list.append('/')
    for i in range (0, oponent_score):
        oponent_score_list.append('/')
    player_score = ''.join(i for i in player_score_list)
    oponent_score = ''.join(i for i in  oponent_score_list)
    print(f'Yo: {player_score[:5]} {player_score[5:10]} {player_score[10:15]} {player_score[15:20]} {player_score[20:25]} {player_score[25:30]}')
    print(f'El: {oponent_score[:5]} {oponent_score[5:10]} {oponent_score[10:15]} {oponent_score[15:20]} {oponent_score[20:25]} {oponent_score[25:30]}')

shuffle(CARDS, 3)
score(23, 16)