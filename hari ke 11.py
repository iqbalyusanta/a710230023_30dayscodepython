class Car:
    def __init__(self, merk, model, tahun):
        self.merk = merk
        self.model = model
        self.tahun = tahun
        self.odometer = 0

    def keterangan(self):
        print(f"Mobil baru saya {self.merk} {self.model} tahun {self.tahun} kilometernya masih {self.odometer}")

mobil_baru = Car('Honda','City',2021)
mobil_baru.keterangan()