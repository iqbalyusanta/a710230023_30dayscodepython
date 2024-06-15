from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QLineEdit, QVBoxLayout, QHBoxLayout, QGridLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Layouts Example')

        # Create some widgets
        label1 = QLabel('Label 1')
        label2 = QLabel('Label 2')
        label3 = QLabel('Label 3')
        button1 = QPushButton('Button 1')
        button2 = QPushButton('Button 2')
        button3 = QPushButton('Button 3')
        textbox1 = QLineEdit()
        textbox2 = QLineEdit()
        textbox3 = QLineEdit()

        # Create a QVBoxLayout
        vbox_layout = QVBoxLayout()
        vbox_layout.addWidget(QLabel('Vertical Layout'))
        vbox_layout.addWidget(label1)
        vbox_layout.addWidget(button1)
        vbox_layout.addWidget(textbox1)

        # Create a QHBoxLayout
        hbox_layout = QHBoxLayout()
        hbox_layout.addWidget(QLabel('Horizontal Layout'))
        hbox_layout.addWidget(label2)
        hbox_layout.addWidget(button2)
        hbox_layout.addWidget(textbox2)

        # Create a QGridLayout
        grid_layout = QGridLayout()
        grid_layout.addWidget(QLabel('Grid Layout'), 0, 0, 1, 2)
        grid_layout.addWidget(label3, 1, 0)
        grid_layout.addWidget(button3, 1, 1)
        grid_layout.addWidget(textbox3, 2, 0, 1, 2)

        # Create a QVBoxLayout for the main layout and add the other layouts
        main_layout = QVBoxLayout()
        main_layout.addLayout(vbox_layout)
        main_layout.addLayout(hbox_layout)
        main_layout.addLayout(grid_layout)

        # Create a QWidget, set its layout, and set it as the central widget
        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

app = QApplication([])
window = MainWindow()
window.show()
app.exec_()
