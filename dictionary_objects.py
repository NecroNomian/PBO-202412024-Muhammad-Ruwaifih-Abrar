class Produk:
    def __init__(self, kode, nama, harga):
        self.kode = kode
        self.nama = nama
        self.harga = harga

    def info(self):
        return f"{self.nama} - Rp {self.harga:,}"

katalog_produk = {
    "P001": Produk("P001", "Laptop", 8000000),
    "P002": Produk("P002", "Mouse", 150000),
    "P003": Produk("P003", "Keyboard", 300000)
}

print("=== Katalog Produk ===")
for kode, produk in katalog_produk.items():
    print(f"{kode}: {produk.info()}")

cari_kode = "P002"
if cari_kode in katalog_produk:
    print(f"\nProduk ditemukan: {katalog_produk[cari_kode].info()}")


class Pelanggan:
    def __init__(self, id_pelanggan, nama, email):
        self.id_pelanggan = id_pelanggan
        self.nama = nama
        self.email = email

    def info(self):
        return f"{self.id_pelanggan} - {self.nama} ({self.email})"


data_pelanggan = {
    "PL001": Pelanggan("PL001", "Andi", "andi@gmail.com"),
    "PL002": Pelanggan("PL002", "Budi", "budi@gmail.com"),
    "PL003": Pelanggan("PL003", "Citra", "citra@gmail.com")
}


def tambah_pelanggan(dict_pelanggan, pelanggan):
    dict_pelanggan[pelanggan.id_pelanggan] = pelanggan


def hapus_pelanggan(dict_pelanggan, id_pelanggan):
    if id_pelanggan in dict_pelanggan:
        del dict_pelanggan[id_pelanggan]


def cari_pelanggan(dict_pelanggan, id_pelanggan):
    return dict_pelanggan.get(id_pelanggan, None)


print("\n=== Daftar Pelanggan ===")
for pelanggan in data_pelanggan.values():
    print(pelanggan.info())


p_baru = Pelanggan("PL004", "Dina", "dina@gmail.com")
tambah_pelanggan(data_pelanggan, p_baru)

hasil = cari_pelanggan(data_pelanggan, "PL002")
if hasil:
    print("\nPelanggan ditemukan:")
    print(hasil.info())

hapus_pelanggan(data_pelanggan, "PL001")

print("\n=== Daftar Pelanggan Setelah Perubahan ===")
for pelanggan in data_pelanggan.values():
    print(pelanggan.info())
