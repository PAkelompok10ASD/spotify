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


### Cara Penggunaan
# Menu Awal
> Pada saat Program pertama kali dijalankan maka akan muncul tampilan/menu awal yang berisi 3 pilihan yakni Registrasi Akun, Login dan Exit.

# Registrasi Pengguna
> Jika pengguna belum mempunyai akun, maka pengguna dapat memilih opsi 1 yakni Registrasi Akun, lalu setelah itu pengguna akan langsung diminta memasukkan username dan juga password. 

# Login Pengguna
> Pada opsi 2 yakni pengguna akan diminta memasukkan username dan juga password terutama yang telah diregistrasi sebelumnya jika pengguna tersebut belum memiliki akun.

# Menu Penguna 
> Setelah login, pengguna akan ditampilkan menu dari pengguna itu sendiri yakni Tambah Lagu Didalam Playlist, Lihat Lagu Didalam Playlist, Hapus Lagu Didalam Playlist, Sorting Lagu, Searching Lagu, Daftar Premium dan Exit. 

# Tambah Lagu 
> Pada menu tambah lagu ini, pengguna diminta memasukkan Judul Lagu, Nama Artis, dan Tahun Rilis lalu dapat dilihat pada gambar diatas, bila pengguna ingin menambahkan lagu lagi maka ketik "y" dan akan dikembalikan pada menu ini lagi, namun bila tidak maka ketik "t" dan akan dikembalikan pada menu pengguna.

# Lihat Lagu
> Pada menu Lihat Lagu ini, pengguna dapat melihat Judul Lagu, Nama Artis dan Tahun Rilis yang telah ditambahkan sebelumnya

# Hapus Lagu
> Pada menu Hapus Lagu ini, pengguna dapat menghapus judul lagu yang telah di tambahkan sebelumnya, otomatis nama artis dan juga tahun rilis akan ikut terhapus juga.

# Sorting Lagu 
> 1. Berdasarkan Judul 
> Data yang ditampilkan akan terurut berdasarkan Judul Lagu

> 2. Berdasarkan Artis
> Data yang ditampilkan akan terurut berdasarkan Nama Artis

> 3. Berdasarkan Tahun Rilis
> Data yang ditampilkan akan terurut berdasarkan Tahun Rilis


# Searching Lagu
> Pada menu Searching Lagu ini, pengguna dapat mengetikkan judul lagu yang ingin dicari, lalu akan muncul tampilan seperti pada gambar diatas

# Daftar Premium
> Langkah 1 : Pada menu Daftar Premium ini, pengguna akan dihadapkan dengan 2 pilihan yakni yang pertama ada Pembayaran Emoney dan yang kedua ada pilihan Back. Dimana Pembayaran Emoney merupakan metode pembayaran yang digunakan untuk membeli paket premium.

> Langkah 2 : Pada tampilan ini, akan muncul 2 pilihan paket premium, pengguna akan diminta memilih sesuai keinginan masing-masing.

> Langkah 3 : Pada tampilan ini, ketika pengguna mengetikkan angka 1 maka langsung muncul tulisan "Masukkan Nominal Pembayaran" dan pengguna bisa mengetikkan nominal bayar sesuai dengan pilihan paket yang diinginkan dan otomatis pengguna telah beralih dari status Non Premium ke Premium.

# Cetak Bukti Pembayaran
> Pada tampilan ini terlihat bahwa Bukti Pembayaran telah tercetak dan terdiri dari beberapa komponen bisa langsung dilihat pada gambar, yang menandakan bahwa paket premium yang diinginkan telah berhasil dibeli

# Keluar
> Ketika pengguna mengetik angka 7 yakni Keluar maka program otomatis akan beralih ke menu utama sebelumnya tadi

# Exit 
> Ketika pengguna mengetik angka 3 yakni Exit maka program otomatis akan berhenti.
