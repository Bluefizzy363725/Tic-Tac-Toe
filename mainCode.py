"""

- TIC TAC TOE

Written: Bluefizzy363725
Date started: 26/10/2024
Status: Complete

Update 1: 07/11/2024
- Added computer smart moving
- Added basic log of moves made

Update 2: 08/11/2024
- Fixed minor syntax errors
- Added parts that I accidentally missed the last update
- 2 player option
- Code formatted better
- Easy and difficult option between the two CPU AIs

Update 3: 08/11/2024
- Minor syntax changes

Update 4: 10/11/2024
- Edits regarding strategies
- Fixed minor logic and syntax errors
- Added draw screen

"""


# IMPORTS

import os
import time
import random
import sys





# CLASS WITH BULK CODE

class code:


    # INITIALISATION

    def __init__(self,choice,compChoice,player,runLis):
        self.choice = choice
        self.compChoice = compChoice
        self.player = player
        self.runLis = runLis


    # USER INPUT HANDLING

    def playerChoice(self):
        loop = True
        while loop == True:
            os.system('cls')
            if player == True:
                print('PLAYER 1 TURN: ')
            else:
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


    # SECOND PLAYER HANDLING

    def player2Choice(self):
        loop = True
        while loop == True:
            os.system('cls')
            print('PLAYER 2 TURN: ')
            print(f' {spaceLis[0]} | {spaceLis[1]} | {spaceLis[2]} \n-----------\n {spaceLis[3]} | {spaceLis[4]} | {spaceLis[5]} \n-----------\n {spaceLis[6]} | {spaceLis[7]} | {spaceLis[8]} ')
            numSelect1 = input('Enter the space to fill: ')
            try:
                int(numSelect1)
            except ValueError:
                print('Not Valid')
                time.sleep(1)
            else:
                if int(numSelect1) in spaceLis:
                    spaceLis[int(numSelect1) - 1] = compChoice
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

            # IF CPU GOES FIRST - FIRST GO

            if runLis[0] == 1:
                spin = random.randint(1,6)
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


            # IF CPU GOES SECOND - FIRST GO

            elif runLis[0] == 2:
                if 5 in spaceLis:
                    spaceLis[4] = compChoice
                    runLis[0] = 0
                    loop = False
                else:
                    x = random.randint(1,4)
                    match x:
                        case 1:
                            spaceLis[0] = compChoice
                            runLis[0] = 0
                            loop = False
                        case 2:
                            spaceLis[2] = compChoice
                            runLis[0] = 0
                            loop = False
                        case 3:
                            spaceLis[6] = compChoice
                            runLis[0] = 0
                            loop = False
                        case 4:
                            spaceLis[8] = compChoice
                            runLis[0] = 0
                            loop = False                   


            # TO COMBAT SOME SCENARIOS

            elif (spaceLis == [1, choice, 3, choice, compChoice, compChoice, 7, 8, 9]) or (spaceLis == [1, 2, choice, 4, choice, 6, compChoice, 8, 9]) or (spaceLis == [1, 2, compChoice, 4, compChoice, 6, choice, 8, 9]) or (spaceLis == [1, 2, choice, choice, compChoice, 6, 7, 8, 9]):
                if 1 in spaceLis:
                    spaceLis[0] = compChoice
                    loop = False
            elif (spaceLis == [1, choice, 3, 4, compChoice, choice, 7, compChoice, 9]) or (spaceLis == [choice, 2, 3, 4, choice, 6, 7, 8, compChoice]) or (spaceLis == [compChoice, 2, 3, 4, compChoice, 6, 7, 8, choice]) or (spaceLis == [1, choice, 3, 4, compChoice, 6, 7, 8, choice]):
                if 3 in spaceLis:
                    spaceLis[2] = compChoice
                    loop = False
            elif (spaceLis == [1, 2, 3, compChoice, compChoice, choice, 7, choice, 9]) or (spaceLis == [1, 2, compChoice, 4, choice, 6, choice, 8, 9]) or (spaceLis == [1, 2, choice, 4, compChoice, 6, compChoice, 8, 9]) or (spaceLis == [1, 2, 3, 4, compChoice, choice, choice, 8, 9]):
                if 9 in spaceLis:
                    spaceLis[8] = compChoice
                    loop = False
            elif (spaceLis == [1, compChoice, 3, choice, compChoice, 6, 7, choice, 9]) or (spaceLis == [compChoice, 2, 3, 4, choice, 6, 7, 8, choice]) or (spaceLis == [choice, 2, 3, 4, compChoice, 6, 7, 8, compChoice]) or (spaceLis == [choice, 2, 3, 4, compChoice, 6, 7, choice, 9]):
                if 7 in spaceLis:
                    spaceLis[6] = compChoice
                    loop = False


            # BASIC LOGIC

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
                elif spaceLis[0] == compChoice and spaceLis[2] == compChoice and 2 in spaceLis:
                    spaceLis[1] = compChoice
                    loop = False
                elif spaceLis[3] == compChoice and spaceLis[5] == compChoice and 5 in spaceLis:
                    spaceLis[4] = compChoice
                    loop = False
                elif spaceLis[6] == compChoice and spaceLis[8] == compChoice and 8 in spaceLis:
                    spaceLis[7] = compChoice
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
                elif spaceLis[0] == compChoice and spaceLis[6] == compChoice and 4 in spaceLis:
                        spaceLis[3] = compChoice
                        loop = False
                elif spaceLis[1] == compChoice and spaceLis[7] == compChoice and 5 in spaceLis:
                        spaceLis[4] = compChoice
                        loop = False
                elif spaceLis[2] == compChoice and spaceLis[8] == compChoice and 6 in spaceLis:
                        spaceLis[5] = compChoice
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
                elif (spaceLis[2] == compChoice and spaceLis[6] == compChoice and 5 in spaceLis) ^ (spaceLis[8] == compChoice and spaceLis[0] == compChoice and 5 in spaceLis):
                        spaceLis[4] = compChoice
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
                elif (spaceLis[2] == choice and spaceLis[6] == choice and 5 in spaceLis) ^ (spaceLis[8] == choice and spaceLis[0] == choice and 5 in spaceLis):
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


                # SOME MORE STRATEGY

                elif (spaceLis[2] == choice and spaceLis[6] == choice and spaceLis[4] == compChoice) or (spaceLis[8] == choice and spaceLis[0] == choice and spaceLis[4] == compChoice):
                    x = random.randint(1,4)
                    match x:
                        case 1:
                            if 2 in spaceLis:
                                spaceLis[1] = compChoice
                        case 2:
                            if 4 in spaceLis:
                                spaceLis[3] = compChoice
                        case 3:
                            if 6 in spaceLis:
                                spaceLis[5] = compChoice
                        case 4:
                            if 8 in spaceLis:
                                spaceLis[7] = compChoice
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


    # GAME WON BY PLAYER

    def winningPatternsPlayer(self):
        if (spaceLis[0] == choice and spaceLis[1] == choice and spaceLis[2] == choice) or (spaceLis[3] == choice and spaceLis[4] == choice and spaceLis[5] == choice) or (spaceLis[6] == choice and spaceLis[7] == choice and spaceLis[8] == choice) or (spaceLis[0] == choice and spaceLis[3] == choice and spaceLis[6] == choice) or (spaceLis[1] == choice and spaceLis[4] == choice and spaceLis[7] == choice) or (spaceLis[2] == choice and spaceLis[5] == choice and spaceLis[8] == choice) or (spaceLis[2] == choice and spaceLis[4] == choice and spaceLis[6] == choice) or (spaceLis[0] == choice and spaceLis[4] == choice and spaceLis[8] == choice):
            os.system('cls')
            print('PLAYER WIN')
            time.sleep(1)
            print(f'FINAL BOARD:\n {spaceLis[0]} | {spaceLis[1]} | {spaceLis[2]} \n-----------\n {spaceLis[3]} | {spaceLis[4]} | {spaceLis[5]} \n-----------\n {spaceLis[6]} | {spaceLis[7]} | {spaceLis[8]} ')
            sys.exit(0)


    # GAME WON BY CPU/PLAYER 2

    def winningPatternsComp(self):
        if (spaceLis[0] == compChoice and spaceLis[1] == compChoice and spaceLis[2] == compChoice) or (spaceLis[3] == compChoice and spaceLis[4] == compChoice and spaceLis[5] == compChoice) or (spaceLis[6] == compChoice and spaceLis[7] == compChoice and spaceLis[8] == compChoice) or (spaceLis[0] == compChoice and spaceLis[3] == compChoice and spaceLis[6] == compChoice) or (spaceLis[1] == compChoice and spaceLis[4] == compChoice and spaceLis[7] == compChoice) or (spaceLis[2] == compChoice and spaceLis[5] == compChoice and spaceLis[8] == compChoice) or (spaceLis[2] == compChoice and spaceLis[4] == compChoice and spaceLis[6] == compChoice) or (spaceLis[0] == compChoice and spaceLis[4] == compChoice and spaceLis[8] == compChoice):
            os.system('cls')
            if player == True:
                print('PLAYER 2 WIN')
            else:
                print('COMPUTER WIN')
            time.sleep(1)
            print(f'FINAL BOARD:\n {spaceLis[0]} | {spaceLis[1]} | {spaceLis[2]} \n-----------\n {spaceLis[3]} | {spaceLis[4]} | {spaceLis[5]} \n-----------\n {spaceLis[6]} | {spaceLis[7]} | {spaceLis[8]} ')
            sys.exit(0)


