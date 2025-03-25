from datetime import datetime

# Dictionary untuk tarif pajak berdasarkan jenis kendaraan
tarif_pajak = {
    "motor": 500000,
    "mobil": 1500000,
    "truk": 2500000
}

# Fungsi untuk menghitung pajak kendaraan
def hitung_pajak(jenis_kendaraan, tahun_pembelian):
    tahun_sekarang = datetime.now().year
    usia_kendaraan = tahun_sekarang - tahun_pembelian
    print(f"Usia kendaraan: {usia_kendaraan} tahun")  
    
    pajak_utama = tarif_pajak[jenis_kendaraan]
    pajak_tambahan = 0
    
    # Jika kendaraan lebih dari 5 tahun, tambahkan 10% pajak tambahan
    if usia_kendaraan > 5:
        pajak_tambahan = 0.1 * pajak_utama
    
    total_pajak = pajak_utama + pajak_tambahan
    return total_pajak

# Validasi input untuk jenis kendaraan
jenis_kendaraan = input("Masukkan jenis kendaraan (motor/mobil/truk): ").strip().lower()
while jenis_kendaraan not in tarif_pajak:
    print("Jenis kendaraan tidak valid! Silakan masukkan ulang.")
    jenis_kendaraan = input("Masukkan jenis kendaraan (motor/mobil/truk): ").strip().lower()

# Validasi input untuk tahun pembelian
while True:
    try:
        tahun_pembelian = int(input("Masukkan tahun pembelian kendaraan: "))
        if tahun_pembelian > datetime.now().year or tahun_pembelian < 1900:
            print("Tahun pembelian tidak valid! Masukkan tahun yang benar.")
        else:
            break  # Keluar dari loop jika input benar
    except ValueError:
        print("Tahun pembelian harus berupa angka!")

# Hitung pajak kendaraan
pajak = hitung_pajak(jenis_kendaraan, tahun_pembelian)

# Tampilkan hasil jika perhitungan berhasil
if pajak is not None:
    print(f"Pajak yang harus dibayar: Rp {pajak:,}")