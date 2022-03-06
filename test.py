from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QApplication
from PyQt5.QtGui import * 
from PyQt5.QtCore import Qt,QTimer
from test_two import WindowTwo

class MainWindow(QWidget):#QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setStyleSheet(
            "background-color: rgb(0, 0, 0);")
        self.setWindowTitle("Viewer")
        self.setMinimumSize(1376, 720)
        #mycode
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.label_animation = QLabel(self)
        self.movie = QMovie('1.gif')
        self.label_animation.setGeometry(688,360,200,200)
        self.label_animation.setMovie(self.movie)
        
        timer = QTimer(self)
        
        self.startAnimation()
        timer.singleShot(5000,self.startWindowTwo)
        self.show()
        
    def startAnimation(self):
        self.movie.start()
        
    # def stopAnimation(self):
    #     self.movie.stop()
    #     self.close()

    def startWindowTwo(self):
        self.movie.stop()
        self.close()
        self.windowTwo = WindowTwo()
        self.windowTwo.show()
