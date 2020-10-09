# Import the csv and os
import csv
import os

# Read Airports.csv
with open('Airports.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    data = list(reader)

# [['Overseas airport code', 'Overseas airport name', 'Distance from Liverpool John Lennon (km)', 'Distance from Bournemouth International (km)'], ['JFK', 'John F Kennedy International', '5326', '5486'], ['ORY', 'Paris-Orly', '629', '379'], ['MAD', 'Adolfo Suarez Madrid-Barajas', '1428', '1151'], ['AMS', 'Amsterdam Schiphol', '526', '489'], ['CAI', 'Cairo International', '3779', '3584']]

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def quitProgram():
        print('You have quit the program.')
        quit()

def mainMenu():
    print('''
=========================================

Welcome to the airline profit calculator

=========================================

(1) Enter airport details
(2) Enter flight details
(3) Enter price plan and calculate profit
(4) Clear data
(Q) Quit

=========================================
    ''')


    menuSelection = input()

    clear()

    # Enter airport details
    if(menuSelection == '1'):
        ukAirport = input('Enter the 3 letter code for the UK airport. \n')
        if(ukAirport == 'LPL' or ukAirport == 'BOH'):
            abrAirport = input('Enter the three letter code for the overseas airport. \n')
            if abrAirport in data:
                print('it exists')
            else:
                print('it doesnt fucking exist shithead')

        else:
            clear()
            print('Airport code not recognised, returning to main menu.')
            mainMenu()


            


    # Quit
    if(menuSelection == 'q' or menuSelection == '5'):
        quitProgram()

mainMenu()