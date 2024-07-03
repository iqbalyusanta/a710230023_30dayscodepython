from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtSql import QSqlDatabase, QSqlQuery

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Main Window')
        
        # Create a connection to the SQLite database
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName("database.sqlite")
        
        # Open the connection to the database
        if not self.db.open():
            print("Failed to open database")
            return
        
        # Create a table in the database (Create)
        query = QSqlQuery()
        query.exec_("CREATE TABLE IF NOT EXISTS people (id INTEGER PRIMARY KEY, name TEXT)")
        
        # Add data to the table (Create)
        query.exec_("INSERT INTO people (name) VALUES ('Setiawan Arif')")
        
        # Retrieve data from the table (Read)
        query.exec_("SELECT * FROM people")
        while query.next():
            for i in range(query.record().count()):  # Adjust the range to the number of columns in the table
                print(query.value(i))
        
        # Update data in the table (Update)
        query.exec_("UPDATE people SET name = 'Jane Doe' WHERE id = 1")
        
        # Delete data from the table (Delete)
        query.exec_("DELETE FROM people WHERE id = 1")

if __name__ == "__main__":
    app = QApplication([])
    main_window = MainWindow()
    main_window.show()
    app.exec_()
