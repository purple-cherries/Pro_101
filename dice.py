import random
import time

roll = 'y'
roll = input('Would you like to roll the dice? y/n ')

while roll == 'y':
    num = random.randint(1,6)
    if num == 1:
        print('[-----]')
        print('[     ]')
        print('[  0  ]')
        print('[     ]')
        print('[-----]')
        print('\n')

    if num == 2:
        print('[-----]')
        print('[     ]')
        print('[0   0]')
        print('[     ]')
        print('[-----]')
        print('\n')
    
    if num == 3:
        print('[-----]')
        print('[     ]')
        print('[0 0 0]')
        print('[     ]')
        print('[-----]')
        print('\n')
    
    if num == 4:
        print('[-----]')
        print('[0   0]')
        print('[     ]')
        print('[0   0]')
        print('[-----]')
        print('\n')

    if num == 5:
        print('[-----]')
        print('[0   0]')
        print('[  0  ]')
        print('[0   0]')
        print('[-----]')
        print('\n')

    if num == 6:
        print('[-----]')
        print('[0   0]')
        print('[0   0]')
        print('[0   0]')
        print('[-----]')
        print('\n')


    time.sleep(3)

    