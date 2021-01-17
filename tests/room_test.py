import unittest

from src.room import Room
from src.guest import Guest
from src.song import Song

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room = Room("Give us a tune")
        self.guest_1 = Guest("Alfie")
        self.song_1 = Song("Dry the Rain", "The Beta Band")

    def test_room_has_a_name(self):
        self.assertEqual("Give us a tune", self.room.name)

    def test_room_can_checkin_guest(self):
        self.room.checkin_guest(self.guest_1)
        self.assertEqual(1, self.room.guest_count())

    def test_room_can_checkout_guest(self):
        self.room.checkin_guest(self.guest_1)
        self.room.checkout_guest(self.guest_1)
        self.assertEqual(0, self.room.guest_count())

    def test_room_can_add_song(self):
        self.room.add_song(self.song_1)
        self.assertEqual(1, self.room.song_count())

    def test_room_can_remove_song(self):
        self.room.add_song(self.song_1)
        self.room.remove_song(self.song_1)
        self.assertEqual(0, self.room.song_count())