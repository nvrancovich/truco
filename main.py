import time
import random
import os

from cards import CARDS
from envido_values import ENVIDO_VALUES
from envido import envido

def clear(): 
    os.system('clear')

def hand(player_first, oponent_first, player_hand, oponent_hand):
    #When player go first
    if player_first:
        oponent_points = 0
        player_points = 0

        #First round
        player_first_round = int(input(f'Tu turno: 1) {player_hand[0]} 2) {player_hand[1]} 3) {player_hand[2]} 4) Envido 5) Real Envido 6) Falta Envido: '))
        print(player_first_round)
        #Envido
        if player_first_round >= 4:
            player_points, oponent_points = envido(player_first, oponent_first, player_hand, oponent_hand, player_first_round)
            player_first_round = int(input(f'Tu turno: 1) {player_hand[0]} 2) {player_hand[1]} 3) {player_hand[2]}: '))
        player_hand.remove(player_hand[player_first_round - 1])
        oponent_first_round = random.randint(0,2)
        print(f'Él tira un {oponent_hand[oponent_first_round]}!')
        oponent_hand.remove(oponent_hand[oponent_first_round])

        #Second round
        player_second_round = int(input(f'Tu turno: 1) {player_hand[0]} 2) {player_hand[1]}: '))
        player_hand.remove(player_hand[player_second_round - 1])
        oponent_second_round = random.randint(0,1)
        print(f'Él tira un {oponent_hand[oponent_second_round]}!')
        oponent_hand.remove(oponent_hand[oponent_second_round])

        #Third round
        player_third_round = int(input(f'Tu turno: 1) {player_hand[0]}: '))
        print(f'Él tira un {oponent_hand[0]}')

    return player_points, oponent_points

def shuffle(deck, hand):
    print('shuffling.')
    time.sleep(1)
    clear()
    print('shuffling..')
    time.sleep(1)
    clear()
    print('shuffling...')
    time.sleep(1)
    list = random.sample(deck, hand)
    player_hand = list[:3]
    oponent_hand = list[3:]
    return player_hand, oponent_hand

def score(player_score, oponent_score):
    player_score_list = []
    oponent_score_list = []
    for i in range (0, player_score):
        player_score_list.append('/')
    for i in range (0, oponent_score):
        oponent_score_list.append('/')
    player_score = ''.join(i for i in player_score_list)
    oponent_score = ''.join(i for i in  oponent_score_list)
    print(f'Yo: {player_score[:5]} {player_score[5:10]} {player_score[10:15]} {player_score[15:20]} {player_score[20:25]} {player_score[25:30]}')
    print(f'Él: {oponent_score[:5]} {oponent_score[5:10]} {oponent_score[10:15]} {oponent_score[15:20]} {oponent_score[20:25]} {oponent_score[25:30]}')

if __name__ == '__main__':
    clear()
    player_hand, oponent_hand = shuffle(CARDS, 6)
    player_score, oponent_score = 0, 0
    clear()
    score(player_score, oponent_score)
    print('')
    print(f'Tu mano: {player_hand}')
    print(f'Su mano: {oponent_hand}')
    new_points = hand(True, False, player_hand, oponent_hand)
    player_score += new_points[0]
    oponent_score += new_points[1]
    clear()
    score(player_score, oponent_score)