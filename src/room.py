class Room:
    def __init__(self, name):
        self.name = name
        self.guests = []
        self.songs = []

    def guest_count(self):
        return len(self.guests)

    def checkin_guest(self, guest):
        self.guests.append(guest)

    def checkout_guest(self, guest):
        self.guests.remove(guest)

    def closeroom(self, guest):
        if len(self.guests) == 5:
            return "Room closed"
     
    def song_count(self):
        return len(self.songs)

    def add_song(self, song):
        self.songs.append(song)

    def remove_song(self, song):
        self.songs.remove(song)

    
