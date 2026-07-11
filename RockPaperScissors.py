### Rock Paper Scissors ###

## Variables:
# rounds - Number of game rounds
# round_num - 1 round in rounds
# pcscore - Score  of PC (Opponent)
# playerscore - Score of Player/User
# playermove - Move of Player
# pcmove - Move of PC (Opponent)

# Importing
import os, random
from colorama import Fore, Style, just_fix_windows_console

# Data
turntomove = ['r', 'p', 's']
movenames = {'r': 'Rock', 'p': 'Paper', 's': 'Scissors'}
# UDFs to use
def clearscreen(): # Clear the screen
    if os.name == 'nt': # for Windows
        os.system('cls')
    else: # other OSs
        os.system('clear')
def intcheck(inttocheck, minimum, maximum):
    if not inttocheck.isdecimal():
        print('Invalid input, please enter an integer')
        return False
    inttocheck = int(inttocheck)
    if inttocheck < minimum or inttocheck > maximum:
        print(f'Out of range, please enter between {minimum} and {maximum}')
        return False
    else:
        return True

def movecheck(move):
    if move in turntomove:
        return True
    else:
        print('Invalid input, please enter one of the options')
        return False
# Main Program
just_fix_windows_console() # ensures formatting works in Windows 8.1 and older
print(Style.BRIGHT + 'Rock Paper Scissors' + Style.RESET_ALL)
pcscore = 0
playerscore = 0
while True:
    rounds = input('Enter number of rounds to play (1-50): ')
    if intcheck(rounds, 1, 50):
        rounds = int(rounds)
        break
    
for round_num in range(rounds):
    print(f'\nRound {round_num + 1}')
    while True:
        playermove = input(Style.BRIGHT + 'Enter a move\n' + Style.RESET_ALL + '[R] Rock\n[P] Paper\n[S] Scissors\n').lower()
        if movecheck(playermove):
            break
    pcmove = random.choice(turntomove)
    print(f'You used {movenames[playermove]}!')
    print(f'Opponent used {movenames[pcmove]}!') 
    if playermove == pcmove:
        print('Tie!')
    elif (playermove == 'r' and pcmove == 'p') or (playermove == 'p' and pcmove == 's') or (playermove == 's' and pcmove == 'r'):
        print('Opponent won this round!')
        pcscore += 1
    elif (playermove == 's' and pcmove == 'p') or (playermove == 'p' and pcmove == 'r') or (playermove == 'r' and pcmove == 's'):
        print(Fore.GREEN + 'You won this round!' + Style.RESET_ALL)
        playerscore += 1
    print(Fore.RED + Style.BRIGHT + 'Your score: ' + Style.RESET_ALL + str(playerscore))
    print(Fore.CYAN + Style.BRIGHT + 'Opponent\'s score: ' + Style.RESET_ALL + str(pcscore))
    input("Press Enter to continue...")
    clearscreen()
print(Style.BRIGHT + "FINAL SCORE")
print(Fore.RED + Style.BRIGHT + 'You: ' + Style.RESET_ALL + str(playerscore))
print(Fore.CYAN + Style.BRIGHT + 'Opponent: ' + Style.RESET_ALL + str(pcscore))
if playerscore < pcscore:
    print('You lost. Good try!')
elif playerscore > pcscore:
    print('You Won! Good Job!')
else:
    print('It\'s a tie!')
input("Press Enter to exit game.")
