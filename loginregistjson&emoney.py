import os
import json
import pwinput
from prettytable import PrettyTable
os.system('cls')

            #DATABASE
#json login
jsonlogin = 'regis1.json'

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
