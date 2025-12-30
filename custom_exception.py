class UmurTidakValidError(Exception):
    pass


class UmurTerlaluMudaError(Exception):
    pass


class UmurTerlaluTuaError(Exception):
    pass


class AkunTidakDiizinkanError(Exception):
    pass


def set_umur(umur):
    if umur < 0:
        raise UmurTidakValidError("Umur tidak boleh negatif!")
    if umur < 5:
        raise UmurTerlaluMudaError("Umur terlalu muda!")
    if umur > 100:
        raise UmurTerlaluTuaError("Umur terlalu tua!")
    return umur


def daftar_akun(umur):
    if umur < 18:
        raise AkunTidakDiizinkanError("Akun hanya boleh untuk umur 18 ke atas.")
    print("Akun berhasil dibuat.")


if __name__ == "__main__":
    while True:
        try:
            u = int(input("Masukkan umur: "))
            umur = set_umur(u)
            break
        except ValueError:
            print("Input harus berupa bilangan bulat!")
        except (UmurTidakValidError, UmurTerlaluMudaError, UmurTerlaluTuaError) as e:
            print(e)

    print("Umur berhasil disimpan:", umur)

    try:
        daftar_akun(umur)
    except AkunTidakDiizinkanError as e:
        print(e)
