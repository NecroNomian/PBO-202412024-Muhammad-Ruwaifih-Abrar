class Burung:
    def terbang(self):
        return "Burung terbang tinggi"


class Pesawat:
    def terbang(self):
        return "Pesawat lepas landas"


def uji_terbang(obj):
    print(obj.terbang())


class Laptop:
    def nyalakan(self):
        return "Laptop menyala"


class Smartphone:
    def nyalakan(self):
        return "Smartphone menyala"


def tes_nyala(obj):
    print(obj.nyalakan())


b = Burung()
p = Pesawat()
l = Laptop()
s = Smartphone()

uji_terbang(b)
uji_terbang(p)
tes_nyala(l)
tes_nyala(s)
