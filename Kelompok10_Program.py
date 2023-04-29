import mysql.connector
import os
from prettytable import PrettyTable
import time
import pwinput
from datetime import datetime
os.system('cls')

                            #DATABASE
#koneksi ke database
def connect () :
    db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="playlist"
    )
    return db

#fungsi registrasi user
def registrasi_user():
    db = connect()
    #membuat objek cursor untuk melakukan operasi database
    cursor = db.cursor()
    #mengambil input user
    username = str(input("Masukkan username: "))
    password = str(input("Masukkan password: "))

    if username == ""  or password == "":
        print("Input tidak boleh kosong")
        time.sleep(3)
    else :
        status = "nonPremium"

        #mengecek apakah username sudah terdaftar di dalam tabel user di database
        cursor.execute("SELECT * FROM user WHERE username=%s", (username,))
        result = cursor.fetchone()

        if result: #jika username telah terdaftar
            print("Username sudah terdaftar.")
            time.sleep(3)

        else: #jika username belum terdaftar

            # menambahkan user baru ke database
            sql = "INSERT INTO user (username, password, status) VALUES (%s, %s, %s)"
            val = (username, password, status)
            cursor.execute(sql, val) # eksekusi query
            db.commit() #menyimpan perubahan pada database setelah query dijalankan

            print("Registrasi berhasil.")

#fungsi login user
def login_user():
    global username

    username = input("Masukkan username: ")
    password = pwinput.pwinput(prompt="Masukkan password: ")

    db = connect()
    cursor = db.cursor()
    sql = "SELECT * FROM user WHERE username = %s AND password = %s"
    val = (username, password)
    cursor.execute(sql, val)
    
    user = cursor.fetchone() #mengambil satu baris data dari hasil query yang telah dieksekusi 
  
    if user: #jika user ditemukan
        print("Login berhasil!")
        menu()
    else: #jika user tidak ditemukan
        print("Username atau password salah.")
        time.sleep(3)


