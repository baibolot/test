from PyQt5.QtWidgets import QMainWindow, QLabel
from PyQt5.QtGui import QPixmap


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setStyleSheet(
            "background-color: rgb(50, 50, 50);")
        self.setWindowTitle("Viewer")
        self.setMinimumSize(1376, 720)

        self.setWindowTitle("Sciberia")
        
        logo_img = QLabel(self)
        pixmap = QPixmap('images/Sciberia_logo.png')
        logo_img.setPixmap(pixmap)
        logo_img.resize(915, 303)
        logo_img.move(230, 208)
    