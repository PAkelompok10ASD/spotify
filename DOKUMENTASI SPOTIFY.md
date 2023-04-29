# PROJECT AKHIR  PROGRAM SPOTIFY
-----------------------------------------------------------------------------------------------------------

### DESKRIPSI PROGRAM
> Program Spotify ini dibuat dengan tujuan untuk membantu pengguna dalam mengelola playlist lagu dan memudahkan pengguna dalam menambahkan lagu-lagu baik itu populer maupun tidak ke dalam playlist sesuai dengan selera musik mereka. Pengguna dapat melihat daftar lagu yang telah ditambahkan ke dalam playlist dan menghapus judul lagu yang tidak diinginkan dari playlist tersebut. Program ini juga menyediakan fitur pencarian lagu dan pengurutan komponen lagu berdasarkan abjad atau angka. Dengan begitu, diharapkan program ini dapat memberikan kemudahan bagi pengguna dalam mengelola playlist lagu mereka. 

> Program ini juga dibuat menggunakan Bahasa Pemrograman yakni Python serta mengimplementasikan struktur data Linked List. Program ini juga menggunakan database localhost untuk menyimpan data akun pengguna dan data lagu dari program Spotify itu sendiri. Dengan adanya database ini, pengguna dapat dengan mudah mengakses playlist dan informasi akun mereka tanpa kehilangan data.


### STRUKTUR PROJECT
> 1. Folder Controller, berisi file-file controller yang akan mengatur alur program serta mengambil data dari model dan menampilkan ke view.                                   - File Controller Account, sebagai file controller yang berisi logika untuk manajemen akun mahasiswa dan staff, seperti registrasi, login, dan profil user.
        - File Controller Linked List, sebagai file controller yang berisi logika untuk manajemen data ruang kelas dalam bentuk linked list, dimana data dalam linked list diambil dari database.
        - File Controller User, sebagai file controller yang berisi logika untuk manajemen data mahasiswa dan staff seperti logika menambahkan peminjaman ruang.
> 2. Folder Model, berisi file-file model yang berisi fungsi-fungsi untuk mengakses database dan memproses data.
        - File Database, sebagai file yang berisi class untuk menghubungkan python dan database.
        - File Ruang, sebagai file yang berisi definisi class Ruang yang digunakan untuk merepresentasikan sebuah node pada struktur data Linked List.
> 3. Folder View, berisi file-file view yang berisi tampilan antarmuka aplikasi yang akan dilihat oleh pengguna.
        - File App, sebagai halaman untuk menampilkan informasi dan melakukan peminjaman ruang kelas oleh pengguna yang belum terdaftar sebagai staff atau mahasiswa.
        - File Mahasiswa, sebagai halaman untuk menampilkan informasi dan melakukan peminjaman ruang kelas oleh mahasiswa.
        - File Staff, sebagai halaman untuk menampilkan informasi dan daftar peminjaman ruang kelas oleh staff.
> 4. File main, sebagai file utama yang berfungsi untuk menjalankan program.

### FITUR
Pada program ini terdapat library yang digunakan, diantaranya adalah PrettyTable, Datetime, time, PyMongo, os dan random.
>  1. PrettyTable merupakan library atau pustaka dalam python yang digunakan untuk membuat / mengeluarkan data dalam bentuk tabel.
>  2. Datetime adalah sebuah library atau modul yang dipanggil jika anda membutuhkan segala operasi yang berhubungan demi waktu.
>  3. Modul time adalah modul yang menyediakan fungsi-fungsi untuk mengelola waktu dan tanggal. 
>  4. PyMongo berisi alat untuk bekerja dengan MongoDB, dan merupakan cara yang disarankan untuk bekerja dengan MongoDB dari Python.
     Untuk menjalankan PyMongo sendiri, hal yang harus dilakukan adalah mengakses MongoDB ataupun menginstall MongoDB. 
     Selanjutnya user dapat memverifikasi apakah instalasi telah selesai dengan sukses, kita akan terhubung ke server database MongoDB menggunakan alat mongo dan melihat status koneksi melalui MongoDB. 
     Terdapat opsi authorization yang memungkinkan Role-Based Access Control (RBAC) yang mengatur akses pengguna ke sumber daya dan operasi database. 
     Jika opsi ini dinonaktifkan, setiap user akan memiliki akses ke semua database dan melakukan tindakan apa pun.
>  5. Modul os dapat digunakan untuk berinteraksi dengan sistem operasi dan melakukan operasi pada file dan direktori.
>  6. Modul random pada adalah modul yang menyediakan fungsi-fungsi untuk menghasilkan bilangan acak. 

### FUNGSIONALITAS 
>
### CARA PENGGUNAAN
Program ini adalah program yang digunakan untuk mengelola sebuah progream manajemen playlist lagu. Program ini menggunakan bahasa Python.

Program ini membutuhkan beberapa library yang akan digunakan seperti os, json, math, pwinput, prettytable, dan time. Library os digunakan untuk membersihkan tampilan konsol, library json digunakan untuk membaca dan menulis file JSON, library pwinput digunakan untuk mengamankan password, library prettytable digunakan untuk membuat tabel di konsol, dan library time digunakan untuk mengatur waktu delay.

Program ini memiliki sebuah database yang berupa file JSON yang berisi data dari akun pengguna seperti nama, password, status (premium atau tidak), dan saldo e-money. 

Setelah mendapatkan data dari file JSON, program ini melakukan definisi terhadap beberapa variabel yang akan digunakan di seluruh program. Variabel yang didefinisikan adalah nama (name), password (pasw), status (status), dan saldo (saldo). Nama, password, status, dan saldo ini digunakan untuk menandai informasi admin yang melakukan login.

bagian REGIST & LOGIN yang berfungsi untuk melakukan registrasi dan login. Fungsi regis digunakan untuk melakukan registrasi dan menginput data username, password, dan status user apakah premium atau tidak. Fungsi login digunakan untuk melakukan login dengan meminta input username dan password dari user. Fungsi reg_prem digunakan untuk melakukan pendaftaran premium dan menampilkan paket yang tersedia. Fungsi emoney digunakan untuk melakukan top-up saldo pada akun user.

pada bagian REGIST & LOGIN, jika pengguna memilih Login, program akan meminta pengguna untuk memasukkan nama dan password. Setelah itu, program akan memeriksa apakah data yang dimasukkan oleh pengguna benar atau tidak. Jika benar, pengguna akan diarahkan ke menu utama dan ditampilkan beberapa pilihan fitur seperti menambahkan lagu ke playlist, menghapus lagu dari playlist, dan sebagainya.

Jika pengguna memilih Registrasi, maka pengguna diminta untuk memasukkan username dan password serta memilih apakah pengguna ingin mendaftar premium atau tidak. Jika memilih mendaftar premium, maka pengguna akan diminta untuk memilih paket premium yang diinginkan.

Setelah berhasil login, pengguna dapat melakukan beberapa operasi seperti menambahkan, menghapus, atau melihat lagu pada playlist menggunakan konsep CRUD (Create, Read, Update, Delete) dan dilakukan menggunakan metode double linked list. Data lagu yang dimasukkan akan disimpan dalam sebuah tabel menggunakan modul prettytable.

Program ini juga menggunakan modul pwinput untuk menyembunyikan password yang dimasukkan oleh pengguna. Program ini juga menggunakan modul time untuk membuat animasi loading iklan saat pengguna tidak premium memilih menu didalam program. 
