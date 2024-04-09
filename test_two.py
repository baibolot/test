from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QTableWidget, QLineEdit, QWidget
import sys

class WindowTwo(QtWidgets.QMainWindow):
    def __init__(self):
        super(WindowTwo, self).__init__()
        centralWidget = QtWidgets.QWidget()
        self.setCentralWidget(centralWidget)

        self.tableWidget = QTableWidget()
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setHorizontalHeaderLabels(["ФИО","Должность","Зарплата"])

        self.lineEdit_x = QLineEdit(placeholderText="введите: ФИО")
        self.lineEdit_y = QLineEdit(placeholderText="введите: Должность")
        self.lineEdit_z = QLineEdit(placeholderText="введите: Зарплату")

        self.pushButton = QtWidgets.QPushButton("Добавить")
        self.pushButton.clicked.connect(self.add_employee)

        self.grid = QtWidgets.QGridLayout(centralWidget)
        self.grid.addWidget(self.tableWidget, 0, 0, 1, 3)
        self.grid.addWidget(self.lineEdit_x, 1, 0)
        self.grid.addWidget(self.lineEdit_y, 1, 1)
        self.grid.addWidget(self.lineEdit_z, 1, 2)
        self.grid.addWidget(self.pushButton, 2, 0, 1, 3)

    def add_employee(self):
        x = self.lineEdit_x.text()
        y = self.lineEdit_y.text()
        z = self.lineEdit_z.text()

        rowPosition = self.tableWidget.rowCount()
        self.tableWidget.insertRow(rowPosition)

        self.tableWidget.setItem(rowPosition, 0, QtWidgets.QTableWidgetItem(x))
        self.tableWidget.setItem(rowPosition, 1, QtWidgets.QTableWidgetItem(y))
        self.tableWidget.setItem(rowPosition, 2, QtWidgets.QTableWidgetItem(z))

        self.lineEdit_x.clear()  # +++
        self.lineEdit_y.clear()
        self.lineEdit_z.clear()
