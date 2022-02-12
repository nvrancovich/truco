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

shuffle(CARDS, 3)