#Practiqué lo que he aprendido en Python sobre bucles y ramificaciones creando una representación del juego de Piedra, Papel y Tijeras.
#Lo hice en inglés para practicar el idioma a la vez.
import random

def player_choice():
    choice = input('\nPress 1 for Rock\nPress 2 for Paper\nPress 3 for Scissors' + '\n: ')
    while choice.isdigit() == False:
        print('\n\nNot a valid option. Try again\n')
        choice = input('\nPress 1 for Rock\nPress 2 for Paper\nPress 3 for Scissors')
        if choice.isdigit():
            break
    choice = int(choice)
    if choice == 1:
        print('\nYou have chosen Rock')
    elif choice == 2:
        print('\nYou have chosen Paper')
    elif choice == 3:
        print('\nYou have chosen Scissors')
    else:
        print('\n\nNot a valid option. Try again\n')
        player_choice()
    return choice


def two_players():
    print('\nPlayer One make a choice...')
    p1_choice = player_choice()
    print('\nPlayer Two make a choice...')
    p2_choice = player_choice()
    game(p1_choice, p2_choice)


def game(p1_choice, p2_choice):
    if p1_choice == p2_choice:
        print("It's a draw")
    else:
        if p1_choice == 1:
            if p2_choice == 2:
                print('\nPaper beats Rock. P2 Wins\n')
            if p2_choice == 3:
                print('\nRock beats Scissors. P1 Wins')
        if p1_choice == 2:
            if p2_choice == 1:
                print('\nPaper beats Rock. P1 Wins\n')
            if p2_choice == 3:
                print('\nScissors beat Paper. P2 Wins')
        if p1_choice == 3:
            if p2_choice == 2:
                print('\nScissors beat Paper. P1 Wins\n')
            if p2_choice == 1:
                print('\nRock beats Scissors. P2 Wins')
    retry()


def retry():
    answer = input('\nEnter a number to play again or any other key to quit: \n')
    if answer.isdigit():
        menu()
    else:
        quit()


def single_player():
    print('\nPlayer One make a choice...\n')
    p1_choice = player_choice()
    p2_choice = random.randint(1,3)
    if p2_choice == 1:
        print('\nP2 has chosen Rock\n')
    elif p2_choice == 2:
        print('\nP2 has chosen Paper\n')
    elif p2_choice == 3:
        print('\nP2 has chosen Scissors\n')    
    game(p1_choice, p2_choice)


def title():
        print("""
    __            _                 
    /__\ ___   ___| | __             
    / \/// _ \ / __| |/ /             
    / _  \ (_) | (__|   <              
    \/ \_/\___/ \___|_|\_\             
                                    
    ___                             
    / _ \__ _ _ __   ___ _ __        
    / /_)/ _` | '_ \ / _ \ '__|       
    / ___/ (_| | |_) |  __/ |          
    \/    \__,_| .__/ \___|_|          
            |_|                     
    __      _                         
    / _\ ___(_)___ ___  ___  _ __ ___  
    \ \ / __| / __/ __|/ _ \| '__/ __| 
    _\ \ (__| \__ \__ \ (_) | |  \__ \ 
    \__/\___|_|___/___/\___/|_|  |___/ 
                                    
    """)


def menu():
    choice = input('\nChoose an option:\n\n1. Single Player\n2. Two players\n3. Exit\n\nYour answer: ')
    while choice.isdigit() == False:
        print('\n\nNot a valid option. Try again\n')
        choice = input('\nChoose an option:\n1. Single Player\n2. Two players\n3. Exit\n\nYour answer: ')
        if choice.isdigit():
            break
    if int(choice) == 1:
        single_player()
    elif int(choice) == 2:
        two_players()
    elif int(choice) == 3:
        quit()
    else:
        print('\n\nNot a valid option. Try again\n')
        menu()

    
def run():
    title()
    menu()


if __name__ == '__main__':
    run()
