from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore
from app.Main import Main as MainUi
from app.Draw import PaintingApplication


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainUi()
    window.show()
    app.exec_()