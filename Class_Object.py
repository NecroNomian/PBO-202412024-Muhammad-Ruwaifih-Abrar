class Dosen:
    def __init__(self, nama, nidn):
        self.nama = nama
        self.nidn = nidn

    def perkenalan(self):
        return f"Halo, saya {self.nama} dengan NIDN {self.nidn}"

# Pembuatan object
mhs1 = Dosen("Budiman", "12345678")
mhs2 = Dosen("Basur Gilang", "123456789")

print(mhs1.perkenalan())
print(mhs2.perkenalan())