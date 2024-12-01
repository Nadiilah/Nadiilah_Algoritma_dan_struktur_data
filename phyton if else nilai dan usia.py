nilai = int(input('masukkan nilai anda :'))
usia = int(input('masukkan usia anda :'))
if nilai >= 75:
    if (usia < 15):
        print('selamat adek, kamu lulus!')
    else :
        print('selamat kakak, kamu lulus!')
else :
    if(usia < 15):
        print('mohon maaf dek, kamu tidak lulus!')
    else :
        print('mohon maaf kakak, kamu tidak lulus!')