class Mobil:
    def move(self):
        print("Berjalan di jalan raya")

class Pesawat:
    def move(self):
        print("Terbang di udara")

class Kapal:
    def move(self):
        print("Berlayar di laut")

# Membuat instance dari class Mobil
mobil = Mobil()
mobil.move()  # Output: Berjalan di jalan raya

# Membuat instance dari class Pesawat
pesawat = Pesawat()
pesawat.move()  # Output: Terbang di udara

# Membuat instance dari class Kapal
kapal = Kapal()
kapal.move()  # Output: Berlayar di laut