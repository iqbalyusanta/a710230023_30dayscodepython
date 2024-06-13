from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QLineEdit, QVBoxLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set the window title
        self.setWindowTitle('My App')

        # Create a QLabel, QPushButton, and QLineEdit
        self.label = QLabel()
        self.button = QPushButton('Show Text')
        self.textbox = QLineEdit()

        # Connect the button's clicked signal to the slot
        self.button.clicked.connect(self.on_button_clicked)

        # Create a QVBoxLayout and add the widgets
        layout = QVBoxLayout()
        layout.addWidget(self.textbox)
        layout.addWidget(self.button)
        layout.addWidget(self.label)

        # Create a QWidget, set its layout, and set it as the central widget
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    # Define the slot that will be called when the button is clicked
    def on_button_clicked(self):
        # Get the text from the QLineEdit and set it as the QLabel's text
        text = self.textbox.text()
        self.label.setText(text)

# Create a QApplication, create a MainWindow, show the main window, and start the event loop
app = QApplication([])
window = MainWindow()
window.show()
app.exec_()
