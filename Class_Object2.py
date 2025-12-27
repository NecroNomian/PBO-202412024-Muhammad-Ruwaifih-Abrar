class Dosen:
    def __init__(self, nama, nidn):
        self.nama = nama
        self.nidn = nidn

    def perkenalan(self):
        return f"Halo, saya {self.nama} dengan NIDN {self.nidn}"

    def ajar_mata_kuliah(self, mata_kuliah):
        return f"{self.nama} mengajar mata kuliah {mata_kuliah}"


# Pembuatan object
mhs1 = Dosen("Budiman", "12345678")
mhs2 = Dosen("Basur Gilang", "123456789")

print(mhs1.perkenalan())
print(mhs2.perkenalan())

print(mhs1.ajar_mata_kuliah("Pemrograman Python"))
print(mhs2.ajar_mata_kuliah("Basis Data"))
