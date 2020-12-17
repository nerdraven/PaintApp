from PyQt5 import QtCore, QtGui, QtWidgets
from build.colorpicker import Ui_colorpicker

class ColorPicker(QtWidgets.QWidget, Ui_colorpicker):

    def __init__(self, color_signal, *args, **kwargs):
        super(ColorPicker, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.color_signal = color_signal
        self.more_color.mousePressEvent = self.man

    def man(self, event: QtGui.QMouseEvent):
        color = QtWidgets.QColorDialog.getColor()
        self.color_signal.emit(color)

    
    def do(self, event: QtGui.QMouseEvent):
        print(event.button() == QtCore.Qt.LeftButton)
        print('Hello')
        

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = ColorPicker()
    window.show()
    app.exec_()