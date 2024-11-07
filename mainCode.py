"""

- TIC TAC TOE

Written: Bluefizzy363725
Date started: 26/10/2024
Status: Incomplete

Update 1:
- Added computer smart moving
- Added basic log of moves made

To add:
- 2 player option
- More/different difficulty levels

"""


# IMPORTS

import os
import time
import random
import sys
f = open('log.txt', 'w+')
f.write('RUNTIME LOG:\n')


# LIST OF AVAILABLE SPACES

spaceLis = [1,2,3,4,5,6,7,8,9]
runLis = [1]


# SYMBOL SELECTION

choice = input('O or X: ')
if choice == 'O':
    compChoice = 'X'
else:
    compChoice = 'O'

ai = input('Harder CPU (Y): ')
if ai == 'Y':
    aiTrue = True
else:
    aiTrue = False

playF = False
x = random.randint(1,2)
if x == 1: playF = True


# CLASS WITH BULK CODE

class code:


    # INITIALISATION

    def __init__(self,choice,compChoice):
        self.choice = choice
        self.compChoice = compChoice


    # USER INPUT HANDLING

    def playerChoice(self):
        loop = True
        while loop == True:
            os.system('cls')
            print('YOUR TURN:')
            print(f' {spaceLis[0]} | {spaceLis[1]} | {spaceLis[2]} \n-----------\n {spaceLis[3]} | {spaceLis[4]} | {spaceLis[5]} \n-----------\n {spaceLis[6]} | {spaceLis[7]} | {spaceLis[8]} ')
            numSelect = input('Enter the space to fill: ')
            try:
                int(numSelect)
            except ValueError:
                print('Not Valid')
                time.sleep(1)
            else:
                if int(numSelect) in spaceLis:
                    spaceLis[int(numSelect) - 1] = choice
                    loop = False


    # PRIMITIVE COMPUTER AI

    def computerChoice(self):
        loop = True
        while loop == True:
            os.system('cls')
            print('COMPUTER TURN:')
            numSelect = random.randint(1,9)
            if int(numSelect) in spaceLis:
                spaceLis[int(numSelect) - 1] = compChoice
                loop = False
        print(f' {spaceLis[0]} | {spaceLis[1]} | {spaceLis[2]} \n-----------\n {spaceLis[3]} | {spaceLis[4]} | {spaceLis[5]} \n-----------\n {spaceLis[6]} | {spaceLis[7]} | {spaceLis[8]} ')
        time.sleep(1)


    # ADVANCED COMPUTER AI

    def computerChoiceAi(self):
        loop = True
        while loop == True:
            os.system('cls')
            print('COMPUTER TURN:')

                    
