from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QDateTimeEdit
from PyQt5.QtCore import QDateTime

class DateTimeEditExample(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QDateTimeEdit Example')

        layout = QVBoxLayout()

        datetime_edit = QDateTimeEdit()
        datetime_edit.setDateTime(QDateTime.currentDateTime()) 
        layout.addWidget(datetime_edit)

        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication([])
    window = DateTimeEditExample()
    window.show()
    app.exec()
