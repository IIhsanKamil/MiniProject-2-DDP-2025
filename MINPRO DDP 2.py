print("-"*45)
print("Nama    : Muhammad Ihsan Kamil")
print("NIM     : 2509116035")
print("Kelas   : Sistem Informasi A 2025")
print("Program : Mini Project 2 (Praktikum DDP)")
print("Tema    : Sistem Menejemen Order Jahitan")
print("-"*45)

users = {
    1: {"password": "abc123", "jabatan": "Manager"},
    2: {"password": "xyz123", "jabatan": "Karyawan"}
}

list_order = []

#Function menampilkan order
def tampilkan_order():
    if not list_order:
        print("Belum ada order")
    else:
        nomor = 1
        for order in list_order:
            print(str(nomor) + ". " + order)
            nomor += 1
    print()

#Function tambah order
def tambah_order():
    nama  = input("Nama pelanggan     : ")
    jenis = input("Jenis pakaian      : ")
    warna = input("Warna pakaian      : ")
    ambil = input("Tanggal pengambilan: ")
    print()

    order = nama + " - " + jenis + " - " + warna + " - " + ambil
    list_order.append(order)

    print("Order berhasil ditambahkan, berikut list terbaru:")
    print()
    tampilkan_order()

#Function update order
def update_order():
    try:
        if not list_order:
            print("Belum ada order")
            return
        
        print("Berikut List Order:")
        tampilkan_order()

        nomor_order = int(input("Masukkan nomor order yang ingin diupdate: "))
        if 1 <= nomor_order <= len(list_order):
            print("Masukkan data baru")
            print()
            nama  = input("Nama baru: ")
            jenis = input("Jenis baru: ")
            warna = input("Warna baru: ")
            ambil = input("Tanggal ambil baru: ")
            print()

            order = nama + " - " + jenis + " - " + warna + " - " + ambil
            list_order[nomor_order-1] = order
            print("Order berhasil diupdate! Berikut list terbaru:")
            tampilkan_order()
            print()
        else:
            print("Nomor order tidak ditemukan.")
    except ValueError:
        print("Input tidak valid, input harus merupakan angka intejer")
        print()
    except KeyboardInterrupt:
        print("Input tidak boleh menekan CTRL + C")
        print()

#Function menu karyawan
def tampilkan_menu_karyawan():
    while True:
        print("=== Menu Karyawan ===")
        print("1. Tambah order")
        print("2. Lihat Semua Order")
        print("3. Keluar")

        try:
            pilih = int(input("Pilih menu antara 1 - 3: "))
            print()
            if pilih == 1:
                tambah_order()
            elif pilih == 2:
                tampilkan_order()
            elif pilih == 3:
                return
            else:
                print("Pilihan tidak valid")

        except ValueError:
            print("Input tidak valid, input harus merupakan angka intejer")
            print()
        except KeyboardInterrupt:
            print("Input tidak boleh menekan CTRL + C")
            print()

#Function hapus order
def hapus_order():
    print("Daftar Order:")
    tampilkan_order()
    print()
    try:
        hapus = int(input("Masukkan nomor order yang ingin dihapus: "))
        if 1 <= hapus <= len(list_order):
            del list_order[hapus-1]
            print("Order telah dihapus, berikut list terbaru:")
            tampilkan_order()
        else:
            print("Input tidak valid, nomor order tidak tersedia")
    except ValueError:
        print("Input tidak valid, input harus merupakan angka intejer")
        print()
    except KeyboardInterrupt:
        print("Input tidak boleh menekan CTRL + C")
        print()

#Function menu manager
def tampilkan_menu_manager():
    while True:
        print("=== Menu Manager ===")
        print("1. Tambah order")
        print("2. Lihat Semua Order")
        print("3. Update Order")
        print("4. Hapus Order")
        print("5. Kembali")
        print()

        try:
            pilih = int(input("Pilih menu antara 1 - 5: "))
            print()
            if pilih == 1:
                tambah_order()
            elif pilih == 2:
                tampilkan_order()
            elif pilih == 3:
                update_order()
            elif pilih == 4:
                hapus_order()
            elif pilih == 5:
                return
            else:
                print("Pilihan tidak valid")
        except ValueError:
            print("Input tidak valid, input harus merupakan angka intejer")
            print()
        except KeyboardInterrupt:
            print("Input tidak boleh menekan CTRL + C")
            print()


#Fungsi login
def login():
    print("Selamat datang di Sistem Manajemen Order Jahitan")
    print("-"*50)
    print()
    try:
        input_pilih = int(input("(1 = Manager, 2 = Karyawan, 3 = Keluar dari program): "))

        if input_pilih == 3:
            print("Keluar dari program")
            return True

        input_password = input("Password: ")
        print()

        if input_pilih in users and users[input_pilih]["password"] == input_password:
            print("Login berhasil!")
            if users[input_pilih]["jabatan"] == "Manager":
                tampilkan_menu_manager()
            else:
                tampilkan_menu_karyawan()
        else:
            print("Jabatan atau password salah! Coba lagi")
        return False
    except ValueError:
        print("Input tidak valid, input harus merupakan angka intejer")
        return False
    except KeyboardInterrupt:
        print("Input tidak boleh menekan CTRL + C")
        return False


#Program utama
while True:
    if login(): 
        break