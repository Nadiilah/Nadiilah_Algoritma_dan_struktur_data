listkota = [
    'Jakarta', 'Surabaya', 'Depok', 'Bekasi', 'Solo',
    'Jogjakarta', 'Semarang', 'Makassar'
]
kotaYangDicari = input('Ketik nama kota yang kamu cari: ')

for i, kota in enumerate(listkota):
    # kita ubah katanya ke lowercase agar
    # menjadi case insensitive
    if kota.lower() == kotaYangDicari.lower():
        print('Kota yang anda cari berada pada indeks', i)
        break
    else:
        print('Maaf, kota yang anda cari tidak ada')