class Car:
    def __init__(self, merk, model, tahun):
        self.merk = merk
        self.model = model
        self.tahun = tahun
        self.odometer = 0

    def keterangan(self):
      print(f"Mobil baru saya {self.merk} {self.model} tahun {self.tahun} kilometernya masih {self.odometer}")


class ElectricCar(Car):
    def __init__(self, merk, model, tahun, baterai):
        super().__init__(merk, model, tahun)
        self.baterai = baterai

    def daya(self):
        print(f"Mobil ini memiliki daya {self.baterai} -kWh")


teslaku = ElectricCar('tesla', 'model X', 2022, 7500)
print(teslaku.daya())