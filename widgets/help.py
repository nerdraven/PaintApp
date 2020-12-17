from PyQt5 import QtCore, QtGui, QtWidgets
from build.help import Ui_Form

class HelpUI(QtWidgets.QWidget, Ui_Form):

    def __init__(self, *args, **kwargs):
        super(HelpUI, self).__init__(*args, **kwargs)
        self.setupUi(self)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = HelpUI()
    window.show()
    app.exec_()

