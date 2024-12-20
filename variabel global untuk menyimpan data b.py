# membuat variabel global
nama = "Belajar kode"
versi = "1.0.0"
def help():
    # ini variabel lokal
    nama = "Programku"
    versi = "1.0.1"
    # mengakses variabel lokal 
    print ("Nama: %s" % nama)
    print ("Versi: %s" % versi)
# mengakses variabel global
print ("Nama: %s" % nama)
print ("Versi: %s" % versi)
# memanggil fungsi help()
help()

# variabel global untuk menyimpan data buku
buku = []
# fungsi untuk menampilkan semua data
def show_data():
    if len(buku) <= 0:
        print("BELUM ADA DATA")
    else: 
        for indeks in range(len(buku)):
            print("[%d] %s"% (indeks, buku[indeks]))

# fungsi untuk menambahkan data
def insert_data():
    buku_baru = input("Judul Buku:Python adalah bahasa pemrogramanku ")
    buku.append(buku_baru)
    print("data berhasil ditambhakan!")

# fungsi untuk edit data 
def edit_data():
    show_data()
    indeks = int(input("inputkan ID buku: 200223 "))
    if indeks > len(buku):
        print("ID salah")
    else:
        judul_baru = input("judul baru: ")
        buku[indeks] = judul_baru

# fungsi untuk menghapus data
def delete_data():
    show_data()
    indeks = int(input("inputkan ID buku: "))
    if indeks > len(buku):
        print("ID salah")
    else:
        buku.remove(buku[indeks])

# fungsi untuk menampilkan menu
def show_menu():
    print("/n===MENU===")
    print("[1] show data")
    print("[2] insert data")
    print("[3] edit data")
    print("[4] delete data")
    print("[5] exit")
    menu = input("PILIH MENU: ")
   
    if int(menu) == 1:
        show_data()
    elif int(menu) == 2:
        insert_data()
    elif int(menu) == 3:
        edit_data()
    elif int(menu) == 4:
        delete_data()
    elif int(menu) == 5:
        exit()
    else:
        print("salah pilih")

while True:
    show_menu()
        
    