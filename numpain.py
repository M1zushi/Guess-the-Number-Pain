import random
import math

print('\n\n! Welcome to this painful game of guessing numbers!')
print('''\n> You will be given a clue everytime you guess incorrectly, but the clue may stay the same
> <-> stands for \'Between\' (included the mentioned numbers)
> + stands for \'Addition\'
> - stands for \'Subtraction\'
> * stands for \'Multiplication\'
> // stands for \'Division\'
> √ stands for \'Square Root\'
''')

dif = int(input('Level of Difficulty (1-5): '))
min = int(input('Choose a number to guess higher than: '))
max = int(input('Choose a number to guess lower than: '))
num = random.randint(min, max)
clue = (f'{min} <-> {max}')
win = False
re = True
tri = 0

while re == True:
    while win == False:
        # First Difficulty
        while dif == 1:
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
                temp1 = num - 30
                temp2 = num + 30
                if temp1 < min:
                    temp1 = min
                elif temp1 > max:
                    temp1 = max
                if temp2 < min:
                    temp2 = min
                elif temp2 > max:
                    temp2 = max
                clue = (f'{temp1} <-> {temp2}')

            elif tri == 2:
                temp1 = num - 20
                temp2 = num + 20
                if temp1 < min:
                    temp1 = min
                elif temp1 > max:
                    temp1 = max
                if temp2 < min:
                    temp2 = min
                elif temp2 > max:
                    temp2 = max
                clue = (f'{temp1} <-> {temp2}')

            elif tri == 3:
                temp1 = num - 10
                temp2 = num + 10
                if temp1 < min:
                    temp1 = min
                elif temp1 > max:
                    temp1 = max
                if temp2 < min:
                    temp2 = min
                elif temp2 > max:
                    temp2 = max
                clue = (f'{temp1} <-> {temp2}')

            elif tri == 4:
                temp1 = num - 5
                temp2 = num + 5
                if temp1 < min:
                    temp1 = min
                elif temp1 > max:
                    temp1 = max
                if temp2 < min:
                    temp2 = min
                elif temp2 > max:
                    temp2 = max
                clue = (f'{temp1} <-> {temp2}')

            elif tri >= 5:
                temp1 = num - 2
                temp2 = num + 2
                if temp1 < min:
                    temp1 = min
                elif temp1 > max:
                    temp1 = max
                if temp2 < min:
                    temp2 = min
                elif temp2 > max:
                    temp2 = max
                clue = (f'{temp1} <-> {temp2}')

        # Second Difficulty
        while dif == 2:
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
                if temp1 < min:
                    temp1 = min
                elif temp1 > max:
                    temp1 = max
                if temp2 < min:
                    temp2 = min
                elif temp2 > max:
                    temp2 = max
                clue = (f'{temp1} <-> {temp2}')

            elif tri == 2:
                temp1 = num - (random.randint(15,25))
                temp2 = num + (random.randint(15,25))
                if temp1 < min:
                    temp1 = min
                elif temp1 > max:
                    temp1 = max
                if temp2 < min:
                    temp2 = min
                elif temp2 > max:
                    temp2 = max
                clue = (f'{temp1} <-> {temp2}')

            elif tri == 3:
                temp1 = num - (random.randint(10,15))
                temp2 = num + (random.randint(10,15))
                if temp1 < min:
                    temp1 = min
                elif temp1 > max:
                    temp1 = max
                if temp2 < min:
                    temp2 = min
                elif temp2 > max:
                    temp2 = max
                clue = (f'{temp1} <-> {temp2}')

            elif tri == 4:
                temp1 = num - (random.randint(4,9))
                temp2 = num + (random.randint(4,9))
                if temp1 < min:
                    temp1 = min
                elif temp1 > max:
                    temp1 = max
                if temp2 < min:
                    temp2 = min
                elif temp2 > max:
                    temp2 = max
                clue = (f'{temp1} <-> {temp2}')

            elif tri >= 5:
                temp1 = num - (random.randint(1,5))
                temp2 = num + (random.randint(1,5))
                if temp1 < min:
                    temp1 = min
                elif temp1 > max:
                    temp1 = max
                if temp2 < min:
                    temp2 = min
                elif temp2 > max:
                    temp2 = max
                clue = (f'{temp1} <-> {temp2}')

        # Third Difficulty
        while dif == 3:
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
                temp1 = num - (random.randint(20,40))
                temp2 = num + (random.randint(20,40))
                if temp1 < min:
                    temp1 = min
                elif temp1 > max:
                    temp1 = max
                if temp2 < min:
                    temp2 = min
                elif temp2 > max:
                    temp2 = max
                clue = (f'{temp1} <-> {temp2}')

            elif tri == 2:
                temp1 = num - (random.randint(10,30))
                temp2 = num + (random.randint(10,30))
                if temp1 < min:
                    temp1 = min
                elif temp1 > max:
                    temp1 = max
                if temp2 < min:
                    temp2 = min
                elif temp2 > max:
                    temp2 = max
                clue = (f'{temp1} <-> {temp2}')

            elif tri == 3:
                temp1 = num - (random.randint(15,35))
                temp2 = num + (random.randint(15,35))
                if temp1 < min:
                    temp1 = min
                elif temp1 > max:
                    temp1 = max
                if temp2 < min:
                    temp2 = min
                elif temp2 > max:
                    temp2 = max
                clue = (f'{temp1} <-> {temp2}')

            elif tri == 4:
                temp1 = num - (random.randint(10,30))
                temp2 = num + (random.randint(10,30))
                if temp1 < min:
                    temp1 = min
                elif temp1 > max:
                    temp1 = max
                if temp2 < min:
                    temp2 = min
                elif temp2 > max:
                    temp2 = max
                clue = (f'{temp1} <-> {temp2}')

            elif tri >= 5:
                temp1 = num - (random.randint(5,15))
                temp2 = num + (random.randint(5,15))
                if temp1 < min:
                    temp1 = min
                elif temp1 > max:
                    temp1 = max
                if temp2 < min:
                    temp2 = min
                elif temp2 > max:
                    temp2 = max
                clue = (f'{temp1} <-> {temp2}')

        # Fourth Difficulty
        while dif == 4:
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
                temp1 = num - (random.randint(10,50))
                if temp1 < min:
                    temp1 = min
                elif temp1 > max:
                    temp1 = max
                if temp2 < min:
                    temp2 = min
                elif temp2 > max:
                    temp2 = max
                clue = (f'{temp1} < x')

            elif tri == 2:
                temp2 = num + (random.randint(10,50))
                if temp1 < min:
                    temp1 = min
                elif temp1 > max:
                    temp1 = max
                if temp2 < min:
                    temp2 = min
                elif temp2 > max:
                    temp2 = max
                clue = (f'{temp1} < x < {temp2}')

            elif tri == 3:
                temp1 = num // (random.randint(2,4))
                temp2 = num + (random.randint(2,32))
                if temp1 < min:
                    temp1 = min
                    clue = (f'{temp1} <-> {temp2}')
                elif temp1 > max:
                    temp1 = max
                    clue = (f'{temp1} <-> {temp2}')
                if temp2 < min:
                    temp2 = min
                    clue = (f'{temp1} <-> {temp2}')
                elif temp2 > max:
                    temp2 = max
                    clue = (f'{temp1} <-> {temp2}')
                else:
                    clue = (f'(x/{temp1}) + {temp2}')

            elif tri == 4:
                temp1 = num // (random.randint(2,4))
                temp2 = num * (random.randint(2,4))
                if temp1 < min:
                    temp1 = min
                    clue = (f'{temp1} <-> {temp2}')
                elif temp1 > max:
                    temp1 = max
                    clue = (f'{temp1} <-> {temp2}')
                if temp2 < min:
                    temp2 = min
                    clue = (f'{temp1} <-> {temp2}')
                elif temp2 > max:
                    temp2 = max
                    clue = (f'{temp1} <-> {temp2}')
                else:
                    clue = (f'(x / {temp1}) * {temp2}')

            elif tri == 5:
                temp1 = (math.sqrt(num))
                clue = (f'√{temp1}')

        # Fifth Difficulty
        while dif == 5:
            print('\nClue: none boop')
            print(f'Tries: {tri}')
            guess = int(input('Guess: '))

            if num == guess:
                print('\n\n! You guessed the right number !')
                print(f'! Tries: {tri} !\n')
                win = True
            else:
                tri += 1

        # Play Again?
        temp5 = str(input('Play Again? (Yes/No): '))
        if temp5.lower() == 'no':
            re = False
        elif temp5.lower() == ' no':
            re = False
        else:
            re = True

else:
    print('Stonks') # Idk stonks, numbers, close enough
