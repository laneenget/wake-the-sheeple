def display_correlations(new_connection):
    print(f"On {new_connection.date} the International Space Sation went over the coordinates, {new_connection.latitude}, {new_connection.longitude}.")  
    if(new_connection.magnitude and new_connection.air):
        print(f"At that exact location there was both an earthquake of magnitude {new_connection.magnitude} and the air quality was {new_connection.air}. The Illuminati world government is clearly behind this.")
    elif(new_connection.magnitude):
        print(f"Around this location there was an earthquake of magnitude {new_connection.magnitude}. The Illuminati world government is clearly behind this.")
    elif(new_connection.air):
        print(f"At that exact location there the air quality was {new_connection.air}. The Illuminati world government is clearly behind this.")
    else:
        print(f"The government has spared us today enjoy a moment of peace.")

# def display_bookmarks():


# def display_bookmark():