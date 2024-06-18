from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Main Window')

        # Membuat widget utama
        widget = QWidget()
        self.setCentralWidget(widget)

        # Membuat layout utama
        layout = QVBoxLayout()
        widget.setLayout(layout)

        # Membuat input nama
        self.name_input = QLineEdit()
        layout.addWidget(self.name_input)

        # Membuat tombol kirim
        send_button = QPushButton('Kirim')
        send_button.clicked.connect(self.send_data)
        layout.addWidget(send_button)

        # Membuat instance widget
        self.name_widget = NameWidget()

    def send_data(self):
        # Mengambil data nama dari input
        name = self.name_input.text()
        # Mengirim data nama ke widget
        self.name_widget.receive_data(name)
        # Menampilkan widget
        self.name_widget.show()

class NameWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Widget')

        # Membuat layout
        layout = QVBoxLayout()
        self.setLayout(layout)

        # Membuat label untuk menampilkan data nama
        self.name_label = QLabel()
        layout.addWidget(self.name_label)

    def receive_data(self, name):
        # Menampilkan data nama pada label
        self.name_label.setText(f'Halo, {name}!')

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
