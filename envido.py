import time
import random
import os

from cards import CARDS
from envido_values import ENVIDO_VALUES

def envido(player_first, oponent_first, player_hand, oponent_hand, envido_level):
    player_envido = ENVIDO_VALUES[player_hand[0]] + ENVIDO_VALUES[player_hand[1]] + ENVIDO_VALUES[player_hand[2]]
    oponent_envido = ENVIDO_VALUES[oponent_hand[0]] + ENVIDO_VALUES[oponent_hand[1]] + ENVIDO_VALUES[oponent_hand[2]]
    player_points = 0
    oponent_points = 0
    if player_first:
        if envido_level == 4:
            print('Yo: Envido!')
            print('Él: Quiero')
            print(f'Tengo {player_envido}')
            if player_envido >= oponent_envido:
                print('Él: Son buenas')
                player_points = 2
            else:
                print(f'Él: {oponent_envido} son mejores')
                oponent_points = 2
        if envido_level == 5:
            print('Yo: Real Envido!')
            print('Él: Quiero')
            print(f'Tengo {player_envido}')
            if player_envido >= oponent_envido:
                print('Él: Son buenas')
                player_points = 3
            else:
                print(f'Él: {oponent_envido} son mejores')
                oponent_points = 3
        if envido_level == 6:
            pass
    if oponent_first:
        pass
    return player_points, oponent_points
