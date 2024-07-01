class Mahasiswa:
    def __init__(self, nama, nim, jurusan):
        self.nama = nama
        self.__nim = nim
        self.__jurusan = jurusan

    def tambah_nilai(self):
        print(f"{self.nama} melakukan remidi untuk tambah nilai")
    
    def rata_rata_nilai(self):
        print(f"{self.nama} memiliki rata rata nilai sangat rendah")
    
    # Getter untuk nim
    def get_nim(self):
        return self.__nim
    
    # Setter untuk nim
    def set_nim(self, nim):
        self.__nim = nim
    
    # Getter untuk jurusan
    def get_jurusan(self):
        return self.__jurusan
    
    # Setter untuk jurusan
    def set_jurusan(self, jurusan):
        self.__jurusan = jurusan

# Membuat objek mahasiswa_ums
mahasiswa_ums = Mahasiswa("madara", "a710230123", "pti")

# Mengakses properti menggunakan getter
print(f"mahasiswa ums dengan nama {mahasiswa_ums.nama}")
print(f"mahasiswa ums dengan nim {mahasiswa_ums.get_nim()}")
print(f"mahasiswa ums dengan jurusan {mahasiswa_ums.get_jurusan()}")

# Menggunakan method
mahasiswa_ums.tambah_nilai()
mahasiswa_ums.rata_rata_nilai()

# Membuat objek baru
mahasiswa_baru = Mahasiswa("sasuke", "b710230124", "teknik informatika")

# Mengakses properti private menggunakan getter dan setter
print(f"mahasiswa baru dengan nama {mahasiswa_baru.nama}")
print(f"mahasiswa baru dengan nim sebelum diubah {mahasiswa_baru.get_nim()}")
mahasiswa_baru.set_nim("b710230125")
print(f"mahasiswa baru dengan nim setelah diubah {mahasiswa_baru.get_nim()}")

print(f"mahasiswa baru dengan jurusan sebelum diubah {mahasiswa_baru.get_jurusan()}")
mahasiswa_baru.set_jurusan("sistem informasi")
print(f"mahasiswa baru dengan jurusan setelah diubah {mahasiswa_baru.get_jurusan()}")
