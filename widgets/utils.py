from PyQt5 import QtCore, QtWidgets, QtGui
from build.utils import Ui_Dialog
from build.utils import Ui_Form


class HelpUI(QtWidgets.QWidget, Ui_Form):
    def __init__(self, *args, **kwargs):
        super(HelpUI, self).__init__(*args, **kwargs)
        self.setupUi(self)


class AboutUI(QtWidgets.QWidget, Ui_Dialog):
    def __init__(self, *args, **kwargs):
        super(AboutUI, self).__init__(*args, **kwargs)
        self.setupUi(self)


# This is for debugging usage
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window1 = AboutUI()
    window2 = HelpUI()
    window1.show()
    window2.show()
    app.exec_()