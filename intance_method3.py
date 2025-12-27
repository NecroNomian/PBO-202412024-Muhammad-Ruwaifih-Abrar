class ManajerInventori:
    def __init__(self):
        self.inventori = {}

    def tambah_barang(self, barang, jumlah=1):
        if barang in self.inventori:
            self.inventori[barang] += jumlah
        else:
            self.inventori[barang] = jumlah
        
        return f"Stok '{barang}' bertambah {jumlah}. Total: {self.inventori[barang]}"

    def hapus_barang(self, barang, jumlah=1):
        if barang not in self.inventori:
            return f"Barang '{barang}' tidak ditemukan."

        if self.inventori[barang] < jumlah:
            return f"Stok '{barang}' tidak cukup untuk dikurangi {jumlah}."

        self.inventori[barang] -= jumlah

        if self.inventori[barang] == 0:
            del self.inventori[barang]
            return f"'{barang}' habis dan dihapus dari inventori."

        return f"Stok '{barang}' berkurang {jumlah}. Sisa: {self.inventori[barang]}"

    def lihat_inventori(self):
        if not self.inventori:
            return "Inventori kosong."
        
        daftar = [f"{barang}: {stok}" for barang, stok in self.inventori.items()]
        return "Daftar barang:\n" + "\n".join(daftar)


# Testing
inv = ManajerInventori()

print(inv.tambah_barang("Laptop", 3))
print(inv.tambah_barang("Mouse", 5))
print(inv.lihat_inventori())

print(inv.hapus_barang("Mouse", 2))
print(inv.hapus_barang("Laptop", 3))
print(inv.lihat_inventori())
