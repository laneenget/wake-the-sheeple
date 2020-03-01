from back.datastore import Connection

def get_choice(menu):

    print(menu)

    while True:
        command = input('Enter a key: ').upper()
        if menu.is_valid(command): #Get command
            return command
        else:
            print('Not a valid choice, try again.')

def get_search_data():

    latitude, longitude = input('Enter the latitude and longitude you\'d like to search separated by a space: ').split()
    return latitude, longitude


def get_save():

    save = input('Would you like to bookmark this data? Enter Y/N: ')
    return save

def get_param():

    string = input('Enter the parameters by which you\'d like to search (coordinates, date, etc.): ')
    data = input('Enter the data you are looking for: ')
    return string, data

def show_data(connections):

    if connections:
        print('')
        for connection in connections:
            print(connection)
        print('')
    else:
        print('No data to display.')

def message(msg):
    
    print(msg)