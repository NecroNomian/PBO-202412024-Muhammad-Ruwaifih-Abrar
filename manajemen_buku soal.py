import tkinter as tk
from tkinter import messagebox, ttk, simpledialog

class Tugas:
    def __init__(self, judul):
        self.judul = judul
        self.status = "Belum Selesai"


class AplikasiManajemenTugas:
    def __init__(self, root):
        self.root = root
        self.root.title("Manajemen Tugas")
        self.root.geometry("600x400")

        self.daftar_tugas = []

        frame_input = tk.Frame(root, padx=10, pady=10)
        frame_input.pack()

        tk.Label(frame_input, text="Judul Tugas:").grid(row=0, column=0)
        self.entry_tugas = tk.Entry(frame_input, width=30)
        self.entry_tugas.grid(row=0, column=1)

        frame_tombol = tk.Frame(root, pady=10)
        frame_tombol.pack()

        tk.Button(frame_tombol, text="Tambah", command=self.tambah_tugas).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_tombol, text="Edit", command=self.edit_tugas).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_tombol, text="Hapus", command=self.hapus_tugas).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_tombol, text="Selesai", command=self.tandai_selesai).pack(side=tk.LEFT, padx=5)

        self.tree = ttk.Treeview(root, columns=("Judul", "Status"), show="headings")
        self.tree.heading("Judul", text="Judul")
        self.tree.heading("Status", text="Status")
        self.tree.pack(fill=tk.BOTH, expand=True)

    def tambah_tugas(self):
        judul = self.entry_tugas.get()
        if judul:
            tugas = Tugas(judul)
            self.daftar_tugas.append(tugas)
            self.tree.insert("", tk.END, values=(tugas.judul, tugas.status))
            self.entry_tugas.delete(0, tk.END)

    def edit_tugas(self):
        selected = self.tree.selection()
        if selected:
            item = self.tree.item(selected[0])
            judul_baru = simpledialog.askstring("Edit", "Judul baru:")
            if judul_baru:
                for t in self.daftar_tugas:
                    if t.judul == item["values"][0]:
                        t.judul = judul_baru
                self.tree.item(selected[0], values=(judul_baru, item["values"][1]))

    def hapus_tugas(self):
        selected = self.tree.selection()
        if selected:
            judul = self.tree.item(selected[0])["values"][0]
            self.daftar_tugas = [t for t in self.daftar_tugas if t.judul != judul]
            self.tree.delete(selected[0])

    def tandai_selesai(self):
        selected = self.tree.selection()
        if selected:
            judul = self.tree.item(selected[0])["values"][0]
            for t in self.daftar_tugas:
                if t.judul == judul:
                    t.status = "Selesai"
            self.tree.item(selected[0], values=(judul, "Selesai"))


if __name__ == "__main__":
    root = tk.Tk()
    app = AplikasiManajemenTugas(root)
    root.mainloop()
