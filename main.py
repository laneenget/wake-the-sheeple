from front.menu import Menu
from front.view import get_choice, show_correlation, get_save, show_data, message

from back.api.iss_api import getAllData
from back.api.earthquake_api import return_quake
from back.api.air_quality_api import return_aq
from back.datastore import Connection, ConnectionStore

connection_log = ConnectionStore()

def main():
    
    menu = create_menu()

    while True:
        command = get_choice(menu) 
        action = menu.get_action(command) 
        action()
        if command.upper() == 'Q': 
            break

def create_menu():

    menu = Menu()
    menu.add_command('1', 'Show how the world government is destroying the earth.', search_apis)
    menu.add_command('2', 'Show all bookmarks', show_all)
    menu.add_command('Q', 'Quit', quit_program)

    return menu

def search_apis():
    lat, lng, dateTime = getAllData()
    magnitude = return_quake()
    qual = return_aq()
    new_connection = Connection(lat, lng, magnitude, qual, dateTime, id)
    
    show_correlation(new_connection)
    save = get_save()
    if save == 'Y':
        new_connection.save()

def show_all():

    connections = connection_log.connections_search_all()
    show_data(connections)

def quit_program():

    message('Thanks!')

if __name__ == '__main__':
    main()