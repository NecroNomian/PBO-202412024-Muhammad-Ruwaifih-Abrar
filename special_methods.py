class Mahasiswa:
    def __init__(self, nama, nilai):
        self.nama = nama
        self.nilai = nilai

    def __str__(self):
        return f"Nama: {self.nama}, Nilai: {self.nilai}"

    def __gt__(self, other):
        return self.nilai > other.nilai

    def __eq__(self, other):
        return self.nilai == other.nilai

    def __add__(self, other):
        return self.nilai + other.nilai

    def __mul__(self, faktor):
        return self.nilai * faktor

    def __len__(self):
        return len(self.nama)


m1 = Mahasiswa("Andi", 85)
m2 = Mahasiswa("Budi", 85)
m3 = Mahasiswa("Citra", 75)

print(m1)
print(m2)

print("Apakah nilai Andi dan Budi sama?", m1 == m2)
print("Total nilai:", m1 + m3)
print("Nilai Andi x 2 =", m1 * 2)

list_mahasiswa = [m1, m2, m3]
hasil_sort = sorted(list_mahasiswa, key=lambda x: x.nilai)

print("Urutan mahasiswa berdasarkan nilai:")
for m in hasil_sort:
    print(m)
