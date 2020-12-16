from PyQt5.QtWidgets import QApplication, QMainWindow,QAction, QFileDialog
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon, QImage, QPainter, QPen, QPixmap
import sys
from PyQt5.QtCore import Qt, QPoint
from pathlib import Path

class PaintingApplication(QtWidgets.QWidget):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.image = QImage(self.size(), QImage.Format_RGB32)
        self.image.fill(Qt.white)

        self.drawing = False
        self.brushSize = 1
        self.brushColor = Qt.black
        self.lastPoint = QPoint()

        self.penStyle = Qt.SolidLine
        self.capStyle = Qt.RoundCap
        self.joinStyle = Qt.RoundJoin

        self.saved = False
        self.filePath = ''

    def set_event_outlet(self, status_bar, title_bar):
        self.statusBar_event = status_bar
        self.titleBar_event = title_bar

    def mousePressEvent(self, event):
        if event.button() ==Qt.LeftButton:
            self.drawing = True
            self.lastPoint = event.pos()
            print(self.lastPoint)

    def mouseMoveEvent(self, event):
     if event.buttons() & Qt.LeftButton & self.drawing:
            painter = QPainter(self.image)
            painter.setPen(QPen(self.brushColor, self.brushSize, 
                            self.penStyle, self.capStyle, self.joinStyle))
            painter.drawLine(self.lastPoint, event.pos())
            self.lastPoint= event.pos()
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button == Qt.LeftButton:
            self.drawing = False

    def paintEvent(self, event):
        canvasPainter = QPainter(self)
        canvasPainter.drawImage(self.rect(), self.image, self.image.rect())

    def resizeEvent(self, event):
        self.image = self.image.scaled(self.width(), self.height())

    def save(self):
        filePath = ''
        if not self.saved:
            filePath, _ = QFileDialog.getSaveFileName(self, "Save Image","", 
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
        self.image.fill(Qt.white)
        self.update()

    def open(self):
        filePath, _ = QFileDialog.getOpenFileName(self, "Open Image", "",
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
    app = QApplication(sys.argv)
    window = PaintingApplication()
    window.show()
    app.exec()