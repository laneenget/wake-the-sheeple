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

    def delete(self):
        
        self.connectionStore._delete_connection(self)

class ConnectionStore:

    def __init__(self):

        insert_connection = 'CREATE TABLE IF NOT EXISTS Connections (id INT PRIMARY KEY, date TEXT, lat FLOAT, long FLOAT, air TEXT, magnitude FLOAT)'

        con = sqlite3.connect(db)

        with con:
            con.execute(insert_connection)

        con.close()

    def _add_connection(self, connection):

        add_connection = 'INSERT INTO Connections (date, lat, long, magnitude, air) VALUES (?, ?, ?, ?, ?)'

        con = sqlite3.connect(db)

        try:
            with sqlite3.connect(db) as con:
                row = con.execute(add_connection, (connection.date, connection.latitude, connection.longitude, connection.air, connection.magnitude))
        except sqlite3.IntegrityError as e:
            raise ConnectionstoreError(f'This data is already in the database.')
        finally:
            con.close()
    
    def _delete_connection(self, connection):

        delete_connection = 'DELETE FROM Connections WHERE id = ?'

        con = sqlite3.connect(db)

        with con:
            con.execute(delete_connection, (connection.id, ))

        con.close()

    def _search_connection(self, search_connection):

        connections = []

        con = sqlite3.connect(db)
        rows = con.execute(search_connection)

        for r in rows:
            connection = Connection(r[0], r[1], r[2], r[3], r[4], r[5])
            connections.append(connection)

        return connections

    def connection_search(self, string, data):

        search_connection = 'SELECT * FROM Connections WHERE ? = ?'
        connections = []

        con = sqlite3.connect(db)
        rows = con.execute(search_connection, (string, data))

        for r in rows:
            connection = Connection(r[0], r[1], r[2], r[3], r[4], r[5])
            connections.append(connection)

        return connections

    def connections_search_all(self):

        search_connection = 'SELECT * FROM Connections'
        connections = []

        con = sqlite3.connect(db)
        rows = con.execute(search_connection)

        for r in rows:
            connection = Connection(r[0], r[1], r[2], r[3], r[4], r[5])
            connections.append(connection)

        return connections

class ConnectionstoreError(Exception):
    pass