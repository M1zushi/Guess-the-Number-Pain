import random
# import math

print('\n\n! Welcome to this painful game of guessing numbers!')
print('''\n+ You will be given a clue everytime you guess incorrectly, but the clue may stay the same
+ <-> stands for \'Between\' (included the mentioned numbers)
''')
# + \'<\' stands for \'less\' than and \'>\' for \'more than\'


num = random.randint(1,100)
clue = ('1 <-> 100')
win = False
tri = 0

while win == False:
    print(f'\nClue: {clue}')
    print(f'Tries: {tri}')
    guess = int(input('Guess: '))

    if num == guess:
        print('\n\n! You guessed the right number !')
        print(f'! Tries: {tri} !\n')
        win = True
    else:
        tri += 1

    if tri == 1:
        temp1 = num - (random.randint(25,35))
        temp2 = num + (random.randint(25,35))
        if temp1 < 0:
            temp1 = 0
        elif temp1 > 100:
            temp1 = 100
        if temp2 < 0:
            temp2 = 0
        elif temp2 > 100:
            temp2 = 100
        clue = (f'{temp1} <-> {temp2}')

    elif tri == 2:
        temp1 = num - (random.randint(15,25))
        temp2 = num + (random.randint(15,25))
        if temp1 < 0:
            temp1 = 0
        elif temp1 > 100:
            temp1 = 100
        if temp2 < 0:
            temp2 = 0
        elif temp2 > 100:
            temp2 = 100
        clue = (f'{temp1} <-> {temp2}')

    elif tri == 3:
        temp1 = num - (random.randint(10,15))
        temp2 = num + (random.randint(10,15))
        if temp1 < 0:
            temp1 = 0
        elif temp1 > 100:
            temp1 = 100
        if temp2 < 0:
            temp2 = 0
        elif temp2 > 100:
            temp2 = 100
        clue = (f'{temp1} <-> {temp2}')

    elif tri == 4:
        temp1 = num - (random.randint(4,9))
        temp2 = num + (random.randint(4,9))
        if temp1 < 0:
            temp1 = 0
        elif temp1 > 100:
            temp1 = 100
        if temp2 < 0:
            temp2 = 0
        elif temp2 > 100:
            temp2 = 100
        clue = (f'{temp1} <-> {temp2}')

    elif tri >= 5:
        temp1 = num - (random.randint(1,5))
        temp2 = num + (random.randint(1,5))
        if temp1 < 0:
            temp1 = 0
        elif temp1 > 100:
            temp1 = 100
        if temp2 < 0:
            temp2 = 0
        elif temp2 > 100:
            temp2 = 100
        clue = (f'{temp1} <-> {temp2}')
