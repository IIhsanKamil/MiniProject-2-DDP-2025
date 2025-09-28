# Mini Project 2 DDP 2025

# Profil
Nama  : Muhammad Ihsan Kamil\
NIM   : 2509116035\
Kelas : Sistem Informasi A 2025\
Tugas Praktikum, Mini Project 2 DDP

# Deskripsi
Sistem Menejemen Order Jahitan dibuat untuk membantu pengguna dalam menyimpan orderan jahitan.\
Sistem ini menyediakan 2 layanan untuk manager dan karyawan, yang dimana masing masing jabatan memiliki hak sistem berbeda.\
Dalam program ini terdapat beberapa menu untuk manager seperti:
- Tambah Order
- Lihat Semua Order
- Update Order
- Hapus Order
- Kembali

Dan menu untuk karyawan yaitu:
- Tambah Order
- Lihat Semua Order
- Kembali

# PENJELASAN PROGRAM
<img width="531" height="148" alt="image" src="https://github.com/user-attachments/assets/63b2c1f8-ceb9-4d7d-8b3f-16cb317b358e" />\
Pada kode tersebut, terdapat dua bagian penting yaitu users dan list_order. Variabel users merupakan sebuah dictionary yang berfungsi untuk menyimpan data login. Di dalamnya terdapat dua akun, yaitu akun dengan key 1 yang memiliki password "abc123" dan jabatan "Manager", serta akun dengan key 2 yang memiliki password "xyz123" dan jabatan "Karyawan". Struktur ini berfungsi untuk membedakan peran pengguna saat login sehingga manager dan karyawan bisa mengakses menu yang berbeda. Variabel list_order adalah list kosong yang disiapkan sebagai wadah untuk menyimpan data order pelanggan. Pada awal program, list ini memang masih kosong, namun nantinya setiap kali pengguna menambahkan order baru, data tersebut akan dimasukkan ke dalam list ini dalam bentuk string yang berisi nama pelanggan, jenis pakaian, warna, serta tanggal pengambilan. Dengan demikian, users berfungsi sebagai data login, sedangkan list_order sebagai tempat menyimpan daftar order jahitan.

# Function Menampilkan Order
<img width="443" height="251" alt="image" src="https://github.com/user-attachments/assets/af359943-94e4-4e4f-8ef4-a54aa155c32f" />\
Fungsi tampilkan_order() di atas digunakan untuk menampilkan daftar order yang sudah tersimpan di dalam list_order. Pertama, program akan mengecek apakah list_order kosong menggunakan if not list_order. Jika kosong, maka akan ditampilkan tulisan "Belum ada order". Namun, kalau ada data di dalamnya, program akan melakukan perulangan for untuk menampilkan setiap order satu per satu dengan menambahkan nomor urut di depannya. Variabel nomor digunakan sebagai penghitung yang dimulai dari angka 1, lalu akan bertambah satu setiap kali perulangan berjalan. Di akhir fungsi terdapat print() kosong agar hasil tampilan lebih rapi, memberikan jarak antar output.

# Function Tambah Order
<img width="636" height="321" alt="image" src="https://github.com/user-attachments/assets/e48ebe02-208d-41ea-8a2e-b5fd19d33742" />\
Fungsi tambah_order() dipakai untuk menambahkan data order baru ke dalam list_order. Pertama, program meminta input dari pengguna berupa nama pelanggan, jenis pakaian, warna pakaian, dan tanggal pengambilan. Setelah semua data diisi, input tersebut digabungkan menjadi satu string dengan format "nama - jenis - warna - tanggal". String ini kemudian dimasukkan ke dalam list list_order menggunakan append(). Setelah data tersimpan, program menampilkan pesan bahwa order berhasil ditambahkan, lalu langsung memanggil fungsi tampilkan_order() agar pengguna bisa melihat daftar order terbaru yang sudah termasuk dengan order yang baru saja dibuat.

# Function Update Order
<img width="636" height="321" alt="Screenshot 2025-09-28 080535" src="https://github.com/user-attachments/assets/64f3c272-5d7d-440b-bcce-eec01e2caaf8" />\
Fungsi update_order() digunakan untuk mengubah atau memperbarui data order yang sudah ada di dalam list_order. Pertama, program memeriksa apakah daftar order kosong. Jika kosong, langsung ditampilkan pesan “Belum ada order” dan fungsi dihentikan dengan return. Kalau ada isinya, maka daftar order ditampilkan ke layar dengan memanggil tampilkan_order(). Setelah itu, pengguna diminta memasukkan nomor order yang ingin diupdate. Nomor yang dimasukkan harus sesuai dengan posisi data di list_order.