# MAIN CODE

# OPEN LOG FILE
f = open('log.txt', 'w+')
f.write('RUNTIME LOG:\n')


# LISTS

spaceLis = [1,2,3,4,5,6,7,8,9]
runLis = [1]


# VARIABLES

x = 0
run = True
choice = ''
compChoice = ''
ai = ''
aiTrue = False
playF = True
player = False


# INITIALISATION AND SELECTION

compOrNo = input('Play person (Y): ').upper()
if compOrNo == 'Y':
       player = True
       choice = input('Player 1 enter symbol: ')
       compChoice = input('Player 2 enter symbol: ')
else:
        choice = input('O or X: ')
        if choice == 'O':
            compChoice = 'X'
        else:
            compChoice = 'O'
        ai = input('Harder (Y): ').upper()
        if ai == 'Y':
            aiTrue = True
        x = random.randint(1,2)
        if x == 1:
            playF = False
        else:
            runLis[0] = 2


# RUNNING GAME

runC = code(choice,compChoice,player,runLis)

while run == True:
    if 1 in spaceLis or 2 in spaceLis or 3 in spaceLis or 4 in spaceLis or 5 in spaceLis or 6 in spaceLis or 7 in spaceLis or 8 in spaceLis or 9 in spaceLis:
        pass
    else:
        os.system('cls')
        print('DRAW')
        time.sleep(1)
        print(f'FINAL BOARD:\n {spaceLis[0]} | {spaceLis[1]} | {spaceLis[2]} \n-----------\n {spaceLis[3]} | {spaceLis[4]} | {spaceLis[5]} \n-----------\n {spaceLis[6]} | {spaceLis[7]} | {spaceLis[8]} ')
        sys.exit(0)
    if playF == True:


                # PLAYER TURN

                runC.playerChoice()
                runC.winningPatternsPlayer()
                playF = False
    else:
                if player == True:


                    # PLAYER 2 TURN

                    runC.player2Choice()
                    runC.winningPatternsComp()

                elif aiTrue == True:


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


# CLOSING LOG

f.close()
