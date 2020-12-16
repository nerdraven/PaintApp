from PyQt5 import QtCore, QtGui, QtWidgets
from build.colorpicker import Ui_colorpicker

class ColorPicker(QtWidgets.QWidget, Ui_colorpicker):

    def __init__(self, width, height, *args, **kwargs):
        super(ColorPicker, self).__init__(*args, **kwargs)
        self.setupUi(self)
    
    def do(self, event: QtGui.QMouseEvent):
        print(event.button() == QtCore.Qt.LeftButton)
        print('Hello')
        

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = ColorPicker()
    window.show()
    app.exec_()