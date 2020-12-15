from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5.QtWidgets import QAction
from PyQt5.QtGui import QIcon
from build.main import Ui_MainWindow
from app.Draw import PaintingApplication

class Join_Style:
    Bevel = QtCore.Qt.BevelJoin
    Miter = QtCore.Qt.MiterJoin
    Round = QtCore.Qt.RoundJoin

class Line_Style:
    Solid  = QtCore.Qt.SolidLine
    Dotted = QtCore.Qt.DotLine
    Dashed = QtCore.Qt.DashLine
    DashDot = QtCore.Qt.DashDotLine
    DashDotDot = QtCore.Qt.DashDotDotLine

class Cap_Style:
    Flat    = QtCore.Qt.FlatCap
    Square  = QtCore.Qt.SquareCap
    Round   = QtCore.Qt.RoundCap


class Main(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(Main, self).__init__(*args, **kwargs)
        self.setupUi(self)
        # self.paint_layout = PaintingApplication(self.centralwidget)
        self.additional_widgets()
        self.setup_drawing()

    def setup_drawing(self):
        self.canDraw    = False
        self.brushSize  = 2
        self.brushColor = QtCore.Qt.black
        self.lastPoint  = QtCore.QPoint()

    def save(self):
        filePath, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Save Image","", 
                          "PNG(*.png);;JPG(*.jpg *.jpeg);;All Files (*.*)")
        if filePath == "":
            return
        self.image.save(filePath)

    def clear(self):
        self.image.fill(QtCore.Qt.white)
        self.update()

    def additional_widgets(self):
        self.label      = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.main_toolBar.addWidget(self.label)

    def contextMenuEvent(self, event, *args, **kwargs):
        contextMenu = QtWidgets.QMenu(self)

        newAction = contextMenu.addAction('&About')
        quitAction = contextMenu.addAction('&Quit')

        action = contextMenu.exec_(self.mapToGlobal(event.pos()))
        if action == quitAction:
            self.close()