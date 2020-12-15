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
        self.setWindowTitle('Paint App')
        self.maximized = False
        self.additional_widgets()
        self.setup_menubar()

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

    def do(self, *args, **kwargs):
        print('JJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJ')
        print(args)
        print(kwargs)
    
    def new_window(self):
        window = Main(self)
        window.show()

    def zoom(self, op):
        width = self.width()
        height = self.height()
        if op == '+':
            self.setFixedWidth(width + 10)
            self.setFixedHeight(height + 10)
        else:
            self.setFixedWidth(width - 10)
            self.setFixedHeight(height - 10)
    
    def toogle_full_screen(self):
        if not self.maximized:
            self.showFullScreen()
            self.maximized = True
        else:
            self.showNormal()
            self.maximized = False

    def setup_menubar(self):
        # File
        self.action_new.triggered.connect(self.new_window)
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