Jika nomor valid, program kemudian meminta input baru berupa nama, jenis, warna, dan tanggal ambil. Input baru tersebut digabungkan kembali menjadi string "nama - jenis - warna - tanggal" dan digunakan untuk menggantikan data lama di indeks yang sesuai dalam list_order. Setelah berhasil, ditampilkan pesan konfirmasi bahwa data sudah diperbarui, lalu daftar order terbaru ditampilkan.

Selain itu, fungsi ini juga dilengkapi error handling. Jika input nomor order bukan angka, akan muncul pesan error “Input tidak valid, input harus merupakan angka intejer”. Jika pengguna menekan CTRL + C, program menangkap error KeyboardInterrupt dan menampilkan pesan bahwa input tersebut tidak diperbolehkan.

# Function Menu Karyawan
<img width="733" height="606" alt="image" src="https://github.com/user-attachments/assets/d8cf1b3b-5df4-41c1-881a-afe7b62f9627" />\
Fungsi tampilkan_menu_karyawan() digunakan untuk menampilkan menu khusus bagi pengguna dengan role karyawan. Fungsi ini berjalan dalam perulangan while True sehingga menu akan terus muncul kembali setelah pengguna selesai melakukan suatu aksi, kecuali jika memilih keluar.
Di dalam menu terdapat tiga pilihan utama, yaitu:
- Tambah order → ketika dipilih, program akan memanggil fungsi tambah_order() untuk menambahkan data order baru.
- Lihat semua order → ketika dipilih, program akan memanggil fungsi tampilkan_order() untuk menampilkan seluruh order yang sudah ada di list_order.
- Keluar → jika dipilih, fungsi akan berhenti dengan return, sehingga keluar dari menu karyawan dan kembali ke menu sebelumnya (misalnya login).

Selain itu, fungsi juga sudah dilengkapi error handling. Jika input yang dimasukkan bukan angka, program akan menampilkan pesan bahwa input harus berupa angka integer. Kalau pengguna menekan CTRL + C, maka akan ditampilkan pesan bahwa input tersebut tidak diperbolehkan.

# Function Hapus Order
<img width="712" height="444" alt="image" src="https://github.com/user-attachments/assets/7b344bbe-ae0e-4327-b38f-984e7418b848" />\
Fungsi hapus_order() digunakan untuk menghapus order yang sudah tersimpan di dalam list_order. Pertama, program akan menampilkan daftar order yang ada dengan memanggil fungsi tampilkan_order(). Setelah itu, pengguna diminta untuk memasukkan nomor order yang ingin dihapus.

Jika nomor yang dimasukkan valid (berada dalam rentang jumlah order yang ada), maka program akan menghapus order tersebut dari list dengan perintah del list_order[hapus-1], karena indeks list python dimulai dari 0. Setelah penghapusan berhasil, program menampilkan kembali daftar order terbaru sebagai konfirmasi.

Namun, jika pengguna memasukkan nomor order yang tidak tersedia, maka akan muncul pesan bahwa input tidak valid. Fungsi ini juga sudah dilengkapi penanganan error. Jika input bukan angka (ValueError), program akan menampilkan pesan kesalahan. Sedangkan jika pengguna menekan kombinasi CTRL + C (KeyboardInterrupt), maka program akan menolak input tersebut dan menampilkan pesan peringatan.

# Function Menu
<img width="747" height="756" alt="image" src="https://github.com/user-attachments/assets/7445414c-72f5-4bcc-8d51-78daad0f924b" />\
Fungsi tampilkan_menu_manager() adalah menu utama yang bisa diakses jika pengguna login sebagai Manager. Di dalam fungsi ini, digunakan perulangan while True supaya menu terus ditampilkan berulang sampai pengguna memilih opsi keluar dengan menekan angka 5.

