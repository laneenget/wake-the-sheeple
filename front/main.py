from menu import Menu
import view

from back.api.issapi import getData
from back.datastore import Connection, ConnectionStore, ConnectionstoreError

connection_log = ConnectionStore()

def main():
    
    menu = create_menu()

    while True:
        command = view.get_choice(menu) #Get appropriate command
        action = menu.get_action(command) #Call action
        action()
        if command.upper() == 'Q': #End program
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
    getData()

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