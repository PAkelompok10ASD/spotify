# Dokumentasi

Program ini adalah program yang digunakan untuk mengelola sebuah progream manajemen playlist lagu. Program ini menggunakan bahasa Python.

Program ini membutuhkan beberapa library yang akan digunakan seperti os, json, math, pwinput, prettytable, dan time. Library os digunakan untuk membersihkan tampilan konsol, library json digunakan untuk membaca dan menulis file JSON, library pwinput digunakan untuk mengamankan password, library prettytable digunakan untuk membuat tabel di konsol, dan library time digunakan untuk mengatur waktu delay.

Program ini memiliki sebuah database yang berupa file JSON yang berisi data dari akun pengguna seperti nama, password, status (premium atau tidak), dan saldo e-money. 

Setelah mendapatkan data dari file JSON, program ini melakukan definisi terhadap beberapa variabel yang akan digunakan di seluruh program. Variabel yang didefinisikan adalah nama (name), password (pasw), status (status), dan saldo (saldo). Nama, password, status, dan saldo ini digunakan untuk menandai informasi admin yang melakukan login.

bagian REGIST & LOGIN yang berfungsi untuk melakukan registrasi dan login. Fungsi regis digunakan untuk melakukan registrasi dan menginput data username, password, dan status user apakah premium atau tidak. Fungsi login digunakan untuk melakukan login dengan meminta input username dan password dari user. Fungsi reg_prem digunakan untuk melakukan pendaftaran premium dan menampilkan paket yang tersedia. Fungsi emoney digunakan untuk melakukan top-up saldo pada akun user.

pada bagian REGIST & LOGIN, jika pengguna memilih Login, program akan meminta pengguna untuk memasukkan nama dan password. Setelah itu, program akan memeriksa apakah data yang dimasukkan oleh pengguna benar atau tidak. Jika benar, pengguna akan diarahkan ke menu utama dan ditampilkan beberapa pilihan fitur seperti menambahkan lagu ke playlist, menghapus lagu dari playlist, dan sebagainya.

Jika pengguna memilih Registrasi, maka pengguna diminta untuk memasukkan username dan password serta memilih apakah pengguna ingin mendaftar premium atau tidak. Jika memilih mendaftar premium, maka pengguna akan diminta untuk memilih paket premium yang diinginkan.

Setelah berhasil login, pengguna dapat melakukan beberapa operasi seperti menambahkan, menghapus, atau melihat lagu pada playlist menggunakan konsep CRUD (Create, Read, Update, Delete) dan dilakukan menggunakan metode double linked list. Data lagu yang dimasukkan akan disimpan dalam sebuah tabel menggunakan modul prettytable.

Program ini juga menggunakan modul pwinput untuk menyembunyikan password yang dimasukkan oleh pengguna. Program ini juga menggunakan modul time untuk membuat animasi loading iklan saat pengguna tidak premium memilih menu didalam program.
