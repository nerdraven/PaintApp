from functools import partial

from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore

from build.main import Ui_MainWindow

from widgets.colorpicker import ColorPicker
from widgets.utils import AboutUI
from widgets.utils import HelpUI


class Main(Ui_MainWindow, QtWidgets.QMainWindow):

    # Core custom signals
    statusSignal = QtCore.pyqtSignal(str)
    titleSignal = QtCore.pyqtSignal(str)
    colorSignal = QtCore.pyqtSignal(QtGui.QColor)

    def __init__(self, *args, **kwargs):

        # Initialize all widgets
        super(Main, self).__init__(*args, **kwargs)
        self.setupUi(self)  # Connect all widgets to the main window
        self.setWindowTitle('Paint App')
        self.maximized = False  # To check if the window is in full screen

        # Additional Widgets
        # Here I am connecting all the widgets not defined in the build package

        # Color picker
        self.colorPicker = ColorPicker(self.colorSignal)
        self.colorPicker.setMaximumHeight(70)
        self.side_bar.layout().addWidget(self.colorPicker)

        # Brush thickness
        label = QtWidgets.QLabel('Brush Thickness')
        self.main_toolBar.addWidget(label)

        self.main_toolBar.addSeparator()

        self.brush_thickness_slider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.brush_thickness_slider.setCursor(QtCore.Qt.PointingHandCursor)
        self.brush_thickness_slider.valueChanged.connect(self.change_brush_size)
        self.main_toolBar.addWidget(self.brush_thickness_slider)

        # Other Program windows
        self.aboutUi = AboutUI()    # This is the About page
        self.helpUi = HelpUI()      # This is for the Help page

        # Toggle on the default buttons
        self.solid_line_radio.toggle()
        self.round_join_radio.toggle()
        self.round_cap_radio.toggle()

        # Connect all the custom Signals
        self.titleSignal.connect(self.window_title_event)
        self.colorSignal.connect(self.change_brush_color)
        self.statusSignal.connect(self.status_bar_event)

        # Connect signals for paint_layout
        # This way the paint layout could communicate with the status and title bar
        self.paint_layout.set_event_outlet(self.statusSignal, self.titleSignal)

        # Connect actions
        # This consists of all the actions from the menu, context,
        self.action_fullScreen.triggered.connect(self.toggle_full_screen)
        self.action_clear.triggered.connect(self.paint_layout.clear)
        self.action_exit.triggered.connect(self.close)

        self.action_sprayPaint.triggered.connect(lambda x: self.set_brush_type('spray'))
        self.action_brush.triggered.connect(lambda x: self.set_brush_type('pen'))
        self.action_eraser.triggered.connect(lambda x: self.set_brush_type('eraser'))

        # Here I modified the set_pen_color method for their values same thing like lambda
        self.colorPicker.yellow.mousePressEvent = partial(self.set_pen_color, color='yellow')
        self.colorPicker.red.mousePressEvent = partial(self.set_pen_color, color='red')
        self.colorPicker.blue.mousePressEvent = partial(self.set_pen_color, color='blue')
        self.colorPicker.green.mousePressEvent = partial(self.set_pen_color, color='green')

        # Connect menu bar
        # File
        self.action_new.triggered.connect(self.create_new_window)
        self.action_open.triggered.connect(self.paint_layout.open)
        self.action_save.triggered.connect(self.paint_layout.save)
        self.action_saveAs.triggered.connect(self.paint_layout.saveAs)

        # View
        self.action_zoomIn.triggered.connect(lambda x: self.zoom('+'))
        self.action_zoomOut.triggered.connect(lambda x: self.zoom('-'))

        # Help
        self.action_help.triggered.connect(self.helpUi.show)
        self.action_about.triggered.connect(self.aboutUi.show)

        # Setup side bar
        # Cap Style
        self.flat_cap_radio.toggled.connect(lambda x: self.set_capStyle('flat'))
        self.round_cap_radio.toggled.connect(lambda x: self.set_capStyle('round'))
        self.square_cap_radio.toggled.connect(lambda x: self.set_capStyle('square'))

        # Line Style
        self.dotted_line_radio.toggled.connect(lambda x: self.set_lineStyle('dotted'))
        self.dashed_line_radio.toggled.connect(lambda x: self.set_lineStyle('dashed'))
        self.solid_line_radio.toggled.connect(lambda x: self.set_lineStyle('solid'))
        self.dash_dot_line_radio.toggled.connect(lambda x: self.set_lineStyle('dashdot'))
        self.dash_dot_dot_line_radio.toggled.connect(lambda x: self.set_lineStyle('dashdotdot'))

        # Join Style
        self.miter_join_radio.toggled.connect(lambda x: self.set_joinStyle('miter'))
        self.bevel_join_radio.toggled.connect(lambda x: self.set_joinStyle('bevel'))
        self.round_join_radio.toggled.connect(lambda x: self.set_joinStyle('round'))

        # Miscellaneous
        self.statusSignal.emit('Hello World')
        self.brush_thickness_slider.setValue(self.paint_layout.brushSize)

    # Slots to the custom signals
    @QtCore.pyqtSlot(int)
    def change_brush_size(self, size):
        self.paint_layout.brushSize = size

    @QtCore.pyqtSlot(str)
    def status_bar_event(self, message: str):
        self.statusbar.showMessage(message)

    @QtCore.pyqtSlot(str)
    def window_title_event(self, message: str):
        title = self.windowTitle()
        self.setWindowTitle(message.format(title=title))

    def contextMenuEvent(self, event, *args, **kwargs):
        """ For all Right click events """
        context_menu = QtWidgets.QMenu(self)

        save_action = context_menu.addAction('&Save')
        full_screen_action = context_menu.addAction('&Full Screen')
        action = context_menu.exec_(self.mapToGlobal(event.pos()))
        if action == save_action:
            self.paint_layout.save()
        elif action == full_screen_action:
            self.toggle_full_screen()

    # Controllers
    def set_pen_color(self, args, color='black'):
        self.paint_layout.brushColor = getattr(QtCore.Qt, color)
        self.statusSignal.emit('Brush now in {} color'.format(color.title()))

    def set_brush_type(self, brush):
        """ Change the brush type by changing the mouseMoveEvent of the paint layout """
        message = ''
        if brush == 'spray':
            self.paint_layout.mouseMoveEvent = self.paint_layout.spray_mouseMoveEvent
            self.brush_thickness_slider.setValue(20)
            self.paint_layout.brushSize = 20
            message = 'Brush is now in Spray mode'
        elif brush == 'pen':
            self.paint_layout.mouseMoveEvent = self.paint_layout.pen_mouseMoveEvent
            message = 'Brush is now in Pen mode'
        elif brush == 'eraser':
            self.paint_layout.mouseMoveEvent = self.paint_layout.eraser_mouseMoveEvent
            message = 'Brush is now in Eraser mode'
        self.statusSignal.emit(message)

    def set_capStyle(self, val):
        values = {
            'round': QtCore.Qt.RoundCap,
            'square': QtCore.Qt.SquareCap,
            'flat': QtCore.Qt.FlatCap
        }
        self.paint_layout.capStyle = values.pop(val)
        self.statusSignal.emit('Changed the cap style to {} cap'.format(val))

    def set_lineStyle(self, val):
        values = {
            'solid': QtCore.Qt.SolidLine,
            'dotted': QtCore.Qt.DotLine,
            'dashed': QtCore.Qt.DashLine,
            'dashdot': QtCore.Qt.DashDotDotLine,
            'dashdotdot': QtCore.Qt.DashDotDotLine
        }
        self.paint_layout.penStyle = values.pop(val)
        self.statusSignal.emit('Changed the line style to {}'.format(val))

    def set_joinStyle(self, val):
        values = {
            'bevel': QtCore.Qt.BevelJoin,
            'miter': QtCore.Qt.MiterJoin,
            'round': QtCore.Qt.RoundJoin
        }
        self.paint_layout.joinStyle = values.pop(val)
        self.statusSignal.emit('Changed the join style to {} join'.format(val))

    def change_brush_color(self, color):
        self.paint_layout.brushColor = color

    def toggle_full_screen(self):
        if not self.maximized:
            self.showFullScreen()
            self.maximized = True
        else:
            self.showNormal()
            self.maximized = False

    def create_new_window(self):
        """ Start a new Window with a clean image """
        window = Main(self)
        window.show()

    def zoom(self, op):
        """ Change window size and canvas scale """
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
