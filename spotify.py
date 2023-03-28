import os
os.system('clear')
from prettytable import PrettyTable

class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
        self.next = None

class Playlist:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_song(self, title, artist):
        new_song = Song(title, artist)
        if not self.head:
            self.head = new_song
            self.tail = new_song
        else:
            self.tail.next = new_song
            self.tail = new_song

    def remove_song(self, title):
        current_song = self.head
        previous_song = None
        while current_song:
            if current_song.title == title:
                if previous_song:
                    previous_song.next = current_song.next
                else:
                    self.head = current_song.next
                return True
            previous_song = current_song
            current_song = current_song.next
        return False

    def display_playlist(self):
        table = PrettyTable()
        table.field_names = ["Title", "Artist"]
        current_song = self.head
        while current_song:
            table.add_row([current_song.title, current_song.artist])
            current_song = current_song.next
        print(table)

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.playlist = Playlist()
        self.history = []

    def add_song_to_playlist(self, title, artist):
        self.playlist.add_song(title, artist)
        self.history.append(Song(title, artist))

    def remove_song_from_playlist(self, title):
        if self.playlist.remove_song(title):
            for song in self.history:
                if song.title == title:
                    self.history.remove(song)
            return True
        return False

    def display_playlist(self):
        self.playlist.display_playlist()

    def display_history(self):
        table = PrettyTable()
        table.field_names = ["Title", "Artist"]
        for song in self.history:
            table.add_row([song.title, song.artist])
        print(table)

def login(username, password, users):
    for user in users:
        if user.username == username and user.password == password:
            return user
    return None

def register(username, password, users):
    for user in users:
        if user.username == username:
            return None
    new_user = User(username, password)
    users.append(new_user)
    return new_user

def main():
    users = []

    while True:
        os.system('clear')
        print("1. Login")
        print("2. Register")
        print("3. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            user = login(username, password, users)
            if user:
                while True:
                    print("1. Add song to playlist")
                    print("2. Remove song from playlist")
                    print("3. Display playlist")
                    print("4. Display history")
                    print("5. Logout")
                    choice = input("Enter your choice: ")

                    if choice == "1":
                        os.system('clear')
                        title = input("Enter the title of the song: ")
                        artist = input("Enter the artist of the song: ")
                        user.add_song_to_playlist(title, artist)
                    elif choice == "2":
                        os.system('clear')
                        title = input("Enter the title of the song: ")
                        user.remove_song_from_playlist(title)
                    elif choice == "3":
                        os.system('clear')
                        user.display_playlist()
                    elif choice == "4":
                        os.system('clear')
                        user.display_history()
                    elif choice == "5":
                        break
                    else:
                        print("Invalid choice.")
                print("Logged out.")
            else:
                print("Invalid username or password.")
        elif choice == "2":
            username = input("Enter your desired username: ")
            password = input("Enter your desired password: ")
            user = register(username, password, users)
            if user:
                print("Account created successfully.")
            else:
                print("Username already exists.")
        elif choice == "3":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()