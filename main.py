from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore
from build.main import Ui_MainWindow

class Main(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(Main, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.label = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.main_toolBar.addWidget(self.label)

    def contextMenuEvent(self, event, *args, **kwargs):
        contextMenu = QtWidgets.QMenu(self)

        newAction = contextMenu.addAction('&About')
        quitAction = contextMenu.addAction('&Quit')

        action = contextMenu.exec_(self.mapToGlobal(event.pos()))

        if action == quitAction:
            self.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = Main()
    window.show()
    app.exec_()