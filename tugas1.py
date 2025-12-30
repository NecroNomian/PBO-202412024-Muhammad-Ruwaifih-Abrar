# =========================
# Parent Class
# =========================
class Karyawan:
    def __init__(self, nama, gaji_pokok):
        self.nama = nama
        self.gaji_pokok = gaji_pokok

    def info_gaji(self):
        return f"{self.nama} - Gaji Pokok: {self.gaji_pokok}"


# =========================
# Child Class: Manager
# =========================
class Manager(Karyawan):
    def __init__(self, nama, gaji_pokok, tunjangan):
        super().__init__(nama, gaji_pokok)
        self.tunjangan = tunjangan

    def info_gaji(self):
        total = self.gaji_pokok + self.tunjangan
        return f"Manager {self.nama} - Total Gaji: {total}"


# =========================
# Child Class: Programmer
# =========================
class Programmer(Karyawan):
    def __init__(self, nama, gaji_pokok, bonus):
        super().__init__(nama, gaji_pokok)
        self.bonus = bonus

    def info_gaji(self):
        total = self.gaji_pokok + self.bonus
        return f"Programmer {self.nama} - Total Gaji: {total}"


# =========================
# Composition: Departemen
# =========================
class Departemen:
    def __init__(self, nama_departemen):
        self.nama_departemen = nama_departemen
        self.karyawan_list = []

    def tambah_karyawan(self, karyawan):
        self.karyawan_list.append(karyawan)

    def tampilkan_karyawan(self):
        print(f"Daftar Karyawan Departemen {self.nama_departemen}:")
        for k in self.karyawan_list:
            print(k.info_gaji())


# =========================
# Instansiasi Object
# =========================
m1 = Manager("Andi", 7000000, 3000000)
m2 = Manager("Budi", 7500000, 2500000)

p1 = Programmer("Citra", 6000000, 1500000)
p2 = Programmer("Dina", 6200000, 1800000)

dept_it = Departemen("IT")

dept_it.tambah_karyawan(m1)
dept_it.tambah_karyawan(m2)
dept_it.tambah_karyawan(p1)
dept_it.tambah_karyawan(p2)

# =========================
# Eksekusi Program
# =========================
dept_it.tampilkan_karyawan()