- Tambah order → memanggil fungsi tambah_order() untuk menambahkan data pesanan baru.
- Lihat Semua Order → memanggil fungsi tampilkan_order() untuk menampilkan seluruh daftar pesanan yang ada.
- Update Order → memanggil fungsi update_order() untuk mengubah data pesanan tertentu.
- Hapus Order → memanggil fungsi hapus_order() untuk menghapus pesanan tertentu.
- Kembali → keluar dari menu Manager dengan perintah return, yang akan menghentikan perulangan dan mengembalikan kontrol ke fungsi login().

Selain itu, fungsi ini juga menggunakan exception handling supaya program tidak error ketika pengguna salah input. Jika pengguna memasukkan selain angka (ValueError), program akan menampilkan pesan bahwa input harus berupa angka integer. Jika pengguna menekan CTRL + C (KeyboardInterrupt), program akan menolak dan menampilkan peringatan.

# Fungsi Login
<img width="901" height="699" alt="image" src="https://github.com/user-attachments/assets/711c9431-c3a8-4c99-ad3d-848b980a49ab" />\
Fungsi login() dipakai untuk mengatur akses masuk ke program. Pengguna diminta memilih jabatan (1 = Manager, 2 = Karyawan, 3 = Keluar) lalu memasukkan password. Jika pilihan 3, program berhenti. Jika jabatan dan password benar, login berhasil dan pengguna diarahkan ke menu sesuai jabatannya. Kalau salah, akan muncul pesan error. Fungsi ini juga sudah dilengkapi penanganan error jika input bukan angka atau pengguna menekan CTRL + C.

# Program Utama
<img width="254" height="82" alt="image" src="https://github.com/user-attachments/assets/66842eb2-9156-4f7d-94ea-2e999aeade7b" />
berfungsi untuk menjalankan program utama secara terus-menerus. Selama login() mengembalikan False, perulangan akan tetap berjalan sehingga user bisa login kembali atau masuk ke menu. Jika login() mengembalikan True (misalnya saat user pilih keluar), maka perulangan berhenti dengan break dan program selesai.

# OUTPUT JIKA KONDISI BENAR
**1. Login sebagai manager**\
<img width="520" height="502" alt="image" src="https://github.com/user-attachments/assets/a21bdd16-f513-4a09-9d83-21c7d43d13db" />

**2. Login sebagai karyawan**\
<img width="519" height="299" alt="image" src="https://github.com/user-attachments/assets/f4a02a74-bd94-4ab1-8fa0-34b35ce673a8" />

**3. Fungsi tambah order**\
<img width="467" height="434" alt="image" src="https://github.com/user-attachments/assets/4b701d02-ff08-4c84-bd4b-e1b6b10ec53f" />

**4. Fungsi lihat order**\
<img width="366" height="272" alt="image" src="https://github.com/user-attachments/assets/9f6be247-2ca1-4171-ab15-f860d5c8c584" />

**5. Fungsi update order**\
<img width="448" height="342" alt="image" src="https://github.com/user-attachments/assets/f75fac72-349b-4d61-be16-27c8a31b2366" />

**6. Fungsi hapus order**\
<img width="360" height="103" alt="image" src="https://github.com/user-attachments/assets/c9b90d83-909b-4167-9024-8000ac7b3a90" />

**7. Fungsi kembali dan keluar dari program**\
<img width="515" height="193" alt="image" src="https://github.com/user-attachments/assets/162b49ea-8266-47a5-8854-f7516784d603" />

# OUTPUT JIKA KONDISI INPUT SALAH/ERROR
**1. Error input pilihan**\
Macam-macam error input pilihan:

a. Error input 0 / kurang dari 0 / float / huruf\
<img width="540" height="489" alt="image" src="https://github.com/user-attachments/assets/8b2498f7-4d2f-4b54-a7f6-05fb68a3f457" />

b. Error input menekan CTRL + C\
<img width="814" height="80" alt="image" src="https://github.com/user-attachments/assets/151cb693-919e-4025-8d70-8ba9d0030996" />

c. Error input dikosongkan\
<img width="515" height="50" alt="image" src="https://github.com/user-attachments/assets/5311473c-5ac3-43d6-bd6f-b545abfdb30c" />

**2. Login sebagai manager**\
Input password:

a. Error input 0 / kurang dari 0 / float / huruf / dikosongkan\
<img width="524" height="752" alt="image" src="https://github.com/user-attachments/assets/cfd63b0e-d2d3-4f8a-8f0e-bb1fed33c82d" />

