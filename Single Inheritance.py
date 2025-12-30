class Person:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def info(self):
        return f"Nama: {self.nama}, Umur: {self.umur} tahun"


class Mahasiswa(Person):
    def __init__(self, nama, umur, nim):
        super().__init__(nama, umur)
        self.nim = nim

    def info(self):
        return f"Nama: {self.nama}, Umur: {self.umur} tahun, NIM: {self.nim}"


p = Person("Andi", 20)
mhs = Mahasiswa("Budi", 21, "231011001")

print(p.info())
print(mhs.info())
