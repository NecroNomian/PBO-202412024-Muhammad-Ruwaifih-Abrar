class Kendaraan:
    # Class attribute
    bahan_bakar = "Bensin"

    # Constructor
    def __init__(self, merk, warna, tahun):
        self.merk = merk
        self.warna = warna
        self.tahun = tahun

    # Method info
    def info_kendaraan(self):
        return f"{self.merk} warna {self.warna} tahun {self.tahun}"


# Instansiasi object
k1 = Kendaraan("Toyota Avanza", "Hitam", 2021)
k2 = Kendaraan("Honda Jazz", "Merah", 2019)

print(k1.info_kendaraan())
print(k2.info_kendaraan())
print(f"Bahan bakar: {Kendaraan.bahan_bakar}")
