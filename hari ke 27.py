from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QPushButton, QVBoxLayout

class CustomDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hello!")
        layout = QVBoxLayout()
        button = QPushButton("Close")
        button.clicked.connect(self.close)
        layout.addWidget(button)
        self.setLayout(layout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        button = QPushButton("Open Dialog")
        button.clicked.connect(self.open_dialog)
        self.setCentralWidget(button)

    def open_dialog(self):
        dialog = CustomDialog()
        dialog.exec_()

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
