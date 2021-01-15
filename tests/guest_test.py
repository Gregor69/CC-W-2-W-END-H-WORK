import unittest

from src.guest import Guest
from src.song import Song

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest = Guest("Alfie")
        self.song= Song("Dry the Rain", "The Beta Band")

    def test_guest_has_a_name(self):
        self.assertEqual("Alfie", self.guest.name)