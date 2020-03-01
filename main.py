from menu import Menu
import view

from issapi import getData
from earthquakeapi import get_earthquake
from airqualityapi import get_aq
from datastore import Connection, ConnectionStore, ConnectionstoreError

connection_log = ConnectionStore()

def main():
    
    menu = create_menu()

    while True:
        command = view.get_choice(menu) 
        action = menu.get_action(command) 
        action()
        if command.upper() == 'Q': 
            break

def create_menu():

    menu = Menu()
    menu.add_command('1', 'Show how the world government is destroying the earth.', search_apis)
    menu.add_command('2', 'Search bookmarks', search_bookmarks)
    menu.add_command('3', 'Show all bookmarks', show_all)
    menu.add_command('Q', 'Quit', quit_program)

    return menu

"""Take user input latitude and longitude, query the three APIs to find appropriate data, and prompt user to save if the user desires"""
def search_apis():
    lat, lng, dateTime = getData()
    magnitude = get_earthquake(lat, lng)
    qual = get_aq(lat, lng)

    if(magnitude):
        print(magnitude)


def search_bookmarks():

    string, data = view.get_param()
    connections = connection_log.connection_search(string, data)
    view.show_data(connections)


def show_all():

    connections = connection_log.connections_search_all()
    view.show_data(connections)

def quit_program():

    view.message('Thanks!')

if __name__ == '__main__':
    main()