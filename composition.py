class Mesin:
    def __init__(self, jenis):
        self.jenis = jenis

    def hidupkan(self):
        return f"Mesin {self.jenis} hidup"


class Mobil:
    def __init__(self, merk, mesin):
        self.merk = merk
        self.mesin = mesin

    def info(self):
        return f"Mobil {self.merk} dengan {self.mesin.hidupkan()}"


class Penulis:
    def __init__(self, nama):
        self.nama = nama


class Buku:
    def __init__(self, judul, penulis):
        self.judul = judul
        self.penulis = penulis


mesin = Mesin("Bensin")
mobil = Mobil("Honda", mesin)

penulis = Penulis("Andrea Hirata")
buku = Buku("Laskar Pelangi", penulis)

print(mobil.info())
print("Judul Buku:", buku.judul)
print("Penulis:", buku.penulis.nama)
