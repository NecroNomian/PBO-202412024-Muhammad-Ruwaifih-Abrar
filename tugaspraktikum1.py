class Mahasiswa:
    # Class attribute
    universitas = "STITEK Bontang"

    # Constructor
    def __init__(self, nama, nim, jurusan, ipk=0.0):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
        self.ipk = ipk

    # Method perkenalan
    def perkenalan_diri(self):
        print(f"Hallo, saya {self.nama} dengan NIM {self.nim}.")
        print(f"Saya berasal dari jurusan {self.jurusan}.")
        print(f"Universitas: {Mahasiswa.universitas}")
        print()

    # Method update IPK
    def update_ipk(self, ipk_baru):
        self.ipk = ipk_baru
        print(f"IPK {self.nama} telah diperbarui menjadi {self.ipk}")
        print()

    # Method predikat kelulusan
    def predikat_kelulusan(self):
        if self.ipk >= 3.5:
            predikat = "Cum Laude"
        elif self.ipk >= 3.0:
            predikat = "Sangat Memuaskan"
        elif self.ipk >= 2.5:
            predikat = "Memuaskan"
        elif self.ipk >= 2.0:
            predikat = "Lulus"
        else:
            predikat = "Tidak Lulus"

        print(f"Predikat Kelulusan {self.nama}: {predikat}")
        print()

mhs1 = Mahasiswa("Abrar", "202412024", "Informatika", 3.6)
mhs2 = Mahasiswa("Aril", "202412005", "Informatika", 2.8)
mhs3 = Mahasiswa("Topik", "202412026", "Informatika", 1.9)

mhs1.perkenalan_diri()
mhs2.perkenalan_diri()
mhs3.perkenalan_diri()

mhs1.predikat_kelulusan()
mhs2.predikat_kelulusan()
mhs3.predikat_kelulusan()

# Update IPK lalu cek predikat lagi
mhs3.update_ipk(2.7)
mhs3.predikat_kelulusan()
