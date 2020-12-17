import sys
import random
from pathlib import Path

from PyQt5 import QtCore, QtGui, QtWidgets


class PaintingApplication(QtWidgets.QWidget):

    def __init__(self, *args, **kwargs):

        # Initialization
        super().__init__(*args, **kwargs)

        # Image canvas
        self.filePath = ''
        self.drawing = False
        self.saved = False
        self.image = QtGui.QImage(self.size(), QtGui.QImage.Format_RGB32)
        self.image.fill(QtCore.Qt.white)

        self.brushSize = 1
        self.spray_size = 100
        self.lastPoint = QtCore.QPoint()

        self.brushColor = QtCore.Qt.black
        self.penStyle = QtCore.Qt.SolidLine
        self.capStyle = QtCore.Qt.RoundCap
        self.joinStyle = QtCore.Qt.RoundJoin

        self.statusBar_event = QtCore.pyqtSignal()
        self.titleBar_event = QtCore.pyqtSignal()
        self.mouseMoveEvent = self.pen_mouseMoveEvent

    def set_event_outlet(self, status_bar, title_bar):
        self.statusBar_event = status_bar
        self.titleBar_event = title_bar

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.drawing = True
            self.lastPoint = event.pos()

    def mouseReleaseEvent(self, event):
        if event.button == QtCore.Qt.LeftButton:
            self.drawing = False

    def paintEvent(self, event):
        canvas_painter = QtGui.QPainter(self)
        canvas_painter.drawImage(self.rect(), self.image, self.image.rect())

    def resizeEvent(self, event):
        self.image = self.image.scaled(self.width(), self.height())

    def save(self):
        if not self.saved:
            file_path, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Save Image", "",
                                                                 "PNG(*.png);;JPG(*.jpg *.jpeg);;All Files (*.*)")
            if file_path == "":
                return
            self.saved = True
            self.filePath = file_path
        else:
            file_path = self.filePath
        self.image.save(file_path)

        path = Path(file_path)
        file_path, _ = path.name.split('.')

        self.statusBar_event.emit('File Saved')
        self.titleBar_event.emit(f'{file_path} project')

    def clear(self):
        self.image.fill(QtCore.Qt.white)
        self.update()

    def open(self):
        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Open Image", "",
                                                             "PNG(*.png);;JPG(*.jpg *.jpeg);;All Files (*.*)")
        if file_path == "":
            return
        with open(file_path, 'rb') as f:
            content = f.read()
        self.image.loadFromData(content)
        width = self.width()
        height = self.height()
        self.image = self.image.scaled(width, height)
        self.update()

    def pen_mouseMoveEvent(self, event):
        if event.buttons() & QtCore.Qt.LeftButton & self.drawing:
            painter = QtGui.QPainter(self.image)
            painter.setPen(QtGui.QPen(self.brushColor, self.brushSize,
                                      self.penStyle, self.capStyle, self.joinStyle))
            painter.drawLine(self.lastPoint, event.pos())
            self.lastPoint = event.pos()
            self.update()

    def spray_mouseMoveEvent(self, e):
        painter = QtGui.QPainter(self.image)
        p = painter.pen()
        p.setWidth(1)
        p.setColor(self.brushColor)
        painter.setPen(p)
        for _ in range(self.spray_size):
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


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = PaintingApplication()
    window.show()
    app.exec()
