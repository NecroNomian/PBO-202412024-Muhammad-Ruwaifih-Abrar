class Nilai:
    def __init__(self, kode_mk: str, skor: float):
        self.kode_mk = kode_mk
        self.skor = skor


class Mahasiswa:
    def __init__(self, nim, nama):
        self.nim = nim
        self.nama = nama
        self.daftar_nilai = []

    def tambah_nilai(self, nilai):
        self.daftar_nilai.append(nilai)

    def rata_rata(self):
        if not self.daftar_nilai:
            return 0
        return sum(n.skor for n in self.daftar_nilai) / len(self.daftar_nilai)


class MataKuliah:
    def __init__(self, kode: str, nama: str):
        self.kode = kode
        self.nama = nama


class ProgramStudi:
    def __init__(self, nama):
        self.nama = nama
        self.daftar_matakuliah = []

    def tambah_matakuliah(self, mk: MataKuliah):
        self.daftar_matakuliah.append(mk)


class Universitas:
    def __init__(self, nama):
        self.nama = nama
        self.programs = []

    def buat_program(self, nama_prodi):
        prodi = ProgramStudi(nama_prodi)
        self.programs.append(prodi)
        return prodi


def report_program(prodi: ProgramStudi, semua_mahasiswa: list[Mahasiswa]):
    print(f"Program Studi: {prodi.nama}")
    print("Matakuliah:", ", ".join([mk.kode for mk in prodi.daftar_matakuliah]) or "-")
    print("Mahasiswa dan rata-rata nilai:")
    for m in semua_mahasiswa:
        relevan = [
            n for n in m.daftar_nilai
            if any(n.kode_mk == mk.kode for mk in prodi.daftar_matakuliah)
        ]
        if relevan:
            avg = sum(n.skor for n in relevan) / len(relevan)
            print(f" {m.nim} - {m.nama}: {round(avg, 2)}")
    print("-" * 40)


if __name__ == "__main__":
    uni = Universitas("Universitas A")

    prodi_ti = uni.buat_program("Teknik Informatika")
    prodi_si = uni.buat_program("Sistem Informasi")
    prodi_mi = uni.buat_program("Manajemen Informatika")

    prodi_ti.tambah_matakuliah(MataKuliah("TI101", "Pemrograman Dasar"))
    prodi_ti.tambah_matakuliah(MataKuliah("TI102", "Struktur Data"))

    prodi_si.tambah_matakuliah(MataKuliah("SI101", "Sistem Informasi"))
    prodi_si.tambah_matakuliah(MataKuliah("SI102", "Analisis Sistem"))

    prodi_mi.tambah_matakuliah(MataKuliah("MI101", "Aplikasi Perkantoran"))
    prodi_mi.tambah_matakuliah(MataKuliah("MI102", "Basis Data"))

    m1 = Mahasiswa("23001", "Budi")
    m2 = Mahasiswa("23002", "Siti")
    m3 = Mahasiswa("23003", "Andi")

    m1.tambah_nilai(Nilai("TI101", 85))
    m1.tambah_nilai(Nilai("TI102", 80))

    m2.tambah_nilai(Nilai("SI101", 90))
    m2.tambah_nilai(Nilai("SI102", 88))

    m3.tambah_nilai(Nilai("MI101", 75))
    m3.tambah_nilai(Nilai("MI102", 78))

    for prodi in uni.programs:
        report_program(prodi, [m1, m2, m3])
