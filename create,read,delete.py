import os
from prettytable import PrettyTable
os.system('cls')

#CRUD
class Song:
    def __init__(self, title, artist, tahun_rilis):
        self.title = title
        self.artist = artist
        self.tahun_rilis = tahun_rilis
        self.next = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, title, artist, tahun_rilis):
        new_song = Song(title, artist, tahun_rilis)
        if self.head is None:
            self.head = new_song
        else:
            self.tail.next = new_song
        self.tail = new_song

    def remove(self, title):
        current_song = self.head
        previous_song = None
        found = False
        while current_song and not found:
            if current_song.title.lower() == title.lower():
                found = True
            else:
                previous_song = current_song
                current_song = current_song.next
        if current_song is None:
            print("Song not found.")
            return
        if previous_song is None:
            self.head = current_song.next
        else:
            previous_song.next = current_song.next
        if current_song.next is None:
            self.tail = previous_song
        print("Song removed.")

    def display(self):
        if self.head is None:
            print("No songs in playlist.")
            return
        table = PrettyTable()
        table.field_names = ["Title", "Artist", "Tahun Rilis"]
        current_song = self.head
        while current_song:
            table.add_row([current_song.title, current_song.artist, current_song.tahun_rilis])
            current_song = current_song.next
        print(table)


def pilih():
    data = DoubleLinkedList()
    listnya2 = DoubleLinkedList()
    while True:
        try:
            os.system('cls')
            menu = int(input("""
            ---------------------------------------------------
                        1. Tambah Lagu Didalam Playlist
                        2. Lihat Lagu Didalam Playlist
                        3. Hapus Lagu Didalam Playlist 
                        4. Sorting lagu 
                        5. Search lagu
                        6. Keluar
            ---------------------------------------------------
                        Masukan pilihan anda :  """))

            
            if menu == 1 :
                ulang = "y"
                while (ulang == "y"):
                    os.system('cls')
                    title = str(input("Masukan Judul Lagu : "))
                    artist = str(input("Masukan Nama Artis: "))
                    tahun_rilis = str(input("Masukan Tahun Rilis : "))
                    data.add(title, artist, tahun_rilis)
                    listnya2.add(title, artist, tahun_rilis)
                    data.display()
                    ulang = input("Apakah anda ingin memasukan data lagi (y/n) : ")
                    if ulang == "n":
                        break
            elif menu == 2 :
                ulang = "y"
                while (ulang == "y"):
                    os.system('cls')
                    data.display()
                    ulang = input("Apakah anda ingin menampilkan data lagi (y/n) : ")
                    if ulang == "n":
                        break
            elif menu == 3 :
                ulang = "y"
                while (ulang == "y"):
                    os.system('cls')
                    hapus = str(input("Masukan title yang akan dihapus : "))
                    data.remove(hapus)
                    data.display()
                    ulang = input("Apakah anda ingin menghapus title lagi (y/n) : ")
                    if ulang == "n":
                        break
            elif menu == 4 :
                ulang = "y"
                while (ulang == "y"):
                    os.system('cls')
                    field = input("Enter the field to sort by (title/artist): ")
                    data.sort_playlist(field)
                    data.display()
                    print("Playlist sorted.")
                    ulang = input("Apakah anda ingin menampilkan data lagi (y/n) : ")
                    if ulang == "n":
                        break
            elif menu == 5 :
                ulang = "y"
                while (ulang == "y"):
                    os.system("cls")
                    cari= input("Masukkan judul lagunya :")
                    data.search(cari)
                    ulang = input("Apakah anda ingin menampilkan data lagi (y/n) : ")
                if ulang == "n":
                    break
            elif menu == 6:
                os.system('cls')
                print("Anda telah keluar dari program")
                break       
        except:
            SyntaxError
