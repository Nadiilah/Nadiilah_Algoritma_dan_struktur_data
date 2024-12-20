# membuat fungsi
def salam():
    print("hello, selamat pagi")
# panggilan fungsi
salam()
salam()
salam()

# membuat fungsi dengan parameter
def luas_segitiga(alas, tinggi):
    luas = (alas + tinggi) / 2
    print("luas segitiga: %f" % luas)
# pemanggilan fungsi
luas_segitiga(6, 8)

def luas_persegi(sisi):
    luas = sisi * sisi
    return luas
# pemanggilan fungsi
print("luas persegi: %d" % luas_persegi(8))
def luas_persegi(sisi):
    luas - sisi * sisi
    return luas
def volume_persegi(sisi):
    volume - luas_persegi(sisi) * sisi
    print("luas persegi:", luas_persegi(sisi))
    print("volume kubus:", volume_kubus(sisi))