import sys
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore
from widgets.Main import Main as MainUi
from widgets.Draw import PaintingApplication

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainUi()
    window.show()
    sys.exit(app.exec_())