# LINKED LIST
class Song:
    def __init__(self, judul, artis, tahun_rilis):
        self.judul = judul
        self.artis = artis
        self.tahun_rilis = tahun_rilis
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def get_data(self):
        #mengambil data dari database
        db = connect()
        cursor = db.cursor()
        sql = "SELECT * FROM playlist WHERE akun = %s ORDER BY judul ASC"
        val = (username,)
        cursor.execute(sql, val)
        data = cursor.fetchall()
        return data

    def refreshList(self):
        #mereset semua data di node
        self.reset_data()
        #untuk mengambil data dari database
        result = self.get_data()
        for i in result:
            # Memasukan data kedalam node
            self.add(i[0], i[1], i[2])

    def reset_data(self):
        # Mengembalikan self.head menjadi None
        self.head = None

    def add_database(self, judul, artis, tahun_rilis, username):
        #menambahkan data ke dalam database
        db = connect()
        cursor = db.cursor()
        sql = "INSERT INTO playlist (judul, artis, tahun_rilis, akun) VALUES (%s, %s, %s, %s)"
        val = (judul, artis, tahun_rilis, username)
        cursor.execute(sql, val)
        db.commit()

    def add(self, judul, artis, tahun_rilis):
        #menambhakan data ke dalam node
        new_song = Song(judul, artis, tahun_rilis)
        if self.head is None:
            self.head = new_song
        else:
            new_song.prev = self.tail
            self.tail.next = new_song
        self.tail = new_song

    def remove(self, judul):
        #menghapus data di database
        db = connect()
        cursor = db.cursor()
        sql = "DELETE FROM playlist WHERE judul = %s"
        val = (judul,)
        cursor.execute(sql, val)
        db.commit()
        print("Lagu berhasil dihapus.")

    def display(self):
        #menampilkan data di node
        if self.head is None:
            print("No songs in playlist.")
            return
        table = PrettyTable()
        table.field_names = ["Judul", "Artis", "Tahun Rilis"]
        current_song = self.head
        while current_song:
            table.add_row([current_song.judul, current_song.artis, current_song.tahun_rilis])
            current_song = current_song.next
        print(table)

    def sort_playlist(self, field):
        song_list = []
        current_song = self.head
        while current_song:
            song_list.append(current_song)
            current_song = current_song.next
        if field == "judul":
            sorted_list = self.merge_sort(song_list, lambda song: song.judul)
        elif field == "artis":
            sorted_list = self.merge_sort(song_list, lambda song: song.artis)
        elif field == "tahun_rilis":
            sorted_list = self.merge_sort(song_list, lambda song: song.tahun_rilis)       
        else:
            print("Invalid Input.")
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

    def search(self, x):
        if self.head is None:
            return False
            
        # menghitung ukuran jump block
        table = PrettyTable()
        table.field_names = ["Judul", "Artis"]
        n = 0
        curr_node = self.head
        while curr_node:
            n += 1
            curr_node = curr_node.next
        jump_size = int(n ** 0.5)
            
        # mencari jump block yang berisi x
        prev_node = None
        curr_node = self.head
        while curr_node and curr_node.judul < x:
            prev_node = curr_node
            for i in range(jump_size):
                if curr_node.next and curr_node.next.judul <= x:
                    curr_node = curr_node.next
                else:
                    break
            
        # mencari nilai x dalam jump block
        while prev_node and prev_node.judul < x:
            prev_node = prev_node.next
        while curr_node and curr_node.judul > x:
            curr_node = curr_node.prev
            
        # mengembalikan hasil pencarian
        if prev_node and prev_node.judul == x:
            table.add_row([prev_node.judul, prev_node.artis])
            print(table)
            return True
        elif curr_node and curr_node.judul == x:
            table.add_row([curr_node.judul, curr_node.artis])
            print(table)
            return True
        else:
            return False

    def status_user(self, username):
        #melakukan pengecekan pada status user di database
        db = connect()
        cursor = db.cursor()
        sql = "SELECT status FROM user WHERE username = %s"
        val = (username,)
        cursor.execute(sql, val)
        result = cursor.fetchone()
        if result: #jika ditemukan
            return result[0]
        else:
            return None

    def tambah_playlist(self, status):
        #melakukan input pada data yang akan ditambahkan
        if status == "Premium": #jika user memiliki status Premium
            judul = str(input("Masukan Judul Lagu : "))
            artis = str(input("Masukan Nama Artis: "))
            tahun_rilis = str(input("Masukan Tahun Rilis : "))
            if judul == "" or artis == "" or tahun_rilis == "":
                print("Input tidak boleh kosong")
            else:
                self.add_database(judul, artis, tahun_rilis, username) #menambahkan ke database
                self.refreshList() #melakukan refresh data
                self.display() #menampilkan data

        else : #jika user memiliki status nonPremium
            db = connect()
            cursor = db.cursor()
            sql = "SELECT COUNT(*) FROM playlist WHERE akun = %s" #query untuk menghitung jumlah data pada setiap akun
            val = (username,)

            # periksa jumlah data di database
            cursor.execute(sql, val)
            count = cursor.fetchone()[0]

            if count >= 5: #jika jumlah lagu dalam playlist user sudah lebih/sama dengan 5 record data
                print("Maaf, jumlah data sudah mencapai batas.")
            
            else : #jika jumlah lagu kurang dari 5
                judul = str(input("Masukan Judul Lagu : "))
                artis = str(input("Masukan Nama Artis: "))
                tahun_rilis = str(input("Masukan Tahun Rilis : "))
                if judul == "" or artis == "" or tahun_rilis == "":
                    print("Input tidak boleh kosong")
                else:
                    self.add_database(judul, artis, tahun_rilis, username)
                    self.refreshList()
                    self.display()

    def daftar_premium(self, status):
        global nominal
        global harga
        #melakukan pendaftaran akun Premium
        if status == "Premium": #jika akun user sudah Premium
            os.system(('cls'))
            print("Anda telah terdaftar sebagai Premium")
            time.sleep(3)

        else : #jika akun user belum Premium
            while True:
                os.system('cls')
                print("Pilih menu: ")
                print("1. Pembayaran E-Money")
                print("2. Back")
                
                pilihan = input("Masukkan pilihan: ")
                
                if pilihan == "1":
                    os.system('cls')
                    print("""   
                        1. 30k/bulan
                        2. 60k/3bulan""")

                    paket = int(input("\nMasukan pilihan anda : "))

                    if paket == 1:
                        harga = 30000
                        nominal = int(input("Masukkan nominal pembayaran: "))
                    
                        if nominal < harga: #jika uang yg diinputkan kurang dari harga
                            print("Mohon maaf uang anda tidak mencukupi")

                        else: #jika uang user mencukupi untuk melakukan pembayaran
                            print("Pembayaran berhasil")

                            db = connect()
                            status = "Premium"
                            cursor = db.cursor()
                            sql = "UPDATE user SET status = %s WHERE username = %s"
                            val = (status, username)
                            cursor.execute(sql, val)
                            db.commit()
                            print("Anda berhasil membeli Premium")
                    
                            print("Pembayaran sejumlah", harga, "telah berhasil dilakukan.")
                            time.sleep(3)
                            struk()
                            break
                    
                    elif paket == 2:
                        harga = 60000
                        nominal = int(input("Masukkan nominal pembayaran: "))

                        if nominal < harga:
                            print("Mohon maaf uang anda tidak mencukupi")
                        else :
                            print("Pembayaran berhasil")

                            db = connect()
                            status = "Premium"
                            cursor = db.cursor()
                            sql = "UPDATE user SET status = %s WHERE username = %s"
                            val = (status, username)
                            cursor.execute(sql, val)
                            db.commit()
                            print("Anda berhasil membeli Premium")
                    
                            print("Pembayaran sejumlah", harga, "telah berhasil dilakukan.")
                            time.sleep(3)
                            struk()
                            break
                    
                elif pilihan == "2":
                    break


