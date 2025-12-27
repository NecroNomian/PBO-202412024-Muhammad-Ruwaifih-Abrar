class ManajerInventori:
    def __init__(self):
        self.inventori = []

    def tambah_barang(self, barang):
        self.inventori.append(barang)
        return f"Barang '{barang}' berhasil ditambahkan."

    def hapus_barang(self, barang):
        if barang in self.inventori:
            self.inventori.remove(barang)
            return f"Barang '{barang}' berhasil dihapus."
        return f"Barang '{barang}' tidak ditemukan."

    def lihat_inventori(self):
        if not self.inventori:
            return "Inventori kosong."
        return f"Daftar barang: {', '.join(self.inventori)}"


# Testing
inv = ManajerInventori()

print(inv.tambah_barang("Laptop"))
print(inv.tambah_barang("Mouse"))
print(inv.lihat_inventori())

print(inv.hapus_barang("Mouse"))
print(inv.lihat_inventori())
