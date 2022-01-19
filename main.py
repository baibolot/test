from PyQt5.QtWidgets import QApplication
from test import MainWindow
import sys



def main():
    """Main"""
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