b. Error input menekan CTRL + C\
<img width="511" height="95" alt="image" src="https://github.com/user-attachments/assets/523156ff-ebce-4d5e-9fec-aa5dd5271edb" />

**3. Login sebagai karyawan**\
Input password:

a. Error input 0 / kurang dari 0 / float / huruf / dikosongkan\
<img width="522" height="757" alt="image" src="https://github.com/user-attachments/assets/e6e3754f-2cfa-4920-a4de-6aff3dd5c9be" />

b. Error input menekan CTRL + C\
<img width="518" height="52" alt="image" src="https://github.com/user-attachments/assets/1ba9f830-7974-441b-a520-c1f1133bdcfe" />

**4. Error input pilih menu**\
Input pilih menu:

a. Error input 0 / kurang dari 0\
<img width="519" height="601" alt="image" src="https://github.com/user-attachments/assets/1ffa3faa-8f35-43c1-99df-49c325ee1427" />

b. Error input float / huruf / dikosongkan\
<img width="554" height="185" alt="image" src="https://github.com/user-attachments/assets/b2d45cbc-c11e-49db-bb96-9ed5da332283" />

**5. Error input function menu update**\
Input nomor order yang ingin dihapus:

a. Error input 0 / kurang dari 0 / float\
<img width="440" height="116" alt="image" src="https://github.com/user-attachments/assets/6e5c1ce1-33af-4bae-b475-b0a384ddf15c" />\
<img width="436" height="110" alt="image" src="https://github.com/user-attachments/assets/2f86414e-34a0-4feb-94d7-ead446868078" />

b. Error input float / huruf / dikosongkan\
<img width="516" height="831" alt="image" src="https://github.com/user-attachments/assets/b45edc7b-852b-452e-a5b9-483a7021b11c" />

c. Error input menekan CTRL + C\
<img width="714" height="33" alt="image" src="https://github.com/user-attachments/assets/a8dc8db7-32dc-4b2a-849b-33c5a8f8881d" />

**6. Error input function menu hapus**\
Input nomor order yang ingin dihapus:

a. Error input 0 / kurang dari 0\
<img width="460" height="486" alt="image" src="https://github.com/user-attachments/assets/ed002c43-7a67-4a73-b002-26c60b220bf3" />

b. Error input huruf / float / dikosongkang\
<img width="555" height="852" alt="image" src="https://github.com/user-attachments/assets/f96e7e26-dbc4-4ce0-8e46-79a5c89b7c49" />

# MEMBUAT FLOWCHART
![FLOWCHART MINPRO 2 (1)](https://github.com/user-attachments/assets/49a487d6-76da-4c84-9e9f-ea589bceffce)

Dalam flowchart ini dimulai dari "Mulai", kemmudian program dilanjutkan dengan input pilihan antara manager, karyawan, atau keluar dari program. Jika Input yang diberikan valid seperti manager dan karyawan, maka program akan menampilkan menu sesuai dengan jabatannya masing-masing. Pertama kali program dijalankan, user akan diminta memilih jabatan, apakah masuk sebagai Manager, Karyawan, atau keluar dari program. Kalau user pilih keluar, maka program langsung berhenti. Tapi kalau user memilih Manager atau Karyawan, maka akan muncul input password. Kalau password yang dimasukkan salah, program akan kasih pesan error dan kembali lagi ke login untuk mencoba ulang.

Kalau password benar, program akan menampilkan menu sesuai dengan jabatan yang dipilih. Kalau login sebagai Manager, maka menu yang muncul ada lima pilihan, yaitu tambah order, lihat semua order, update order, hapus order, atau kembali ke login. Setiap menu punya fungsi masing-masing, dan setelah dijalankan akan kembali ke menu Manager sampai user memilih opsi kembali.

Sedangkan kalau login sebagai Karyawan, pilihan menunya hanya ada tiga, yaitu tambah order, lihat semua order, atau kembali ke login. Sama seperti menu Manager, setiap pilihan akan diproses sesuai fungsi yang ada, lalu balik lagi ke menu Karyawan sampai user pilih kembali. Program ini akan benar-benar berhenti hanya ketika di awal login user memilih keluar. Jadi flowchart-nya menunjukkan alur mulai dari login, cek password, masuk ke menu sesuai jabatan, sampai akhirnya bisa kembali ke login lagi atau mengakhiri program.



