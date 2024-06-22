while True:
    try:
        num = int(input("Masukkan bilangan bulat: "))
        break
    except ValueError:
        print("Input yang dimasukkan tidak valid!")

square = num ** 2
print(f"Hasil pangkat dua dari {num} adalah {square}.")