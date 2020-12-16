from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5.QtWidgets import QAction
from PyQt5.QtGui import QIcon
from build.main import Ui_MainWindow
from widgets.Draw import PaintingApplication


class Main(QtWidgets.QMainWindow, Ui_MainWindow):

    statusSignal    = QtCore.pyqtSignal(str)

    def __init__(self, *args, **kwargs):
        super(Main, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.setWindowTitle('Paint App')
        self.maximized = False
        self.statusSignal.connect(self.statusBar_event)
        self.statusSignal.emit('Hello World')
        self.additional_widgets()
        self.setup_menubar()
        self.setup_sideBar()
        
        self.horizontal_slider.setValue(1)

        self.toolbar_action_new.triggered.connect(self.create_new_window)
        self.toolbar_action_full_screen.triggered.connect(self.toogle_full_screen)
        self.toolbar_action_clear.triggered.connect(self.paint_layout.clear)
        # self.setup_statusBar()

    def additional_widgets(self):
        label = QtWidgets.QLabel('Brush Thickness')
        self.main_toolBar.addWidget(label)
        self.main_toolBar.addSeparator()
        self.horizontal_slider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.main_toolBar.addWidget(self.horizontal_slider)
        self.horizontal_slider.valueChanged.connect(self.changeBrushSize)

        undo_action = QAction(self)
        undo_action.setObjectName("undo_action")
        self.main_toolBar.addAction(undo_action)
        undo_action.setText('Undo')
        # undo_action.triggered.connect() # TODO

        redo_action = QAction(self)
        redo_action.setObjectName("redo_action")
        self.main_toolBar.addAction(redo_action)
        redo_action.setText('Redo')
        # redo_action.triggered.connect() # TODO
    
    @QtCore.pyqtSlot(int)
    def changeBrushSize(self, size):
        self.paint_layout.brushSize = size
    
    def toogle_full_screen(self):
        if not self.maximized:
            self.showFullScreen()
            self.maximized = True
        else:
            self.showNormal()
            self.maximized = False

    def do(self, *args, **kwargs):
        print('JJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJ')
        print(args)
        print(kwargs)

    @QtCore.pyqtSlot(str)
    def statusBar_event(self, mesg):
        self.statusbar.showMessage(mesg)
    
    def create_new_window(self):
        window = Main(self)
        window.show()

    def zoom(self, op):
        width = self.width()
        height = self.height()
        if op == '+':
            self.setFixedWidth(width + 10)
            self.setFixedHeight(height + 10)
            self.statusSignal.emit('Zoomed In')
        else:
            self.setFixedWidth(width - 10)
            self.setFixedHeight(height - 10)
            self.statusSignal.emit('Zoomed Out')

    def set_capStyle(self, val):
        values = {
                'round': QtCore.Qt.RoundCap,
                'square': QtCore.Qt.SquareCap,
                'flat': QtCore.Qt.FlatCap
            }
        self.paint_layout.capStyle = values.pop(val)
    
    def set_lineStyle(self, val):
        values = {
            'solid': QtCore.Qt.SolidLine,
            'dotted': QtCore.Qt.DotLine,
            'dashed': QtCore.Qt.DashLine,
            'dashdot': QtCore.Qt.DashDotDotLine,
            'dashdotdot': QtCore.Qt.DashDotDotLine
        }
        self.paint_layout.penStyle = values.pop(val)
    
    def set_joinStyle(self, val):
        values = {
            'bevel': QtCore.Qt.BevelJoin,
            'miter': QtCore.Qt.MiterJoin,
            'round': QtCore.Qt.RoundJoin
        }
        self.paint_layout.joinStyle = values.pop(val)
    
    def setup_sideBar(self):
        # Cap Style
        self.flat_cap_radio.toggled.connect(lambda x: self.set_capStyle('flat'))
        self.radio_cap_radio.toggled.connect(lambda x: self.set_capStyle('round'))
        self.square_cap_radio.toggled.connect(lambda x: self.set_capStyle('square'))

        # Line Style
        self.dotted_line_radio.toggled.connect(lambda x: self.set_lineStyle('dotted'))
        self.dashed_line_radio.toggled.connect(lambda x: self.set_lineStyle('dashed'))
        self.solid_line_radio.toggled.connect(lambda x: self.set_lineStyle('solid'))

        # Join Style
        self.miter_join_radio.toggled.connect(lambda x: self.set_joinStyle('miter'))
        self.bevel_join_radio.toggled.connect(lambda x: self.set_joinStyle('bevel'))
        self.round_join_radio.toggled.connect(lambda x: self.set_joinStyle('round'))


    def setup_menubar(self):
        # File
        self.action_new.triggered.connect(self.create_new_window)
        self.action_open.triggered.connect(self.paint_layout.open)
        self.action_save.triggered.connect(self.paint_layout.save)
        self.action_print.triggered.connect(self.do)      # TODO

        # View
        self.action_zoom_In.triggered.connect(lambda x: self.zoom('+'))
        self.action_zoom_out.triggered.connect(lambda x: self.zoom('-'))
        self.action_full_screen.triggered.connect(self.toogle_full_screen)

        # Help
        self.action_help.triggered.connect(self.do)  # TODO
        self.action_about.triggered.connect(self.do) # TODO


    def contextMenuEvent(self, event, *args, **kwargs):
        contextMenu         = QtWidgets.QMenu(self)

        save_action         = contextMenu.addAction('&Save')
        duplicate_action    = contextMenu.addAction('&Duplicate')
        settings_action     = contextMenu.addAction('S&ettings')
        full_screen_action  = contextMenu.addAction('&Full Screen')

        action = contextMenu.exec_(self.mapToGlobal(event.pos()))
        if action == save_action:
            self.close()