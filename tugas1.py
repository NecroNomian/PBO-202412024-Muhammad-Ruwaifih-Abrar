from abc import ABC, abstractmethod


# =========================
# 1. ABSTRACTION
# =========================
class Pengguna(ABC):
    def __init__(self, nama):
        self.nama = nama

    @abstractmethod
    def akses(self):
        pass


class Member(Pengguna):
    def __init__(self, nama, poin):
        super().__init__(nama)
        self.poin = poin

    def akses(self):
        print(f"{self.nama} memiliki akses sebagai MEMBER.")

    # =========================
    # 2. SPECIAL METHODS
    # =========================
    def __str__(self):
        return f"Member: {self.nama} – Poin: {self.poin}"

    def __add__(self, other):
        return self.poin + other.poin

    def __len__(self):
        return len(self.nama)


# =========================
# 4. CUSTOM EXCEPTION
# =========================
class PoinTidakValidError(Exception):
    pass


# =========================
# PROGRAM UTAMA
# =========================
def input_poin():
    nilai = input("Masukkan poin member: ").strip()

    if nilai == "":
        raise ValueError("Input poin tidak boleh kosong!")

    poin = int(nilai)

    if poin < 0:
        raise PoinTidakValidError("Poin tidak boleh negatif!")

    return poin


if __name__ == "__main__":
    try:
        # =========================
        # 3. EXCEPTION HANDLING
        # =========================
        poin1 = input_poin()
        poin2 = input_poin()

        # =========================
        # 5. INSTANSIASI OBJEK
        # =========================
        m1 = Member("Andi", poin1)
        m2 = Member("Budi", poin2)

        # Tampilkan info member
        print("\n=== INFO MEMBER ===")
        print(m1)
        print(m2)

        # Hak akses
        m1.akses()
        m2.akses()

        # Operasi special methods
        print("\n=== OPERASI ===")
        print("Jumlah poin:", m1 + m2)
        print("Panjang nama m1:", len(m1))

    except ValueError as ve:
        print("Error Input:", ve)

    except PoinTidakValidError as pe:
        print("Error Poin:", pe)

    finally:
        print("\nProgram selesai dijalankan.")
