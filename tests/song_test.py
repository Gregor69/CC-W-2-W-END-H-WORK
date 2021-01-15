import unittest
from src.song import Song

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song = Song("Dry the Rain", "The Beta Band")
        self.song.title = ("Dry the Rain")
        self.song.artist = ("The Beta Band")

    def test_song_has_a_title(self):
        self.assertEqual("Dry the Rain", self.song.title)
    
    def test_song_has_artist(self):
        self.assertEqual("The Beta Band", self.song.artist)