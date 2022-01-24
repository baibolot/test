from PyQt5.QtWidgets import QMainWindow, QWidget, QProgressBar, QLabel, QFrame, QVBoxLayout
from PyQt5.QtCore import Qt, QTimer

class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        
        self.setWindowTitle("Viewer")
        self.setMinimumSize(1376, 720)
        self.setStyleSheet('''
            
            #Title {
                font-size: 60px;
                font-family: "Lucida Console", "Courier New", monospace;
                color: #EDF5E1;
            }

            #Desc {
                font-size: 15px;
                font-family: "Lucida Console", "Courier New", monospace;
                color: #c2ced1;
            }

            #Quote {
                font-size: 20px;
                font-family: "Lucida Console", "Courier New", monospace;
                color: white;
            }

            QFrame {
                background-color: rgb(50, 50, 50);
            }

            QProgressBar {
                background-color: black;
                color: rgb(200, 200, 200);
                border-style: none;
                border-radius: 20px;
                text-align: center;
                font-size: 20px;
                font-family: "Lucida Console", "Courier New", monospace;
            }

            QProgressBar::chunk {
                border-radius: 20px;
                background-color: qlineargradient(spread:pad x1:0, x2:1, y1:0.511364, y2:0.523, stop:0 rgb(120, 200, 200), stop:1 white);
            }
        ''')
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.counter = 0
        self.end = 1000
        self.timer = QTimer()
        self.timer.timeout.connect(self.action)
        self.timer.start(10)

        myLayout = QVBoxLayout()
        self.setLayout(myLayout)

        self.frame = QFrame()
        myLayout.addWidget(self.frame)
        self.frame.autoFillBackground()

        self.title = QLabel(self.frame)
        self.title.setObjectName('Title')

        #better place icon and some quote here instead of title and description
        self.title.resize(self.width(), 300)
        self.title.move(0, 100)
        self.title.setText('Splash Screen')
        self.title.setAlignment(Qt.AlignCenter)

        self.description = QLabel(self.frame)
        self.description.resize(self.width(), 20)
        self.description.move(0, self.title.height())
        self.description.setObjectName('Desc')
        self.description.setText('<strong>by Fedorov Nikita</strong>')
        self.description.setAlignment(Qt.AlignCenter)

        self.loading = QProgressBar(self.frame)
        self.loading.resize(self.width() - 400, 40)
        self.loading.move(200, self.description.y() + 100)
        self.loading.setAlignment(Qt.AlignCenter)
        self.loading.setFormat('Loading...%p%')
        self.loading.setTextVisible(True)
        self.loading.setRange(0, self.end)
        self.loading.setValue(25)


    def action(self):
        self.loading.setValue(self.counter)

        self.counter += 1

        if self.counter >= self.end:
            self.timer.stop()
            self.close()