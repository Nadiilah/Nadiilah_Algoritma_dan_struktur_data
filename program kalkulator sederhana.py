def tambah(a, b):
    return a + b

def kurang(a, b):
    return a - b

def kali(a, b):
    return a * b

def bagi(a, b):
    if b == 0:
        return "Kesalahan: Pembagian dengan nol tidak diperbolehkan."
    return a / b

def main():
    print("Kalkulator Sederhana")
    print("Pilih operasi:")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")

    pilihan = input("Masukkan pilihan (1/2/3/4): ")

    if pilihan not in ['1', '2', '3', '4']:
        print("Pilihan tidak valid.")
        return

    try:
        angka1 = float(input("Masukkan angka pertama: "))
        angka2 = float(input("Masukkan angka kedua: "))
    except ValueError:
        print("Masukkan angka yang valid.")
        return

    if pilihan == '1':
        print(f"Hasil: {angka1} + {angka2} = {tambah(angka1, angka2)}")
    elif pilihan == '2':
        print(f"Hasil: {angka1} - {angka2} = {kurang(angka1, angka2)}")
    elif pilihan == '3':
        print(f"Hasil: {angka1} * {angka2} = {kali(angka1, angka2)}")
    elif pilihan == '4':
        hasil = bagi(angka1, angka2)
        print(f"Hasil: {angka1} / {angka2} = {hasil}")

if __name__ == "__main__":
    main()
