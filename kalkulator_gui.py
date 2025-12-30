import tkinter as tk
from tkinter import messagebox

class KonversiSuhu:
    def __init__(self, root):
        self.root = root
        self.root.title("Konversi Suhu")
        self.root.geometry("300x200")

        self.label = tk.Label(
            root, text="Masukkan Suhu (Celsius)",
            font=("Arial", 12)
        )
        self.label.pack(pady=10)

        self.entry = tk.Entry(root, width=25)
        self.entry.pack(pady=5)

        self.button = tk.Button(
            root,
            text="Konversi",
            command=self.konversi_suhu
        )
        self.button.pack(pady=5)

        self.hasil = tk.Label(root, text="", font=("Arial", 12))
        self.hasil.pack(pady=10)

    def konversi_suhu(self):
        nilai = self.entry.get()

        if nilai == "":
            messagebox.showwarning("Error", "Input tidak boleh kosong!")
            return

        try:
            celsius = float(nilai)
            fahrenheit = (celsius * 9/5) + 32
            self.hasil.config(
                text=f"Hasil: {fahrenheit:.2f} °F"
            )
        except ValueError:
            messagebox.showerror(
                "Error", "Input harus berupa angka!"
            )

if __name__ == "__main__":
    root = tk.Tk()
    app = KonversiSuhu(root)
    root.mainloop()
