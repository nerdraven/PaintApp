from PyQt5 import QtCore, QtWidgets, QtGui
from build.utils import Ui_Dialog
from build.utils import Ui_Form


class HelpUI(QtWidgets.QWidget, Ui_Form):
    def __init__(self, *args, **kwargs):
        super(HelpUI, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.about_btn.clicked.connect(lambda x: self.do('about'))
        self.features_btn.clicked.connect(lambda x: self.do('features'))

    def do(self, button: str):
        page = ''
        page = self.load_page("pages/{}.html".format(button.capitalize()))
        self.main_page.setText(page)

    def load_page(self, page):
        """ This will load the required HTML to the page """
        page = open(page, 'r')
        return page.read()


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