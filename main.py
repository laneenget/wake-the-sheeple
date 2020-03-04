"""
    main.py
    Main file that handles the flow of the program
"""

from front.menu import Menu
from front.view import get_choice, show_correlation, get_save, show_data, message, delete_selection

from exceptions import handle_air_n_quake_exceptions

from back.api.iss_api import get_all_data
from back.api.earthquake_api import return_quake
from back.api.air_quality_api import return_aq
from back.datastore import Connection, ConnectionStore

from concurrent.futures import ThreadPoolExecutor

connection_log = ConnectionStore()


def main():
    
    menu = create_menu()

    # Loop until user wants to quit
    while True:
        command = get_choice(menu) 
        action = menu.get_action(command) 
        action()
        if command.upper() == 'Q': # Exit program
            break


# Create the menu for user
def create_menu():

    menu = Menu()
    menu.add_command('1', 'Show how the world government is destroying the earth.', search_apis)
    menu.add_command('2', 'Show all bookmarks', show_all)
    menu.add_command('3', 'Delete a bookmark', delete_bookmark)
    menu.add_command('Q', 'Quit', quit_program)

    return menu


# Triggered when user enters command 1, get api results for ISS, then earthquake api and air quality api
def search_apis():
    lat, lng, dateTime = get_all_data()
    magnitude = return_quake()
    qual = return_aq()

    # Exception handling
    qual = handle_air_n_quake_exceptions(qual)
    magnitude =handle_air_n_quake_exceptions(magnitude)

    new_connection = Connection(lat, lng, magnitude, qual, dateTime, id)
    
    show_correlation(new_connection) # Show data retrieved from api calls
    save = get_save()  # Ask user if they want to bookmark results
    if save == 'Y':
        new_connection.save()  # If yes, add info to table in database


# Retrieve all bookmarks from database table and print them
def show_all():

    connections = connection_log.connections_search_all()
    show_data(connections)


# User wants to delete a bookmark
def delete_bookmark():

    connections = connection_log.connections_search_all() # Get all from table in a list
    show_data(connections) # Print connections
    response = delete_selection(connections) # Get bookmark id user wants to delete
    connection_log.delete_bookmark(response)
    print('Bookmark Deleted.')


# Exit program
def quit_program():

    message('Thanks!')


if __name__ == '__main__':
    main()