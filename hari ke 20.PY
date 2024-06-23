class Employee:
    def __init__(self, name, age, salary):
        self.__name = name
        self.__age = age
        self.__salary = salary

    def set_name(self, name):
        if isinstance(name, str):
            self.__name = name
        else:
            raise ValueError("Nama harus berupa string")

    def set_age(self, age):
        if isinstance(age, int) and age >= 18:
            self.__age = age
        else:
            raise ValueError("Umur harus berupa integer dan minimal 18 tahun")

    def set_salary(self, salary):
        if isinstance(salary, (int, float)) and salary > 0:
            self.__salary = salary
        else:
            raise ValueError("Gaji harus berupa integer atau float dan lebih besar dari 0")

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_salary(self):
        return self.__salary

# Membuat object berdasarkan class Employee
employee = Employee("John Doe", 25, 5000000)

# Mengakses dan mengubah nilai atribut menggunakan metode set
employee.set_name("Jane Doe")
employee.set_age(30)
employee.set_salary(6000000)

# Mengakses dan mencetak nilai atribut menggunakan metode get
print("Nama:", employee.get_name())
print("Umur:", employee.get_age())
print("Gaji:", employee.get_salary())
