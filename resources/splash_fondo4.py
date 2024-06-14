# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'splash_fondo.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
    QProgressBar, QSizePolicy, QVBoxLayout, QWidget)

class Ui_SplashScreen(object):
    def setupUi(self, SplashScreen):
        if not SplashScreen.objectName():
            SplashScreen.setObjectName(u"SplashScreen")
        SplashScreen.resize(680, 400)
        self.centralwidget = QWidget(SplashScreen)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, -1, -1, -1)
        self.dropShadowFrame = QFrame(self.centralwidget)
        self.dropShadowFrame.setObjectName(u"dropShadowFrame")
        self.dropShadowFrame.setStyleSheet(u"QFrame{\n"
"background-color: rgb(240, 243, 252);\n"
"border-radius: 10px;\n"
"}")
        self.dropShadowFrame.setFrameShape(QFrame.StyledPanel)
        self.dropShadowFrame.setFrameShadow(QFrame.Raised)
        self.label_title = QLabel(self.dropShadowFrame)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setGeometry(QRect(190, 80, 271, 61))
        font = QFont()
        font.setPointSize(40)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet(u"color: rgb(20, 5, 48);")
        self.label_description = QLabel(self.dropShadowFrame)
        self.label_description.setObjectName(u"label_description")
        self.label_description.setGeometry(QRect(160, 150, 331, 31))
        self.label_description.setFont(font)
        self.label_description.setStyleSheet(u"color: rgb(20, 5, 48);")
        self.progressBar = QProgressBar(self.dropShadowFrame)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(70, 190, 541, 23))
        self.progressBar.setStyleSheet(u"QProgressBar {\n"
"	border-radius: 10px;\n"
"	background-color: rgb(219, 192, 245);\n"
"	color: rgb(20, 5, 48);\n"
"	text-align: center; \n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"	border-radius: 10px;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.539773, x2:1, y2:0.557, stop:0 rgba(170, 0, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"}")
        self.progressBar.setValue(24)
        self.label_loading = QLabel(self.dropShadowFrame)
        self.label_loading.setObjectName(u"label_loading")
        self.label_loading.setGeometry(QRect(310, 220, 61, 20))
        self.label_loading.setFont(font)
        self.label_loading.setStyleSheet(u"color: rgb(20, 5, 48);")
        self.label_creadores = QLabel(self.dropShadowFrame)
        self.label_creadores.setObjectName(u"label_creadores")
        self.label_creadores.setGeometry(QRect(10, 360, 231, 20))
        self.label_creadores.setFont(font)
        self.label_creadores.setStyleSheet(u"color: rgb(20, 5, 48);")
        self.label_directores = QLabel(self.dropShadowFrame)
        self.label_directores.setObjectName(u"label_directores")
        self.label_directores.setGeometry(QRect(430, 360, 241, 20))
        self.label_directores.setFont(font)
        self.label_directores.setStyleSheet(u"color: rgb(20, 5, 48);")

        self.verticalLayout.addWidget(self.dropShadowFrame)

        SplashScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(SplashScreen)

        QMetaObject.connectSlotsByName(SplashScreen)
    # setupUi

    def retranslateUi(self, SplashScreen):
        SplashScreen.setWindowTitle(QCoreApplication.translate("SplashScreen", u"MainWindow", None))
        self.label_title.setText(QCoreApplication.translate("SplashScreen", u"<strong>ChemSolid", None))
        self.label_description.setText(QCoreApplication.translate("SplashScreen", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700;\">Desing </span><span style=\" font-size:14pt;\">Your Solid Handling Equipment</span></p></body></html>", None))
        self.label_loading.setText(QCoreApplication.translate("SplashScreen", u"<html><head/><body><p><span style=\" font-size:10pt;\">Loading...</span></p></body></html>", None))
        self.label_creadores.setText(QCoreApplication.translate("SplashScreen", u"<html><head/><body><p><span style=\" font-size:8pt; font-weight:700;\">Created by Kaleth Padilla &amp; Ronald Borja</span></p></body></html>", None))
        self.label_directores.setText(QCoreApplication.translate("SplashScreen", u"<html><head/><body><p><span style=\" font-size:8pt; font-weight:700;\">Directed by Jorge Pi\u00f1eres &amp; Luis Obreg\u00f3n</span></p></body></html>", None))
    # retranslateUi

