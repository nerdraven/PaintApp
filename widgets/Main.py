from functools import partialmethod, partial

from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5.QtWidgets import QAction
from PyQt5.QtGui import QIcon
from build.main import Ui_MainWindow
from widgets.Draw import PaintingApplication
from widgets.Colorpicker import ColorPicker


class Main(Ui_MainWindow, QtWidgets.QMainWindow):

    statusSignal    = QtCore.pyqtSignal(str)
    titleSignal     = QtCore.pyqtSignal(str)

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
        self.colorPicker = ColorPicker(self.width(), self.height())
        self.side_bar.layout().addWidget(self.colorPicker)
        self.colorPicker.setFixedHeight(30)
        self.paint_layout.set_event_outlet(self.statusSignal, self.titleSignal)
        self.titleSignal.connect(self.windowTitle_event)

        self.solid_line_radio.toggle()
        self.round_join_radio.toggle()
        self.radio_cap_radio.toggle()

        self.colorPicker.yellow.mousePressEvent = partial(self.set_penColor, color='yellow')
        self.colorPicker.red.mousePressEvent    = partial(self.set_penColor, color='red')
        self.colorPicker.blue.mousePressEvent   = partial(self.set_penColor, color='blue')
        self.colorPicker.green.mousePressEvent  = partial(self.set_penColor, color='green')
        
        self.horizontal_slider.setValue(1)

        self.toolbar_action_new.triggered.connect(self.create_new_window)
        self.toolbar_action_full_screen.triggered.connect(self.toogle_full_screen)
        self.toolbar_action_clear.triggered.connect(self.paint_layout.clear)

        self.action_spray_paint.triggered.connect(lambda x: self.set_brush('spray'))
        self.toolbar_action_brush.triggered.connect(lambda x: self.set_brush('pen'))
        self.action_eraser.triggered.connect(lambda x: self.set_brush('eraser'))

    def set_penColor(self, event, color='black'):
        self.paint_layout.brushColor = getattr(QtCore.Qt, color)
        self.statusSignal.emit('Brush now in {} color'.format(color.title()))
    
    def set_brush(self, brush):
        if brush == 'spray':
            self.paint_layout.mouseMoveEvent = self.paint_layout.spray_mouseMoveEvent
        elif brush == 'pen':
            self.paint_layout.mouseMoveEvent = self.paint_layout.pen_mouseMoveEvent
        elif brush == 'eraser':
            self.paint_layout.mouseMoveEvent = self.paint_layout.eraser_mouseMoveEvent


    def additional_widgets(self):
        label = QtWidgets.QLabel('Brush Thickness')
        self.main_toolBar.addWidget(label)
        self.main_toolBar.addSeparator()
        self.horizontal_slider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.main_toolBar.addWidget(self.horizontal_slider)
        self.horizontal_slider.valueChanged.connect(self.changeBrushSize)

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

    @QtCore.pyqtSlot(str)
    def windowTitle_event(self, mesg):
        title = self.windowTitle()
        self.setWindowTitle(f'{mesg} | {title}')
    
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
        full_screen_action  = contextMenu.addAction('&Full Screen')

        action = contextMenu.exec_(self.mapToGlobal(event.pos()))
        if action == save_action:
            self.paint_layout.save()
        elif action == full_screen_action:
            self.toogle_full_screen()