# MANUAL INPUT OF SCENARIOS IN IF/ELSE CHAIN

            # SOME STRATEGY

            if runLis[0] == 1:
                spin = random.randint(1,4)

                if spin == 1:
                    side = random.randint(1,4)
                    match side:
                        case 1:
                            side = 2
                        case 2:
                            side = 4
                        case 3:
                            side = 6
                        case 4:
                            side = 8
                    spaceLis[side-1] = compChoice
                    loop = False

                elif spin == 2:
                    side = random.randint(1,4)
                    match side:
                        case 1:
                            side = 1
                        case 2:
                            side = 3
                        case 3:
                            side = 7
                        case 4:
                            side = 9
                    spaceLis[side-1] = compChoice
                    loop = False

                elif spin == 3 or spin == 4:
                    spaceLis[4] = compChoice
                    loop = False

                runLis[0] = 0

            else:


                # TO GET 3 IN A ROW

                if spaceLis[0] == compChoice and spaceLis[1] == compChoice and 3 in spaceLis:
                    spaceLis[2] = compChoice
                    loop = False
                elif spaceLis[3] == compChoice and spaceLis[4] == compChoice and 6 in spaceLis:
                    spaceLis[5] = compChoice
                    loop = False
                elif spaceLis[6] == compChoice and spaceLis[7] == compChoice and 9 in spaceLis:
                    spaceLis[8] = compChoice
                    loop = False
                elif spaceLis[0] == compChoice and spaceLis[3] == compChoice and 7 in spaceLis:
                        spaceLis[6] = compChoice
                        loop = False
                elif spaceLis[1] == compChoice and spaceLis[4] == compChoice and 8 in spaceLis:
                        spaceLis[7] = compChoice
                        loop = False
                elif spaceLis[2] == compChoice and spaceLis[5] == compChoice and 9 in spaceLis:
                        spaceLis[8] = compChoice
                        loop = False
                elif spaceLis[0] == compChoice and spaceLis[4] == compChoice and 9 in spaceLis:
                        spaceLis[8] = compChoice
                        loop = False
                elif spaceLis[2] == compChoice and spaceLis[4] == compChoice  and 7 in spaceLis:
                        spaceLis[6] = compChoice
                        loop = False
                elif spaceLis[8] == compChoice and spaceLis[4] == compChoice and 1 in spaceLis:
                        spaceLis[0] = compChoice
                        loop = False
                elif spaceLis[6] == compChoice and spaceLis[4] == compChoice and 3 in spaceLis:
                        spaceLis[2] = compChoice
                        loop = False
                elif spaceLis[2] == compChoice and spaceLis[1] == compChoice and 1 in spaceLis:
                        spaceLis[0] = compChoice
                        loop = False
                elif spaceLis[5] == compChoice and spaceLis[4] == compChoice and 4 in spaceLis:
                        spaceLis[3] = compChoice
                        loop = False
                elif spaceLis[8] == compChoice and spaceLis[7] == compChoice and 7 in spaceLis:
                        spaceLis[6] = compChoice
                        loop = False
                elif spaceLis[6] == compChoice and spaceLis[3] == compChoice and 1 in spaceLis:
                        spaceLis[0] = compChoice
                        loop = False
                elif spaceLis[7] == compChoice and spaceLis[4] == compChoice and 2 in spaceLis:
                        spaceLis[1] = compChoice
                        loop = False
                elif spaceLis[8] == compChoice and spaceLis[5] == compChoice and 3 in spaceLis:
                        spaceLis[2] = compChoice
                        loop = False


                # TO PREVENT 3 IN A ROW

                elif spaceLis[0] == choice and spaceLis[1] == choice and 3 in spaceLis:
                    spaceLis[2] = compChoice
                    loop = False
                elif spaceLis[3] == choice and spaceLis[4] == choice and 6 in spaceLis:
                    spaceLis[5] = compChoice
                    loop = False
                elif spaceLis[6] == choice and spaceLis[7] == choice and 9 in spaceLis:
                    spaceLis[8] = compChoice
                    loop = False

                elif spaceLis[0] == choice and spaceLis[2] == choice and 2 in spaceLis:
                    spaceLis[1] = compChoice
                    loop = False
                elif spaceLis[3] == choice and spaceLis[5] == choice and 5 in spaceLis:
                    spaceLis[4] = compChoice
                    loop = False
                elif spaceLis[6] == choice and spaceLis[8] == choice and 8 in spaceLis:
                    spaceLis[7] = compChoice
                    loop = False

                elif spaceLis[0] == choice and spaceLis[3] == choice and 7 in spaceLis:
                        spaceLis[6] = compChoice
                        loop = False
                elif spaceLis[1] == choice and spaceLis[4] == choice and 8 in spaceLis:
                        spaceLis[7] = compChoice
                        loop = False
                elif spaceLis[2] == choice and spaceLis[5] == choice and 9 in spaceLis:
                        spaceLis[8] = compChoice
                        loop = False

                elif spaceLis[0] == choice and spaceLis[6] == choice and 4 in spaceLis:
                        spaceLis[3] = compChoice
                        loop = False
                elif spaceLis[1] == choice and spaceLis[7] == choice and 5 in spaceLis:
                        spaceLis[4] = compChoice
                        loop = False
                elif spaceLis[2] == choice and spaceLis[8] == choice and 6 in spaceLis:
                        spaceLis[5] = compChoice
                        loop = False

                elif spaceLis[0] == choice and spaceLis[4] == choice and 9 in spaceLis:
                        spaceLis[8] = compChoice
                        loop = False
                elif spaceLis[2] == choice and spaceLis[4] == choice  and 7 in spaceLis:
                        spaceLis[6] = compChoice
                        loop = False
                elif spaceLis[8] == choice and spaceLis[4] == choice and 1 in spaceLis:
                        spaceLis[0] = compChoice
                        loop = False
                elif spaceLis[6] == choice and spaceLis[4] == choice and 3 in spaceLis:
                        spaceLis[2] = compChoice
                        loop = False

                elif (spaceLis[2] == choice and spaceLis[6] == choice and 5 in spaceLis) ^ (spaceLis[8] == choice and spaceLis[0] and 5 in spaceLis):
                        spaceLis[4] = compChoice
                        loop = False

                elif spaceLis[2] == choice and spaceLis[1] == choice and 1 in spaceLis:
                        spaceLis[0] = compChoice
                        loop = False
                elif spaceLis[5] == choice and spaceLis[4] == choice and 4 in spaceLis:
                        spaceLis[3] = compChoice
                        loop = False
                elif spaceLis[8] == choice and spaceLis[7] == choice and 7 in spaceLis:
                        spaceLis[6] = compChoice
                        loop = False

                elif spaceLis[6] == choice and spaceLis[3] == choice and 1 in spaceLis:
                        spaceLis[0] = compChoice
                        loop = False
                elif spaceLis[7] == choice and spaceLis[4] == choice and 2 in spaceLis:
                        spaceLis[1] = compChoice
                        loop = False
                elif spaceLis[8] == choice and spaceLis[5] == choice and 3 in spaceLis:
                        spaceLis[2] = compChoice
                        loop = False


                # RANDOM IF NO CONDITIONS ARE MET

                else:
                    numSelect = random.randint(1,9)
                    if int(numSelect) in spaceLis:
                        spaceLis[int(numSelect) - 1] = compChoice
                        loop = False


        # DISPLAYING BOARD

        print(f' {spaceLis[0]} | {spaceLis[1]} | {spaceLis[2]} \n-----------\n {spaceLis[3]} | {spaceLis[4]} | {spaceLis[5]} \n-----------\n {spaceLis[6]} | {spaceLis[7]} | {spaceLis[8]} ')
        time.sleep(1)


        # WINNING POSITIONS FOR PLAYER AND CPU - DETECTS IF GAME HAS BEEN WON

    def winningPatternsPlayer(self):
        if (spaceLis[0] == choice and spaceLis[1] == choice and spaceLis[2] == choice) or (spaceLis[3] == choice and spaceLis[4] == choice and spaceLis[5] == choice) or (spaceLis[6] == choice and spaceLis[7] == choice and spaceLis[8] == choice) or (spaceLis[0] == choice and spaceLis[3] == choice and spaceLis[6] == choice) or (spaceLis[1] == choice and spaceLis[4] == choice and spaceLis[7] == choice) or (spaceLis[2] == choice and spaceLis[5] == choice and spaceLis[8] == choice) or (spaceLis[2] == choice and spaceLis[4] == choice and spaceLis[6] == choice) or (spaceLis[0] == choice and spaceLis[4] == choice and spaceLis[8] == choice):
            os.system('cls')
            print('PLAYER WIN')
            time.sleep(1)
            print(f'FINAL BOARD:\n {spaceLis[0]} | {spaceLis[1]} | {spaceLis[2]} \n-----------\n {spaceLis[3]} | {spaceLis[4]} | {spaceLis[5]} \n-----------\n {spaceLis[6]} | {spaceLis[7]} | {spaceLis[8]} ')
            time.sleep(5)
            sys.exit(0)

    def winningPatternsComp(self):
        if (spaceLis[0] == compChoice and spaceLis[1] == compChoice and spaceLis[2] == compChoice) or (spaceLis[3] == compChoice and spaceLis[4] == compChoice and spaceLis[5] == compChoice) or (spaceLis[6] == compChoice and spaceLis[7] == compChoice and spaceLis[8] == compChoice) or (spaceLis[0] == compChoice and spaceLis[3] == compChoice and spaceLis[6] == compChoice) or (spaceLis[1] == compChoice and spaceLis[4] == compChoice and spaceLis[7] == compChoice) or (spaceLis[2] == compChoice and spaceLis[5] == compChoice and spaceLis[8] == compChoice) or (spaceLis[2] == compChoice and spaceLis[4] == compChoice and spaceLis[6] == compChoice) or (spaceLis[0] == compChoice and spaceLis[4] == compChoice and spaceLis[8] == compChoice):
            os.system('cls')
            print('COMPUTER WIN')
            time.sleep(1)
            print(f'FINAL BOARD:\n {spaceLis[0]} | {spaceLis[1]} | {spaceLis[2]} \n-----------\n {spaceLis[3]} | {spaceLis[4]} | {spaceLis[5]} \n-----------\n {spaceLis[6]} | {spaceLis[7]} | {spaceLis[8]} ')
            time.sleep(5)
            sys.exit(0)



# MAIN CODE

runC = code(choice,compChoice,)
for i in range(9):
    if playF == True:


        # PLAYER TURN

        runC.playerChoice()
        runC.winningPatternsPlayer()
        playF = False
    else:
        if aiTrue == True:


            # ADVANCED AI TURN

            runC.computerChoiceAi()
            runC.winningPatternsComp()
        else:


            # PRIMITIVE AI TURN

            runC.computerChoice()
            runC.winningPatternsComp()
        playF = True


    # GAMEPLAY LOG

    f.write(f'{str(spaceLis)}\n')


os.system('cls')
print(f' {spaceLis[0]} | {spaceLis[1]} | {spaceLis[2]} \n-----------\n {spaceLis[3]} | {spaceLis[4]} | {spaceLis[5]} \n-----------\n {spaceLis[6]} | {spaceLis[7]} | {spaceLis[8]} ')

f.close()
