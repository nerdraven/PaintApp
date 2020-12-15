# Inspired by PyQt5 Creating Paint Application In 40 Minutes
#  https://www.youtube.com/watch?v=qEgyGyVA1ZQ

# NB If the menus do not work then click on another application ad then click back
# and they will work https://python-forum.io/Thread-Tkinter-macOS-Catalina-and-Python-menu-issue

# PyQt documentation links are prefixed with the word 'documentation' in the code below and can be accessed automatically
#  in PyCharm using the following technique https://www.jetbrains.com/help/pycharm/inline-documentation.html

from PyQt5.QtWidgets import QApplication, QMainWindow,QAction, QFileDialog
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon, QImage, QPainter, QPen, QPixmap
import sys
from PyQt5.QtCore import Qt, QPoint

class PaintingApplication(QtWidgets.QWidget): # documentation https://doc.qt.io/qt-5/qmainwindow.html
    '''
    Painting Application class
    '''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # set window title
        self.setWindowTitle("Paint Application")

        # set the windows dimensions
        top = 400
        left = 400
        width = 800
        height = 600
        self.setGeometry(top, left, width, height)

        #set the icon
        # windows version
        self.setWindowIcon(QIcon("./icons/paint-brush.png"))

        self.image = QImage(self.size(), QImage.Format_RGB32)
        self.image.fill(Qt.white)

        self.drawing = False
        self.brushSize = 3
        self.brushColor = Qt.black

        self.lastPoint = QPoint()

    def mousePressEvent(self, event):       # when the mouse is pressed, documentation: https://doc.qt.io/qt-5/qwidget.html#mousePressEvent
        if event.button() ==Qt.LeftButton:  # if the pressed button is the left button
            self.drawing = True             # enter drawing mode
            self.lastPoint = event.pos()    # save the location of the mouse press as the lastPoint
            print(self.lastPoint)           # print the lastPoint for debigging purposes

    def mouseMoveEvent(self, event):                        # when the mouse is moved, documenation: documentation: https://doc.qt.io/qt-5/qwidget.html#mouseMoveEvent
     if event.buttons() & Qt.LeftButton & self.drawing:     # if there was a press, and it was the left button and we are in drawing mode
            painter = QPainter(self.image)                  # object which allows drawing to take place on an image
            # allows the selection of brush colour, brish size, line type, cap type, join type. Images available here http://doc.qt.io/qt-5/qpen.html
            painter.setPen(QPen(self.brushColor, self.brushSize, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
            painter.drawLine(self.lastPoint, event.pos())   # draw a line from the point of the orginal press to the point to where the mouse was dragged to
            self.lastPoint= event.pos()                     # set the last point to refer to the point we have just moved to, this helps when drawing the next line segment
            self.update()                                   # call the update method of the widget which calls the paintEvent of this class

    def mouseReleaseEvent(self, event):                     # when the mouse is released, documentation: https://doc.qt.io/qt-5/qwidget.html#mouseReleaseEvent
        if event.button == Qt.LeftButton:                   # if the released button is the left button, documenation: https://doc.qt.io/qt-5/qt.html#MouseButton-enum ,
            self.drawing = False                            # exit drawing mode

    # paint events
    def paintEvent(self, event):
        # you should only create and use the QPainter object in this method, it should be a local variable
        canvasPainter = QPainter(self)                      # create a new QPainter object, documenation: https://doc.qt.io/qt-5/qpainter.html
        canvasPainter.drawImage(self.rect(), self.image, self.image.rect()) # draw the image , documentation: https://doc.qt.io/qt-5/qpainter.html#drawImage-1

    # resize event - this fuction is called
    def resizeEvent(self, event):
        self.image = self.image.scaled(self.width(), self.height())

    # slots
    def save(self):
        filePath, _ = QFileDialog.getSaveFileName(self, "Save Image","", "PNG(*.png);;JPG(*.jpg *.jpeg);;All Files (*.*)")
        if filePath =="": # if the file path is empty
            return # do nothing and return
        self.image.save(filePath) # save file image to the file path


    def clear(self):
        self.image.fill(Qt.white)   # fill the image with white, documentaiton: https://doc.qt.io/qt-5/qimage.html#fill-2
        self.update()               # call the update method of the widget which calls the paintEvent of this class

    def threepx(self):              # the brush size is set to 3
        self.brushSize = 3

    def fivepx(self):
        self.brushSize = 5

    def sevenpx(self):
        self.brushSize = 7

    def ninepx(self):
        self.brushSize = 9

    def black(self):                # the brush color is set to black
        self.brushColor = Qt.black

    def black(self):
        self.brushColor = Qt.black

    def red(self):
        self.brushColor = Qt.red

    def green(self):
        self.brushColor = Qt.green

    def yellow(self):
        self.brushColor = Qt.yellow

    # open a file
    def open(self):
        '''
        This is an additional function which is not part of the tutorial. It will allow you to:
         - open a file doalog box,
         - filter the list of files according to file extension
         - set the QImage of your application (self.image) to a scaled version of the file)
         - update the widget
        '''
        filePath, _ = QFileDialog.getOpenFileName(self, "Open Image", "",
                                                  "PNG(*.png);;JPG(*.jpg *.jpeg);;All Files (*.*)")
        if filePath == "":   # if not file is selected exit
            return
        with open(filePath, 'rb') as f: #open the file in binary mode for reading
            content = f.read() # read the file
        self.image.loadFromData(content) # load the data into the file
        width = self.width() # get the width of the current QImage in your application
        height = self.height() # get the height of the current QImage in your application
        self.image = self.image.scaled(width, height) # scale the image from file and put it in your QImage
        self.update() # call the update method of the widget which calls the paintEvent of this class


# this code will be executed if it is the main module but not if the module is imported
#  https://stackoverflow.com/questions/419163/what-does-if-name-main-do
if __name__=="__main__":
    app = QApplication(sys.argv)
    window = PaintingApplication()
    window.show()
    app.exec() # start the event loop running