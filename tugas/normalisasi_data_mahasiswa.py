
def normalisasi_nama(nama):
    return " ".join(nama.strip().split()).title()


def buat_inisial(nama):
    kata = normalisasi_nama(nama).split()
    return "".join(k[0] for k in kata)


def normalisasi_kode(kode):
    return "-".join(kode.strip().upper().split())


def hitung_kata(nama):
    return len(normalisasi_nama(nama).split())


nama = input("Nama: ")
kode = input("Kode kelas: ")

nama_bersih = normalisasi_nama(nama)
kode_bersih = normalisasi_kode(kode)

print("Nama bersih :", nama_bersih)
print("Kode kelas  :", kode_bersih)
print("Jumlah kata :", hitung_kata(nama))
print("Inisial     :", buat_inisial(nama))
