import sqlite3
import os

db = os.path.join('conspiracystore.db')

class Connection:

    def __init__(self, latitude, longitude, magnitude, air, date, id):

        self.latitude = latitude
        self.longitude = longitude
        self.magnitude = magnitude
        self.air = air
        self.date = date
        self.id = id

        self.connectionStore = ConnectionStore()

    def __str__(self):

        return f'{self.id}. Date and time: {self.date}, Coordinates: [{self.latitude}, {self.longitude}], Air quality: {self.air}, Magnitude: {self.magnitude}'

    def __repr__(self):

        return f'{self.id}. Date and time: {self.date}, Coordinates: [{self.latitude}, {self.longitude}], Air quality: {self.air}, Magnitude: {self.magnitude}'

    def save(self):

        self.connectionStore._add_connection(self)

class ConnectionStore:

    def __init__(self):

        insert_connection = 'CREATE TABLE IF NOT EXISTS Connections (id INTEGER PRIMARY KEY AUTOINCREMENT, date TEXT, lat FLOAT, long FLOAT, air TEXT, magnitude FLOAT)'

        con = sqlite3.connect(db)

        with con:
            con.execute(insert_connection)

        con.close()

    def _add_connection(self, connection):

        add_connection = 'INSERT INTO Connections (date, lat, long, magnitude, air) VALUES (?, ?, ?, ?, ?)'

        con = sqlite3.connect(db)

        with con:
            row = con.execute(add_connection, (connection.date, connection.latitude, connection.longitude, connection.magnitude, connection.air))
    
        con.close()

    def delete_all_connections(self):

            delete = "DELETE FROM connections"

            with sqlite3.connect(db) as con:
                con.execute(delete)

            con.close()

    def connections_search_all(self):

        search_connection = 'SELECT * FROM Connections'
        connections = []

        con = sqlite3.connect(db)
        con.row_factory = sqlite3.Row
        rows = con.execute(search_connection)

        for r in rows:
            connection = Connection(r['lat'], r['long'], r['magnitude'], r['air'], r['date'], r['id'])
            connections.append(connection)

        return connections