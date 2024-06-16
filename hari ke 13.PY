from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QLineEdit, QVBoxLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set the window title
        self.setWindowTitle('Kalkulator Sederhana')

        # Create two QLineEdit widgets for the user to enter numbers
        self.first_number = QLineEdit()
        self.second_number = QLineEdit()

        # Create a QLabel to display input and the result
        self.labelinput1 = QLabel("Masukkan Angka 1")
        self.labelinput2 = QLabel("Masukkan Angka 2")
        self.hasil_label = QLabel("Hasil Perhitungan")
        self.result_label = QLabel()

        # Create four QPushButton widgets for the mathematical operations
        self.add_button = QPushButton('Tambah')
        self.subtract_button = QPushButton('Kurang')
        self.multiply_button = QPushButton('Kali')
        self.divide_button = QPushButton('Bagi')

        # Connect each button's clicked signal to the appropriate slot
        self.add_button.clicked.connect(self.add_numbers)
        self.subtract_button.clicked.connect(self.subtract_numbers)
        self.multiply_button.clicked.connect(self.multiply_numbers)
        self.divide_button.clicked.connect(self.divide_numbers)

        # Create a QVBoxLayout and add the widgets
        layout = QVBoxLayout()
        layout.addWidget(self.labelinput1)
        layout.addWidget(self.first_number)
        layout.addWidget(self.labelinput2)
        layout.addWidget(self.second_number)
        layout.addWidget(self.add_button)
        layout.addWidget(self.subtract_button)
        layout.addWidget(self.multiply_button)
        layout.addWidget(self.divide_button)
        layout.addWidget(self.hasil_label)
        layout.addWidget(self.result_label)

        # Create a QWidget, set its layout, and set it as the central widget
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    # Define the slots that will be called when the buttons are clicked
    def add_numbers(self):
        # Add the numbers entered by the user and display the result
        result = float(self.first_number.text()) + float(self.second_number.text())
        self.result_label.setText(str(result))

    def subtract_numbers(self):
        # Subtract the second number from the first and display the result
        result = float(self.first_number.text()) - float(self.second_number.text())
        self.result_label.setText(str(result))

    def multiply_numbers(self):
        # Multiply the numbers entered by the user and display the result
        result = float(self.first_number.text()) * float(self.second_number.text())
        self.result_label.setText(str(result))

    def divide_numbers(self):
        # Divide the first number by the second and display the result
        result = float(self.first_number.text()) / float(self.second_number.text())
        self.result_label.setText(str(result))

# Create a QApplication, create a MainWindow, show the main window, and start the event loop
app = QApplication([])
window = MainWindow()
window.show()
app.exec_()
