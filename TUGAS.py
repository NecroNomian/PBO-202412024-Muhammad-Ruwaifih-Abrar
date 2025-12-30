import tkinter as tk
from tkinter import ttk, messagebox, filedialog


class Mahasiswa:
    def __init__(self, nim, nama, jurusan, ipk):
        self.nim = nim
        self.nama = nama
        self.jurusan = jurusan
        self.ipk = ipk

    def info(self):
        return f"{self.nim} - {self.nama} - {self.jurusan} - {self.ipk}"

    def update_ipk(self, ipk_baru):
        self.ipk = ipk_baru


class AplikasiManajemenMahasiswa:
    def __init__(self, root):
        self.root = root
        self.root.title("Manajemen Mahasiswa")
        self.root.geometry("800x500")

        self.data_mahasiswa = {}

        # ===== Frame Input =====
        frame_input = tk.Frame(root, padx=10, pady=10)
        frame_input.pack()

        tk.Label(frame_input, text="NIM").grid(row=0, column=0)
        tk.Label(frame_input, text="Nama").grid(row=1, column=0)
        tk.Label(frame_input, text="Jurusan").grid(row=2, column=0)
        tk.Label(frame_input, text="IPK").grid(row=3, column=0)

        self.entry_nim = tk.Entry(frame_input)
        self.entry_nama = tk.Entry(frame_input)
        self.entry_jurusan = tk.Entry(frame_input)
        self.entry_ipk = tk.Entry(frame_input)

        self.entry_nim.grid(row=0, column=1)
        self.entry_nama.grid(row=1, column=1)
        self.entry_jurusan.grid(row=2, column=1)
        self.entry_ipk.grid(row=3, column=1)

        # ===== Frame Tombol =====
        frame_tombol = tk.Frame(root, pady=10)
        frame_tombol.pack()

        tk.Button(frame_tombol, text="Tambah", command=self.tambah).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_tombol, text="Hapus", command=self.hapus).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_tombol, text="Cari", command=self.cari).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_tombol, text="Update IPK", command=self.update_ipk).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_tombol, text="Rata-rata IPK", command=self.rata_ipk).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_tombol, text="IPK Tertinggi", command=self.ipk_tertinggi).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_tombol, text="Export", command=self.export).pack(side=tk.LEFT, padx=5)

        # ===== Filter Jurusan =====
        tk.Label(frame_tombol, text="Filter Jurusan:").pack(side=tk.LEFT, padx=5)
        self.entry_filter = tk.Entry(frame_tombol, width=10)
        self.entry_filter.pack(side=tk.LEFT)
        tk.Button(frame_tombol, text="Filter", command=self.filter_jurusan).pack(side=tk.LEFT, padx=5)

        # ===== Treeview =====
        self.tree = ttk.Treeview(root, columns=("NIM", "Nama", "Jurusan", "IPK"), show="headings")
        for col in ("NIM", "Nama", "Jurusan", "IPK"):
            self.tree.heading(col, text=col)
        self.tree.pack(fill=tk.BOTH, expand=True)

    # ===== CRUD & Fitur =====
    def tambah(self):
        nim = self.entry_nim.get()
        nama = self.entry_nama.get()
        jurusan = self.entry_jurusan.get()
        ipk = self.entry_ipk.get()

        if not (nim and nama and jurusan and ipk):
            messagebox.showwarning("Error", "Semua data wajib diisi")
            return

        if nim in self.data_mahasiswa:
            messagebox.showwarning("Error", "NIM sudah ada")
            return

        mhs = Mahasiswa(nim, nama, jurusan, float(ipk))
        self.data_mahasiswa[nim] = mhs
        self.refresh()

    def hapus(self):
        selected = self.tree.selection()
        if selected:
            nim = self.tree.item(selected[0])["values"][0]
            del self.data_mahasiswa[nim]
            self.refresh()

    def cari(self):
        keyword = self.entry_nama.get().lower()
        self.tree.delete(*self.tree.get_children())
        for m in self.data_mahasiswa.values():
            if keyword in m.nama.lower() or keyword == m.nim:
                self.tree.insert("", tk.END, values=(m.nim, m.nama, m.jurusan, m.ipk))

    def update_ipk(self):
        selected = self.tree.selection()
        if selected:
            nim = self.tree.item(selected[0])["values"][0]
            ipk_baru = float(self.entry_ipk.get())
            self.data_mahasiswa[nim].update_ipk(ipk_baru)
            self.refresh()

    def rata_ipk(self):
        if self.data_mahasiswa:
            avg = sum(m.ipk for m in self.data_mahasiswa.values()) / len(self.data_mahasiswa)
            messagebox.showinfo("Rata-rata IPK", round(avg, 2))

    def ipk_tertinggi(self):
        if self.data_mahasiswa:
            m = max(self.data_mahasiswa.values(), key=lambda x: x.ipk)
            messagebox.showinfo("IPK Tertinggi", m.info())

    def filter_jurusan(self):
        jur = self.entry_filter.get().lower()
        self.tree.delete(*self.tree.get_children())
        for m in self.data_mahasiswa.values():
            if jur in m.jurusan.lower():
                self.tree.insert("", tk.END, values=(m.nim, m.nama, m.jurusan, m.ipk))

    def export(self):
        file = filedialog.asksaveasfilename(defaultextension=".txt")
        if file:
            with open(file, "w") as f:
                for m in self.data_mahasiswa.values():
                    f.write(m.info() + "\n")

    def refresh(self):
        self.tree.delete(*self.tree.get_children())
        for m in self.data_mahasiswa.values():
            self.tree.insert("", tk.END, values=(m.nim, m.nama, m.jurusan, m.ipk))


if __name__ == "__main__":
    root = tk.Tk()
    app = AplikasiManajemenMahasiswa(root)
    root.mainloop()
