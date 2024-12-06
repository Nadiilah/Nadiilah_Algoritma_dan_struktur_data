listKota = [
    'Jakarta', 'Surabaya', 'Depok', 'Bekasi', 'Solo',
    'Jogjakarta', 'Semarang', 'Makassar'
]
kotaYangDicari = input('masukkan nama kota yang dicari: ')
i = 0
while i < len(listKota):
    if listKota[i].lower() == kotaYangDicari.lower():
        print('ketemu di index', i)
        break
    print('Bukan', listKota[i])
    i += 1
else: 
    print('maaf, kota yang anda cari tidak ditemukan.')   
    