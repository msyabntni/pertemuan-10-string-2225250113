
# Latihan 7: Normalisasi Data

def normalisasi_nama(nama):
    return nama.strip().title()


def buat_inisial(nama):
    kata = nama.strip().split()
    inisial = ""

    for bagian in kata:
        inisial += bagian[0].upper()

    return inisial


def normalisasi_kode(kode):
    return kode.strip().upper()


# Input data
nama = input("Nama: ")
kode = input("Kode kelas: ")

# Proses normalisasi
nama_normal = normalisasi_nama(nama)
inisial = buat_inisial(nama)
kode_normal = normalisasi_kode(kode)

# Tampilkan hasil
print("\n=== Hasil Normalisasi ===")
print("Nama normalisasi:", nama_normal)
print("Inisial nama:", inisial)
print("Kode kelas normalisasi:", kode_normal)