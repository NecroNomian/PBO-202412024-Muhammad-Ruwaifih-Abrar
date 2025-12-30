class Mahasiswa:
    def __init__(self, nama, nim, ipk):
        self.nama = nama
        self.nim = nim
        self.ipk = ipk

    def info(self):
        return f"{self.nama} (NIM: {self.nim}) - IPK: {self.ipk}"

daftar_mahasiswa = [
    Mahasiswa("Ahmad", "TI001", 3.5),
    Mahasiswa("Budi", "TI002", 3.2),
    Mahasiswa("Citra", "TI003", 3.8)
]

print("=== Daftar Mahasiswa ===")
for mhs in daftar_mahasiswa:
    print(mhs.info())

print("\n=== Mahasiswa dengan IPK > 3.5 ===")
for mhs in daftar_mahasiswa:
    if mhs.ipk > 3.5:
        print(mhs.info())

class Buku:
    def __init__(self, judul, penulis, tahun):
        self.judul = judul
        self.penulis = penulis
        self.tahun = tahun

    def info(self):
        return f"{self.judul} | Penulis: {self.penulis} | Tahun: {self.tahun}"


daftar_buku = [
    Buku("Laskar Pelangi", "Andrea Hirata", 2005),
    Buku("Bumi Manusia", "Pramoedya Ananta Toer", 1980),
    Buku("Negeri 5 Menara", "Ahmad Fuadi", 2009),
    Buku("Hujan", "Tere Liye", 2016),
    Buku("Perahu Kertas", "Dewi Lestari", 2008)
]

print("\n=== Daftar Buku ===")
for buku in daftar_buku:
    print(buku.info())

print("\n=== Buku karya Tere Liye ===")
for buku in daftar_buku:
    if buku.penulis == "Tere Liye":
        print(buku.info())

print("\n=== Program selesai dijalankan ===")
