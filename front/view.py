"""
    view.py
    This file contains functions that provide the command line interface.
"""
from back.datastore import Connection

# Ask user for a menu choice and validates response
def get_choice(menu):

    print(menu)

    while True:
        command = input('Enter a key: ').upper()
        if menu.is_valid(command): #Get command
            return command
        else:
            print('Not a valid choice, try again.')


# Asks the user if they want to save the data returns valid answer
def get_save():

    while True:
        save = input('Would you like to bookmark this data? Enter Y/N: ').upper()
        if save in ['Y', 'N']:
            return save
        else:
            print('Not a valid choice. Try again.')


# Display all data from table or no data message
def show_data(connections):

    if connections:
        print('')
        for connection in connections:
            print(connection)
        print('')
    else:
        print('No data to display.')


# Messages containing info from the apis printed in various ways based on results
def show_correlation(new_connection):

    print(f"On {new_connection.date} the International Space Sation went over the coordinates, {new_connection.latitude}, {new_connection.longitude}.")  
    if(new_connection.magnitude and new_connection.air):
        print(f"At that exact location there was both an earthquake of magnitude {new_connection.magnitude} and the air quality was {new_connection.air}. The Illuminati world government is clearly behind this.")
    elif(new_connection.magnitude):
        print(f"Around this location there was an earthquake of magnitude {new_connection.magnitude}. The Illuminati world government is clearly behind this.")
    elif(new_connection.air):
        print(f"At that exact location there the air quality was {new_connection.air}. The Illuminati world government is clearly behind this.")
    else:
        print(f"The government has spared us today enjoy a moment of peace.")

# Print messages
def message(msg):
    
    print(msg)


# Get choice for which bookmark user would like to delete
def delete_selection(connections):

    print('Which bookmark would you like to delete?')
    choice = input('Enter bookmark number (Ex. 1,2,3...): ')

    while not choice.isdigit(): # Make sure choice is a number
        print('Not a valid choice. Try again')
        choice = input('Enter bookmark number (Ex. 1,2,3...): ')
        if choice.isdigit():
            choice = int(choice)
            if choice > 0 and choice <= len(connections): # If choice is a number between 1 and the number of bookmarks
                break   # Break -- choice is acceptable

    return choice
    