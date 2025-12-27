#== == == == == == == == == == == == =
#Class Buku
#== == == == == == == == == == == == =
class Buku:
    def __init__(self, kode_buku, judul, penulis, stok, lokasi_rak):
        self.kode_buku = kode_buku        # public
        self.judul = judul                # public
        self.penulis = penulis            # public
        self._stok = stok                 # protected
        self.__lokasi_rak = lokasi_rak    # private

    def get_lokasi_rak(self):
        return self.__lokasi_rak

    def set_lokasi_rak(self, lokasi):
        self.__lokasi_rak = lokasi

    def tambah_stok(self, jumlah):
        self._stok += jumlah

    def kurangi_stok(self, jumlah):
        if self._stok >= jumlah:
            self._stok -= jumlah

#== == == == == == == == == == == == =
#Class Peminjaman
#== == == == == == == == == == == == =
class Peminjaman:
    def __init__(self, kode_buku, tanggal_pinjam, tanggal_kembali=None):
        self.kode_buku = kode_buku
        self.tanggal_pinjam = tanggal_pinjam
        self.tanggal_kembali = tanggal_kembali
        self.status = "Dipinjam"

    def info_peminjaman(self):
        return f"{self.kode_buku} | {self.tanggal_pinjam} | {self.tanggal_kembali} | {self.status}"

#== == == == == == == == == == == == =
#Class Anggota
#== == == == == == == == == == == == =
class Anggota:
    def __init__(self, id_anggota, nama, maks_pinjam=3):
        self.id_anggota = id_anggota      # public
        self.nama = nama                  # public
        self._maks_pinjam = maks_pinjam   # protected
        self.__status_aktif = True        # private
        self.daftar_peminjaman = []       # aggregation

    def get_status(self):
        return self.__status_aktif

    def set_status(self, status):
        self.__status_aktif = status

    def pinjam_buku(self, buku, tanggal):
        if self.__status_aktif and len(self.daftar_peminjaman) < self._maks_pinjam and buku._stok > 0:
            peminjaman = Peminjaman(buku.kode_buku, tanggal)
            self.daftar_peminjaman.append(peminjaman)
            buku.kurangi_stok(1)

    def kembalikan_buku(self, buku, tanggal_kembali):
        for p in self.daftar_peminjaman:
            if p.kode_buku == buku.kode_buku and p.status == "Dipinjam":
                p.status = "Dikembalikan"
                p.tanggal_kembali = tanggal_kembali
                buku.tambah_stok(1)

#== == == == == == == == == == == == =
#Class Perpustakaan
#== == == == == == == == == == == == =
class Perpustakaan:
    def __init__(self, nama):
        self.nama = nama
        self.daftar_buku = []  # composition

    def tambah_buku(self, buku):
        self.daftar_buku.append(buku)

#== == == == == == == == == == == == =
#Instansiasi &Demonstrasi
#== == == == == == == == == == == == =
if __name__ == "__main__":
    perpustakaan = Perpustakaan("Perpustakaan Kampus")

    buku1 = Buku("B001", "Pemrograman Python", "Guido", 5, "Rak A1")
    buku2 = Buku("B002", "Basis Data", "Codd", 3, "Rak B2")
    buku3 = Buku("B003", "OOP Python", "Rossum", 4, "Rak C3")

    perpustakaan.tambah_buku(buku1)
    perpustakaan.tambah_buku(buku2)
    perpustakaan.tambah_buku(buku3)

    anggota1 = Anggota("A001", "Budi")
    anggota2 = Anggota("A002", "Siti")

    anggota1.pinjam_buku(buku1, "2025-01-01")
    anggota1.pinjam_buku(buku2, "2025-01-01")

    anggota2.pinjam_buku(buku3, "2025-01-02")

    anggota1.kembalikan_buku(buku1, "2025-01-05")

    print("=== Informasi Buku ===")
    for b in perpustakaan.daftar_buku:
        print(b.kode_buku, b.judul, b.penulis, "Stok:", b._stok)

    print("\n=== Informasi Anggota ===")
    print(anggota1.id_anggota, anggota1.nama, "Status:", anggota1.get_status())
    print(anggota2.id_anggota, anggota2.nama, "Status:", anggota2.get_status())

    print("\n=== Daftar Peminjaman ===")
    for p in anggota1.daftar_peminjaman:
        print("Budi:", p.info_peminjaman())

    for p in anggota2.daftar_peminjaman:
        print("Siti:", p.info_peminjaman())
