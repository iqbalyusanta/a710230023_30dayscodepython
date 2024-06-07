class Kendaraan:
    def __init__(self, jenis):
        self.jenis = jenis

class Sepeda(Kendaraan):
    def __init__(self, jenis, warna):
        super().__init__(jenis)
        self.warna = warna

class SepedaMotor(Sepeda):
    def __init__(self, jenis, warna, merk):
        super().__init__(jenis, warna)
        self.merk = merk

class Mobil(SepedaMotor):
    def __init__(self, jenis, warna, merk, tahun):
        super().__init__(jenis, warna, merk)
        self.tahun = tahun

    def info(self):
        print(f"Jenis: {self.jenis}")
        print(f"Warna: {self.warna}")
        print(f"Merk: {self.merk}")
        print(f"Tahun: {self.tahun}")

mobil1 = Mobil("Sedan", "Merah", "Toyota", 2022)
mobil1.info()
