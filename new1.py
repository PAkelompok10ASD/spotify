import os
import json
import math
import pwinput
from prettytable import PrettyTable
os.system('cls')

            #DATABASE
#json login
jsonlogin = 'D:\\Kuliah\\Semester 2\\praktikum\\ASD\\PA\\regis1.json'

with open(jsonlogin, "r") as lihat_admin:
    admin = json.load(lihat_admin)

def tambah_admin(data_admin):
    with open(jsonlogin, "w") as add_admin:
        json.dump(data_admin, add_admin, indent=4)

name = admin.get("Nama")
pasw = admin.get("Password")
status = admin.get("Status")
saldo = admin.get("e-Money")


# REGIST & LOGIN 
def regis():
    global cari
    nama = input("~ Masukan Username yang anda inginkan : ")
    password = pwinput.pwinput("~ Masukan Password yang anda inginkan : ")
    prem = str(input("Apakah anda ingin mendaftar premium (y/t) : "))
    if prem == "y":
        s = 100000
        name.append(nama)
        pasw.append(password)
        saldo.append(s)
        tambah_admin(admin)
        cari = admin.get("Nama").index(nama)
        print("Registrasi berhasil")
        reg_prem()
            
    elif prem == "t":
        status.append(False)
        s = 100000
        name.append(nama)
        pasw.append(password)
        saldo.append(s)
        tambah_admin(admin)
        print("Registrasi berhasil")
    
def login():
    nama = input("~ Username : ")
    password = pwinput.pwinput("~ Password : ")
    cari = name.index(nama)
    if nama == name[cari] and password == pasw[cari]:
        print("Login berhasil")
        pilih()

def reg_prem():
        print("Daftar premium")
        print("""
        1. Paket 1 : 30k/bulan
        2. Paket 2 : 60k/3bulan
              """)
        pilihp = int(input("Pilih paket yang anda inginkan : "))
        if pilihp == 1:
            harga = 30000
            sd = saldo[cari]
            if sd < harga :
                emoney()
                top = saldo[cari]
                sisa = top - harga
                print("Sisa saldo", sisa)
            else :
                sisa = sd - harga
                print("Sisa saldo", sisa)
        elif pilihp == 2:
            harga = 60000
            sd = saldo[cari]
            if sd < harga :
                emoney()
                top = saldo[cari]
                sisa = top - harga
                print("Sisa saldo", sisa)
            else :
                sisa = sd - harga
                print("Sisa saldo", sisa)

def emoney():
    top = int(input("Masukan nominal top up : "))
    hasil = saldo[cari] + top
    saldo[cari] += hasil

def utama():
    while True:
        try:
            pilih = int(input("""
            1. Login
            2. Registrasi

            Masukan pilihan anda : """))
            if pilih == 1:
                login()
            elif pilih == 2:
                regis()
                utama()
            break 
        except:
            SyntaxError
            os.system("cls")



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

    def sort_playlist(self, field):
        song_list = []
        current_song = self.head
        while current_song:
            song_list.append(current_song)
            current_song = current_song.next
        if field == "title":
            sorted_list = self.merge_sort(song_list, lambda song: song.title)
        elif field == "artist":
            sorted_list = self.merge_sort(song_list, lambda song: song.artist)
        elif field == "year":
            sorted_list = self.merge_sort(song_list, lambda song: song.tahun_rilis)       
        else:
            print("Invalid field.")
            return
        self.head = sorted_list[0]
        for i in range(len(sorted_list)-1):
            sorted_list[i].next = sorted_list[i+1]
        self.tail = sorted_list[-1]
        self.tail.next = None
    
    def merge_sort(self, song_list, key_func):
        if len(song_list) <= 1:
            return song_list
        mid = len(song_list) // 2
        left_list = song_list[:mid]
        right_list = song_list[mid:]
        left_list = self.merge_sort(left_list, key_func)
        right_list = self.merge_sort(right_list, key_func)
        return self.merge(left_list, right_list, key_func)
    
    def merge(self, left_list, right_list, key_func):
        result_list = []
        left_index = 0
        right_index = 0
        while left_index < len(left_list) and right_index < len(right_list):
            if key_func(left_list[left_index]) < key_func(right_list[right_index]):
                result_list.append(left_list[left_index])
                left_index += 1
            else:
                result_list.append(right_list[right_index])
                right_index += 1
        result_list += left_list[left_index:]
        result_list += right_list[right_index:]
        return result_list

    def search(self, keyword):
        table = PrettyTable()
        table.field_names = ["Title", "Artist"]
        n = 0
        current_song = self.head
        while current_song:
            n += 1
            current_song = current_song.next

        current_song = self.head
        jump_size = int(math.sqrt(n))
        prev = None
        while current_song:
            if current_song.title.lower() == keyword.lower() or current_song.artist.lower() == keyword.lower():
                table.add_row([current_song.title, current_song.artist])
            elif current_song.title.lower() > keyword.lower() or current_song.artist.lower() > keyword.lower():
                jump = 0
                while jump < jump_size:
                    if prev:
                        prev = prev.prev
                    jump += 1
                current_song = prev
                continue
            prev = current_song
            current_song = current_song.next
            jump = 0
            while jump < jump_size and current_song:
                prev = current_song
                current_song = current_song.next
                jump += 1
        if len(table._rows) == 0:
            print("No matching songs found.")
        else:
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
                    field = input("Enter the field to sort by (title/artist/year): ")
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
    


utama()