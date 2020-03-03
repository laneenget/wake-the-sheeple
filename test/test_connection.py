from unittest import TestCase
import os

import back.datastore
from back.datastore import Connection, ConnectionStore

class TestConnection(TestCase):

    @classmethod
    def setUpClass(cls):
        back.datastore.db = os.path.join('test_datastore.db')
        ConnectionStore.instance = None

    def setUp(self):
        self.CS = ConnectionStore()
        self.clear_connections()

    def test_save(self):
        self.clear_connections()

        connection = Connection(-100.23, 24.34, 4.7, 'good', '2020-03-02 16:17:13', 1)
        connection.save()

        db = ConnectionStore()
        connections = db.connections_search_all()
        self.assertEqual(1, len(connections))

    def clear_connections(self):
        self.CS.delete_all_entries()