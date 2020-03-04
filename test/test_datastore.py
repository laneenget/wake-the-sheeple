from unittest import TestCase
import os

import back.datastore
from back.datastore import Connection, ConnectionStore

class TestDataStore(TestCase):

    @classmethod
    def setUpClass(cls):
        back.datastore.db = os.path.join('test_datastore.db')
        ConnectionStore.instance = None

    def setUp(self):
        self.CS = ConnectionStore()
        self.clear_db()

    def clear_db(self):
        self.CS.delete_all_connections()

    def add_data(self):
        self.clear_db()

        self.c1 = Connection(4.0401, -72.9593, 4.5, 'good', '2020-03-02 16:17:13', 1)
        self.c2 = Connection(-3.5641, -67.5623, 3.2, 'poor', '2020-03-02 16:44:46', 2)
        self.c3 = Connection(46.5141, 32.2419, 1.1, 'poor', '2020-03-03 01:06:56', 3)

        self.c1.save()
        self.c2.save()
        self.c3.save()

    def test_add_data(self):
        self.add_data()

        connections = self.CS.connections_search_all()

        self.assertEqual(3, len(connections))

    def test_delete_all_connections(self):
        self.add_data()
        self.clear_db()

        connections = self.CS.connections_search_all()

        self.assertEqual(0, len(connections))