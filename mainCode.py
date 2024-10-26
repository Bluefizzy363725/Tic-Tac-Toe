"""

- TIC TAC TOE

Written: Bluefizzy363725
Date: 26/10/2024
Status: Incomplete

- Player vs computer
- Computer random generation
- To add computer smart generation
- To add 2 player option

"""


# IMPORTS

import os
import time
import random
import sys


# LIST OF AVAILABLE SPACES

spaceLis = [1,2,3,4,5,6,7,8,9]


# SYMBOL SELECTION

choice = input('O or X: ')
if choice == 'O':
    compChoice = 'X'
else:
    compChoice = 'O'
playF = False
x = random.randint(1,2)
if x == 1: playF = True


# CLASS WITH BULK CODE

class code:
    def __init__(self,choice,compChoice):
        self.choice = choice
        self.compChoice = compChoice

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

runC = code(choice,compChoice)
for i in range(9):
    if playF == True:
        runC.playerChoice()
        runC.winningPatternsPlayer()
        playF = False
    else:
        runC.computerChoice()
        runC.winningPatternsComp()
        playF = True


os.system('cls')
print(f' {spaceLis[0]} | {spaceLis[1]} | {spaceLis[2]} \n-----------\n {spaceLis[3]} | {spaceLis[4]} | {spaceLis[5]} \n-----------\n {spaceLis[6]} | {spaceLis[7]} | {spaceLis[8]} ')
