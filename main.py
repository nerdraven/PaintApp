from PyQt5.QtWidgets import QApplication, QMainWindow
from build.main import Ui_MainWindow

class Main(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(Main, self).__init__(*args, **kwargs)
        self.setupUi(self)


if __name__ == "__main__":
    app = QApplication([])
    window = Main()
    window.show()
    app.exec_()