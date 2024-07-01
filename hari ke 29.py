from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidget 

class MainWindow(QMainWindow): 
    def __init__(self): 
        super().__init__() 
        
        # Membuat QListWidget (Creating a QListWidget)
        self.list_widget = QListWidget() 
        
        # Menambahkan item ke QListWidget (Adding items to the QListWidget)
        self.list_widget.addItem('Alice') 
        self.list_widget.addItem('Bob') 
        self.list_widget.addItem('Charlie') 
        
        # Menetapkan QListWidget sebagai widget pusat (Setting QListWidget as the central widget)
        self.setCentralWidget(self.list_widget) 

if __name__ == "__main__": 
    app = QApplication([]) 
    window = MainWindow() 
    window.show() 
    app.exec_()
