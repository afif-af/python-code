import sys
from PyQt6 import QtCore, QtWidgets, QtSql
import sportsconnection  # Assuming this is a custom module you need to maintain


def initializeModel(model):
    model.setTable('sportsmen')
    model.setEditStrategy(QtSql.QSqlTableModel.EditStrategy.OnFieldChange)
    model.select()
    model.setHeaderData(0, QtCore.Qt.Orientation.Horizontal, "ID")
    model.setHeaderData(1, QtCore.Qt.Orientation.Horizontal, "First name")
    model.setHeaderData(2, QtCore.Qt.Orientation.Horizontal, "Last name")


def createView(title, model):
    view = QtWidgets.QTableView()
    view.setModel(model)
    view.setWindowTitle(title)
    return view


def addrow():
    print(model.rowCount())
    ret = model.insertRows(model.rowCount(), 1)
    print(ret)


def findrow(i):
    global delrow
    delrow = i.row()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    # Database setup
    db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
    db.setDatabaseName('sports.db')
    if not db.open():
        print("Unable to open the database")
        sys.exit(1)

    # Model setup
    model = QtSql.QSqlTableModel()
    delrow = -1
    initializeModel(model)

    # Create view and connect signals
    view1 = createView("Table Model (View 1)", model)
    view1.clicked.connect(findrow)

    # Dialog and layout
    dlg = QtWidgets.QDialog()
    layout = QtWidgets.QVBoxLayout()
    layout.addWidget(view1)

    # Add a row button
    button = QtWidgets.QPushButton("Add a row")
    button.clicked.connect(addrow)
    layout.addWidget(button)

    # Delete a row button
    btn1 = QtWidgets.QPushButton("Delete selected row")
    btn1.clicked.connect(lambda: model.removeRow(view1.currentIndex().row()))
    layout.addWidget(btn1)

    # Set layout and show the dialog
    dlg.setLayout(layout)
    dlg.setWindowTitle("Database Demo")
    dlg.show()

    sys.exit(app.exec())
