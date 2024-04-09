from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QApplication, QFrame, QHBoxLayout, QVBoxLayout
from PyQt5.QtGui import * 
from PyQt5.QtCore import Qt,QTimer, QSize
from test_two import WindowTwo

#Splash Screen begins
class MainWindow(QWidget):#QMainWindow): 
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setStyleSheet('''
           #LabelTitle{
           font-size: 40px;
                font-family: "Lucida Console", "Courier New", monospace;
                color: #EDF5E1
                }
            #LabelDesc{
           font-size: 20px;
                font-family: "Lucida Console", "Courier New", monospace;
                color: #EDF5E1
                }    
            
            QFrame{
                background-color: rgb(0,0,0);
            }
                ''')
        self.setWindowTitle("Viewer")
        self.setFixedSize(720,480)
        #mycode
        self.setWindowFlag(Qt.FramelessWindowHint) 
        self.setAttribute(Qt.WA_TranslucentBackground)
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        self.frame = QFrame()
        layout.addWidget(self.frame) 
        
        #image 1
        self.label_image_1 = QLabel(self)
        self.pixmap = QPixmap('images/icon.png')
        self.label_image_1.setGeometry(440,290,100,100)
        self.pixmap = self.pixmap.scaled(100,100, Qt.KeepAspectRatio) #resize image
        self.label_image_1.setPixmap(self.pixmap)
        
        #image 2
        self.label_image_2 = QLabel(self)
        self.pixmap = QPixmap('images/icon.png')
        self.label_image_2.setGeometry(170,290,100,100)
        self.pixmap = self.pixmap.scaled(100,100, Qt.KeepAspectRatio)
        self.label_image_2.setPixmap(self.pixmap)
        
        #Center Title            
        self.labelTitle = QLabel(self.frame)
        self.labelTitle.setObjectName('LabelTitle')
        self.labelTitle.resize(self.width() -10,150)
        self.labelTitle.move(0,40) #x,y
        self.labelTitle.setText('Splash Screen of Aelwen')
        self.labelTitle.setAlignment(Qt.AlignCenter)
        
        #center Description
        self.labelDescription = QLabel(self.frame)
        self.labelDescription.setObjectName('LabelDesc')
        self.labelDescription.resize(self.width() -10,50)
        self.labelDescription.move(0,self.labelTitle.height()) #x,y
        self.labelDescription.setText('Some text appears')
        self.labelDescription.setAlignment(Qt.AlignCenter)
        
        #loading gif
        self.label_animation = QLabel(self)
        self.movie = QMovie('1.gif')
        self.movie.setScaledSize(QSize().scaled(100,100, Qt.KeepAspectRatio)) #resizing gif while keeping aspect ratio 
        self.label_animation.setGeometry(310,290,100,100)
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

#Splash Screen ends

    def startWindowTwo(self):
        self.movie.stop()
        self.close()
        self.windowTwo = WindowTwo()
        self.windowTwo.show()
