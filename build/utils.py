# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setObjectName("widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.heading = QtWidgets.QLabel(self.widget)
        self.heading.setObjectName("heading")
        self.verticalLayout_2.addWidget(self.heading)
        self.Developers = QtWidgets.QLabel(self.widget)
        self.Developers.setObjectName("Developers")
        self.verticalLayout_2.addWidget(self.Developers)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.heading.setText(_translate("Dialog", "<html><head/><body><p align=\"center\">Course Code: BSCO - No/Dub/ft</p></body></html>"))
        self.Developers.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Moses Akinwale</span></p><p align=\"center\">Griffiti College</p></body></html>"))


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(613, 457)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setObjectName("widget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout.addWidget(self.widget)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.jfk = QtWidgets.QWidget(Form)
        self.jfk.setMinimumSize(QtCore.QSize(150, 0))
        self.jfk.setObjectName("jfk")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.jfk)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(20, 50, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_3.addItem(spacerItem)
        self.features_btn = QtWidgets.QPushButton(self.jfk)
        self.features_btn.setObjectName("features_btn")
        self.verticalLayout_3.addWidget(self.features_btn)
        self.about_btn = QtWidgets.QPushButton(self.jfk)
        self.about_btn.setObjectName("about_btn")
        self.verticalLayout_3.addWidget(self.about_btn)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.verticalLayout_5.addLayout(self.verticalLayout_3)
        self.horizontalLayout_2.addWidget(self.jfk)
        self.main_page = QtWidgets.QTextBrowser(Form)
        self.main_page.setObjectName("main_page")
        self.horizontalLayout_2.addWidget(self.main_page)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.features_btn.setText(_translate("Form", "Features"))
        self.about_btn.setText(_translate("Form", "About"))
        self.main_page.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Product Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-weight:600;\">About</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">This is a simple paint application.</p></body></html>"))


class Ui_colorpicker(object):
    def setupUi(self, colorpicker):
        colorpicker.setObjectName("colorpicker")
        colorpicker.resize(302, 100)
        colorpicker.setMinimumSize(QtCore.QSize(0, 100))
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(colorpicker)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.green = QtWidgets.QWidget(colorpicker)
        self.green.setStyleSheet("background-color: rgb(85, 255, 0);")
        self.green.setObjectName("green")
        self.gridLayout.addWidget(self.green, 0, 2, 1, 1)
        self.yellow = QtWidgets.QWidget(colorpicker)
        self.yellow.setStyleSheet("background-color: rgb(255, 119, 51);")
        self.yellow.setObjectName("yellow")
        self.gridLayout.addWidget(self.yellow, 0, 3, 1, 1)
        self.red = QtWidgets.QWidget(colorpicker)
        self.red.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.red.setObjectName("red")
        self.gridLayout.addWidget(self.red, 0, 0, 1, 1)
        self.black = QtWidgets.QLabel(colorpicker)
        self.black.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.black.setObjectName("black")
        self.gridLayout.addWidget(self.black, 0, 4, 1, 1)
        self.blue = QtWidgets.QWidget(colorpicker)
        self.blue.setStyleSheet("background-color: rgb(0, 0, 255);")
        self.blue.setObjectName("blue")
        self.gridLayout.addWidget(self.blue, 0, 1, 1, 1)
        self.more_color = QtWidgets.QLabel(colorpicker)
        self.more_color.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 0, 0, 255), stop:1 rgba(0, 0, 255, 255));")
        self.more_color.setObjectName("more_color")
        self.gridLayout.addWidget(self.more_color, 1, 4, 1, 1)
        self.label_2 = QtWidgets.QLabel(colorpicker)
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 6);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 3, 1, 1)
        self.label_3 = QtWidgets.QLabel(colorpicker)
        self.label_3.setStyleSheet("background-color: rgb(255, 0, 127);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(colorpicker)
        self.label_4.setStyleSheet("background-color: rgb(255, 85, 255);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 1, 1, 1)
        self.rgb_85_170_255 = QtWidgets.QLabel(colorpicker)
        self.rgb_85_170_255.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.rgb_85_170_255.setText("")
        self.rgb_85_170_255.setObjectName("rgb_85_170_255")
        self.gridLayout.addWidget(self.rgb_85_170_255, 1, 0, 1, 1)
        self.horizontalLayout_2.addLayout(self.gridLayout)

        self.retranslateUi(colorpicker)
        QtCore.QMetaObject.connectSlotsByName(colorpicker)

    def retranslateUi(self, colorpicker):
        _translate = QtCore.QCoreApplication.translate
        colorpicker.setWindowTitle(_translate("colorpicker", "Form"))
        self.black.setText(_translate("colorpicker", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.more_color.setText(_translate("colorpicker", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">+</span></p></body></html>"))