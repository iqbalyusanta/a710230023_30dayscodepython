class Hewan:
    def __init__(self, nama, jenis):
        self.nama = nama
        self.jenis = jenis

class Mamalia(Hewan):
    def __init__(self, nama, jenis, mamalia_bertelur):
        super().__init__(nama, jenis)
        self.mamalia_bertelur = mamalia_bertelur

class Unggas(Hewan):
    def __init__(self, nama, jenis, unggas_terbang):
        super().__init__(nama, jenis)
        self.unggas_terbang = unggas_terbang

class Gajah(Mamalia):
    def __init__(self, nama, jenis, berat_badan, mamalia_bertelur=True):
        super().__init__(nama, jenis, mamalia_bertelur)
        self.berat_badan = berat_badan

class Ayam(Unggas):
    def __init__(self, nama, jenis, jumlah_telur, unggas_terbang=True):
        super().__init__(nama, jenis, unggas_terbang)
        self.jumlah_telur = jumlah_telur

    def info(self):
        print(f"Nama: {self.nama}")
        print(f"Jenis: {self.jenis}")
        print(f"Unggas Terbang: {self.unggas_terbang}")
        print(f"Jumlah Telur: {self.jumlah_telur}")

ayam1 = Ayam("Ayam Serama", "Ayam", 20)
ayam1.info()

gajah1 = Gajah("Gajah Sumatera", "Gajah", 4000)
print(f"Nama: {gajah1.nama}")
print(f"Jenis: {gajah1.jenis}")
print(f"Mamalia Bertelur: {gajah1.mamalia_bertelur}")
print(f"Berat Badan: {gajah1.berat_badan}")
