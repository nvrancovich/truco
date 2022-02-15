import time
import random
import os

from cards import CARDS
from envido_values import ENVIDO_VALUES

def clear(): 
    os.system('clear')

def envido(first_hand, second_hand):
    first_envido = ENVIDO_VALUES[first_hand[0]] + ENVIDO_VALUES[first_hand[1]] + ENVIDO_VALUES[first_hand[2]]
    second_envido = ENVIDO_VALUES[second_hand[0]] + ENVIDO_VALUES[second_hand[1]] + ENVIDO_VALUES[second_hand[2]]
    return first_envido, second_envido

def hand(player_first, oponent_first, hand1, hand2):
    #When player go first
    if player_first:
        oponent_points = 0
        player_points = 0

        #First round
        player_first_round = int(input(f'Tu turno: 1) {hand1[0]} 2) {hand1[1]} 3) {hand1[2]} 4) Cantar Envido 5) Real Envido 6) Falta Envido: '))
        #Envido
        if player_first_round == 4:
            envido_player, envido_oponent = envido(hand1, hand2)
            print('Yo: Envido!')
            #Envido, envido
            envido_envido = random.random()
            if envido_envido() > 0.3:
                print('Él: Envido!')
                want = bool(input('Envido, envido (3ptos): 1) Quiero 2) No Quiero: '))
                if want:
                    print('Yo: Quiero!')
                    print(f'Yo: Tengo {envido_player}')
                    if envido_oponent > envido_player:
                        print(f'Él: {envido_oponent} son mejores')
                        oponent_points += 4
                    else:
                        print('Él: Son buenas')
                        player_points += 4
                else:
                    print('Yo: No quiero!')
                    oponent_points += 2
            
            print('Él: Quiero')
            print(f'Yo: Tengo {envido_player}')
            if envido_oponent > envido_player:
                print(f'Él: {envido_oponent} son mejores')
                oponent_points += 2
            else:
                print('Él: Son buenas')
                player_points += 2
            player_first_round = int(input(f'Tu turno: 1) {hand1[0]} 2) {hand1[1]} 3) {hand1[2]}'))
        hand1.remove(hand1[player_first_round - 1])
        oponent_first_round = random.randint(0,2)
        print(f'Él tira un {hand2[oponent_first_round]}!')
        hand2.remove(hand2[oponent_first_round])

        #Second round
        player_second_round = int(input(f'Tu turno: 1) {hand1[0]} 2) {hand1[1]}'))
        hand1.remove(hand1[player_second_round - 1])
        oponent_second_round = random.randint(0,1)
        print(f'Él tira un {hand2[oponent_second_round]}!')
        hand2.remove(hand2[oponent_second_round])

        #Third round
        player_third_round = int(input(f'Tu turno: 1) {hand1[0]}'))
        print(f'Él tira un {hand2[0]}')

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
    hand1 = list[:3]
    hand2 = list[3:]
    return hand1, hand2

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
    hand1, hand2 = shuffle(CARDS, 6)
    player_score, oponent_score = 0, 0
    clear()
    score(player_score, oponent_score)
    print('')
    print(f'Tu mano: {hand1}')
    print(f'Su mano: {hand2}')
    new_points = hand(True, False, hand1, hand2)
    player_score += new_points[0]
    oponent_score += new_points[1]
    clear()
    score(player_score, oponent_score)