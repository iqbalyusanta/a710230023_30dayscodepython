# Import necessary modules from PyQt5
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel

# Define a MainWindow class that inherits from QMainWindow
class MainWindow(QMainWindow):
    def __init__(self):
        # Call the constructor of the parent class
        super().__init__()
        
        # Set some basic attributes for the window
        self.title = "Hello PyQt5"
        self.top = 100
        self.left = 100
        self.width = 400
        self.height = 300
        
        # Call the method that initializes the window
        self.initWindow()

    def initWindow(self):
        # Create a QLabel widget and set it as the central widget of the window
        self.label = QLabel("Welcome to PyQt5", self)
        self.label.adjustSize()  # Adjust the size of the label to fit the text
        self.label.move(100, 100)  # Move the label to the position (100, 100)
        
        # Set the title of the window
        self.setWindowTitle(self.title)
        # Set the position and size of the window
        self.setGeometry(self.left, self.top, self.width, self.height)
        # Show the window
        self.show()

# Create an instance of QApplication
app = QApplication([])

# Create an instance of MainWindow
window = MainWindow()

# Start the event loop
app.exec_()
