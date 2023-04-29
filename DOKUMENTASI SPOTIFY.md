# PROJECT AKHIR  PROGRAM SPOTIFY
-----------------------------------------------------------------------------------------------------------

## DESKRIPSI PROGRAM
> Program Spotify ini dibuat dengan tujuan untuk membantu pengguna dalam mengelola playlist lagu dan memudahkan pengguna dalam menambahkan lagu-lagu baik itu populer maupun tidak ke dalam playlist sesuai dengan selera musik mereka. Pengguna dapat melihat daftar lagu yang telah ditambahkan ke dalam playlist dan menghapus judul lagu yang tidak diinginkan dari playlist tersebut. Program ini juga menyediakan fitur pencarian lagu dan pengurutan komponen lagu berdasarkan abjad atau angka. Dengan begitu, diharapkan program ini dapat memberikan kemudahan bagi pengguna dalam mengelola playlist lagu mereka. 

> Program ini juga dibuat menggunakan Bahasa Pemrograman yakni Python serta mengimplementasikan struktur data Linked List. Program ini juga menggunakan database localhost untuk menyimpan data akun pengguna dan data lagu dari program Spotify itu sendiri. Dengan adanya database ini, pengguna dapat dengan mudah mengakses playlist dan informasi akun mereka tanpa kehilangan data.

## STRUKTUR PROJECT
### A. LIBRARY
1. Import Time, yaitu modul yang menyediakan berbagai fungsi yang berhubungan dengan waktu dan tanggal
2. Import Os, yaitu modul yang dapat digunakan untuk berinteraksi dengan sistem operasi dan melakukan operasi pada file dan folder.
3. Import pwinput, yaitu modul python yang menampilkan sejenis tanda bintang * untuk input kata sandi.
4. From PrettyTable import PrettyTable, yaitu pustaka atau library dalam Python yang digunakan untuk membuat atau mengeluarkan data dalam bentuk tabel
5. From datetime import datetime, yakni modul yang dipanggil jika anda membutuhkan segala operasi yang berhubungan dengan waktu/untuk memanipulasi tanggal dan waktu
6. import mysql.connector, yaitu modul untuk menghubungkan dan berinteraksi dengan database MySQL dari program Python. Dengan mengimpor modul ini, kita bisa menggunakan fungsi-fungsi dan objek-objek yang tersedia di dalamnya untuk melakukan operasi-operasi pada database MySQL

### B. LINKED LIST
- Class Song
- Class DoubleLinkedList

**Fungsi dalam Class DoublyLinkedList :**
- get_data
- refreshList                
- reset_data                   
- add_database                
- add
- remove
- display
- sort_playlist
- merge_sort
- merge
- search
- status_user
- tambah_playlist
- daftar_premium

### C. FUNGSI 
- def connect (koneksi ke database)
- def registrasi_user
- def login_user
- def menu
- def struk

**Main Program/Program Utama (Tidak termasuk fungsi dan berada di luar class)**

## FITUR
Beberapa fitur yang terdapat pada program ini, yaitu :
- Registrasi Pengguna (Premium dan Non Premium)
- Login Pengguna (Premium dan Non Premium)
- Menambahkan lagu pada playlist
- Melihat daftar lagu pada playlist
- Menghapus lagu pada playlist
- Mendaftar paket premium
- Mencetak bukti pembayaran

## FUNGSIONALITAS 
> Pengguna dapat melakukan registrasi akun terlebih dahulu untuk memasuki program dengan cara memasukkan username dan juga password dan otomatis akan tersimpan di database
> Pengguna dapat login menggunakan akun yang telah diregistrasi sebelumnya dan otomatis akan tersimpan di database
> Pengguna juga dapat keluar dari program melalui pilihan Exit.
> Terdapat 2 jenis pengguna yakni Premium dan Non Premium :

> 1. Pengguna Premium :
- Menambah : Pengguna dapat menambah judul, nama artis dan tahun rilis lagu kedalam playlist dengan total lagu yakni > 5, tidak ada batasan sama sekali.
- Melihat : Pengguna dapat melihat judul, nama artis dan tahun rilis lagu yang ada didalam playlist yang telah ditambahkan sebelumnya.
- Menghapus : Pengguna dapat menghapus judul lagu yang ada didalam playlist yang telah dibuat
- Mengurutkan : Pengguna dapat melakukan pengurutan judul, nama artis dan tahun rilis berdasarkan abjad ataupun angka.
- Mencari : Pengguna dapat melakukan pencarian judul lagu dimana saat judul lagu tersebut telah tertulis, akan muncul tulisan yang berisi judul lagu beserta nama artis dari lagu tersebut.
- Mendaftar : Pengguna dapat melakukan pendaftaran untuk menjadi Premium dengan pilihan paket yang tersedia.
- Mencetak : Setelah melakukan pendaftaran dan memilih paket premium yang diinginkan, maka pengguna dapat langsung mencetak bukti pembayaran (invoice) sebagai bukti bahwa pengguna telah beralih dari Non Premium ke Premium. (Semuanya otomatis akan tersimpan di database).

> 2. Pengguna Non Premium
- Menambah : Pengguna dapat menambah judul, nama artis dan tahun rilis lagu kedalam playlist dengan total maksimal 5 lagu, tidak boleh lebih dari itu.
- Melihat : Pengguna dapat melihat judul, nama artis dan tahun rilis lagu yang ada didalam playlist yang telah ditambahkan sebelumnya.
- Menghapus : Pengguna dapat menghapus judul lagu yang ada didalam playlist yang telah dibuat
- Mengurutkan : Pengguna dapat melakukan pengurutan judul, nama artis dan tahun rilis berdasarkan abjad ataupun angka.
- Mencari : Pengguna dapat melakukan pencarian judul lagu dimana saat judul lagu tersebut telah tertulis, akan muncul tulisan yang berisi judul lagu beserta nama artis dari lagu tersebut.
- Mendaftar : Pengguna dapat melakukan pendaftaran untuk menjadi Premium dengan pilihan paket yang tersedia.
- Mencetak : Setelah melakukan pendaftaran dan memilih paket premium yang diinginkan, maka pengguna dapat langsung mencetak bukti pembayaran (invoice) sebagai bukti bahwa pengguna telah beralih dari Non Premium ke Premium. (Semuanya otomatis akan tersimpan di database).
