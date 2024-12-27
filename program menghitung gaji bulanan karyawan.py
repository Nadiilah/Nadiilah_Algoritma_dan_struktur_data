def hitung_gaji(tarif_per_jam, jam_kerja_per_hari, hari_kerja):
    total_gaji = 0
    
    for hari in range(1, hari_kerja + 1):
        jam_kerja = int(input(f"Masukkan jam kerja pada hari ke-{hari}: "))
        if jam_kerja <= jam_kerja_per_hari:
            # Tidak ada lembur
            total_gaji += jam_kerja * tarif_per_jam
        else:
            # Ada lembur
            jam_lembur = jam_kerja - jam_kerja_per_hari
            total_gaji += (jam_kerja_per_hari * tarif_per_jam) + (jam_lembur * tarif_per_jam * 1.5)
    
    return total_gaji

def main():
    print("=== Program Perhitungan Gaji Bulanan Karyawan ===")
    
    try:
        tarif_per_jam = float(input("Masukkan tarif gaji per jam: "))
        jam_kerja_per_hari = 8  # Jam kerja normal
        hari_kerja = int(input("Masukkan jumlah hari kerja dalam sebulan: "))
        
        total_gaji = hitung_gaji(tarif_per_jam, jam_kerja_per_hari, hari_kerja)
        print(f"\nTotal gaji bulanan Anda adalah: Rp {total_gaji:,.2f}")
    
    except ValueError:
        print("Harap masukkan input yang valid (angka).")

if __name__ == "__main__":
    main()
