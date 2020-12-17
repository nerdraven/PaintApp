import sys
import random
from pathlib import Path

from PyQt5 import QtCore, QtGui, QtWidgets


SPRAY_PARTICLES = 100

class PaintingApplication(QtWidgets.QWidget):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.image = QtGui.QImage(self.size(), QtGui.QImage.Format_RGB32)
        self.image.fill(QtCore.Qt.white)
        self.setCursor(QtCore.Qt.CrossCursor)

        self.drawing = False
        self.brushSize = 1
        self.brushColor = QtCore.Qt.black
        self.lastPoint = QtCore.QPoint()

        self.penStyle = QtCore.Qt.SolidLine
        self.capStyle = QtCore.Qt.RoundCap
        self.joinStyle = QtCore.Qt.RoundJoin

        self.saved = False
        self.filePath = ''

        self.mouseMoveEvent = self.pen_mouseMoveEvent

    def set_event_outlet(self, status_bar, title_bar):
        self.statusBar_event = status_bar
        self.titleBar_event = title_bar

    def mousePressEvent(self, event):
        if event.button() ==QtCore.Qt.LeftButton:
            self.drawing = True
            self.lastPoint = event.pos()

    def pen_mouseMoveEvent(self, event):
     if event.buttons() & QtCore.Qt.LeftButton & self.drawing:
            painter = QtGui.QPainter(self.image)
            painter.setPen(QtGui.QPen(self.brushColor, self.brushSize, 
                            self.penStyle, self.capStyle, self.joinStyle))
            painter.drawLine(self.lastPoint, event.pos())
            self.lastPoint= event.pos()
            self.update()

    def spray_mouseMoveEvent(self, e):
        painter = QtGui.QPainter(self.image)
        p = painter.pen()
        p.setWidth(1)
        p.setColor(self.brushColor)
        painter.setPen(p)
        for _ in range(SPRAY_PARTICLES):
            xo = random.gauss(0, self.brushSize)
            yo = random.gauss(0, self.brushSize)
            painter.drawPoint(e.x() + xo, e.y() + yo)
        self.update()

    def eraser_mouseMoveEvent(self, e):
        painter = QtGui.QPainter(self.image)
        p = painter.pen()
        p.setWidth(self.brushSize)
        p.setColor(QtCore.Qt.white)
        painter.setPen(p)
        p.setCapStyle(QtCore.Qt.SquareCap)
        painter.drawPoint(e.x(), e.y())
        self.update()

    # def text_mouseMoveEvent(self):
    #     painter = QtGui.QPainter(self.image)
    #     # p = painter.pen()
    #     # p.setWidth(self.brushSize)
    #     # p.setColor(QtCore.Qt.white)
    #     # painter.setPen(p)
    #     # p.setCapStyle(QtCore.Qt.SquareCap)
    #     # painter.drawPoint(e.x(), e.y())
    #     # self.update()

    def mouseReleaseEvent(self, event):
        if event.button == QtCore.Qt.LeftButton:
            self.drawing = False

    def paintEvent(self, event):
        canvasPainter = QtGui.QPainter(self)
        canvasPainter.drawImage(self.rect(), self.image, self.image.rect())

    def resizeEvent(self, event):
        self.image = self.image.scaled(self.width(), self.height())

    def save(self):
        filePath = ''
        if not self.saved:
            filePath, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Save Image","", 
                                    "PNG(*.png);;JPG(*.jpg *.jpeg);;All Files (*.*)")
            if filePath == "":
                return
            self.saved = True
            self.filePath = filePath
        else:
            filePath = self.filePath
        self.image.save(filePath)

        path = Path(filePath)
        filePath, _ = path.name.split('.')

        self.statusBar_event.emit('File Saved')
        self.titleBar_event.emit(f'{filePath} project')

    def clear(self):
        self.image.fill(QtCore.Qt.white)
        self.update()

    def open(self):
        filePath, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Open Image", "",
                                                  "PNG(*.png);;JPG(*.jpg *.jpeg);;All Files (*.*)")
        if filePath == "":
            return
        with open(filePath, 'rb') as f:
            content = f.read()
        self.image.loadFromData(content)
        width = self.width()
        height = self.height()
        self.image = self.image.scaled(width, height)
        self.update()


if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = PaintingApplication()
    window.show()
    app.exec()