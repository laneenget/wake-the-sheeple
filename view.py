from datastore import Connection

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

def message(msg):
    
    print(msg)