def menu():
    data = DoubleLinkedList()
    while True:
        try:
            os.system('cls')
            menu = int(input("""
            ===================================================
            |                      MENU                       |
            ===================================================
            |            1. Tambah Lagu Didalam Playlist      |
            |            2. Lihat Lagu Didalam Playlist       |
            |            3. Hapus Lagu Didalam Playlist       |
            |            4. Sorting lagu                      |
            |            5. Search lagu                       |
            |            6. Daftar Premium                    |
            |            7. Keluar                            |
            ===================================================
                        Masukan pilihan anda :  """))
            
            if menu == 1 :
                ulang = "y"
                while (ulang == "y"):
                    os.system('cls')
                    status = data.status_user(username) #melakukan pengecekan status user
                    if status:
                        data.tambah_playlist(status) #menampilkan menu sesuai status user
                        
                    ulang = input("Apakah anda ingin memasukan data lagi (y/n) : ")
                    if ulang == "n":
                        break

            elif menu == 2 :
                ulang = "y"
                while (ulang == "y"):
                    os.system('cls')
                    data.refreshList()
                    data.display()
                    ulang = input("Apakah anda ingin menampilkan data lagi (y/n) : ")
                    if ulang == "n":
                        break

            elif menu == 3 :
                ulang = "y"
                while (ulang == "y"):
                    os.system('cls')
                    data.refreshList()
                    hapus = str(input("Masukan judul yang akan dihapus : "))
                    data.remove(hapus)
                    data.refreshList()
                    data.display()
                    ulang = input("Apakah anda ingin menghapus judul lagi (y/n) : ")
                    if ulang == "n":
                        break

            elif menu == 4 :
                ulang = "y"
                while (ulang == "y"):
                    os.system('cls')
                    data.refreshList()
                    field = input("Pilih sorting menggunakan (judul/artis/tahun_rilis): ")
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
                    data.refreshList()
                    cari= input("Masukkan judul lagunya :")
                    data.search(cari)
                    ulang = input("Apakah anda ingin menampilkan data lagi (y/n) : ")
                    if ulang == "n":
                        break

            elif menu == 6:
                status = data.status_user(username) #melakukan pengecekan status user
                if status:
                    data.daftar_premium(status) #menampilkan menu sesuai status user

            elif menu == 7:
                os.system('cls')
                print("Anda telah keluar dari program")
                break       
        except:
            SyntaxError

def struk():
    waktu = datetime.now()
    time = waktu.strftime("%H:%M:%S")
    angsul = nominal - harga
    with open("invoice.txt", "a") as c:
        print("===========================================================",file=c,)
        print("Struk",  file=c)
        print(f"akun : {username} ",file=c,)
        print(f"dibayar : {nominal}",file=c)
        print(f"kembalian : {angsul}",file=c)
        print(f"pembayaran dilakukan pada pukul : {time}",file=c)
        print("===========================================================",file=c,)

#program utama
while True:
    try :
        os.system('cls')
        print("======================================================")
        print(" >>>  Selamat datang di program Playlist Spotify  <<< ")
        print("======================================================")
        print("|                 1. Registrasi Akun                 |")
        print("|                 2.     Login                       |")
        print("|                 3.     Exit                        |")
        print("======================================================")


        pilihan = input("Masukkan pilihan: ")

        if pilihan == "1":
            os.system('cls')
            registrasi_user()

        elif pilihan == "2":
            os.system('cls')
            login_user()

        elif pilihan == "3":
            os.system('cls')
            print (">>> Anda Telah Keluar dari Program <<<")
            break
        
        else:
            print("Pilihan salah.")

    except :
        print("INVALID INPUT")
