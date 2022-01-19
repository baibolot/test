from PyQt5.QtWidgets import QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setStyleSheet(
            "background-color: rgb(50, 50, 50);")
        self.setWindowTitle("Viewer")
        self.setMinimumSize(1376, 720)
    