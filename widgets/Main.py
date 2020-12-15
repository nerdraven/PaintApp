from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5.QtWidgets import QAction
from PyQt5.QtGui import QIcon
from build.main import Ui_MainWindow
from widgets.Draw import PaintingApplication


class Main(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(Main, self).__init__(*args, **kwargs)
        self.setupUi(self)
        # self.paint_layout = PaintingApplication(self.centralwidget)
        self.additional_widgets()
        self.setup_drawing()

    def setup_drawing(self):
        self.canDraw        = False
        self.brushSize      = 2
        self.brushColor     = QtCore.Qt.black
        self.lastPoint      = QtCore.QPoint()

    def save(self):
        filePath, _         = QtWidgets.QFileDialog.getSaveFileName(self, "Save Image","", 
                                "PNG(*.png);;JPG(*.jpg *.jpeg);;All Files (*.*)")
        if filePath == "":
            return
        self.image.save(filePath)

    def clear(self):
        self.image.fill(QtCore.Qt.white)
        self.update()

    def additional_widgets(self):
        label               = QtWidgets.QLabel('Brush Thickness')
        self.main_toolBar.addWidget(label)

        self.main_toolBar.addSeparator()

        self.horizontal_slider    = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.main_toolBar.addWidget(self.horizontal_slider)

        undo_action = QAction(self)
        undo_action.setObjectName("undo_action")
        self.main_toolBar.addAction(undo_action)
        undo_action.setText('Undo')

        redo_action = QAction(self)
        redo_action.setObjectName("redo_action")
        self.main_toolBar.addAction(redo_action)
        redo_action.setText('Redo')


    def contextMenuEvent(self, event, *args, **kwargs):
        contextMenu         = QtWidgets.QMenu(self)

        save_action         = contextMenu.addAction('&Save')
        duplicate_action    = contextMenu.addAction('&Duplicate')
        settings_action     = contextMenu.addAction('S&ettings')
        full_screen_action  = contextMenu.addAction('&Full Screen')

        action = contextMenu.exec_(self.mapToGlobal(event.pos()))
        if action == save_action:
            self.close()