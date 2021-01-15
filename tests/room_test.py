import unittest

from src.room import Room
from src.guest import Guest
from src.song import Song

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room = Room("Give us a tune, son")
        # self.song= Song("Dry the Rain", "The Beta Band")

    def test_room_has_a_name(self):
        self.assertEqual("Give us a tune, son", self.room.name)