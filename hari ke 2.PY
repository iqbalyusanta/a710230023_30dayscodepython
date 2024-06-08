class Employee:
    def __init__(self, name, position, salary):  # Perbaikan: Gunakan __init__ (dua garis bawah)
        self.name = name
        self.position = position
        self.salary = salary

class EmployeeManager:
    def __init__(self):  # Perbaikan: Gunakan __init__ (dua garis bawah)
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def remove_employee(self, employee):
        self.employees.remove(employee)

    def find_employee(self, name):
        for employee in self.employees:
            if employee.name == name:
                return employee
        return None

class EmployeeReport:
    def generate_report(self, employee):
        return f"Employee: {employee.name}, Position: {employee.position}, Salary: {employee.salary}"

class SalaryReport(EmployeeReport):
    def generate_report(self, employee):
        return f"Salary Report: {employee.name} earns {employee.salary}"

class EmployeeManagerAbstraction:
    def get_employee(self, name):
        pass

class EmployeeManagerAdapter(EmployeeManagerAbstraction):
    def __init__(self, manager):  # Perbaikan: Gunakan __init__ (dua garis bawah)
        self.manager = manager

    def get_employee(self, name):
        return self.manager.find_employee(name)

class ReportGenerator:
    def __init__(self, manager, report):  # Perbaikan: Gunakan __init__ (dua garis bawah)
        self.manager = manager
        self.report = report

    def generate_report(self, name):
        employee = self.manager.get_employee(name)
        if employee:
            return self.report.generate_report(employee)
        return f"Employee {name} not found"

# Mencoba implementasi
manager = EmployeeManager()
manager.add_employee(Employee("John Doe", "Developer", 5000))
manager.add_employee(Employee("Jane Smith", "Manager", 6000))

adapter = EmployeeManagerAdapter(manager)

generator = ReportGenerator(adapter, SalaryReport())
print(generator.generate_report("John Doe"))  # Output: Salary Report: John Doe earns 5000
print(generator.generate_report("Jane Smith"))  # Output: Salary Report: Jane Smith earns 6000
