from PyQt5 import QtCore, QtWidgets, QtGui
from build.about import Ui_Dialog

class AboutUI(QtWidgets.QWidget, Ui_Dialog):

    def __init__(self, *args, **kwargs):
        super(AboutUI, self).__init__(*args, **kwargs)
        self.setupUi(self)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = AboutUI()
    window.show()
    app.exec_()