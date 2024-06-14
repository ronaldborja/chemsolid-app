# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QFrame,
    QGridLayout, QGroupBox, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QScrollArea, QSizePolicy, QSpacerItem, QStackedWidget,
    QTableWidget, QTableWidgetItem, QTextEdit, QVBoxLayout,
    QWidget)
import resources.resources_rc as resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1276, 735)
        MainWindow.setMinimumSize(QSize(940, 180))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setPointSize(11)
        MainWindow.setFont(font)
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        self.styleSheet.setMinimumSize(QSize(0, 180))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(10)
        font1.setBold(False)
        font1.setItalic(False)
        self.styleSheet.setFont(font1)
        self.styleSheet.setStyleSheet(u"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"\n"
"DARK THEME - DRACULA COLOR BASED\n"
"\n"
"///////////////////////////////////////////////////////////////////////////////////////////////// */\n"
"\n"
"QWidget{\n"
"	color: solid black;\n"
"	font: 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Tooltip */\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(33, 37, 43, 180);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	background-image: none;\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 2px solid rgb(255, 121, 198);\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	margin: 0px;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Bg App */\n"
"#bgApp {	\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: 1p"
                        "x solid #ffffff;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Left Menu */\n"
"#leftMenuBg {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#topLogo {\n"
"	background-color: #F0F0F0;\n"
"	background-image: url(:/images/images/images/PyDracula.png);\n"
"	background-position: centered;\n"
"	background-repeat: no-repeat;\n"
"	\n"
"\n"
"}\n"
"#titleLeftApp { font: 63 12pt \"Segoe UI Semibold\"; }\n"
"#titleLeftDescription { font: 8pt \"Effra Heavy\"; color: rgb(189, 147, 249); }\n"
"\n"
"/* MENUS */\n"
"#topMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color: transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#topMenu .QPushButton:hover {\n"
"	background-color:rgb(255, 255, 255) ;\n"
"	\n"
"}\n"
"#topMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255"
                        ", 255, 255);\n"
"}\n"
"#bottomMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#bottomMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#bottomMenu .QPushButton:pressed {	\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#leftMenuFrame{\n"
"	\n"
"	background-color: #F0F0F0;\n"
"}\n"
"\n"
"/* Toggle Button */\n"
"#toggleButton {\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color: #F0F0F0;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"	color: rgb(113, 126, 149);\n"
"}\n"
"#toggleButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#toggleButton:pressed {\n"
"	background-color: rgb(189, 147, 249);\n"
"}\n"
"\n"
"/* Title M"
                        "enu */\n"
"#titleRightInfo { padding-left: 10px; \n"
" background-color: #F0F0F0;\n"
"border-top: 0px solid #F0F0F0;\n"
"}\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Extra Tab */\n"
"#extraLeftBox {	\n"
"	background-color: rgb(44, 49, 58);\n"
"}\n"
"#extraTopBg{	\n"
"	background-color: rgb(189, 147, 249)\n"
"}\n"
"\n"
"/* Icon */\n"
"#extraIcon {\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"	background-image: url(:/icons/images/icons/icon_settings.png);\n"
"}\n"
"\n"
"/* Label */\n"
"#extraLabel { color: rgb(255, 255, 255); }\n"
"\n"
"/* Btn Close */\n"
"#extraCloseColumnBtn { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#extraCloseColumnBtn:hover { background-color: rgb(196, 161, 249); border-style: solid; border-radius: 4px; }\n"
"#extraCloseColumnBtn:pressed { background-color: rgb(180, 141, 238); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Extra Content */"
                        "\n"
"#extraContent{\n"
"	border-top: 3px solid #F0F0F0;\n"
"}\n"
"\n"
"/* Extra Top Menus */\n"
"#extraTopMenu .QPushButton {\n"
"background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#extraTopMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#extraTopMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Content App */\n"
"#contentTopBg{	\n"
"	background-color: rgb(250,250,250);\n"
"	border-top: 5px solid #F0F0F0;\n"
"	\n"
"}\n"
"\n"
"\n"
"/* Top Buttons */\n"
"#rightButtons .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#rightButtons .QPushButton:hover { background-color: rgb(44, 49, 57); border-st"
                        "yle: solid; border-radius: 4px; }\n"
"#rightButtons .QPushButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Theme Settings */\n"
"#extraRightBox { background-color: rgb(250,250,250); }\n"
"#themeSettingsTopDetail { background-color: rgb(189, 147, 249); }\n"
"\n"
"/* Bottom Bar */\n"
"\n"
"#bottomBar QLabel { font-size: 11px; color: rgb(113, 126, 149); padding-left: 10px; padding-right: 10px; padding-bottom: 2px; }\n"
"\n"
"/* CONTENT SETTINGS */\n"
"/* MENUS */\n"
"#contentSettings .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#contentSettings .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#contentSettings .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* ////////////"
                        "/////////////////////////////////////////////////////////////////////////////////////\n"
"QTableWidget */\n"
"QTableWidget {	\n"
"	background-color: transparent;\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 58);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: transparent;\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: transparent;\n"
"}\n"
"QHeaderView::section{\n"
"	background-color: rgb(33, 37, 43);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: transparent;\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(33, 37, 43);\n"
"	background-color: transparent;\n"
"	padding: 3px;\n"
"	border-top-left-radi"
                        "us: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"LineEdit */\n"
"QLineEdit {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"PlainTextEdit */\n"
"QPlainTextEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QPlainTextEdit  QScrollBar:ver"
                        "tical {\n"
"    width: 8px;\n"
" }\n"
"QPlainTextEdit  QScrollBar:horizontal {\n"
"    height: 8px;\n"
" }\n"
"QPlainTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ScrollBars */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(189, 147, 249);\n"
"    min-width: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    "
                        "background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(189, 147, 249);\n"
"    min-height: 25px;\n"
"	border-radius: 4px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertic"
                        "al {\n"
"	border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CheckBox */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"	background-image: url(:/icons/images/icons/cil-check-alt.png);\n"
"}"
                        "\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"RadioButton */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ComboBox */\n"
"QComboBox{\n"
"	background-color: #FFFFFF;\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3p"
                        "x;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	background: #FFFFFF;\n"
"    background-color: #FFFFFF; /* Cambia el color de fondo de las opciones\n"
"	 desplegadas a blanco */\n"
"	color: #000000; /* Cambia el color del texto a negro */\n"
"}\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Sliders */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 5px;\n"
"    height: 10px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(189, 147, 249);\n"
"    border: none;\n"
"    height: 10px;\n"
"    wid"
                        "th: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 5px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background-color: rgb(189, 147, 249);\n"
"	border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CommandLinkButton */\n"
"QCommandLinkButton {	\n"
"	color: "
                        "rgb(255, 121, 198);\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"	color: rgb(255, 170, 255);\n"
"}\n"
"QCommandLinkButton:hover {	\n"
"	color: rgb(255, 170, 255);\n"
"	background-color: rgb(44, 49, 60);\n"
"}\n"
"QCommandLinkButton:pressed {	\n"
"	color: rgb(189, 147, 249);\n"
"	background-color: rgb(52, 58, 71);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Button */\n"
"#pagesContainer QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"#pagesContainer QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"#pagesContainer QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"\n"
"\n"
"/* paginas\n"
"*/\n"
"#stackedWidget .QLineEdit {	\n"
"	border: 1px solid black;\n"
"\n"
"}\n"
"\n"
"#stackedWidget .QComboBox {	\n"
"	border: 1px solid black;\n"
""
                        "}\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.horizontalLayout_8 = QHBoxLayout(self.styleSheet)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(10, 10, 10, 10)
        self.bgApp = QFrame(self.styleSheet)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setFont(font1)
        self.bgApp.setStyleSheet(u"background-color: rgb(240, 240, 240);")
        self.bgApp.setFrameShape(QFrame.NoFrame)
        self.bgApp.setFrameShadow(QFrame.Raised)
        self.appLayout = QHBoxLayout(self.bgApp)
        self.appLayout.setSpacing(0)
        self.appLayout.setObjectName(u"appLayout")
        self.appLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuBg = QFrame(self.bgApp)
        self.leftMenuBg.setObjectName(u"leftMenuBg")
        self.leftMenuBg.setMinimumSize(QSize(60, 0))
        self.leftMenuBg.setMaximumSize(QSize(60, 16777215))
        self.leftMenuBg.setFrameShape(QFrame.NoFrame)
        self.leftMenuBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.leftMenuBg)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.topLogoInfo = QFrame(self.leftMenuBg)
        self.topLogoInfo.setObjectName(u"topLogoInfo")
        self.topLogoInfo.setMinimumSize(QSize(0, 50))
        self.topLogoInfo.setMaximumSize(QSize(16777215, 50))
        self.topLogoInfo.setFrameShape(QFrame.NoFrame)
        self.topLogoInfo.setFrameShadow(QFrame.Raised)
        self.topLogo = QFrame(self.topLogoInfo)
        self.topLogo.setObjectName(u"topLogo")
        self.topLogo.setGeometry(QRect(10, 5, 42, 42))
        self.topLogo.setMinimumSize(QSize(42, 42))
        self.topLogo.setMaximumSize(QSize(42, 42))
        self.topLogo.setFrameShape(QFrame.NoFrame)
        self.topLogo.setFrameShadow(QFrame.Raised)
        self.titleLeftApp = QLabel(self.topLogoInfo)
        self.titleLeftApp.setObjectName(u"titleLeftApp")
        self.titleLeftApp.setEnabled(True)
        self.titleLeftApp.setGeometry(QRect(70, 8, 160, 20))
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.titleLeftApp.sizePolicy().hasHeightForWidth())
        self.titleLeftApp.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setFamilies([u"Segoe UI Semibold"])
        font2.setPointSize(12)
        font2.setBold(False)
        font2.setItalic(False)
        self.titleLeftApp.setFont(font2)
        self.titleLeftApp.setStyleSheet(u"")
        self.titleLeftApp.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.titleLeftDescription = QLabel(self.topLogoInfo)
        self.titleLeftDescription.setObjectName(u"titleLeftDescription")
        self.titleLeftDescription.setGeometry(QRect(70, 27, 160, 16))
        self.titleLeftDescription.setMaximumSize(QSize(16777215, 16))
        font3 = QFont()
        font3.setFamilies([u"Effra Heavy"])
        font3.setPointSize(8)
        font3.setBold(False)
        font3.setItalic(False)
        self.titleLeftDescription.setFont(font3)
        self.titleLeftDescription.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_3.addWidget(self.topLogoInfo)

        self.leftMenuFrame = QFrame(self.leftMenuBg)
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        sizePolicy.setHeightForWidth(self.leftMenuFrame.sizePolicy().hasHeightForWidth())
        self.leftMenuFrame.setSizePolicy(sizePolicy)
        self.leftMenuFrame.setMinimumSize(QSize(0, 0))
        self.leftMenuFrame.setStyleSheet(u"")
        self.leftMenuFrame.setFrameShape(QFrame.NoFrame)
        self.leftMenuFrame.setFrameShadow(QFrame.Raised)
        self.verticalMenuLayout = QVBoxLayout(self.leftMenuFrame)
        self.verticalMenuLayout.setSpacing(0)
        self.verticalMenuLayout.setObjectName(u"verticalMenuLayout")
        self.verticalMenuLayout.setContentsMargins(0, 0, 0, 0)
        self.toggleBox = QFrame(self.leftMenuFrame)
        self.toggleBox.setObjectName(u"toggleBox")
        self.toggleBox.setMaximumSize(QSize(16777215, 45))
        self.toggleBox.setFrameShape(QFrame.NoFrame)
        self.toggleBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.toggleBox)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.toggleButton = QPushButton(self.toggleBox)
        self.toggleButton.setObjectName(u"toggleButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.toggleButton.sizePolicy().hasHeightForWidth())
        self.toggleButton.setSizePolicy(sizePolicy1)
        self.toggleButton.setMinimumSize(QSize(0, 45))
        self.toggleButton.setFont(font1)
        self.toggleButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleButton.setLayoutDirection(Qt.LeftToRight)
        self.toggleButton.setStyleSheet(u"background-image: url(:/icons/images/icons/barras.png);")

        self.verticalLayout_4.addWidget(self.toggleButton)


        self.verticalMenuLayout.addWidget(self.toggleBox)

        self.topMenu = QFrame(self.leftMenuFrame)
        self.topMenu.setObjectName(u"topMenu")
        self.topMenu.setStyleSheet(u"")
        self.topMenu.setFrameShape(QFrame.NoFrame)
        self.topMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.topMenu)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.btn_home = QPushButton(self.topMenu)
        self.btn_home.setObjectName(u"btn_home")
        sizePolicy1.setHeightForWidth(self.btn_home.sizePolicy().hasHeightForWidth())
        self.btn_home.setSizePolicy(sizePolicy1)
        self.btn_home.setMinimumSize(QSize(0, 45))
        self.btn_home.setFont(font1)
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_home.setLayoutDirection(Qt.LeftToRight)
        self.btn_home.setStyleSheet(u"background-image: url(:/icons/images/icons/pagina-de-inicio.png);\n"
"\n"
"")

        self.verticalLayout_8.addWidget(self.btn_home)

        self.btn_zarandas = QPushButton(self.topMenu)
        self.btn_zarandas.setObjectName(u"btn_zarandas")
        sizePolicy1.setHeightForWidth(self.btn_zarandas.sizePolicy().hasHeightForWidth())
        self.btn_zarandas.setSizePolicy(sizePolicy1)
        self.btn_zarandas.setMinimumSize(QSize(0, 45))
        self.btn_zarandas.setFont(font1)
        self.btn_zarandas.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_zarandas.setLayoutDirection(Qt.LeftToRight)
        self.btn_zarandas.setStyleSheet(u"background-image: url(:/images/images/icons/elKale.png);")

        self.verticalLayout_8.addWidget(self.btn_zarandas)

        self.btn_elevadores = QPushButton(self.topMenu)
        self.btn_elevadores.setObjectName(u"btn_elevadores")
        sizePolicy1.setHeightForWidth(self.btn_elevadores.sizePolicy().hasHeightForWidth())
        self.btn_elevadores.setSizePolicy(sizePolicy1)
        self.btn_elevadores.setMinimumSize(QSize(0, 45))
        self.btn_elevadores.setFont(font1)
        self.btn_elevadores.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_elevadores.setLayoutDirection(Qt.LeftToRight)
        self.btn_elevadores.setStyleSheet(u"background-image: url(:/icons/images/icons/elevador-de-cangilonesnegro.png);")

        self.verticalLayout_8.addWidget(self.btn_elevadores)

        self.btn_molino = QPushButton(self.topMenu)
        self.btn_molino.setObjectName(u"btn_molino")
        sizePolicy1.setHeightForWidth(self.btn_molino.sizePolicy().hasHeightForWidth())
        self.btn_molino.setSizePolicy(sizePolicy1)
        self.btn_molino.setMinimumSize(QSize(0, 45))
        self.btn_molino.setFont(font1)
        self.btn_molino.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_molino.setLayoutDirection(Qt.LeftToRight)
        self.btn_molino.setAutoFillBackground(False)
        self.btn_molino.setStyleSheet(u"background-image: url(:/icons/images/icons/molino-de-piedranegro.png);")
        self.btn_molino.setIconSize(QSize(20, 20))

        self.verticalLayout_8.addWidget(self.btn_molino)

        self.btn_bandas = QPushButton(self.topMenu)
        self.btn_bandas.setObjectName(u"btn_bandas")
        sizePolicy1.setHeightForWidth(self.btn_bandas.sizePolicy().hasHeightForWidth())
        self.btn_bandas.setSizePolicy(sizePolicy1)
        self.btn_bandas.setMinimumSize(QSize(0, 45))
        self.btn_bandas.setFont(font1)
        self.btn_bandas.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_bandas.setLayoutDirection(Qt.LeftToRight)
        self.btn_bandas.setStyleSheet(u"background-image: url(:/icons/images/icons/cinta-transportadoranegra1.png);")

        self.verticalLayout_8.addWidget(self.btn_bandas)

        self.btn_tornillo = QPushButton(self.topMenu)
        self.btn_tornillo.setObjectName(u"btn_tornillo")
        self.btn_tornillo.setMinimumSize(QSize(0, 46))
        self.btn_tornillo.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_tornillo.setStyleSheet(u"\n"
"background-image: url(:/icons/images/icons/tornilloloco_1.png);\n"
"")

        self.verticalLayout_8.addWidget(self.btn_tornillo)


        self.verticalMenuLayout.addWidget(self.topMenu)

        self.bottomMenu = QFrame(self.leftMenuFrame)
        self.bottomMenu.setObjectName(u"bottomMenu")
        self.bottomMenu.setFrameShape(QFrame.NoFrame)
        self.bottomMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.bottomMenu)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.toggleLeftBox = QPushButton(self.bottomMenu)
        self.toggleLeftBox.setObjectName(u"toggleLeftBox")
        sizePolicy1.setHeightForWidth(self.toggleLeftBox.sizePolicy().hasHeightForWidth())
        self.toggleLeftBox.setSizePolicy(sizePolicy1)
        self.toggleLeftBox.setMinimumSize(QSize(0, 45))
        self.toggleLeftBox.setFont(font1)
        self.toggleLeftBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleLeftBox.setLayoutDirection(Qt.LeftToRight)
        self.toggleLeftBox.setStyleSheet(u"QPushButton{\n"
"background-image: url(:/icons/images/icons/cinematografia.png);\n"
"}\n"
"QPushButton:hover {\n"
"    font-size: 15px;\n"
"	\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"}")

        self.verticalLayout_9.addWidget(self.toggleLeftBox)


        self.verticalMenuLayout.addWidget(self.bottomMenu, 0, Qt.AlignBottom)


        self.verticalLayout_3.addWidget(self.leftMenuFrame)


        self.appLayout.addWidget(self.leftMenuBg)

        self.extraLeftBox = QFrame(self.bgApp)
        self.extraLeftBox.setObjectName(u"extraLeftBox")
        self.extraLeftBox.setMinimumSize(QSize(0, 0))
        self.extraLeftBox.setMaximumSize(QSize(0, 16777215))
        self.extraLeftBox.setFrameShape(QFrame.NoFrame)
        self.extraLeftBox.setFrameShadow(QFrame.Raised)
        self.extraColumLayout = QVBoxLayout(self.extraLeftBox)
        self.extraColumLayout.setSpacing(0)
        self.extraColumLayout.setObjectName(u"extraColumLayout")
        self.extraColumLayout.setContentsMargins(0, 0, 0, 0)
        self.extraTopBg = QFrame(self.extraLeftBox)
        self.extraTopBg.setObjectName(u"extraTopBg")
        self.extraTopBg.setMinimumSize(QSize(0, 50))
        self.extraTopBg.setMaximumSize(QSize(16777215, 50))
        self.extraTopBg.setFrameShape(QFrame.NoFrame)
        self.extraTopBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.extraTopBg)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.extraTopLayout = QGridLayout()
        self.extraTopLayout.setObjectName(u"extraTopLayout")
        self.extraTopLayout.setHorizontalSpacing(10)
        self.extraTopLayout.setVerticalSpacing(0)
        self.extraTopLayout.setContentsMargins(10, -1, 10, -1)
        self.extraIcon = QFrame(self.extraTopBg)
        self.extraIcon.setObjectName(u"extraIcon")
        self.extraIcon.setMinimumSize(QSize(20, 0))
        self.extraIcon.setMaximumSize(QSize(20, 20))
        self.extraIcon.setFrameShape(QFrame.NoFrame)
        self.extraIcon.setFrameShadow(QFrame.Raised)

        self.extraTopLayout.addWidget(self.extraIcon, 0, 0, 1, 1)

        self.extraLabel = QLabel(self.extraTopBg)
        self.extraLabel.setObjectName(u"extraLabel")
        self.extraLabel.setMinimumSize(QSize(150, 0))
        self.extraLabel.setStyleSheet(u"color: rgb(85, 85, 0);")

        self.extraTopLayout.addWidget(self.extraLabel, 0, 1, 1, 1)

        self.extraCloseColumnBtn = QPushButton(self.extraTopBg)
        self.extraCloseColumnBtn.setObjectName(u"extraCloseColumnBtn")
        self.extraCloseColumnBtn.setMinimumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setMaximumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.extraCloseColumnBtn.setStyleSheet(u"QPushButton:hover {\n"
"    font-size: 15px;\n"
"	\n"
"	background-color: rgb(255, 0, 0);\n"
"\n"
"}\n"
"")
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.extraCloseColumnBtn.setIcon(icon)
        self.extraCloseColumnBtn.setIconSize(QSize(20, 20))

        self.extraTopLayout.addWidget(self.extraCloseColumnBtn, 0, 2, 1, 1)


        self.verticalLayout_5.addLayout(self.extraTopLayout)


        self.extraColumLayout.addWidget(self.extraTopBg)

        self.extraContent = QFrame(self.extraLeftBox)
        self.extraContent.setObjectName(u"extraContent")
        self.extraContent.setFrameShape(QFrame.NoFrame)
        self.extraContent.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.extraContent)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.extraTopMenu = QFrame(self.extraContent)
        self.extraTopMenu.setObjectName(u"extraTopMenu")
        self.extraTopMenu.setStyleSheet(u"QPushButton:hover {\n"
"    font-size: 15px;\n"
"	\n"
"	color: rgb(0, 0, 0);\n"
"\n"
"	background-color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"")
        self.extraTopMenu.setFrameShape(QFrame.NoFrame)
        self.extraTopMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.extraTopMenu)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.btn_share = QPushButton(self.extraTopMenu)
        self.btn_share.setObjectName(u"btn_share")
        sizePolicy1.setHeightForWidth(self.btn_share.sizePolicy().hasHeightForWidth())
        self.btn_share.setSizePolicy(sizePolicy1)
        self.btn_share.setMinimumSize(QSize(0, 45))
        self.btn_share.setFont(font1)
        self.btn_share.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_share.setLayoutDirection(Qt.LeftToRight)
        self.btn_share.setStyleSheet(u"background-image: url(:/icons/images/icons/usuarios.png);")
        self.btn_share.setFlat(False)

        self.verticalLayout_11.addWidget(self.btn_share)

        self.btn_adjustments = QPushButton(self.extraTopMenu)
        self.btn_adjustments.setObjectName(u"btn_adjustments")
        sizePolicy1.setHeightForWidth(self.btn_adjustments.sizePolicy().hasHeightForWidth())
        self.btn_adjustments.setSizePolicy(sizePolicy1)
        self.btn_adjustments.setMinimumSize(QSize(0, 45))
        self.btn_adjustments.setFont(font1)
        self.btn_adjustments.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_adjustments.setLayoutDirection(Qt.LeftToRight)
        self.btn_adjustments.setStyleSheet(u"background-image: url(:/icons/images/icons/configuraciones (1).png);")

        self.verticalLayout_11.addWidget(self.btn_adjustments)

        self.btn_more = QPushButton(self.extraTopMenu)
        self.btn_more.setObjectName(u"btn_more")
        sizePolicy1.setHeightForWidth(self.btn_more.sizePolicy().hasHeightForWidth())
        self.btn_more.setSizePolicy(sizePolicy1)
        self.btn_more.setMinimumSize(QSize(0, 45))
        self.btn_more.setFont(font1)
        self.btn_more.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_more.setLayoutDirection(Qt.LeftToRight)
        self.btn_more.setStyleSheet(u"background-image: url(:/icons/images/icons/archivo.png);")

        self.verticalLayout_11.addWidget(self.btn_more)


        self.verticalLayout_12.addWidget(self.extraTopMenu, 0, Qt.AlignTop)

        self.extraCenter = QFrame(self.extraContent)
        self.extraCenter.setObjectName(u"extraCenter")
        self.extraCenter.setFrameShape(QFrame.NoFrame)
        self.extraCenter.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.extraCenter)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.textEdit = QTextEdit(self.extraCenter)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMinimumSize(QSize(0, 0))
        self.textEdit.setFont(font1)
        self.textEdit.setStyleSheet(u"background: transparent;")
        self.textEdit.setFrameShape(QFrame.NoFrame)
        self.textEdit.setReadOnly(True)

        self.verticalLayout_10.addWidget(self.textEdit)


        self.verticalLayout_12.addWidget(self.extraCenter)

        self.extraBottom = QFrame(self.extraContent)
        self.extraBottom.setObjectName(u"extraBottom")
        self.extraBottom.setFrameShape(QFrame.NoFrame)
        self.extraBottom.setFrameShadow(QFrame.Raised)

        self.verticalLayout_12.addWidget(self.extraBottom)


        self.extraColumLayout.addWidget(self.extraContent)


        self.appLayout.addWidget(self.extraLeftBox)

        self.contentBox = QFrame(self.bgApp)
        self.contentBox.setObjectName(u"contentBox")
        self.contentBox.setFrameShape(QFrame.NoFrame)
        self.contentBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.contentBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.contentTopBg = QFrame(self.contentBox)
        self.contentTopBg.setObjectName(u"contentTopBg")
        self.contentTopBg.setMinimumSize(QSize(0, 50))
        self.contentTopBg.setMaximumSize(QSize(16777215, 50))
        self.contentTopBg.setFrameShape(QFrame.NoFrame)
        self.contentTopBg.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.contentTopBg)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
        self.leftBox = QFrame(self.contentTopBg)
        self.leftBox.setObjectName(u"leftBox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.leftBox.sizePolicy().hasHeightForWidth())
        self.leftBox.setSizePolicy(sizePolicy2)
        self.leftBox.setFrameShape(QFrame.NoFrame)
        self.leftBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.leftBox)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.titleRightInfo = QLabel(self.leftBox)
        self.titleRightInfo.setObjectName(u"titleRightInfo")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.titleRightInfo.sizePolicy().hasHeightForWidth())
        self.titleRightInfo.setSizePolicy(sizePolicy3)
        self.titleRightInfo.setMaximumSize(QSize(16777215, 45))
        font4 = QFont()
        font4.setFamilies([u"Bookman Old Style"])
        font4.setPointSize(12)
        font4.setBold(True)
        font4.setItalic(False)
        self.titleRightInfo.setFont(font4)
        self.titleRightInfo.setStyleSheet(u"QLabel{\n"
"font: 600 12pt \"Bookman Old Style\";\n"
"}")
        self.titleRightInfo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.titleRightInfo)


        self.horizontalLayout.addWidget(self.leftBox)

        self.rightButtons = QFrame(self.contentTopBg)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setMinimumSize(QSize(0, 28))
        self.rightButtons.setFrameShape(QFrame.NoFrame)
        self.rightButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.rightButtons)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.settingsTopBtn = QPushButton(self.rightButtons)
        self.settingsTopBtn.setObjectName(u"settingsTopBtn")
        self.settingsTopBtn.setMinimumSize(QSize(28, 28))
        self.settingsTopBtn.setMaximumSize(QSize(28, 28))
        self.settingsTopBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.settingsTopBtn.setStyleSheet(u"QPushButton:hover {\n"
"    font-size: 15px;\n"
"	\n"
"	background-color:rgb(153, 209, 255);\n"
"\n"
"}\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/pregunta2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settingsTopBtn.setIcon(icon1)
        self.settingsTopBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.settingsTopBtn)

        self.minimizeAppBtn = QPushButton(self.rightButtons)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setMinimumSize(QSize(28, 28))
        self.minimizeAppBtn.setMaximumSize(QSize(28, 28))
        self.minimizeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.minimizeAppBtn.setStyleSheet(u"QPushButton:hover {\n"
"    font-size: 15px;\n"
"	\n"
"	background-color:rgb(153, 209, 255);\n"
"\n"
"}\n"
"")
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/minimizar-signo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeAppBtn.setIcon(icon2)
        self.minimizeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.minimizeAppBtn)

        self.maximizeRestoreAppBtn = QPushButton(self.rightButtons)
        self.maximizeRestoreAppBtn.setObjectName(u"maximizeRestoreAppBtn")
        self.maximizeRestoreAppBtn.setEnabled(False)
        self.maximizeRestoreAppBtn.setMinimumSize(QSize(28, 28))
        self.maximizeRestoreAppBtn.setMaximumSize(QSize(28, 28))
        font5 = QFont()
        font5.setFamilies([u"Segoe UI"])
        font5.setPointSize(10)
        font5.setBold(False)
        font5.setItalic(False)
        font5.setStyleStrategy(QFont.PreferDefault)
        self.maximizeRestoreAppBtn.setFont(font5)
        self.maximizeRestoreAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.maximizeRestoreAppBtn.setStyleSheet(u"QPushButton:hover {\n"
"    font-size: 15px;\n"
"	\n"
"	background-color:rgb(153, 209, 255);\n"
"\n"
"}\n"
"")
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/icons/maximizar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximizeRestoreAppBtn.setIcon(icon3)
        self.maximizeRestoreAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.maximizeRestoreAppBtn)

        self.closeAppBtn = QPushButton(self.rightButtons)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setMinimumSize(QSize(28, 28))
        self.closeAppBtn.setMaximumSize(QSize(28, 28))
        self.closeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.closeAppBtn.setStyleSheet(u"QPushButton:hover {\n"
"    font-size: 15px;\n"
"	\n"
"	background-color: rgb(255, 0, 0);\n"
"\n"
"}\n"
"")
        icon4 = QIcon()
        icon4.addFile(u":/icons/images/icons/incorrecto.png", QSize(), QIcon.Normal, QIcon.Off)
        self.closeAppBtn.setIcon(icon4)
        self.closeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.closeAppBtn)

        self.minimizeAppBtn.raise_()
        self.maximizeRestoreAppBtn.raise_()
        self.closeAppBtn.raise_()
        self.settingsTopBtn.raise_()

        self.horizontalLayout.addWidget(self.rightButtons, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.contentTopBg)

        self.contentBottom = QFrame(self.contentBox)
        self.contentBottom.setObjectName(u"contentBottom")
        self.contentBottom.setMinimumSize(QSize(0, 0))
        self.contentBottom.setStyleSheet(u"QFrame #content{ \n"
"            \n"
"				\n"
"                border-radius: 0px;\n"
"                border: 4px solid #E6E6E6;\n"
"                box-shadow: 0px 0px 20px #E6E6E6;\n"
"					\n"
"				border-top: 0px;\n"
"border-left-color:qlineargradient(spread:pad, x1:0.994318, y1:0, x2:0, y2:0, stop:0 rgba(149, 149, 149, 255), stop:1 rgba(255, 255, 255, 213)) ;\n"
"            }")
        self.contentBottom.setFrameShape(QFrame.NoFrame)
        self.contentBottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.contentBottom)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.contentBottom)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 50))
        self.frame.setStyleSheet(u"QFrame#frame{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(247, 232, 235, 255), stop:0.55 rgba(205, 182, 212, 217), stop:0.553672 rgba(194, 179, 212, 208), stop:0.98 rgba(237, 242, 250, 255), stop:1 rgba(0, 0, 0, 0))\n"
"}\n"
"QFrame#frame{\n"
" border: 4px solid #E6E6E6;\n"
"                box-shadow: 0px 0px 20px #E6E6E6;\n"
"					\n"
"				border-top: 0px;\n"
"	border-bottom: 0px;\n"
"\n"
"\n"
"border-left-color:qlineargradient(spread:pad, x1:0.994318, y1:0, x2:0, y2:0, stop:0 rgba(149, 149, 149, 255), stop:1 rgba(255, 255, 255, 213)) ;\n"
"}\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.verticalLayout_6.addWidget(self.frame)

        self.content = QFrame(self.contentBottom)
        self.content.setObjectName(u"content")
        self.content.setMinimumSize(QSize(0, 0))
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.content)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pagesContainer = QFrame(self.content)
        self.pagesContainer.setObjectName(u"pagesContainer")
        self.pagesContainer.setStyleSheet(u"QStackedWidget#stackedWidget{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0.0909091 rgba(238, 234, 250, 255), stop:0.244318 rgba(239, 240, 250, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"")
        self.pagesContainer.setFrameShape(QFrame.NoFrame)
        self.pagesContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.pagesContainer)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.pagesContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"QWidget{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0.0909091 rgba(238, 234, 250, 255), stop:0.159091 rgba(239, 240, 250, 255), stop:0.431818 rgba(255, 255, 255, 242));\n"
"}\n"
"QLabel{\n"
"background:transparent\n"
"}\n"
"\n"
"QLineEdit{\n"
"background:transparent\n"
"}\n"
"\n"
"QGroupBox{\n"
"background:transparent\n"
"}\n"
"QComboBox{background:transparent\n"
"}\n"
"QFrame{\n"
"background:transparent\n"
"}\n"
"QGroupBox QWidget{\n"
"background:transparent\n"
"}\n"
"QGroupBox QWidget QPushButton{\n"
"border: 1px solid black\n"
"}\n"
"\n"
"\n"
"")
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.home.setStyleSheet(u"\n"
"background-position: center;\n"
"background-repeat: no-repeat;")
        self.gridLayout_24 = QGridLayout(self.home)
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.groupBox_36 = QGroupBox(self.home)
        self.groupBox_36.setObjectName(u"groupBox_36")
        self.groupBox_36.setCursor(QCursor(Qt.ArrowCursor))
        self.groupBox_36.setStyleSheet(u"QGroupBox {\n"
"	\n"
"	font: 15pt \"Effra Heavy\";\n"
"    border: 2px;\n"
"	\n"
"\n"
" \n"
"}\n"
"\n"
"")
        self.groupBox_36.setAlignment(Qt.AlignCenter)
        self.gridLayout_25 = QGridLayout(self.groupBox_36)
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.gridLayout_25.setHorizontalSpacing(50)
        self.gridLayout_25.setVerticalSpacing(40)
        self.gridLayout_25.setContentsMargins(50, 50, 50, 25)
        self.bton_home_cangilon = QPushButton(self.groupBox_36)
        self.bton_home_cangilon.setObjectName(u"bton_home_cangilon")
        self.bton_home_cangilon.setMinimumSize(QSize(0, 170))
        self.bton_home_cangilon.setCursor(QCursor(Qt.PointingHandCursor))
        self.bton_home_cangilon.setStyleSheet(u"QPushButton {\n"
"	background-image: url(:/images/images/icons/fondoelevadores.png);\n"
"    background-repeat: no-repeat;\n"
"	border-radius: 15px;\n"
"    background-position: center; /* Puedes ajustar la posici\u00f3n */\n"
"    /* Otros estilos... */\n"
"	\n"
"	 border: 1.5px solid #808080; \n"
"    border-radius: 15px;\n"
"\n"
"	color: rgb(0, 0, 0);\n"
"	font: 700 14pt \"Georgia\";\n"
"text-align: bottom;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  	\n"
"	background-color:#EBEBEB;\n"
"}\n"
"")

        self.gridLayout_25.addWidget(self.bton_home_cangilon, 0, 1, 1, 1)

        self.bton_home_tornillo = QPushButton(self.groupBox_36)
        self.bton_home_tornillo.setObjectName(u"bton_home_tornillo")
        self.bton_home_tornillo.setMinimumSize(QSize(0, 170))
        self.bton_home_tornillo.setCursor(QCursor(Qt.PointingHandCursor))
        self.bton_home_tornillo.setStyleSheet(u"QPushButton {\n"
"	background-image:  url(:/images/images/icons/fondoTornillos.png);\n"
"    background-repeat: no-repeat;\n"
"	border-radius: 15px;\n"
"    background-position: center; /* Puedes ajustar la posici\u00f3n */\n"
"    /* Otros estilos... */\n"
"	\n"
"	 border: 1.5px solid #808080; \n"
"    border-radius: 15px;\n"
"\n"
"	color: rgb(0, 0, 0);\n"
"	font: 700 14pt \"Georgia\";\n"
"text-align: bottom;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  	\n"
"	background-color:#EBEBEB;\n"
"}\n"
"\n"
"")

        self.gridLayout_25.addWidget(self.bton_home_tornillo, 0, 2, 1, 1)

        self.pushButton_17 = QPushButton(self.groupBox_36)
        self.pushButton_17.setObjectName(u"pushButton_17")
        self.pushButton_17.setMinimumSize(QSize(0, 170))
        self.pushButton_17.setStyleSheet(u"QPushButton {\n"
"    background-image: url(:/images/images/icons/fondoFinal.png);\n"
"    background-repeat: no-repeat;\n"
"\n"
"    background-position: center; /* Puedes ajustar la posici\u00f3n */\n"
"    /* Otros estilos... */\n"
"	\n"
"	border: 1.5px solid #808080; \n"
"    border-radius: 15px;\n"
"\n"
"\n"
"	color: rgb(0, 0, 0);\n"
"	font: 700 14pt \"Georgia\";\n"
"text-align: bottom;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  	\n"
"	background-color:#EBEBEB;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	padding-left:5px;\n"
"	padding-top:5px;\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(247, 232, 235, 255), stop:0.55 rgba(205, 182, 212, 217), stop:0.553672 rgba(194, 179, 212, 208), stop:0.98 rgba(237, 242, 250, 255), stop:1 rgba(0, 0, 0, 0))\n"
"}")

        self.gridLayout_25.addWidget(self.pushButton_17, 1, 2, 1, 1)

        self.bton_home_zaranda = QPushButton(self.groupBox_36)
        self.bton_home_zaranda.setObjectName(u"bton_home_zaranda")
        self.bton_home_zaranda.setMinimumSize(QSize(0, 170))
        self.bton_home_zaranda.setCursor(QCursor(Qt.PointingHandCursor))
        self.bton_home_zaranda.setStyleSheet(u"QPushButton {\n"
"    background-image: url(:/images/images/icons/fondoZarandas.png);\n"
"    background-position: center; /* Puedes ajustar la posici\u00f3n */\n"
"    /* Otros estilos... */\n"
"\n"
"    border: 1.5px solid #808080; \n"
"    border-radius: 15px;\n"
"\n"
"	color: rgb(0, 0, 0);\n"
"	font: 700 14pt \"Georgia\";\n"
"	text-align: bottom;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  	box-shadow: 5px 5px 10px rgba(0, 0, 0, 0.7);\n"
"	background-color:#EBEBEB;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	padding-left:5px;\n"
"	padding-top:5px;\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(247, 232, 235, 255), stop:0.55 rgba(205, 182, 212, 217), stop:0.553672 rgba(194, 179, 212, 208), stop:0.98 rgba(237, 242, 250, 255), stop:1 rgba(0, 0, 0, 0))\n"
"}")

        self.gridLayout_25.addWidget(self.bton_home_zaranda, 0, 0, 1, 1)

        self.bton_home_banda = QPushButton(self.groupBox_36)
        self.bton_home_banda.setObjectName(u"bton_home_banda")
        self.bton_home_banda.setMinimumSize(QSize(0, 170))
        self.bton_home_banda.setCursor(QCursor(Qt.PointingHandCursor))
        self.bton_home_banda.setStyleSheet(u"QPushButton {\n"
"    background-image: url(:/images/images/icons/fondoBandas.png);\n"
"    background-repeat: no-repeat;\n"
"    \n"
"	 border: 1.5px solid #808080; \n"
"    border-radius: 15px;\n"
"\n"
"	color: rgb(0, 0, 0);\n"
"	font: 700 14pt \"Georgia\";\n"
"text-align: bottom;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  	\n"
"	background-color:#EBEBEB;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	padding-left:5px;\n"
"	padding-top:5px;\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(247, 232, 235, 255), stop:0.55 rgba(205, 182, 212, 217), stop:0.553672 rgba(194, 179, 212, 208), stop:0.98 rgba(237, 242, 250, 255), stop:1 rgba(0, 0, 0, 0))\n"
"}")

        self.gridLayout_25.addWidget(self.bton_home_banda, 1, 0, 1, 1)

        self.bton_home_molino = QPushButton(self.groupBox_36)
        self.bton_home_molino.setObjectName(u"bton_home_molino")
        self.bton_home_molino.setMinimumSize(QSize(0, 170))
        self.bton_home_molino.setCursor(QCursor(Qt.PointingHandCursor))
        self.bton_home_molino.setStyleSheet(u"QPushButton {\n"
"    background-image: url(:/images/images/icons/fondoMolinos.png);\n"
"    background-repeat: no-repeat;\n"
"\n"
"    background-position: center; /* Puedes ajustar la posici\u00f3n */\n"
"    /* Otros estilos... */\n"
"	\n"
"	border: 1.5px solid #808080; \n"
"    border-radius: 15px;\n"
"\n"
"\n"
"	color: rgb(0, 0, 0);\n"
"	font: 700 14pt \"Georgia\";\n"
"text-align: bottom;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  	\n"
"	background-color:#EBEBEB;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	padding-left:5px;\n"
"	padding-top:5px;\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(247, 232, 235, 255), stop:0.55 rgba(205, 182, 212, 217), stop:0.553672 rgba(194, 179, 212, 208), stop:0.98 rgba(237, 242, 250, 255), stop:1 rgba(0, 0, 0, 0))\n"
"}")

        self.gridLayout_25.addWidget(self.bton_home_molino, 1, 1, 1, 1)


        self.gridLayout_24.addWidget(self.groupBox_36, 0, 1, 1, 1)

        self.stackedWidget.addWidget(self.home)
        self.menu_molino = QWidget()
        self.menu_molino.setObjectName(u"menu_molino")
        self.gridLayout_20 = QGridLayout(self.menu_molino)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.groupBox_12 = QGroupBox(self.menu_molino)
        self.groupBox_12.setObjectName(u"groupBox_12")
        self.groupBox_12.setStyleSheet(u"")
        self.gridLayout_22 = QGridLayout(self.groupBox_12)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.gridLayout_22.setHorizontalSpacing(140)
        self.gridLayout_22.setContentsMargins(150, -1, 150, -1)
        self.menu_molino_mandibula = QPushButton(self.groupBox_12)
        self.menu_molino_mandibula.setObjectName(u"menu_molino_mandibula")
        self.menu_molino_mandibula.setMinimumSize(QSize(0, 180))
        self.menu_molino_mandibula.setCursor(QCursor(Qt.PointingHandCursor))
        self.menu_molino_mandibula.setStyleSheet(u"QPushButton {\n"
"	background-image: url(:/images/images/icons/JawCrusher.png);\n"
"    background-repeat: no-repeat;\n"
"    background-size: cover; /* Puedes ajustar el tama\u00f1o */\n"
"	border-radius: 15px;\n"
"    background-position: center; /* Puedes ajustar la posici\u00f3n */\n"
"    /* Otros estilos... */\n"
"	\n"
"	 border: 1.5px solid #808080; \n"
"    border-radius: 15px;\n"
"    box-shadow: 5px 5px 5px rgba(0, 0, 0, 0.5);\n"
"\n"
"	color: rgb(0, 0, 0);\n"
"	font: 700 14pt \"Georgia\";\n"
"text-align: bottom;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  	\n"
"	background-color:#EBEBEB;\n"
"}\n"
"")

        self.gridLayout_22.addWidget(self.menu_molino_mandibula, 1, 1, 1, 1)

        self.menu_molino_rodillo = QPushButton(self.groupBox_12)
        self.menu_molino_rodillo.setObjectName(u"menu_molino_rodillo")
        sizePolicy.setHeightForWidth(self.menu_molino_rodillo.sizePolicy().hasHeightForWidth())
        self.menu_molino_rodillo.setSizePolicy(sizePolicy)
        self.menu_molino_rodillo.setMinimumSize(QSize(20, 180))
        self.menu_molino_rodillo.setCursor(QCursor(Qt.PointingHandCursor))
        self.menu_molino_rodillo.setStyleSheet(u"QPushButton {\n"
"	background-image: url(:/images/images/icons/RollerMill.png);\n"
"    background-repeat: no-repeat;\n"
"    background-size: cover; /* Puedes ajustar el tama\u00f1o */\n"
"	border-radius: 15px;\n"
"    background-position: center; /* Puedes ajustar la posici\u00f3n */\n"
"    /* Otros estilos... */\n"
"	\n"
"	 border: 1.5px solid #808080; \n"
"    border-radius: 15px;\n"
"    box-shadow: 5px 5px 5px rgba(0, 0, 0, 0.5);\n"
"\n"
"	color: rgb(0, 0, 0);\n"
"	font: 700 14pt \"Georgia\";\n"
"text-align: bottom;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  	\n"
"	background-color:#EBEBEB;\n"
"}\n"
"\n"
"\n"
"")

        self.gridLayout_22.addWidget(self.menu_molino_rodillo, 0, 0, 1, 1)

        self.menu_molino_bola = QPushButton(self.groupBox_12)
        self.menu_molino_bola.setObjectName(u"menu_molino_bola")
        self.menu_molino_bola.setMinimumSize(QSize(0, 180))
        self.menu_molino_bola.setCursor(QCursor(Qt.PointingHandCursor))
        self.menu_molino_bola.setStyleSheet(u"QPushButton {\n"
"	background-image: url(:/images/images/icons/BallMill.png);\n"
"    background-repeat: no-repeat;\n"
"    background-size: cover; /* Puedes ajustar el tama\u00f1o */\n"
"	border-radius: 15px;\n"
"    background-position: center; /* Puedes ajustar la posici\u00f3n */\n"
"    /* Otros estilos... */\n"
"	\n"
"	 border: 1.5px solid #808080; \n"
"    border-radius: 15px;\n"
"    box-shadow: 5px 5px 5px rgba(0, 0, 0, 0.5);\n"
"\n"
"	color: rgb(0, 0, 0);\n"
"	font: 700 14pt \"Georgia\";\n"
"text-align: bottom;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  	\n"
"	background-color:#EBEBEB;\n"
"}\n"
"\n"
"")

        self.gridLayout_22.addWidget(self.menu_molino_bola, 1, 0, 1, 1)

        self.menu_molino_cono = QPushButton(self.groupBox_12)
        self.menu_molino_cono.setObjectName(u"menu_molino_cono")
        self.menu_molino_cono.setMinimumSize(QSize(0, 180))
        self.menu_molino_cono.setCursor(QCursor(Qt.PointingHandCursor))
        self.menu_molino_cono.setStyleSheet(u"QPushButton {\n"
"	background-image: url(:/images/images/icons/ConeCrusher.png);\n"
"    background-repeat: no-repeat;\n"
"    background-size: cover; /* Puedes ajustar el tama\u00f1o */\n"
"	border-radius: 15px;\n"
"    background-position: center; /* Puedes ajustar la posici\u00f3n */\n"
"    /* Otros estilos... */\n"
"	\n"
"	 border: 1.5px solid #808080; \n"
"    border-radius: 15px;\n"
"    box-shadow: 5px 5px 5px rgba(0, 0, 0, 0.5);\n"
"\n"
"	color: rgb(0, 0, 0);\n"
"	font: 700 14pt \"Georgia\";\n"
"text-align: bottom;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  	\n"
"	background-color:#EBEBEB;\n"
"}\n"
"")

        self.gridLayout_22.addWidget(self.menu_molino_cono, 0, 1, 1, 1)


        self.gridLayout_20.addWidget(self.groupBox_12, 1, 1, 1, 1)

        self.stackedWidget.addWidget(self.menu_molino)
        self.tornillo = QWidget()
        self.tornillo.setObjectName(u"tornillo")
        self.tornillo.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.tornillo)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.widget = QWidget(self.tornillo)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_17 = QHBoxLayout(self.widget)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.groupBox_3 = QGroupBox(self.widget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setStyleSheet(u"QGroupBox {\n"
"    border: 2px;\n"
"	font: 600 12pt \"Bookman Old Style\";\n"
"    margin-top: 10px; /* Ajusta el margen superior seg\u00fan tus necesidades */\n"
"    padding-top: 30px; /* Ajusta el espaciado superior seg\u00fan tus necesidades */\n"
"}\n"
"\n"
"")
        self.groupBox_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.gridLayout_10 = QGridLayout(self.groupBox_3)
        self.gridLayout_10.setSpacing(0)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setContentsMargins(4, 0, 6, 0)
        self.groupBox = QGroupBox(self.groupBox_3)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy2.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy2)
        self.groupBox.setStyleSheet(u"QGroupBox {\n"
"    border: 1px solid rgba(128, 128, 128, 0.5); /* Ajusta la opacidad seg\u00fan tus necesidades */\n"
"    margin-top: 10px; /* Ajusta el margen superior seg\u00fan tus necesidades */\n"
"    padding-top: 20px; /* Ajusta el espaciado superior seg\u00fan tus necesidades */\n"
"	\n"
"	font: 600 12pt \"Bookman Old Style\";\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"    border: 1px solid rgb(189, 147, 249);\n"
"}\n"
"QGroupBox{border: 2px}\n"
"\n"
"QGroupBox {\n"
"    	\n"
"    border: 10px;\n"
"	/*font: 350 20pt \"Yu Gothic UI Semilight\";*/\n"
" \n"
"}")
        self.groupBox.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.gridLayout_5 = QGridLayout(self.groupBox)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setVerticalSpacing(4)
        self.gridLayout_5.setContentsMargins(-1, -1, -1, 0)
        self.label_19 = QLabel(self.groupBox)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout_5.addWidget(self.label_19, 4, 0, 1, 1)

        self.label_29 = QLabel(self.groupBox)
        self.label_29.setObjectName(u"label_29")

        self.gridLayout_5.addWidget(self.label_29, 6, 0, 1, 1)

        self.label_27 = QLabel(self.groupBox)
        self.label_27.setObjectName(u"label_27")

        self.gridLayout_5.addWidget(self.label_27, 8, 0, 1, 1)

        self.lineEdit_L_tornillo = QLineEdit(self.groupBox)
        self.lineEdit_L_tornillo.setObjectName(u"lineEdit_L_tornillo")
        self.lineEdit_L_tornillo.setStyleSheet(u"")

        self.gridLayout_5.addWidget(self.lineEdit_L_tornillo, 6, 1, 1, 1)

        self.lineEdit_t_tornillo = QLineEdit(self.groupBox)
        self.lineEdit_t_tornillo.setObjectName(u"lineEdit_t_tornillo")
        self.lineEdit_t_tornillo.setStyleSheet(u"")

        self.gridLayout_5.addWidget(self.lineEdit_t_tornillo, 2, 1, 1, 1)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_5.addWidget(self.label_6, 0, 0, 1, 1)

        self.comboBox_lambda_tornillo = QComboBox(self.groupBox)
        self.comboBox_lambda_tornillo.addItem("")
        self.comboBox_lambda_tornillo.addItem("")
        self.comboBox_lambda_tornillo.addItem("")
        self.comboBox_lambda_tornillo.addItem("")
        self.comboBox_lambda_tornillo.addItem("")
        self.comboBox_lambda_tornillo.setObjectName(u"comboBox_lambda_tornillo")
        self.comboBox_lambda_tornillo.setCursor(QCursor(Qt.PointingHandCursor))
        self.comboBox_lambda_tornillo.setStyleSheet(u"QComboBox {\n"
"    font-size: 11px; /* Cambia el tama\u00f1o de la fuente en el QComboBox */\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"	background: transparent;\n"
"    background-color: #FFFFFF; /* Cambia el color de fondo de las opciones\n"
"	 desplegadas a blanco */\n"
"	color: #000000; /* Cambia el color del texto a negro */\n"
"}")

        self.gridLayout_5.addWidget(self.comboBox_lambda_tornillo, 1, 1, 1, 1)

        self.comboBox_k_tornillo = QComboBox(self.groupBox)
        self.comboBox_k_tornillo.addItem("")
        self.comboBox_k_tornillo.addItem("")
        self.comboBox_k_tornillo.addItem("")
        self.comboBox_k_tornillo.addItem("")
        self.comboBox_k_tornillo.addItem("")
        self.comboBox_k_tornillo.addItem("")
        self.comboBox_k_tornillo.setObjectName(u"comboBox_k_tornillo")
        self.comboBox_k_tornillo.setCursor(QCursor(Qt.PointingHandCursor))
        self.comboBox_k_tornillo.setStyleSheet(u"QComboBox {\n"
"    font-size: 11px; /* Cambia el tama\u00f1o de la fuente en el QComboBox */\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"	background: transparent;\n"
"    background-color: #FFFFFF; /* Cambia el color de fondo de las opciones\n"
"	 desplegadas a blanco */\n"
"	color: #000000; /* Cambia el color del texto a negro */\n"
"}")

        self.gridLayout_5.addWidget(self.comboBox_k_tornillo, 4, 1, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"")

        self.gridLayout_5.addWidget(self.label_2, 9, 0, 1, 1)

        self.label_17 = QLabel(self.groupBox)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_5.addWidget(self.label_17, 11, 0, 1, 1)

        self.lineEdit_P_tornillo = QLineEdit(self.groupBox)
        self.lineEdit_P_tornillo.setObjectName(u"lineEdit_P_tornillo")
        self.lineEdit_P_tornillo.setStyleSheet(u"")

        self.gridLayout_5.addWidget(self.lineEdit_P_tornillo, 15, 1, 1, 1)

        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_5.addWidget(self.label_7, 2, 0, 1, 1)

        self.label_28 = QLabel(self.groupBox)
        self.label_28.setObjectName(u"label_28")

        self.gridLayout_5.addWidget(self.label_28, 14, 0, 1, 1)

        self.lineEdit_v_tornillo = QLineEdit(self.groupBox)
        self.lineEdit_v_tornillo.setObjectName(u"lineEdit_v_tornillo")
        self.lineEdit_v_tornillo.setStyleSheet(u"")

        self.gridLayout_5.addWidget(self.lineEdit_v_tornillo, 10, 1, 1, 1)

        self.lineEdit_Q_tornillo = QLineEdit(self.groupBox)
        self.lineEdit_Q_tornillo.setObjectName(u"lineEdit_Q_tornillo")
        self.lineEdit_Q_tornillo.setStyleSheet(u"")

        self.gridLayout_5.addWidget(self.lineEdit_Q_tornillo, 11, 1, 1, 1)

        self.label_26 = QLabel(self.groupBox)
        self.label_26.setObjectName(u"label_26")

        self.gridLayout_5.addWidget(self.label_26, 13, 0, 1, 1)

        self.lineEdit_PN_tornillo = QLineEdit(self.groupBox)
        self.lineEdit_PN_tornillo.setObjectName(u"lineEdit_PN_tornillo")
        self.lineEdit_PN_tornillo.setStyleSheet(u"")

        self.gridLayout_5.addWidget(self.lineEdit_PN_tornillo, 13, 1, 1, 1)

        self.lineEdit_s_tornillo = QLineEdit(self.groupBox)
        self.lineEdit_s_tornillo.setObjectName(u"lineEdit_s_tornillo")
        self.lineEdit_s_tornillo.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_s_tornillo.setStyleSheet(u"")

        self.gridLayout_5.addWidget(self.lineEdit_s_tornillo, 9, 1, 1, 1)

        self.reset_button_tornillo = QPushButton(self.groupBox)
        self.reset_button_tornillo.setObjectName(u"reset_button_tornillo")
        self.reset_button_tornillo.setCursor(QCursor(Qt.PointingHandCursor))
        self.reset_button_tornillo.setStyleSheet(u"\n"
"QPushButton:hover {\n"
"    font-size: 15px;\n"
"	\n"
"	background-color: rgb(255, 44, 44);\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	padding-left:5px;\n"
"	padding-top:5px;\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(53, 21, 21, 255), stop:0.55 rgba(235, 93, 44, 255), stop:0.98 rgba(146, 91, 9, 255), stop:1 rgba(0, 0, 0, 0));\n"
"}\n"
"")

        self.gridLayout_5.addWidget(self.reset_button_tornillo, 17, 0, 1, 1)

        self.label_10 = QLabel(self.groupBox)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_5.addWidget(self.label_10, 10, 0, 1, 1)

        self.label_25 = QLabel(self.groupBox)
        self.label_25.setObjectName(u"label_25")

        self.gridLayout_5.addWidget(self.label_25, 18, 0, 1, 1)

        self.lineEdit_H_tornillo = QLineEdit(self.groupBox)
        self.lineEdit_H_tornillo.setObjectName(u"lineEdit_H_tornillo")
        self.lineEdit_H_tornillo.setStyleSheet(u"")

        self.gridLayout_5.addWidget(self.lineEdit_H_tornillo, 7, 1, 1, 1)

        self.label_9 = QLabel(self.groupBox)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.label_9, 1, 0, 1, 1)

        self.lineEdit_n_tornillo = QLineEdit(self.groupBox)
        self.lineEdit_n_tornillo.setObjectName(u"lineEdit_n_tornillo")
        self.lineEdit_n_tornillo.setStyleSheet(u"")

        self.gridLayout_5.addWidget(self.lineEdit_n_tornillo, 3, 1, 1, 1)

        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_5.addWidget(self.label_8, 3, 0, 1, 1)

        self.lineEdit_pst_tornillo = QLineEdit(self.groupBox)
        self.lineEdit_pst_tornillo.setObjectName(u"lineEdit_pst_tornillo")
        self.lineEdit_pst_tornillo.setStyleSheet(u"")

        self.gridLayout_5.addWidget(self.lineEdit_pst_tornillo, 12, 1, 1, 1)

        self.label_15 = QLabel(self.groupBox)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_5.addWidget(self.label_15, 15, 0, 1, 1)

        self.pushButton = QPushButton(self.groupBox)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(u"\n"
"\n"
"QPushButton:hover {\n"
"    font-size: 15px;\n"
"	\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(0, 255, 69);\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	padding-left:5px;\n"
"	padding-top:5px;\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(211, 255, 102, 255), stop:0.55 rgba(139, 235, 44, 255), stop:0.98 rgba(9, 146, 76, 149), stop:1 rgba(0, 0, 0, 0));\n"
"}")

        self.gridLayout_5.addWidget(self.pushButton, 17, 1, 1, 1)

        self.label_20 = QLabel(self.groupBox)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font1)

        self.gridLayout_5.addWidget(self.label_20, 12, 0, 1, 1)

        self.label_18 = QLabel(self.groupBox)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_5.addWidget(self.label_18, 5, 0, 1, 1)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_5.addWidget(self.label_3, 7, 0, 1, 1)

        self.lineEdit_D_tornillo = QLineEdit(self.groupBox)
        self.lineEdit_D_tornillo.setObjectName(u"lineEdit_D_tornillo")
        self.lineEdit_D_tornillo.setStyleSheet(u"")

        self.gridLayout_5.addWidget(self.lineEdit_D_tornillo, 0, 1, 1, 1)

        self.lineEdit_y_tornillo = QLineEdit(self.groupBox)
        self.lineEdit_y_tornillo.setObjectName(u"lineEdit_y_tornillo")
        self.lineEdit_y_tornillo.setStyleSheet(u"")

        self.gridLayout_5.addWidget(self.lineEdit_y_tornillo, 5, 1, 1, 1)

        self.comboBox_Co_tornillo = QComboBox(self.groupBox)
        self.comboBox_Co_tornillo.addItem("")
        self.comboBox_Co_tornillo.addItem("")
        self.comboBox_Co_tornillo.addItem("")
        self.comboBox_Co_tornillo.addItem("")
        self.comboBox_Co_tornillo.addItem("")
        self.comboBox_Co_tornillo.setObjectName(u"comboBox_Co_tornillo")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(28)
        sizePolicy4.setVerticalStretch(21)
        sizePolicy4.setHeightForWidth(self.comboBox_Co_tornillo.sizePolicy().hasHeightForWidth())
        self.comboBox_Co_tornillo.setSizePolicy(sizePolicy4)
        self.comboBox_Co_tornillo.setCursor(QCursor(Qt.PointingHandCursor))
        self.comboBox_Co_tornillo.setStyleSheet(u"QComboBox {\n"
"    font-size: 11px; /* Cambia el tama\u00f1o de la fuente en el QComboBox */\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"	background: transparent;\n"
"    background-color: #FFFFFF; /* Cambia el color de fondo de las opciones\n"
"	 desplegadas a blanco */\n"
"	color: #000000; /* Cambia el color del texto a negro */\n"
"}")

        self.gridLayout_5.addWidget(self.comboBox_Co_tornillo, 8, 1, 1, 1)

        self.lineEdit_PH_tornillo = QLineEdit(self.groupBox)
        self.lineEdit_PH_tornillo.setObjectName(u"lineEdit_PH_tornillo")
        self.lineEdit_PH_tornillo.setStyleSheet(u"")

        self.gridLayout_5.addWidget(self.lineEdit_PH_tornillo, 14, 1, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_4, 16, 1, 1, 1)


        self.gridLayout_10.addWidget(self.groupBox, 1, 0, 1, 1)

        self.groupBox_10 = QGroupBox(self.groupBox_3)
        self.groupBox_10.setObjectName(u"groupBox_10")
        sizePolicy5 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.groupBox_10.sizePolicy().hasHeightForWidth())
        self.groupBox_10.setSizePolicy(sizePolicy5)
        self.groupBox_10.setStyleSheet(u"\n"
"QLineEdit:focus{\n"
"    border: 1px solid rgb(189, 147, 249);\n"
"}\n"
"QGroupBox {\n"
"    	font: 700 20pt \"Georgia\";\n"
"    border: 10px;\n"
"	margin: 10px;\n"
"\n"
"	/*font: 350 20pt \"Yu Gothic UI Semilight\";*/\n"
" \n"
"}\n"
"\n"
"QGroupBox{border: 2px}")
        self.gridLayout_4 = QGridLayout(self.groupBox_10)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setVerticalSpacing(20)
        self.gridLayout_4.setContentsMargins(-1, 0, -1, -1)
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_3, 13, 1, 1, 1)

        self.pushButton_8 = QPushButton(self.groupBox_10)
        self.pushButton_8.setObjectName(u"pushButton_8")
        sizePolicy6 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.pushButton_8.sizePolicy().hasHeightForWidth())
        self.pushButton_8.setSizePolicy(sizePolicy6)
        self.pushButton_8.setMinimumSize(QSize(450, 430))
        self.pushButton_8.setStyleSheet(u"QPushButton {\n"
"    background-image: url(:/images/images/icons/tornillo-grande-removebg-preview.png);\n"
"    background-repeat: no-repeat;\n"
"background-position: center 60px ; /* Puedes ajustar la posici\u00f3n */\n"
"}")

        self.gridLayout_4.addWidget(self.pushButton_8, 6, 1, 1, 1)


        self.gridLayout_10.addWidget(self.groupBox_10, 1, 1, 1, 1)

        self.modos_tornillo = QComboBox(self.groupBox_3)
        self.modos_tornillo.addItem("")
        self.modos_tornillo.addItem("")
        self.modos_tornillo.addItem("")
        self.modos_tornillo.addItem("")
        self.modos_tornillo.addItem("")
        self.modos_tornillo.addItem("")
        self.modos_tornillo.addItem("")
        self.modos_tornillo.addItem("")
        self.modos_tornillo.setObjectName(u"modos_tornillo")
        self.modos_tornillo.setStyleSheet(u"QComboBox QAbstractItemView {\n"
"	background: transparent;\n"
"    background-color: #FFFFFF; /* Cambia el color de fondo de las opciones\n"
"	 desplegadas a blanco */\n"
"	color: #000000; /* Cambia el color del texto a negro */\n"
"}")

        self.gridLayout_10.addWidget(self.modos_tornillo, 0, 0, 1, 1)


        self.horizontalLayout_17.addWidget(self.groupBox_3)


        self.verticalLayout.addWidget(self.widget)

        self.stackedWidget.addWidget(self.tornillo)
        self.elevadores = QWidget()
        self.elevadores.setObjectName(u"elevadores")
        self.verticalLayout_20 = QVBoxLayout(self.elevadores)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.widget_6 = QWidget(self.elevadores)
        self.widget_6.setObjectName(u"widget_6")
        self.gridLayout_9 = QGridLayout(self.widget_6)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.groupBox_30 = QGroupBox(self.widget_6)
        self.groupBox_30.setObjectName(u"groupBox_30")
        self.groupBox_30.setStyleSheet(u"QGroupBox {\n"
"    border: 2px;\n"
"	font: 600 12pt \"Bookman Old Style\";\n"
"    margin-top: 13px; /* Ajusta el margen superior seg\u00fan tus necesidades */\n"
"    padding-top: 30px; /* Ajusta el espaciado superior seg\u00fan tus necesidades */\n"
"}\n"
"")
        self.groupBox_30.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.gridLayout_23 = QGridLayout(self.groupBox_30)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.gridLayout_23.setVerticalSpacing(4)
        self.gridLayout_23.setContentsMargins(-1, 0, -1, 0)
        self.groupBox_6 = QGroupBox(self.groupBox_30)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setStyleSheet(u"QGroupBox {\n"
"    border: 1px solid rgba(128, 128, 128, 0.5); /* Ajusta la opacidad seg\u00fan tus necesidades */\n"
"    margin-top: 10px; /* Ajusta el margen superior seg\u00fan tus necesidades */\n"
"    padding-top: 20px; /* Ajusta el espaciado superior seg\u00fan tus necesidades */\n"
"	\n"
"	font: 600 12pt \"Bookman Old Style\";\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"    border: 1px solid rgb(189, 147, 249);\n"
"}\n"
"")
        self.groupBox_6.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.gridLayout_8 = QGridLayout(self.groupBox_6)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setHorizontalSpacing(9)
        self.gridLayout_8.setContentsMargins(-1, 10, -1, 10)
        self.label_39 = QLabel(self.groupBox_6)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_8.addWidget(self.label_39, 14, 3, 1, 1)

        self.lineEdit_pp_elevador = QLineEdit(self.groupBox_6)
        self.lineEdit_pp_elevador.setObjectName(u"lineEdit_pp_elevador")
        self.lineEdit_pp_elevador.setEnabled(False)
        self.lineEdit_pp_elevador.setStyleSheet(u"background-color: lightgray;")

        self.gridLayout_8.addWidget(self.lineEdit_pp_elevador, 10, 4, 1, 1)

        self.label_45 = QLabel(self.groupBox_6)
        self.label_45.setObjectName(u"label_45")

        self.gridLayout_8.addWidget(self.label_45, 22, 3, 1, 1)

        self.lineEdit_n_elevador = QLineEdit(self.groupBox_6)
        self.lineEdit_n_elevador.setObjectName(u"lineEdit_n_elevador")
        self.lineEdit_n_elevador.setStyleSheet(u"")

        self.gridLayout_8.addWidget(self.lineEdit_n_elevador, 22, 4, 1, 1)

        self.comboBox_tipo_elevador = QComboBox(self.groupBox_6)
        self.comboBox_tipo_elevador.addItem("")
        self.comboBox_tipo_elevador.addItem("")
        self.comboBox_tipo_elevador.addItem("")
        self.comboBox_tipo_elevador.addItem("")
        self.comboBox_tipo_elevador.setObjectName(u"comboBox_tipo_elevador")
        self.comboBox_tipo_elevador.setCursor(QCursor(Qt.PointingHandCursor))
        self.comboBox_tipo_elevador.setStyleSheet(u"QComboBox {\n"
"    font-size: 11px; /* Cambia el tama\u00f1o de la fuente en el QComboBox */\n"
"}\n"
"\n"
"\n"
"QComboBox QAbstractItemView {\n"
"	background: #FFFFFF;\n"
"    background-color: #FFFFFF; /* Cambia el color de fondo de las opciones\n"
"	 desplegadas a blanco */\n"
"	color: #000000; /* Cambia el color del texto a negro */\n"
"}\n"
"\n"
"")

        self.gridLayout_8.addWidget(self.comboBox_tipo_elevador, 7, 4, 1, 1)

        self.label_35 = QLabel(self.groupBox_6)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_8.addWidget(self.label_35, 3, 3, 1, 1)

        self.label_38 = QLabel(self.groupBox_6)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_8.addWidget(self.label_38, 7, 3, 1, 1)

        self.lineEdit_t_elevador = QLineEdit(self.groupBox_6)
        self.lineEdit_t_elevador.setObjectName(u"lineEdit_t_elevador")
        self.lineEdit_t_elevador.setStyleSheet(u"")

        self.gridLayout_8.addWidget(self.lineEdit_t_elevador, 14, 4, 1, 1)

        self.lineEdit_cte_elevador = QLineEdit(self.groupBox_6)
        self.lineEdit_cte_elevador.setObjectName(u"lineEdit_cte_elevador")
        self.lineEdit_cte_elevador.setEnabled(False)
        self.lineEdit_cte_elevador.setStyleSheet(u"background-color: lightgray;")

        self.gridLayout_8.addWidget(self.lineEdit_cte_elevador, 11, 4, 1, 1)

        self.comboBox_sistema_elevador = QComboBox(self.groupBox_6)
        self.comboBox_sistema_elevador.addItem("")
        self.comboBox_sistema_elevador.addItem("")
        self.comboBox_sistema_elevador.addItem("")
        self.comboBox_sistema_elevador.setObjectName(u"comboBox_sistema_elevador")
        self.comboBox_sistema_elevador.setCursor(QCursor(Qt.PointingHandCursor))
        self.comboBox_sistema_elevador.setStyleSheet(u"QComboBox {\n"
"    font-size: 11px; /* Cambia el tama\u00f1o de la fuente en el QComboBox */\n"
"}\n"
"\n"
"\n"
"QComboBox QAbstractItemView {\n"
"	background: transparent;\n"
"    background-color: #FFFFFF; /* Cambia el color de fondo de las opciones\n"
"	 desplegadas a blanco */\n"
"	color: #000000; /* Cambia el color del texto a negro */\n"
"}")

        self.gridLayout_8.addWidget(self.comboBox_sistema_elevador, 21, 4, 1, 1)

        self.label_33 = QLabel(self.groupBox_6)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_8.addWidget(self.label_33, 1, 3, 1, 1)

        self.lineEdit_tc_elevador = QLineEdit(self.groupBox_6)
        self.lineEdit_tc_elevador.setObjectName(u"lineEdit_tc_elevador")
        self.lineEdit_tc_elevador.setEnabled(False)
        self.lineEdit_tc_elevador.setStyleSheet(u"background-color: lightgray;")

        self.gridLayout_8.addWidget(self.lineEdit_tc_elevador, 12, 4, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_8.addItem(self.verticalSpacer_5, 24, 4, 1, 1)

        self.lineEdit_h_elevador = QLineEdit(self.groupBox_6)
        self.lineEdit_h_elevador.setObjectName(u"lineEdit_h_elevador")
        self.lineEdit_h_elevador.setEnabled(False)
        self.lineEdit_h_elevador.setStyleSheet(u"background-color: lightgray;")

        self.gridLayout_8.addWidget(self.lineEdit_h_elevador, 9, 4, 1, 1)

        self.label_41 = QLabel(self.groupBox_6)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_8.addWidget(self.label_41, 18, 3, 1, 1)

        self.label_55 = QLabel(self.groupBox_6)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_8.addWidget(self.label_55, 12, 3, 1, 1)

        self.label_42 = QLabel(self.groupBox_6)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_8.addWidget(self.label_42, 11, 3, 1, 1)

        self.label_44 = QLabel(self.groupBox_6)
        self.label_44.setObjectName(u"label_44")

        self.gridLayout_8.addWidget(self.label_44, 8, 3, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_8.addItem(self.verticalSpacer_2, 23, 4, 1, 1)

        self.lineEdit_H_elevador = QLineEdit(self.groupBox_6)
        self.lineEdit_H_elevador.setObjectName(u"lineEdit_H_elevador")
        self.lineEdit_H_elevador.setStyleSheet(u"")

        self.gridLayout_8.addWidget(self.lineEdit_H_elevador, 18, 4, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_8.addItem(self.verticalSpacer, 25, 4, 1, 1)

        self.label_56 = QLabel(self.groupBox_6)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_8.addWidget(self.label_56, 9, 3, 1, 1)

        self.lineEdit_v_elevador = QLineEdit(self.groupBox_6)
        self.lineEdit_v_elevador.setObjectName(u"lineEdit_v_elevador")
        self.lineEdit_v_elevador.setStyleSheet(u"")

        self.gridLayout_8.addWidget(self.lineEdit_v_elevador, 5, 4, 1, 1)

        self.label_37 = QLabel(self.groupBox_6)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_8.addWidget(self.label_37, 5, 3, 1, 1)

        self.label_34 = QLabel(self.groupBox_6)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_8.addWidget(self.label_34, 2, 3, 1, 1)

        self.lineEdit_i_elevador = QLineEdit(self.groupBox_6)
        self.lineEdit_i_elevador.setObjectName(u"lineEdit_i_elevador")
        self.lineEdit_i_elevador.setStyleSheet(u"")

        self.gridLayout_8.addWidget(self.lineEdit_i_elevador, 1, 4, 1, 1)

        self.label_43 = QLabel(self.groupBox_6)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_8.addWidget(self.label_43, 21, 3, 1, 1)

        self.lineEdit_j_elevador = QLineEdit(self.groupBox_6)
        self.lineEdit_j_elevador.setObjectName(u"lineEdit_j_elevador")
        self.lineEdit_j_elevador.setStyleSheet(u"")

        self.gridLayout_8.addWidget(self.lineEdit_j_elevador, 3, 4, 1, 1)

        self.comboBox_Tparticula_elevador = QComboBox(self.groupBox_6)
        self.comboBox_Tparticula_elevador.addItem("")
        self.comboBox_Tparticula_elevador.addItem("")
        self.comboBox_Tparticula_elevador.addItem("")
        self.comboBox_Tparticula_elevador.addItem("")
        self.comboBox_Tparticula_elevador.setObjectName(u"comboBox_Tparticula_elevador")
        self.comboBox_Tparticula_elevador.setEnabled(False)
        self.comboBox_Tparticula_elevador.setCursor(QCursor(Qt.PointingHandCursor))
        self.comboBox_Tparticula_elevador.setStyleSheet(u"QComboBox {\n"
"background-color: lightgray;\n"
"    font-size: 11px; /* Cambia el tama\u00f1o de la fuente en el QComboBox */\n"
"}\n"
"\n"
"\n"
"QComboBox QAbstractItemView {\n"
"	background: #FFFFFF;\n"
"    background-color: #FFFFFF; /* Cambia el color de fondo de las opciones\n"
"	 desplegadas a blanco */\n"
"	color: #000000; /* Cambia el color del texto a negro */\n"
"}")

        self.gridLayout_8.addWidget(self.comboBox_Tparticula_elevador, 8, 4, 1, 1)

        self.lineEdit_p_elevador = QLineEdit(self.groupBox_6)
        self.lineEdit_p_elevador.setObjectName(u"lineEdit_p_elevador")
        self.lineEdit_p_elevador.setStyleSheet(u"")

        self.gridLayout_8.addWidget(self.lineEdit_p_elevador, 2, 4, 1, 1)

        self.label_5 = QLabel(self.groupBox_6)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_8.addWidget(self.label_5, 10, 3, 1, 1)


        self.gridLayout_23.addWidget(self.groupBox_6, 2, 0, 1, 1)

        self.calculate_elevador = QPushButton(self.groupBox_30)
        self.calculate_elevador.setObjectName(u"calculate_elevador")
        self.calculate_elevador.setCursor(QCursor(Qt.PointingHandCursor))
        self.calculate_elevador.setStyleSheet(u"QPushButton{\n"
"    border: 1px solid black;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    font-size: 15px;\n"
"	\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(0, 255, 69);\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	padding-left:5px;\n"
"	padding-top:5px;\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(211, 255, 102, 255), stop:0.55 rgba(139, 235, 44, 255), stop:0.98 rgba(9, 146, 76, 149), stop:1 rgba(0, 0, 0, 0));\n"
"}")

        self.gridLayout_23.addWidget(self.calculate_elevador, 3, 1, 1, 1)

        self.reset_elevador = QPushButton(self.groupBox_30)
        self.reset_elevador.setObjectName(u"reset_elevador")
        self.reset_elevador.setCursor(QCursor(Qt.PointingHandCursor))
        self.reset_elevador.setStyleSheet(u"QPushButton{\n"
"    border: 1px solid black;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    font-size: 15px;\n"
"	\n"
"	font: 300 9pt \"Bookman Old Style\";\n"
"	background-color: rgb(255, 44, 44);\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	padding-left:5px;\n"
"	padding-top:5px;\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(53, 21, 21, 255), stop:0.55 rgba(235, 93, 44, 255), stop:0.98 rgba(146, 91, 9, 255), stop:1 rgba(0, 0, 0, 0));\n"
"}\n"
"")

        self.gridLayout_23.addWidget(self.reset_elevador, 3, 0, 1, 1)

        self.combo_modos_elevador = QComboBox(self.groupBox_30)
        self.combo_modos_elevador.addItem("")
        self.combo_modos_elevador.addItem("")
        self.combo_modos_elevador.addItem("")
        self.combo_modos_elevador.addItem("")
        self.combo_modos_elevador.addItem("")
        self.combo_modos_elevador.addItem("")
        self.combo_modos_elevador.addItem("")
        self.combo_modos_elevador.addItem("")
        self.combo_modos_elevador.setObjectName(u"combo_modos_elevador")
        self.combo_modos_elevador.setCursor(QCursor(Qt.PointingHandCursor))
        self.combo_modos_elevador.setStyleSheet(u"QComboBox QAbstractItemView {\n"
"	background: transparent;\n"
"    background-color: #FFFFFF; /* Cambia el color de fondo de las opciones\n"
"	 desplegadas a blanco */\n"
"	color: #000000; /* Cambia el color del texto a negro */\n"
"}")

        self.gridLayout_23.addWidget(self.combo_modos_elevador, 0, 0, 1, 1)

        self.groupBox_7 = QGroupBox(self.groupBox_30)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setStyleSheet(u"QGroupBox {\n"
"    border: 1px solid rgba(128, 128, 128, 0.5); /* Ajusta la opacidad seg\u00fan tus necesidades */\n"
"    margin-top: 10px; /* Ajusta el margen superior seg\u00fan tus necesidades */\n"
"    padding-top: 10px; /* Ajusta el espaciado superior seg\u00fan tus necesidades */\n"
"margin-botton: 5px; /* Ajusta el margen superior seg\u00fan tus necesidades */\n"
"	\n"
"	font: 600 12pt \"Bookman Old Style\";\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"    border: 1px solid rgb(189, 147, 249);\n"
"}")
        self.formLayout_10 = QFormLayout(self.groupBox_7)
        self.formLayout_10.setObjectName(u"formLayout_10")
        self.formLayout_10.setHorizontalSpacing(10)
        self.formLayout_10.setVerticalSpacing(7)
        self.formLayout_10.setContentsMargins(-1, 10, -1, 0)
        self.label = QLabel(self.groupBox_7)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout_10.setWidget(1, QFormLayout.LabelRole, self.label)

        self.lineEdit_Pc_elevador = QLineEdit(self.groupBox_7)
        self.lineEdit_Pc_elevador.setObjectName(u"lineEdit_Pc_elevador")
        self.lineEdit_Pc_elevador.setStyleSheet(u"")

        self.formLayout_10.setWidget(1, QFormLayout.FieldRole, self.lineEdit_Pc_elevador)

        self.label_36 = QLabel(self.groupBox_7)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout_10.setWidget(2, QFormLayout.LabelRole, self.label_36)

        self.lineEdit_q_elevador = QLineEdit(self.groupBox_7)
        self.lineEdit_q_elevador.setObjectName(u"lineEdit_q_elevador")
        self.lineEdit_q_elevador.setStyleSheet(u"")

        self.formLayout_10.setWidget(2, QFormLayout.FieldRole, self.lineEdit_q_elevador)

        self.label_30 = QLabel(self.groupBox_7)
        self.label_30.setObjectName(u"label_30")

        self.formLayout_10.setWidget(4, QFormLayout.LabelRole, self.label_30)

        self.lineEdit_Na_elevador = QLineEdit(self.groupBox_7)
        self.lineEdit_Na_elevador.setObjectName(u"lineEdit_Na_elevador")
        self.lineEdit_Na_elevador.setStyleSheet(u"")

        self.formLayout_10.setWidget(4, QFormLayout.FieldRole, self.lineEdit_Na_elevador)

        self.label_40 = QLabel(self.groupBox_7)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout_10.setWidget(5, QFormLayout.LabelRole, self.label_40)

        self.lineEdit_Fa_elevador = QLineEdit(self.groupBox_7)
        self.lineEdit_Fa_elevador.setObjectName(u"lineEdit_Fa_elevador")
        self.lineEdit_Fa_elevador.setStyleSheet(u"")

        self.formLayout_10.setWidget(5, QFormLayout.FieldRole, self.lineEdit_Fa_elevador)

        self.label_14 = QLabel(self.groupBox_7)
        self.label_14.setObjectName(u"label_14")

        self.formLayout_10.setWidget(6, QFormLayout.LabelRole, self.label_14)

        self.lineEdit_FR_elevador = QLineEdit(self.groupBox_7)
        self.lineEdit_FR_elevador.setObjectName(u"lineEdit_FR_elevador")

        self.formLayout_10.setWidget(6, QFormLayout.FieldRole, self.lineEdit_FR_elevador)

        self.label_32 = QLabel(self.groupBox_7)
        self.label_32.setObjectName(u"label_32")

        self.formLayout_10.setWidget(7, QFormLayout.LabelRole, self.label_32)

        self.lineEdit_m_elevador = QLineEdit(self.groupBox_7)
        self.lineEdit_m_elevador.setObjectName(u"lineEdit_m_elevador")

        self.formLayout_10.setWidget(7, QFormLayout.FieldRole, self.lineEdit_m_elevador)

        self.label_46 = QLabel(self.groupBox_7)
        self.label_46.setObjectName(u"label_46")

        self.formLayout_10.setWidget(8, QFormLayout.LabelRole, self.label_46)

        self.lineEdit_Ta_elevador = QLineEdit(self.groupBox_7)
        self.lineEdit_Ta_elevador.setObjectName(u"lineEdit_Ta_elevador")
        self.lineEdit_Ta_elevador.setStyleSheet(u"")

        self.formLayout_10.setWidget(8, QFormLayout.FieldRole, self.lineEdit_Ta_elevador)

        self.label_47 = QLabel(self.groupBox_7)
        self.label_47.setObjectName(u"label_47")

        self.formLayout_10.setWidget(9, QFormLayout.LabelRole, self.label_47)

        self.comboBox_k_elevador = QComboBox(self.groupBox_7)
        self.comboBox_k_elevador.addItem("")
        self.comboBox_k_elevador.addItem("")
        self.comboBox_k_elevador.addItem("")
        self.comboBox_k_elevador.addItem("")
        self.comboBox_k_elevador.addItem("")
        self.comboBox_k_elevador.setObjectName(u"comboBox_k_elevador")
        sizePolicy7 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(250)
        sizePolicy7.setHeightForWidth(self.comboBox_k_elevador.sizePolicy().hasHeightForWidth())
        self.comboBox_k_elevador.setSizePolicy(sizePolicy7)
        self.comboBox_k_elevador.setMinimumSize(QSize(0, 20))
        self.comboBox_k_elevador.setCursor(QCursor(Qt.PointingHandCursor))
        self.comboBox_k_elevador.setStyleSheet(u"QComboBox {\n"
"    font-size: 11px; /* Cambia el tama\u00f1o de la fuente en el QComboBox */\n"
"}\n"
"\n"
"\n"
"QComboBox QAbstractItemView {\n"
"	background: transparent;\n"
"    background-color: #FFFFFF; /* Cambia el color de fondo de las opciones\n"
"	 desplegadas a blanco */\n"
"	color: #000000; /* Cambia el color del texto a negro */\n"
"}")

        self.formLayout_10.setWidget(9, QFormLayout.FieldRole, self.comboBox_k_elevador)

        self.label_198 = QLabel(self.groupBox_7)
        self.label_198.setObjectName(u"label_198")

        self.formLayout_10.setWidget(10, QFormLayout.LabelRole, self.label_198)

        self.lineEdit_D_elevador = QLineEdit(self.groupBox_7)
        self.lineEdit_D_elevador.setObjectName(u"lineEdit_D_elevador")

        self.formLayout_10.setWidget(10, QFormLayout.FieldRole, self.lineEdit_D_elevador)

        self.label_199 = QLabel(self.groupBox_7)
        self.label_199.setObjectName(u"label_199")

        self.formLayout_10.setWidget(11, QFormLayout.LabelRole, self.label_199)

        self.lineEdit_Nc_elevador = QLineEdit(self.groupBox_7)
        self.lineEdit_Nc_elevador.setObjectName(u"lineEdit_Nc_elevador")

        self.formLayout_10.setWidget(11, QFormLayout.FieldRole, self.lineEdit_Nc_elevador)

        self.label_52 = QLabel(self.groupBox_7)
        self.label_52.setObjectName(u"label_52")

        self.formLayout_10.setWidget(12, QFormLayout.LabelRole, self.label_52)

        self.lineEdit_sh_elevador = QLineEdit(self.groupBox_7)
        self.lineEdit_sh_elevador.setObjectName(u"lineEdit_sh_elevador")
        self.lineEdit_sh_elevador.setStyleSheet(u"")

        self.formLayout_10.setWidget(12, QFormLayout.FieldRole, self.lineEdit_sh_elevador)

        self.label_53 = QLabel(self.groupBox_7)
        self.label_53.setObjectName(u"label_53")

        self.formLayout_10.setWidget(13, QFormLayout.LabelRole, self.label_53)

        self.lineEdit_sv_elevador = QLineEdit(self.groupBox_7)
        self.lineEdit_sv_elevador.setObjectName(u"lineEdit_sv_elevador")
        self.lineEdit_sv_elevador.setStyleSheet(u"")

        self.formLayout_10.setWidget(13, QFormLayout.FieldRole, self.lineEdit_sv_elevador)

        self.label_54 = QLabel(self.groupBox_7)
        self.label_54.setObjectName(u"label_54")

        self.formLayout_10.setWidget(14, QFormLayout.LabelRole, self.label_54)

        self.lineEdit_a_elevador = QLineEdit(self.groupBox_7)
        self.lineEdit_a_elevador.setObjectName(u"lineEdit_a_elevador")
        self.lineEdit_a_elevador.setStyleSheet(u"")

        self.formLayout_10.setWidget(14, QFormLayout.FieldRole, self.lineEdit_a_elevador)

        self.label_57 = QLabel(self.groupBox_7)
        self.label_57.setObjectName(u"label_57")

        self.formLayout_10.setWidget(15, QFormLayout.LabelRole, self.label_57)

        self.lineEdit_s_elevador = QLineEdit(self.groupBox_7)
        self.lineEdit_s_elevador.setObjectName(u"lineEdit_s_elevador")
        self.lineEdit_s_elevador.setStyleSheet(u"")

        self.formLayout_10.setWidget(15, QFormLayout.FieldRole, self.lineEdit_s_elevador)

        self.label_48 = QLabel(self.groupBox_7)
        self.label_48.setObjectName(u"label_48")

        self.formLayout_10.setWidget(16, QFormLayout.LabelRole, self.label_48)

        self.lineEdit_alfa_elevador = QLineEdit(self.groupBox_7)
        self.lineEdit_alfa_elevador.setObjectName(u"lineEdit_alfa_elevador")

        self.formLayout_10.setWidget(16, QFormLayout.FieldRole, self.lineEdit_alfa_elevador)

        self.label_49 = QLabel(self.groupBox_7)
        self.label_49.setObjectName(u"label_49")

        self.formLayout_10.setWidget(17, QFormLayout.LabelRole, self.label_49)

        self.lineEdit_R_elevador = QLineEdit(self.groupBox_7)
        self.lineEdit_R_elevador.setObjectName(u"lineEdit_R_elevador")

        self.formLayout_10.setWidget(17, QFormLayout.FieldRole, self.lineEdit_R_elevador)


        self.gridLayout_23.addWidget(self.groupBox_7, 2, 1, 1, 1)


        self.gridLayout_9.addWidget(self.groupBox_30, 0, 0, 1, 2)


        self.verticalLayout_20.addWidget(self.widget_6)

        self.stackedWidget.addWidget(self.elevadores)
        self.molinos = QWidget()
        self.molinos.setObjectName(u"molinos")
        self.verticalLayout_16 = QVBoxLayout(self.molinos)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.widget_molinos = QWidget(self.molinos)
        self.widget_molinos.setObjectName(u"widget_molinos")
        self.gridLayout_2 = QGridLayout(self.widget_molinos)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget_14 = QWidget(self.widget_molinos)
        self.widget_14.setObjectName(u"widget_14")
        self.verticalLayout_31 = QVBoxLayout(self.widget_14)
        self.verticalLayout_31.setSpacing(0)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.top_molino = QFrame(self.widget_14)
        self.top_molino.setObjectName(u"top_molino")
        sizePolicy8 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(20)
        sizePolicy8.setHeightForWidth(self.top_molino.sizePolicy().hasHeightForWidth())
        self.top_molino.setSizePolicy(sizePolicy8)
        self.top_molino.setMinimumSize(QSize(0, 20))
        self.top_molino.setStyleSheet(u"QPushButton:hover {\n"
"    font-size: 15px;\n"
"	background-color: rgb(204, 232, 255);\n"
"\n"
"}\n"
"QPushButton {\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-radius: 0px;\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed{\n"
"	padding-left:5px;\n"
"	padding-top:5px;\n"
"	\n"
"	\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.1875 rgba(200, 147, 243, 224), stop:0.4375 rgba(181, 109, 239, 231), stop:0.715909 rgba(127, 92, 174, 242));\n"
"	}\n"
"")
        self.top_molino.setFrameShape(QFrame.StyledPanel)
        self.top_molino.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.top_molino)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.btn_molinobola = QPushButton(self.top_molino)
        self.btn_molinobola.setObjectName(u"btn_molinobola")
        self.btn_molinobola.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_molinobola.setStyleSheet(u"")

        self.horizontalLayout_16.addWidget(self.btn_molinobola)

        self.btn_molino_rodillo = QPushButton(self.top_molino)
        self.btn_molino_rodillo.setObjectName(u"btn_molino_rodillo")
        self.btn_molino_rodillo.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_molino_rodillo.setStyleSheet(u"")

        self.horizontalLayout_16.addWidget(self.btn_molino_rodillo)

        self.pushButton_trituradora_mand = QPushButton(self.top_molino)
        self.pushButton_trituradora_mand.setObjectName(u"pushButton_trituradora_mand")
        self.pushButton_trituradora_mand.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_trituradora_mand.setStyleSheet(u"")

        self.horizontalLayout_16.addWidget(self.pushButton_trituradora_mand)

        self.pushButton_trituradora_cono = QPushButton(self.top_molino)
        self.pushButton_trituradora_cono.setObjectName(u"pushButton_trituradora_cono")
        self.pushButton_trituradora_cono.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_trituradora_cono.setStyleSheet(u"")

        self.horizontalLayout_16.addWidget(self.pushButton_trituradora_cono)


        self.verticalLayout_31.addWidget(self.top_molino)

        self.stackedWidget_3 = QStackedWidget(self.widget_14)
        self.stackedWidget_3.setObjectName(u"stackedWidget_3")
        self.stackedWidget_3.setStyleSheet(u"")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.stackedWidget_3.addWidget(self.page)
        self.molino_bola = QWidget()
        self.molino_bola.setObjectName(u"molino_bola")
        self.gridLayout_19 = QGridLayout(self.molino_bola)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.widget_15 = QWidget(self.molino_bola)
        self.widget_15.setObjectName(u"widget_15")
        self.widget_15.setStyleSheet(u"QLineEdit:focus{\n"
"    border: 1px solid rgb(147, 0, 221);\n"
"}")
        self.horizontalLayout_18 = QHBoxLayout(self.widget_15)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(-1, 0, -1, 0)
        self.groupBox_8 = QGroupBox(self.widget_15)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.groupBox_8.setStyleSheet(u"QGroupBox {\n"
"    border: 2px;\n"
"	font: 600 12pt \"Bookman Old Style\";\n"
"    margin-top: 10px; /* Ajusta el margen superior seg\u00fan tus necesidades */\n"
"    padding-top: 30px; /* Ajusta el espaciado superior seg\u00fan tus necesidades */\n"
"}\n"
"\n"
"")
        self.groupBox_8.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.gridLayout_15 = QGridLayout(self.groupBox_8)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.gridLayout_15.setContentsMargins(-1, 0, -1, -1)
        self.groupBox_32 = QGroupBox(self.groupBox_8)
        self.groupBox_32.setObjectName(u"groupBox_32")
        self.groupBox_32.setStyleSheet(u"QGroupBox {\n"
"    border: 1px solid rgba(128, 128, 128, 0.5); /* Ajusta la opacidad seg\u00fan tus necesidades */\n"
"    margin-top: 10px; /* Ajusta el margen superior seg\u00fan tus necesidades */\n"
"    padding-top: 20px; /* Ajusta el espaciado superior seg\u00fan tus necesidades */\n"
"	\n"
"	font: 600 12pt \"Bookman Old Style\";\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"    border: 1px solid rgb(189, 147, 249);\n"
"}")
        self.gridLayout_16 = QGridLayout(self.groupBox_32)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.gridLayout_16.setContentsMargins(-1, 9, -1, 0)
        self.lineEditFactorCorrecionCapacidad = QLineEdit(self.groupBox_32)
        self.lineEditFactorCorrecionCapacidad.setObjectName(u"lineEditFactorCorrecionCapacidad")

        self.gridLayout_16.addWidget(self.lineEditFactorCorrecionCapacidad, 6, 1, 1, 1)

        self.lineEditCapacidadMolino = QLineEdit(self.groupBox_32)
        self.lineEditCapacidadMolino.setObjectName(u"lineEditCapacidadMolino")

        self.gridLayout_16.addWidget(self.lineEditCapacidadMolino, 9, 1, 1, 1)

        self.lineEditFrecuenciaCritica_2 = QLineEdit(self.groupBox_32)
        self.lineEditFrecuenciaCritica_2.setObjectName(u"lineEditFrecuenciaCritica_2")

        self.gridLayout_16.addWidget(self.lineEditFrecuenciaCritica_2, 2, 1, 1, 1)

        self.lineEditDesgasteBolas = QLineEdit(self.groupBox_32)
        self.lineEditDesgasteBolas.setObjectName(u"lineEditDesgasteBolas")

        self.gridLayout_16.addWidget(self.lineEditDesgasteBolas, 8, 1, 1, 1)

        self.lineEditFrecuenciaMolienda_2 = QLineEdit(self.groupBox_32)
        self.lineEditFrecuenciaMolienda_2.setObjectName(u"lineEditFrecuenciaMolienda_2")

        self.gridLayout_16.addWidget(self.lineEditFrecuenciaMolienda_2, 1, 1, 1, 1)

        self.lineEditIndiceBond = QLineEdit(self.groupBox_32)
        self.lineEditIndiceBond.setObjectName(u"lineEditIndiceBond")

        self.gridLayout_16.addWidget(self.lineEditIndiceBond, 5, 1, 1, 1)

        self.label_225 = QLabel(self.groupBox_32)
        self.label_225.setObjectName(u"label_225")

        self.gridLayout_16.addWidget(self.label_225, 4, 0, 1, 1)

        self.comboBoxTipoMolienda = QComboBox(self.groupBox_32)
        self.comboBoxTipoMolienda.addItem("")
        self.comboBoxTipoMolienda.addItem("")
        self.comboBoxTipoMolienda.setObjectName(u"comboBoxTipoMolienda")
        self.comboBoxTipoMolienda.setCursor(QCursor(Qt.PointingHandCursor))
        self.comboBoxTipoMolienda.setStyleSheet(u"QComboBox QAbstractItemView {\n"
"	background: transparent;\n"
"    background-color: #FFFFFF; /* Cambia el color de fondo de las opciones\n"
"	 desplegadas a blanco */\n"
"	color: #000000; /* Cambia el color del texto a negro */\n"
"}")

        self.gridLayout_16.addWidget(self.comboBoxTipoMolienda, 7, 1, 1, 1)

        self.lineEditPotenciaMolino = QLineEdit(self.groupBox_32)
        self.lineEditPotenciaMolino.setObjectName(u"lineEditPotenciaMolino")

        self.gridLayout_16.addWidget(self.lineEditPotenciaMolino, 10, 1, 1, 1)

        self.label_226 = QLabel(self.groupBox_32)
        self.label_226.setObjectName(u"label_226")

        self.gridLayout_16.addWidget(self.label_226, 7, 0, 1, 1)

        self.label_233 = QLabel(self.groupBox_32)
        self.label_233.setObjectName(u"label_233")

        self.gridLayout_16.addWidget(self.label_233, 0, 0, 1, 1)

        self.label_231 = QLabel(self.groupBox_32)
        self.label_231.setObjectName(u"label_231")

        self.gridLayout_16.addWidget(self.label_231, 10, 0, 1, 1)

        self.lineEditFraccionFrecuenciaC = QLineEdit(self.groupBox_32)
        self.lineEditFraccionFrecuenciaC.setObjectName(u"lineEditFraccionFrecuenciaC")

        self.gridLayout_16.addWidget(self.lineEditFraccionFrecuenciaC, 3, 1, 1, 1)

        self.label_229 = QLabel(self.groupBox_32)
        self.label_229.setObjectName(u"label_229")

        self.gridLayout_16.addWidget(self.label_229, 5, 0, 1, 1)

        self.label_227 = QLabel(self.groupBox_32)
        self.label_227.setObjectName(u"label_227")

        self.gridLayout_16.addWidget(self.label_227, 8, 0, 1, 1)

        self.label_72 = QLabel(self.groupBox_32)
        self.label_72.setObjectName(u"label_72")

        self.gridLayout_16.addWidget(self.label_72, 2, 0, 1, 1)

        self.label_230 = QLabel(self.groupBox_32)
        self.label_230.setObjectName(u"label_230")

        self.gridLayout_16.addWidget(self.label_230, 6, 0, 1, 1)

        self.verticalSpacer_12 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_16.addItem(self.verticalSpacer_12, 11, 1, 1, 1)

        self.label_73 = QLabel(self.groupBox_32)
        self.label_73.setObjectName(u"label_73")
        self.label_73.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_16.addWidget(self.label_73, 3, 0, 1, 1)

        self.lineEditIndiceAbrasion = QLineEdit(self.groupBox_32)
        self.lineEditIndiceAbrasion.setObjectName(u"lineEditIndiceAbrasion")

        self.gridLayout_16.addWidget(self.lineEditIndiceAbrasion, 4, 1, 1, 1)

        self.lineEditConstanteMolino = QLineEdit(self.groupBox_32)
        self.lineEditConstanteMolino.setObjectName(u"lineEditConstanteMolino")

        self.gridLayout_16.addWidget(self.lineEditConstanteMolino, 0, 1, 1, 1)

        self.label_228 = QLabel(self.groupBox_32)
        self.label_228.setObjectName(u"label_228")

        self.gridLayout_16.addWidget(self.label_228, 9, 0, 1, 1)

        self.label_71 = QLabel(self.groupBox_32)
        self.label_71.setObjectName(u"label_71")
        self.label_71.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_16.addWidget(self.label_71, 1, 0, 1, 1)


        self.gridLayout_15.addWidget(self.groupBox_32, 1, 1, 1, 1)

        self.comboBox_2 = QComboBox(self.groupBox_8)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.comboBox_2.setStyleSheet(u"QComboBox QAbstractItemView {\n"
"	background: transparent;\n"
"    background-color: #FFFFFF; /* Cambia el color de fondo de las opciones\n"
"	 desplegadas a blanco */\n"
"	color: #000000; /* Cambia el color del texto a negro */\n"
"}")

        self.gridLayout_15.addWidget(self.comboBox_2, 0, 0, 1, 1)

        self.botonLimpiar = QPushButton(self.groupBox_8)
        self.botonLimpiar.setObjectName(u"botonLimpiar")
        self.botonLimpiar.setCursor(QCursor(Qt.PointingHandCursor))
        self.botonLimpiar.setStyleSheet(u"\n"
"QPushButton:hover {\n"
"    font-size: 15px;\n"
"	\n"
"	background-color: rgb(255, 44, 44);\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	padding-left:5px;\n"
"	padding-top:5px;\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(53, 21, 21, 255), stop:0.55 rgba(235, 93, 44, 255), stop:0.98 rgba(146, 91, 9, 255), stop:1 rgba(0, 0, 0, 0));\n"
"}\n"
"")

        self.gridLayout_15.addWidget(self.botonLimpiar, 2, 0, 1, 1)

        self.groupBox_21 = QGroupBox(self.groupBox_8)
        self.groupBox_21.setObjectName(u"groupBox_21")
        self.groupBox_21.setStyleSheet(u"QGroupBox {\n"
"    border: 1px solid rgba(128, 128, 128, 0.5); /* Ajusta la opacidad seg\u00fan tus necesidades */\n"
"\n"
"	\n"
"	font: 600 12pt \"Bookman Old Style\";\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"    border: 1px solid rgb(189, 147, 249);\n"
"	\n"
"	\n"
"	\n"
"}")
        self.formLayout_8 = QFormLayout(self.groupBox_21)
        self.formLayout_8.setObjectName(u"formLayout_8")
        self.formLayout_8.setContentsMargins(-1, 0, -1, 9)
        self.label_68 = QLabel(self.groupBox_21)
        self.label_68.setObjectName(u"label_68")

        self.formLayout_8.setWidget(0, QFormLayout.LabelRole, self.label_68)

        self.lineEditSizeAlimento = QLineEdit(self.groupBox_21)
        self.lineEditSizeAlimento.setObjectName(u"lineEditSizeAlimento")

        self.formLayout_8.setWidget(0, QFormLayout.FieldRole, self.lineEditSizeAlimento)

        self.label_69 = QLabel(self.groupBox_21)
        self.label_69.setObjectName(u"label_69")

        self.formLayout_8.setWidget(1, QFormLayout.LabelRole, self.label_69)

        self.lineEditSizeProducto = QLineEdit(self.groupBox_21)
        self.lineEditSizeProducto.setObjectName(u"lineEditSizeProducto")

        self.formLayout_8.setWidget(1, QFormLayout.FieldRole, self.lineEditSizeProducto)

        self.label_70 = QLabel(self.groupBox_21)
        self.label_70.setObjectName(u"label_70")
        self.label_70.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout_8.setWidget(2, QFormLayout.LabelRole, self.label_70)

        self.lineEditDensidadAlimento = QLineEdit(self.groupBox_21)
        self.lineEditDensidadAlimento.setObjectName(u"lineEditDensidadAlimento")

        self.formLayout_8.setWidget(2, QFormLayout.FieldRole, self.lineEditDensidadAlimento)

        self.label_218 = QLabel(self.groupBox_21)
        self.label_218.setObjectName(u"label_218")
        self.label_218.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout_8.setWidget(3, QFormLayout.LabelRole, self.label_218)

        self.lineEditDensidadBolas = QLineEdit(self.groupBox_21)
        self.lineEditDensidadBolas.setObjectName(u"lineEditDensidadBolas")

        self.formLayout_8.setWidget(3, QFormLayout.FieldRole, self.lineEditDensidadBolas)

        self.label_74 = QLabel(self.groupBox_21)
        self.label_74.setObjectName(u"label_74")
        self.label_74.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout_8.setWidget(4, QFormLayout.LabelRole, self.label_74)

        self.lineEditDiametroMolino = QLineEdit(self.groupBox_21)
        self.lineEditDiametroMolino.setObjectName(u"lineEditDiametroMolino")

        self.formLayout_8.setWidget(4, QFormLayout.FieldRole, self.lineEditDiametroMolino)

        self.label_232 = QLabel(self.groupBox_21)
        self.label_232.setObjectName(u"label_232")

        self.formLayout_8.setWidget(5, QFormLayout.LabelRole, self.label_232)

        self.lineEditLongitudMolino = QLineEdit(self.groupBox_21)
        self.lineEditLongitudMolino.setObjectName(u"lineEditLongitudMolino")

        self.formLayout_8.setWidget(5, QFormLayout.FieldRole, self.lineEditLongitudMolino)

        self.label_219 = QLabel(self.groupBox_21)
        self.label_219.setObjectName(u"label_219")
        self.label_219.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout_8.setWidget(6, QFormLayout.LabelRole, self.label_219)

        self.lineEditPorosidadLecho = QLineEdit(self.groupBox_21)
        self.lineEditPorosidadLecho.setObjectName(u"lineEditPorosidadLecho")

        self.formLayout_8.setWidget(6, QFormLayout.FieldRole, self.lineEditPorosidadLecho)

        self.label_220 = QLabel(self.groupBox_21)
        self.label_220.setObjectName(u"label_220")
        self.label_220.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout_8.setWidget(7, QFormLayout.LabelRole, self.label_220)

        self.lineEditMasaRocas = QLineEdit(self.groupBox_21)
        self.lineEditMasaRocas.setObjectName(u"lineEditMasaRocas")

        self.formLayout_8.setWidget(7, QFormLayout.FieldRole, self.lineEditMasaRocas)

        self.label_221 = QLabel(self.groupBox_21)
        self.label_221.setObjectName(u"label_221")
        self.label_221.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout_8.setWidget(8, QFormLayout.LabelRole, self.label_221)

        self.lineEditMasaBolas = QLineEdit(self.groupBox_21)
        self.lineEditMasaBolas.setObjectName(u"lineEditMasaBolas")

        self.formLayout_8.setWidget(8, QFormLayout.FieldRole, self.lineEditMasaBolas)

        self.label_222 = QLabel(self.groupBox_21)
        self.label_222.setObjectName(u"label_222")
        self.label_222.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout_8.setWidget(9, QFormLayout.LabelRole, self.label_222)

        self.lineEditNumeroLevantadores = QLineEdit(self.groupBox_21)
        self.lineEditNumeroLevantadores.setObjectName(u"lineEditNumeroLevantadores")

        self.formLayout_8.setWidget(9, QFormLayout.FieldRole, self.lineEditNumeroLevantadores)

        self.label_234 = QLabel(self.groupBox_21)
        self.label_234.setObjectName(u"label_234")

        self.formLayout_8.setWidget(10, QFormLayout.LabelRole, self.label_234)

        self.lineEditSizeBolas = QLineEdit(self.groupBox_21)
        self.lineEditSizeBolas.setObjectName(u"lineEditSizeBolas")

        self.formLayout_8.setWidget(10, QFormLayout.FieldRole, self.lineEditSizeBolas)

        self.label_223 = QLabel(self.groupBox_21)
        self.label_223.setObjectName(u"label_223")
        self.label_223.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout_8.setWidget(11, QFormLayout.LabelRole, self.label_223)

        self.lineEditFraccionRocas = QLineEdit(self.groupBox_21)
        self.lineEditFraccionRocas.setObjectName(u"lineEditFraccionRocas")

        self.formLayout_8.setWidget(11, QFormLayout.FieldRole, self.lineEditFraccionRocas)

        self.label_224 = QLabel(self.groupBox_21)
        self.label_224.setObjectName(u"label_224")
        self.label_224.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout_8.setWidget(12, QFormLayout.LabelRole, self.label_224)

        self.lineEditFraccionBolas = QLineEdit(self.groupBox_21)
        self.lineEditFraccionBolas.setObjectName(u"lineEditFraccionBolas")

        self.formLayout_8.setWidget(12, QFormLayout.FieldRole, self.lineEditFraccionBolas)


        self.gridLayout_15.addWidget(self.groupBox_21, 1, 0, 1, 1)

        self.botonCalcular = QPushButton(self.groupBox_8)
        self.botonCalcular.setObjectName(u"botonCalcular")
        self.botonCalcular.setCursor(QCursor(Qt.PointingHandCursor))
        self.botonCalcular.setStyleSheet(u"\n"
"QPushButton:hover {\n"
"    font-size: 15px;\n"
"	\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(0, 255, 69);\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	padding-left:5px;\n"
"	padding-top:5px;\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(211, 255, 102, 255), stop:0.55 rgba(139, 235, 44, 255), stop:0.98 rgba(9, 146, 76, 149), stop:1 rgba(0, 0, 0, 0));\n"
"}")

        self.gridLayout_15.addWidget(self.botonCalcular, 2, 1, 1, 1)


        self.horizontalLayout_18.addWidget(self.groupBox_8)


        self.gridLayout_19.addWidget(self.widget_15, 0, 0, 1, 1)

        self.stackedWidget_3.addWidget(self.molino_bola)
        self.molino_cono = QWidget()
        self.molino_cono.setObjectName(u"molino_cono")
        self.verticalLayout_33 = QVBoxLayout(self.molino_cono)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(-1, 9, -1, 9)
        self.widget_18 = QWidget(self.molino_cono)
        self.widget_18.setObjectName(u"widget_18")
        self.horizontalLayout_25 = QHBoxLayout(self.widget_18)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(-1, 9, -1, -1)
        self.groupBox_26 = QGroupBox(self.widget_18)
        self.groupBox_26.setObjectName(u"groupBox_26")
        self.groupBox_26.setStyleSheet(u"QGroupBox {\n"
"    border: 2px;\n"
"	font: 600 12pt \"Bookman Old Style\";\n"
"    margin-top: 10px; /* Ajusta el margen superior seg\u00fan tus necesidades */\n"
"    padding-top: 30px; /* Ajusta el espaciado superior seg\u00fan tus necesidades */\n"
"}\n"
"\n"
"")
        self.groupBox_26.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.gridLayout_13 = QGridLayout(self.groupBox_26)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_13.setContentsMargins(-1, 0, -1, 9)
        self.groupBox_29 = QGroupBox(self.groupBox_26)
        self.groupBox_29.setObjectName(u"groupBox_29")
        self.groupBox_29.setStyleSheet(u"QGroupBox {\n"
"    border: 1px solid rgba(128, 128, 128, 0.5); /* Ajusta la opacidad seg\u00fan tus necesidades */\n"
"    margin-top: 10px; /* Ajusta el margen superior seg\u00fan tus necesidades */\n"
"    padding-top: 20px; /* Ajusta el espaciado superior seg\u00fan tus necesidades */\n"
"	\n"
"	font: 600 12pt \"Bookman Old Style\";\n"
"}")
        self.formLayout_9 = QFormLayout(self.groupBox_29)
        self.formLayout_9.setObjectName(u"formLayout_9")
        self.formLayout_9.setContentsMargins(-1, 7, 25, 0)
        self.label_237 = QLabel(self.groupBox_29)
        self.label_237.setObjectName(u"label_237")

        self.formLayout_9.setWidget(0, QFormLayout.LabelRole, self.label_237)

        self.lineEditFactorK = QLineEdit(self.groupBox_29)
        self.lineEditFactorK.setObjectName(u"lineEditFactorK")

        self.formLayout_9.setWidget(0, QFormLayout.FieldRole, self.lineEditFactorK)

        self.label_58 = QLabel(self.groupBox_29)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout_9.setWidget(1, QFormLayout.LabelRole, self.label_58)

        self.lineEditRelacionR = QLineEdit(self.groupBox_29)
        self.lineEditRelacionR.setObjectName(u"lineEditRelacionR")

        self.formLayout_9.setWidget(1, QFormLayout.FieldRole, self.lineEditRelacionR)

        self.lineEditCapacidadCono = QLineEdit(self.groupBox_29)
        self.lineEditCapacidadCono.setObjectName(u"lineEditCapacidadCono")

        self.formLayout_9.setWidget(2, QFormLayout.FieldRole, self.lineEditCapacidadCono)

        self.label_67 = QLabel(self.groupBox_29)
        self.label_67.setObjectName(u"label_67")

        self.formLayout_9.setWidget(2, QFormLayout.LabelRole, self.label_67)

        self.lineEditOtroIndiceCono = QLineEdit(self.groupBox_29)
        self.lineEditOtroIndiceCono.setObjectName(u"lineEditOtroIndiceCono")

        self.formLayout_9.setWidget(3, QFormLayout.FieldRole, self.lineEditOtroIndiceCono)

        self.label_59 = QLabel(self.groupBox_29)
        self.label_59.setObjectName(u"label_59")

        self.formLayout_9.setWidget(3, QFormLayout.LabelRole, self.label_59)

        self.label_64 = QLabel(self.groupBox_29)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout_9.setWidget(4, QFormLayout.LabelRole, self.label_64)

        self.lineEditPotenciaCono = QLineEdit(self.groupBox_29)
        self.lineEditPotenciaCono.setObjectName(u"lineEditPotenciaCono")

        self.formLayout_9.setWidget(4, QFormLayout.FieldRole, self.lineEditPotenciaCono)


        self.gridLayout_13.addWidget(self.groupBox_29, 1, 1, 1, 1)

        self.comboBox_3 = QComboBox(self.groupBox_26)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.comboBox_3.setStyleSheet(u"QComboBox QAbstractItemView {\n"
"	background: transparent;\n"
"    background-color: #FFFFFF; /* Cambia el color de fondo de las opciones\n"
"	 desplegadas a blanco */\n"
"	color: #000000; /* Cambia el color del texto a negro */\n"
"}")

        self.gridLayout_13.addWidget(self.comboBox_3, 0, 0, 1, 1)

        self.groupBox_27 = QGroupBox(self.groupBox_26)
        self.groupBox_27.setObjectName(u"groupBox_27")
        self.groupBox_27.setStyleSheet(u"QGroupBox {\n"
"    border: 1px solid rgba(128, 128, 128, 0.5); /* Ajusta la opacidad seg\u00fan tus necesidades */\n"
"    margin-top: 10px; /* Ajusta el margen superior seg\u00fan tus necesidades */\n"
"    padding-top: 20px; /* Ajusta el espaciado superior seg\u00fan tus necesidades */\n"
"	\n"
"	font: 600 12pt \"Bookman Old Style\";\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"    border: 1px solid rgb(189, 147, 249);\n"
"}")
        self.gridLayout_12 = QGridLayout(self.groupBox_27)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setHorizontalSpacing(6)
        self.gridLayout_12.setVerticalSpacing(7)
        self.gridLayout_12.setContentsMargins(-1, 9, 9, 9)
        self.lineEditDensidadAlimento_2 = QLineEdit(self.groupBox_27)
        self.lineEditDensidadAlimento_2.setObjectName(u"lineEditDensidadAlimento_2")

        self.gridLayout_12.addWidget(self.lineEditDensidadAlimento_2, 6, 1, 1, 1)

        self.lineEditLminCono = QLineEdit(self.groupBox_27)
        self.lineEditLminCono.setObjectName(u"lineEditLminCono")

        self.gridLayout_12.addWidget(self.lineEditLminCono, 7, 1, 1, 1)

        self.label_61 = QLabel(self.groupBox_27)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_12.addWidget(self.label_61, 8, 0, 1, 1)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_12.addItem(self.verticalSpacer_8, 12, 1, 1, 1)

        self.label_24 = QLabel(self.groupBox_27)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_12.addWidget(self.label_24, 4, 0, 1, 1)

        self.lineEditSizeProducto_2 = QLineEdit(self.groupBox_27)
        self.lineEditSizeProducto_2.setObjectName(u"lineEditSizeProducto_2")

        self.gridLayout_12.addWidget(self.lineEditSizeProducto_2, 1, 1, 1, 1)

        self.lineEditSizeMayor_2 = QLineEdit(self.groupBox_27)
        self.lineEditSizeMayor_2.setObjectName(u"lineEditSizeMayor_2")

        self.gridLayout_12.addWidget(self.lineEditSizeMayor_2, 2, 1, 1, 1)

        self.label_236 = QLabel(self.groupBox_27)
        self.label_236.setObjectName(u"label_236")

        self.gridLayout_12.addWidget(self.label_236, 1, 0, 1, 1)

        self.label_63 = QLabel(self.groupBox_27)
        self.label_63.setObjectName(u"label_63")
        self.label_63.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_12.addWidget(self.label_63, 5, 0, 1, 1)

        self.label_62 = QLabel(self.groupBox_27)
        self.label_62.setObjectName(u"label_62")

        self.gridLayout_12.addWidget(self.label_62, 2, 0, 1, 1)

        self.label_31 = QLabel(self.groupBox_27)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_12.addWidget(self.label_31, 3, 0, 1, 1)

        self.lineEditDiametroBowl = QLineEdit(self.groupBox_27)
        self.lineEditDiametroBowl.setObjectName(u"lineEditDiametroBowl")

        self.gridLayout_12.addWidget(self.lineEditDiametroBowl, 5, 1, 1, 1)

        self.lineEditSizeAlimento_2 = QLineEdit(self.groupBox_27)
        self.lineEditSizeAlimento_2.setObjectName(u"lineEditSizeAlimento_2")

        self.gridLayout_12.addWidget(self.lineEditSizeAlimento_2, 0, 1, 1, 1)

        self.label_235 = QLabel(self.groupBox_27)
        self.label_235.setObjectName(u"label_235")

        self.gridLayout_12.addWidget(self.label_235, 0, 0, 1, 1)

        self.lineEditGape_2 = QLineEdit(self.groupBox_27)
        self.lineEditGape_2.setObjectName(u"lineEditGape_2")

        self.gridLayout_12.addWidget(self.lineEditGape_2, 4, 1, 1, 1)

        self.label_60 = QLabel(self.groupBox_27)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_12.addWidget(self.label_60, 7, 0, 1, 1)

        self.lineEditSetCono = QLineEdit(self.groupBox_27)
        self.lineEditSetCono.setObjectName(u"lineEditSetCono")

        self.gridLayout_12.addWidget(self.lineEditSetCono, 3, 1, 1, 1)

        self.label_238 = QLabel(self.groupBox_27)
        self.label_238.setObjectName(u"label_238")

        self.gridLayout_12.addWidget(self.label_238, 6, 0, 1, 1)

        self.lineEditLmax = QLineEdit(self.groupBox_27)
        self.lineEditLmax.setObjectName(u"lineEditLmax")

        self.gridLayout_12.addWidget(self.lineEditLmax, 8, 1, 1, 1)


        self.gridLayout_13.addWidget(self.groupBox_27, 1, 0, 1, 1)

        self.botonLimpiar_3 = QPushButton(self.groupBox_26)
        self.botonLimpiar_3.setObjectName(u"botonLimpiar_3")
        self.botonLimpiar_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.botonLimpiar_3.setStyleSheet(u"\n"
"\n"
"QPushButton:hover {\n"
"    font-size: 15px;\n"
"	\n"
"	background-color: rgb(255, 44, 44);\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	padding-left:5px;\n"
"	padding-top:5px;\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(53, 21, 21, 255), stop:0.55 rgba(235, 93, 44, 255), stop:0.98 rgba(146, 91, 9, 255), stop:1 rgba(0, 0, 0, 0));\n"
"}\n"
"")

        self.gridLayout_13.addWidget(self.botonLimpiar_3, 2, 0, 1, 1)

        self.botonCalcular_3 = QPushButton(self.groupBox_26)
        self.botonCalcular_3.setObjectName(u"botonCalcular_3")
        self.botonCalcular_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.botonCalcular_3.setStyleSheet(u"\n"
"QPushButton:hover {\n"
"    font-size: 15px;\n"
"	\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(0, 255, 69);\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	padding-left:5px;\n"
"	padding-top:5px;\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(211, 255, 102, 255), stop:0.55 rgba(139, 235, 44, 255), stop:0.98 rgba(9, 146, 76, 149), stop:1 rgba(0, 0, 0, 0));\n"
"}")

        self.gridLayout_13.addWidget(self.botonCalcular_3, 2, 1, 1, 1)


        self.horizontalLayout_25.addWidget(self.groupBox_26)


        self.verticalLayout_33.addWidget(self.widget_18)

        self.stackedWidget_3.addWidget(self.molino_cono)
        self.molino_rodillo = QWidget()
        self.molino_rodillo.setObjectName(u"molino_rodillo")
        self.horizontalLayout_20 = QHBoxLayout(self.molino_rodillo)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.widget_17 = QWidget(self.molino_rodillo)
        self.widget_17.setObjectName(u"widget_17")
        self.horizontalLayout_21 = QHBoxLayout(self.widget_17)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(-1, 0, -1, 0)
        self.groupBox_24 = QGroupBox(self.widget_17)
        self.groupBox_24.setObjectName(u"groupBox_24")
        self.groupBox_24.setStyleSheet(u"QGroupBox {\n"
"    border: 2px;\n"
"	font: 600 12pt \"Bookman Old Style\";\n"
"    margin-top: 13px; /* Ajusta el margen superior seg\u00fan tus necesidades */\n"
"    padding-top: 30px; /* Ajusta el espaciado superior seg\u00fan tus necesidades */\n"
"}\n"
"\n"
"")
        self.groupBox_24.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.gridLayout_11 = QGridLayout(self.groupBox_24)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setContentsMargins(9, 0, -1, -1)
        self.groupBox_28 = QGroupBox(self.groupBox_24)
        self.groupBox_28.setObjectName(u"groupBox_28")
        self.groupBox_28.setStyleSheet(u"QGroupBox {\n"
"    border: 1px solid rgba(128, 128, 128, 0.5); /* Ajusta la opacidad seg\u00fan tus necesidades */\n"
"    margin-top: 10px; /* Ajusta el margen superior seg\u00fan tus necesidades */\n"
"    padding-top: 20px; /* Ajusta el espaciado superior seg\u00fan tus necesidades */\n"
"	\n"
"	font: 600 12pt \"Bookman Old Style\";\n"
"\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"    border: 1px solid rgb(189, 147, 249);\n"
"}")
        self.gridLayout_3 = QGridLayout(self.groupBox_28)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_212 = QLabel(self.groupBox_28)
        self.label_212.setObjectName(u"label_212")

        self.gridLayout_3.addWidget(self.label_212, 5, 0, 1, 1)

        self.lineEditDistanciaRodillos = QLineEdit(self.groupBox_28)
        self.lineEditDistanciaRodillos.setObjectName(u"lineEditDistanciaRodillos")

        self.gridLayout_3.addWidget(self.lineEditDistanciaRodillos, 6, 1, 1, 1)

        self.label_209 = QLabel(self.groupBox_28)
        self.label_209.setObjectName(u"label_209")

        self.gridLayout_3.addWidget(self.label_209, 1, 0, 1, 1)

        self.label_215 = QLabel(self.groupBox_28)
        self.label_215.setObjectName(u"label_215")

        self.gridLayout_3.addWidget(self.label_215, 8, 0, 1, 1)

        self.label_211 = QLabel(self.groupBox_28)
        self.label_211.setObjectName(u"label_211")

        self.gridLayout_3.addWidget(self.label_211, 3, 0, 1, 1)

        self.lineEditk2 = QLineEdit(self.groupBox_28)
        self.lineEditk2.setObjectName(u"lineEditk2")

        self.gridLayout_3.addWidget(self.lineEditk2, 1, 1, 1, 1)

        self.widget_20 = QWidget(self.groupBox_28)
        self.widget_20.setObjectName(u"widget_20")
        self.horizontalLayout_33 = QHBoxLayout(self.widget_20)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")

        self.gridLayout_3.addWidget(self.widget_20, 12, 0, 1, 2)

        self.label_214 = QLabel(self.groupBox_28)
        self.label_214.setObjectName(u"label_214")

        self.gridLayout_3.addWidget(self.label_214, 6, 0, 1, 1)

        self.label_210 = QLabel(self.groupBox_28)
        self.label_210.setObjectName(u"label_210")

        self.gridLayout_3.addWidget(self.label_210, 2, 0, 1, 1)

        self.label_213 = QLabel(self.groupBox_28)
        self.label_213.setObjectName(u"label_213")

        self.gridLayout_3.addWidget(self.label_213, 7, 0, 1, 1)

        self.lineEditk1 = QLineEdit(self.groupBox_28)
        self.lineEditk1.setObjectName(u"lineEditk1")

        self.gridLayout_3.addWidget(self.lineEditk1, 0, 1, 1, 1)

        self.lineEditCapacidadRodillos = QLineEdit(self.groupBox_28)
        self.lineEditCapacidadRodillos.setObjectName(u"lineEditCapacidadRodillos")

        self.gridLayout_3.addWidget(self.lineEditCapacidadRodillos, 8, 1, 1, 1)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_7, 11, 1, 1, 1)

        self.lineEditSizePotenciaRodillos = QLineEdit(self.groupBox_28)
        self.lineEditSizePotenciaRodillos.setObjectName(u"lineEditSizePotenciaRodillos")

        self.gridLayout_3.addWidget(self.lineEditSizePotenciaRodillos, 10, 1, 1, 1)

        self.label_16 = QLabel(self.groupBox_28)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_3.addWidget(self.label_16, 10, 0, 1, 1)

        self.lineEditk4 = QLineEdit(self.groupBox_28)
        self.lineEditk4.setObjectName(u"lineEditk4")

        self.gridLayout_3.addWidget(self.lineEditk4, 3, 1, 1, 1)

        self.lineEditVelocidadRodillos = QLineEdit(self.groupBox_28)
        self.lineEditVelocidadRodillos.setObjectName(u"lineEditVelocidadRodillos")

        self.gridLayout_3.addWidget(self.lineEditVelocidadRodillos, 7, 1, 1, 1)

        self.lineEditFuerzaEspecifica = QLineEdit(self.groupBox_28)
        self.lineEditFuerzaEspecifica.setObjectName(u"lineEditFuerzaEspecifica")

        self.gridLayout_3.addWidget(self.lineEditFuerzaEspecifica, 5, 1, 1, 1)

        self.lineEditk3 = QLineEdit(self.groupBox_28)
        self.lineEditk3.setObjectName(u"lineEditk3")

        self.gridLayout_3.addWidget(self.lineEditk3, 2, 1, 1, 1)

        self.label_204 = QLabel(self.groupBox_28)
        self.label_204.setObjectName(u"label_204")

        self.gridLayout_3.addWidget(self.label_204, 0, 0, 1, 1)

        self.label_12 = QLabel(self.groupBox_28)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_3.addWidget(self.label_12, 4, 0, 1, 1)

        self.lineEditTorqueMolienda = QLineEdit(self.groupBox_28)
        self.lineEditTorqueMolienda.setObjectName(u"lineEditTorqueMolienda")

        self.gridLayout_3.addWidget(self.lineEditTorqueMolienda, 4, 1, 1, 1)


        self.gridLayout_11.addWidget(self.groupBox_28, 2, 1, 1, 1)

        self.botonLimpiar_5 = QPushButton(self.groupBox_24)
        self.botonLimpiar_5.setObjectName(u"botonLimpiar_5")
        sizePolicy9 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy9.setHorizontalStretch(20)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.botonLimpiar_5.sizePolicy().hasHeightForWidth())
        self.botonLimpiar_5.setSizePolicy(sizePolicy9)
        self.botonLimpiar_5.setMinimumSize(QSize(20, 0))
        self.botonLimpiar_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.botonLimpiar_5.setStyleSheet(u"QPushButton:hover {\n"
"    font-size: 15px;\n"
"	font: 600 12pt \"Bookman Old Style\";\n"
"	background-color: rgb(255, 44, 44);\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	padding-left:5px;\n"
"	padding-top:5px;\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(53, 21, 21, 255), stop:0.55 rgba(235, 93, 44, 255), stop:0.98 rgba(146, 91, 9, 255), stop:1 rgba(0, 0, 0, 0));\n"
"}\n"
"")

        self.gridLayout_11.addWidget(self.botonLimpiar_5, 3, 0, 1, 1)

        self.groupBox_25 = QGroupBox(self.groupBox_24)
        self.groupBox_25.setObjectName(u"groupBox_25")
        self.groupBox_25.setStyleSheet(u"QGroupBox {\n"
"    border: 1px solid rgba(128, 128, 128, 0.5); /* Ajusta la opacidad seg\u00fan tus necesidades */\n"
"    margin-top: 10px; /* Ajusta el margen superior seg\u00fan tus necesidades */\n"
"    padding-top: 20px; /* Ajusta el espaciado superior seg\u00fan tus necesidades */\n"
"	\n"
"	font: 600 12pt \"Bookman Old Style\";\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"    border: 1px solid rgb(189, 147, 249);\n"
"}")
        self.gridLayout = QGridLayout(self.groupBox_25)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_21 = QLabel(self.groupBox_25)
        self.label_21.setObjectName(u"label_21")

        self.gridLayout.addWidget(self.label_21, 6, 0, 1, 1)

        self.lineEditAnguloFractura = QLineEdit(self.groupBox_25)
        self.lineEditAnguloFractura.setObjectName(u"lineEditAnguloFractura")

        self.gridLayout.addWidget(self.lineEditAnguloFractura, 8, 1, 1, 1)

        self.label_206 = QLabel(self.groupBox_25)
        self.label_206.setObjectName(u"label_206")

        self.gridLayout.addWidget(self.label_206, 4, 0, 1, 1)

        self.label_203 = QLabel(self.groupBox_25)
        self.label_203.setObjectName(u"label_203")

        self.gridLayout.addWidget(self.label_203, 2, 0, 1, 1)

        self.lineEditWidthRodillos = QLineEdit(self.groupBox_25)
        self.lineEditWidthRodillos.setObjectName(u"lineEditWidthRodillos")

        self.gridLayout.addWidget(self.lineEditWidthRodillos, 10, 1, 1, 1)

        self.lineEditCoeficienteFriccion = QLineEdit(self.groupBox_25)
        self.lineEditCoeficienteFriccion.setObjectName(u"lineEditCoeficienteFriccion")

        self.gridLayout.addWidget(self.lineEditCoeficienteFriccion, 6, 1, 1, 1)

        self.lineEditAnguloApertura = QLineEdit(self.groupBox_25)
        self.lineEditAnguloApertura.setObjectName(u"lineEditAnguloApertura")

        self.gridLayout.addWidget(self.lineEditAnguloApertura, 7, 1, 1, 1)

        self.label_22 = QLabel(self.groupBox_25)
        self.label_22.setObjectName(u"label_22")

        self.gridLayout.addWidget(self.label_22, 11, 0, 1, 1)

        self.lineEditProductoRodillo = QLineEdit(self.groupBox_25)
        self.lineEditProductoRodillo.setObjectName(u"lineEditProductoRodillo")

        self.gridLayout.addWidget(self.lineEditProductoRodillo, 1, 1, 1, 1)

        self.lineEditDiametroRodillos = QLineEdit(self.groupBox_25)
        self.lineEditDiametroRodillos.setObjectName(u"lineEditDiametroRodillos")

        self.gridLayout.addWidget(self.lineEditDiametroRodillos, 11, 1, 1, 1)

        self.lineEditTortaSalida = QLineEdit(self.groupBox_25)
        self.lineEditTortaSalida.setObjectName(u"lineEditTortaSalida")

        self.gridLayout.addWidget(self.lineEditTortaSalida, 4, 1, 1, 1)

        self.label_207 = QLabel(self.groupBox_25)
        self.label_207.setObjectName(u"label_207")

        self.gridLayout.addWidget(self.label_207, 8, 0, 1, 1)

        self.label_11 = QLabel(self.groupBox_25)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout.addWidget(self.label_11, 0, 0, 1, 1)

        self.label_208 = QLabel(self.groupBox_25)
        self.label_208.setObjectName(u"label_208")

        self.gridLayout.addWidget(self.label_208, 9, 0, 1, 1)

        self.label_13 = QLabel(self.groupBox_25)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout.addWidget(self.label_13, 1, 0, 1, 1)

        self.label_23 = QLabel(self.groupBox_25)
        self.label_23.setObjectName(u"label_23")

        self.gridLayout.addWidget(self.label_23, 7, 0, 1, 1)

        self.lineEditTamaoMaximo = QLineEdit(self.groupBox_25)
        self.lineEditTamaoMaximo.setObjectName(u"lineEditTamaoMaximo")

        self.gridLayout.addWidget(self.lineEditTamaoMaximo, 2, 1, 1, 1)

        self.lineEditDensidadRodillo = QLineEdit(self.groupBox_25)
        self.lineEditDensidadRodillo.setObjectName(u"lineEditDensidadRodillo")

        self.gridLayout.addWidget(self.lineEditDensidadRodillo, 3, 1, 1, 1)

        self.label_216 = QLabel(self.groupBox_25)
        self.label_216.setObjectName(u"label_216")

        self.gridLayout.addWidget(self.label_216, 10, 0, 1, 1)

        self.lineEditAnguloCompresion = QLineEdit(self.groupBox_25)
        self.lineEditAnguloCompresion.setObjectName(u"lineEditAnguloCompresion")

        self.gridLayout.addWidget(self.lineEditAnguloCompresion, 9, 1, 1, 1)

        self.lineEditAlimentoRodillo = QLineEdit(self.groupBox_25)
        self.lineEditAlimentoRodillo.setObjectName(u"lineEditAlimentoRodillo")
        self.lineEditAlimentoRodillo.setStyleSheet(u"")

        self.gridLayout.addWidget(self.lineEditAlimentoRodillo, 0, 1, 1, 1)

        self.label_205 = QLabel(self.groupBox_25)
        self.label_205.setObjectName(u"label_205")

        self.gridLayout.addWidget(self.label_205, 3, 0, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_6, 12, 1, 1, 1)

        self.label_217 = QLabel(self.groupBox_25)
        self.label_217.setObjectName(u"label_217")

        self.gridLayout.addWidget(self.label_217, 5, 0, 1, 1)

        self.lineEditGrosorTorta = QLineEdit(self.groupBox_25)
        self.lineEditGrosorTorta.setObjectName(u"lineEditGrosorTorta")

        self.gridLayout.addWidget(self.lineEditGrosorTorta, 5, 1, 1, 1)


        self.gridLayout_11.addWidget(self.groupBox_25, 2, 0, 1, 1)

        self.opcionesMolinoRodillo = QComboBox(self.groupBox_24)
        self.opcionesMolinoRodillo.addItem("")
        self.opcionesMolinoRodillo.addItem("")
        self.opcionesMolinoRodillo.addItem("")
        self.opcionesMolinoRodillo.addItem("")
        self.opcionesMolinoRodillo.addItem("")
        self.opcionesMolinoRodillo.addItem("")
        self.opcionesMolinoRodillo.setObjectName(u"opcionesMolinoRodillo")
        sizePolicy.setHeightForWidth(self.opcionesMolinoRodillo.sizePolicy().hasHeightForWidth())
        self.opcionesMolinoRodillo.setSizePolicy(sizePolicy)
        self.opcionesMolinoRodillo.setCursor(QCursor(Qt.PointingHandCursor))
        self.opcionesMolinoRodillo.setStyleSheet(u"QComboBox QAbstractItemView {\n"
"	background: transparent;\n"
"    background-color: #FFFFFF; /* Cambia el color de fondo de las opciones\n"
"	 desplegadas a blanco */\n"
"	color: #000000; /* Cambia el color del texto a negro */\n"
"}")

        self.gridLayout_11.addWidget(self.opcionesMolinoRodillo, 0, 0, 1, 1)

        self.botonCalcular_5 = QPushButton(self.groupBox_24)
        self.botonCalcular_5.setObjectName(u"botonCalcular_5")
        sizePolicy9.setHeightForWidth(self.botonCalcular_5.sizePolicy().hasHeightForWidth())
        self.botonCalcular_5.setSizePolicy(sizePolicy9)
        self.botonCalcular_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.botonCalcular_5.setStyleSheet(u"\n"
"QPushButton:hover {\n"
"    font-size: 15px;\n"
"	\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(0, 255, 69);\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	padding-left:5px;\n"
"	padding-top:5px;\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(211, 255, 102, 255), stop:0.55 rgba(139, 235, 44, 255), stop:0.98 rgba(9, 146, 76, 149), stop:1 rgba(0, 0, 0, 0));\n"
"}")

        self.gridLayout_11.addWidget(self.botonCalcular_5, 3, 1, 1, 1)


        self.horizontalLayout_21.addWidget(self.groupBox_24)


        self.horizontalLayout_20.addWidget(self.widget_17)

        self.stackedWidget_3.addWidget(self.molino_rodillo)
        self.molino_mandibula = QWidget()
        self.molino_mandibula.setObjectName(u"molino_mandibula")
        self.verticalLayout_32 = QVBoxLayout(self.molino_mandibula)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.widget_16 = QWidget(self.molino_mandibula)
        self.widget_16.setObjectName(u"widget_16")
        self.horizontalLayout_19 = QHBoxLayout(self.widget_16)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.groupBox_22 = QGroupBox(self.widget_16)
        self.groupBox_22.setObjectName(u"groupBox_22")
        self.groupBox_22.setStyleSheet(u"QGroupBox {\n"
"    border: 2px;\n"
"	font: 600 12pt \"Bookman Old Style\";\n"
"    margin-top: 10px; /* Ajusta el margen superior seg\u00fan tus necesidades */\n"
"    padding-top: 30px; /* Ajusta el espaciado superior seg\u00fan tus necesidades */\n"
"}\n"
"")
        self.groupBox_22.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.gridLayout_18 = QGridLayout(self.groupBox_22)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.gridLayout_18.setContentsMargins(-1, 0, -1, -1)
        self.botonLimpiarMandibula = QPushButton(self.groupBox_22)
        self.botonLimpiarMandibula.setObjectName(u"botonLimpiarMandibula")
        self.botonLimpiarMandibula.setCursor(QCursor(Qt.PointingHandCursor))
        self.botonLimpiarMandibula.setStyleSheet(u"QPushButton:hover {\n"
"    font-size: 15px;\n"
"	font: 600 12pt \"Bookman Old Style\";\n"
"	background-color: rgb(255, 44, 44);\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	padding-left:5px;\n"
"	padding-top:5px;\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(53, 21, 21, 255), stop:0.55 rgba(235, 93, 44, 255), stop:0.98 rgba(146, 91, 9, 255), stop:1 rgba(0, 0, 0, 0));\n"
"}")

        self.gridLayout_18.addWidget(self.botonLimpiarMandibula, 2, 1, 1, 1)

        self.botonCalcularMandibula = QPushButton(self.groupBox_22)
        self.botonCalcularMandibula.setObjectName(u"botonCalcularMandibula")
        self.botonCalcularMandibula.setCursor(QCursor(Qt.PointingHandCursor))
        self.botonCalcularMandibula.setStyleSheet(u"\n"
"QPushButton:hover {\n"
"    font-size: 15px;\n"
"	\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(0, 255, 69);\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	padding-left:5px;\n"
"	padding-top:5px;\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(211, 255, 102, 255), stop:0.55 rgba(139, 235, 44, 255), stop:0.98 rgba(9, 146, 76, 149), stop:1 rgba(0, 0, 0, 0));\n"
"}")

        self.gridLayout_18.addWidget(self.botonCalcularMandibula, 2, 2, 1, 1)

        self.groupBox_23 = QGroupBox(self.groupBox_22)
        self.groupBox_23.setObjectName(u"groupBox_23")
        self.groupBox_23.setStyleSheet(u"QGroupBox {\n"
"    border: 1px solid rgba(128, 128, 128, 0.5); /* Ajusta la opacidad seg\u00fan tus necesidades */\n"
"    margin-top: 10px; /* Ajusta el margen superior seg\u00fan tus necesidades */\n"
"    padding-top: 20px; /* Ajusta el espaciado superior seg\u00fan tus necesidades */\n"
"	\n"
"	font: 600 12pt \"Bookman Old Style\";\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"    border: 1px solid rgb(189, 147, 249);\n"
"}")
        self.gridLayout_17 = QGridLayout(self.groupBox_23)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.gridLayout_17.setVerticalSpacing(6)
        self.gridLayout_17.setContentsMargins(-1, 9, -1, 9)
        self.lineEditSizeMayor = QLineEdit(self.groupBox_23)
        self.lineEditSizeMayor.setObjectName(u"lineEditSizeMayor")

        self.gridLayout_17.addWidget(self.lineEditSizeMayor, 0, 1, 1, 1)

        self.label_86 = QLabel(self.groupBox_23)
        self.label_86.setObjectName(u"label_86")

        self.gridLayout_17.addWidget(self.label_86, 5, 0, 1, 1)

        self.label_79 = QLabel(self.groupBox_23)
        self.label_79.setObjectName(u"label_79")

        self.gridLayout_17.addWidget(self.label_79, 13, 0, 1, 1)

        self.lineEditFrecuenciaMolienda = QLineEdit(self.groupBox_23)
        self.lineEditFrecuenciaMolienda.setObjectName(u"lineEditFrecuenciaMolienda")

        self.gridLayout_17.addWidget(self.lineEditFrecuenciaMolienda, 5, 1, 1, 1)

        self.lineEditLmin = QLineEdit(self.groupBox_23)
        self.lineEditLmin.setObjectName(u"lineEditLmin")

        self.gridLayout_17.addWidget(self.lineEditLmin, 4, 1, 1, 1)

        self.lineEditWidth = QLineEdit(self.groupBox_23)
        self.lineEditWidth.setObjectName(u"lineEditWidth")

        self.gridLayout_17.addWidget(self.lineEditWidth, 13, 1, 1, 1)

        self.label_201 = QLabel(self.groupBox_23)
        self.label_201.setObjectName(u"label_201")

        self.gridLayout_17.addWidget(self.label_201, 1, 0, 1, 1)

        self.lineEditThrow = QLineEdit(self.groupBox_23)
        self.lineEditThrow.setObjectName(u"lineEditThrow")

        self.gridLayout_17.addWidget(self.lineEditThrow, 14, 1, 1, 1)

        self.lineEditAlturaTriturador = QLineEdit(self.groupBox_23)
        self.lineEditAlturaTriturador.setObjectName(u"lineEditAlturaTriturador")

        self.gridLayout_17.addWidget(self.lineEditAlturaTriturador, 8, 1, 1, 1)

        self.label_76 = QLabel(self.groupBox_23)
        self.label_76.setObjectName(u"label_76")

        self.gridLayout_17.addWidget(self.label_76, 4, 0, 1, 1)

        self.label_78 = QLabel(self.groupBox_23)
        self.label_78.setObjectName(u"label_78")

        self.gridLayout_17.addWidget(self.label_78, 8, 0, 1, 1)

        self.lineEditGape = QLineEdit(self.groupBox_23)
        self.lineEditGape.setObjectName(u"lineEditGape")

        self.gridLayout_17.addWidget(self.lineEditGape, 7, 1, 1, 1)

        self.lineEditSet = QLineEdit(self.groupBox_23)
        self.lineEditSet.setObjectName(u"lineEditSet")

        self.gridLayout_17.addWidget(self.lineEditSet, 6, 1, 1, 1)

        self.lineEditDensidad = QLineEdit(self.groupBox_23)
        self.lineEditDensidad.setObjectName(u"lineEditDensidad")

        self.gridLayout_17.addWidget(self.lineEditDensidad, 2, 1, 1, 1)

        self.label_87 = QLabel(self.groupBox_23)
        self.label_87.setObjectName(u"label_87")

        self.gridLayout_17.addWidget(self.label_87, 7, 0, 1, 1)

        self.label_200 = QLabel(self.groupBox_23)
        self.label_200.setObjectName(u"label_200")

        self.gridLayout_17.addWidget(self.label_200, 0, 0, 1, 1)

        self.label_75 = QLabel(self.groupBox_23)
        self.label_75.setObjectName(u"label_75")

        self.gridLayout_17.addWidget(self.label_75, 6, 0, 1, 1)

        self.lineEditSizeMenor = QLineEdit(self.groupBox_23)
        self.lineEditSizeMenor.setObjectName(u"lineEditSizeMenor")

        self.gridLayout_17.addWidget(self.lineEditSizeMenor, 1, 1, 1, 1)

        self.label_77 = QLabel(self.groupBox_23)
        self.label_77.setObjectName(u"label_77")

        self.gridLayout_17.addWidget(self.label_77, 2, 0, 1, 1)

        self.label_80 = QLabel(self.groupBox_23)
        self.label_80.setObjectName(u"label_80")

        self.gridLayout_17.addWidget(self.label_80, 14, 0, 1, 1)

        self.verticalSpacer_13 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_17.addItem(self.verticalSpacer_13, 16, 1, 1, 1)


        self.gridLayout_18.addWidget(self.groupBox_23, 1, 1, 1, 1)

        self.groupBox_33 = QGroupBox(self.groupBox_22)
        self.groupBox_33.setObjectName(u"groupBox_33")
        self.groupBox_33.setStyleSheet(u"QGroupBox {\n"
"    border: 1px solid rgba(128, 128, 128, 0.5); /* Ajusta la opacidad seg\u00fan tus necesidades */\n"
"    margin-top: 10px; /* Ajusta el margen superior seg\u00fan tus necesidades */\n"
"    padding-top: 20px; /* Ajusta el espaciado superior seg\u00fan tus necesidades */\n"
"	\n"
"	font: 600 12pt \"Bookman Old Style\";\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"    border: 1px solid rgb(189, 147, 249);\n"
"}")
        self.formLayout_5 = QFormLayout(self.groupBox_33)
        self.formLayout_5.setObjectName(u"formLayout_5")
        self.label_82 = QLabel(self.groupBox_33)
        self.label_82.setObjectName(u"label_82")

        self.formLayout_5.setWidget(0, QFormLayout.LabelRole, self.label_82)

        self.lineEditCapacidadTrituradora = QLineEdit(self.groupBox_33)
        self.lineEditCapacidadTrituradora.setObjectName(u"lineEditCapacidadTrituradora")

        self.formLayout_5.setWidget(0, QFormLayout.FieldRole, self.lineEditCapacidadTrituradora)

        self.label_83 = QLabel(self.groupBox_33)
        self.label_83.setObjectName(u"label_83")

        self.formLayout_5.setWidget(1, QFormLayout.LabelRole, self.label_83)

        self.lineEditFrecuenciaCritica = QLineEdit(self.groupBox_33)
        self.lineEditFrecuenciaCritica.setObjectName(u"lineEditFrecuenciaCritica")

        self.formLayout_5.setWidget(1, QFormLayout.FieldRole, self.lineEditFrecuenciaCritica)

        self.lineEditRelacionReduccion = QLineEdit(self.groupBox_33)
        self.lineEditRelacionReduccion.setObjectName(u"lineEditRelacionReduccion")

        self.formLayout_5.setWidget(3, QFormLayout.FieldRole, self.lineEditRelacionReduccion)

        self.lineEditCapacidadReal = QLineEdit(self.groupBox_33)
        self.lineEditCapacidadReal.setObjectName(u"lineEditCapacidadReal")

        self.formLayout_5.setWidget(2, QFormLayout.FieldRole, self.lineEditCapacidadReal)

        self.label_202 = QLabel(self.groupBox_33)
        self.label_202.setObjectName(u"label_202")

        self.formLayout_5.setWidget(2, QFormLayout.LabelRole, self.label_202)

        self.label_81 = QLabel(self.groupBox_33)
        self.label_81.setObjectName(u"label_81")

        self.formLayout_5.setWidget(3, QFormLayout.LabelRole, self.label_81)

        self.label_84 = QLabel(self.groupBox_33)
        self.label_84.setObjectName(u"label_84")

        self.formLayout_5.setWidget(4, QFormLayout.LabelRole, self.label_84)

        self.lineEditOtroIndiceTrituradora = QLineEdit(self.groupBox_33)
        self.lineEditOtroIndiceTrituradora.setObjectName(u"lineEditOtroIndiceTrituradora")

        self.formLayout_5.setWidget(4, QFormLayout.FieldRole, self.lineEditOtroIndiceTrituradora)

        self.lineEditPotenciaTrituradora = QLineEdit(self.groupBox_33)
        self.lineEditPotenciaTrituradora.setObjectName(u"lineEditPotenciaTrituradora")

        self.formLayout_5.setWidget(5, QFormLayout.FieldRole, self.lineEditPotenciaTrituradora)

        self.label_85 = QLabel(self.groupBox_33)
        self.label_85.setObjectName(u"label_85")

        self.formLayout_5.setWidget(5, QFormLayout.LabelRole, self.label_85)


        self.gridLayout_18.addWidget(self.groupBox_33, 1, 2, 1, 1)

        self.comboBox = QComboBox(self.groupBox_22)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.comboBox.setStyleSheet(u"QComboBox QAbstractItemView {\n"
"	background: transparent;\n"
"    background-color: #FFFFFF; /* Cambia el color de fondo de las opciones\n"
"	 desplegadas a blanco */\n"
"	color: #000000; /* Cambia el color del texto a negro */\n"
"}")

        self.gridLayout_18.addWidget(self.comboBox, 0, 1, 1, 1)


        self.horizontalLayout_19.addWidget(self.groupBox_22)


        self.verticalLayout_32.addWidget(self.widget_16)

        self.stackedWidget_3.addWidget(self.molino_mandibula)

        self.verticalLayout_31.addWidget(self.stackedWidget_3)


        self.gridLayout_2.addWidget(self.widget_14, 0, 0, 1, 1)


        self.verticalLayout_16.addWidget(self.widget_molinos)

        self.stackedWidget.addWidget(self.molinos)
        self.bandas = QWidget()
        self.bandas.setObjectName(u"bandas")
        self.verticalLayout_17 = QVBoxLayout(self.bandas)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.widget_8 = QWidget(self.bandas)
        self.widget_8.setObjectName(u"widget_8")
        self.verticalLayout_18 = QVBoxLayout(self.widget_8)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.top_bandas = QFrame(self.widget_8)
        self.top_bandas.setObjectName(u"top_bandas")
        sizePolicy10 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(15)
        sizePolicy10.setHeightForWidth(self.top_bandas.sizePolicy().hasHeightForWidth())
        self.top_bandas.setSizePolicy(sizePolicy10)
        self.top_bandas.setMinimumSize(QSize(0, 20))
        self.top_bandas.setStyleSheet(u"QPushButton:hover {\n"
"    font-size: 15px;\n"
"	background-color: rgb(189, 147, 249);\n"
"\n"
"}\n"
"QPushButton {\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-radius: 0px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	padding-left:5px;\n"
"	padding-top:5px;\n"
"	\n"
"	background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:1, stop:0.00564972 rgba(80, 105, 255, 255), stop:0.55 rgba(171, 120, 206, 255), stop:0.98 rgba(182, 14, 235, 255), stop:1 rgba(0, 0, 0, 0));\n"
"	}\n"
"\n"
"QPushButton:hover {\n"
"    font-size: 15px;\n"
"	background-color: rgb(189, 147, 249);\n"
"\n"
"}\n"
"QPushButton {\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-radius: 0px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	padding-left:5px;\n"
"	padding-top:5px;\n"
"	\n"
"	background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:1, stop:0.00564972 rgba(80, 105, 255, 255), stop:0.55 rgba(171, 120, 206, 255), stop:0.98 rgba(182, 14, 235, 255), stop:1 rgba(0, 0, 0, 0));"
                        "\n"
"	}\n"
"\n"
"")
        self.top_bandas.setFrameShape(QFrame.StyledPanel)
        self.top_bandas.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.top_bandas)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.parte1 = QPushButton(self.top_bandas)
        self.parte1.setObjectName(u"parte1")
        sizePolicy11 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy11.setHorizontalStretch(0)
        sizePolicy11.setVerticalStretch(20)
        sizePolicy11.setHeightForWidth(self.parte1.sizePolicy().hasHeightForWidth())
        self.parte1.setSizePolicy(sizePolicy11)
        self.parte1.setMinimumSize(QSize(0, 20))
        self.parte1.setCursor(QCursor(Qt.PointingHandCursor))
        self.parte1.setStyleSheet(u"")

        self.horizontalLayout_9.addWidget(self.parte1)

        self.parte2 = QPushButton(self.top_bandas)
        self.parte2.setObjectName(u"parte2")
        self.parte2.setMinimumSize(QSize(0, 20))
        self.parte2.setCursor(QCursor(Qt.PointingHandCursor))
        self.parte2.setStyleSheet(u"")

        self.horizontalLayout_9.addWidget(self.parte2)

        self.parte3 = QPushButton(self.top_bandas)
        self.parte3.setObjectName(u"parte3")
        sizePolicy11.setHeightForWidth(self.parte3.sizePolicy().hasHeightForWidth())
        self.parte3.setSizePolicy(sizePolicy11)
        self.parte3.setMinimumSize(QSize(0, 20))
        self.parte3.setCursor(QCursor(Qt.PointingHandCursor))
        self.parte3.setStyleSheet(u"")

        self.horizontalLayout_9.addWidget(self.parte3)


        self.verticalLayout_18.addWidget(self.top_bandas)

        self.stackedWidget_2 = QStackedWidget(self.widget_8)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        sizePolicy.setHeightForWidth(self.stackedWidget_2.sizePolicy().hasHeightForWidth())
        self.stackedWidget_2.setSizePolicy(sizePolicy)
        self.stackedWidget_2.setStyleSheet(u"")
        self.parte_0 = QWidget()
        self.parte_0.setObjectName(u"parte_0")
        self.verticalLayout_30 = QVBoxLayout(self.parte_0)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.label_4 = QLabel(self.parte_0)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_30.addWidget(self.label_4)

        self.stackedWidget_2.addWidget(self.parte_0)
        self.Parte_1 = QWidget()
        self.Parte_1.setObjectName(u"Parte_1")
        self.verticalLayout_25 = QVBoxLayout(self.Parte_1)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.widget_9 = QWidget(self.Parte_1)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setStyleSheet(u"QLineEdit:focus{\n"
"    border: 1px solid rgb(189, 147, 249);\n"
"	\n"
"}")
        self.horizontalLayout_10 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.groupBox_11 = QGroupBox(self.widget_9)
        self.groupBox_11.setObjectName(u"groupBox_11")
        self.groupBox_11.setStyleSheet(u"QGroupBox {\n"
"    border: 1px solid rgba(128, 128, 128, 0.5); /* Ajusta la opacidad seg\u00fan tus necesidades */\n"
"    margin-top: 10px; /* Ajusta el margen superior seg\u00fan tus necesidades */\n"
"    padding-top: 20px; /* Ajusta el espaciado superior seg\u00fan tus necesidades */\n"
"	\n"
"	font: 600 12pt \"Bookman Old Style\";\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"    border: 1px solid rgb(189, 147, 249);\n"
"}\n"
"QLineEdit:focus{\n"
"    border: 1px solid rgb(189, 147, 249);\n"
"}")
        self.formLayout_2 = QFormLayout(self.groupBox_11)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_109 = QLabel(self.groupBox_11)
        self.label_109.setObjectName(u"label_109")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_109)

        self.searchBar = QLineEdit(self.groupBox_11)
        self.searchBar.setObjectName(u"searchBar")
        self.searchBar.setStyleSheet(u"")
        self.searchBar.setDragEnabled(False)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.searchBar)

        self.tableWidget = QTableWidget(self.groupBox_11)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        if (self.tableWidget.rowCount() < 4):
            self.tableWidget.setRowCount(4)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setItem(0, 1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setItem(0, 2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setItem(0, 3, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setItem(1, 0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setItem(1, 1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setItem(1, 2, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setItem(1, 3, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setItem(2, 0, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setItem(2, 1, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget.setItem(2, 2, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget.setItem(2, 3, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget.setItem(3, 0, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget.setItem(3, 1, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget.setItem(3, 2, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget.setItem(3, 3, __qtablewidgetitem19)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setStyleSheet(u"QTableWidget {\n"
"    font-size: 14px;\n"
"}")

        self.formLayout_2.setWidget(1, QFormLayout.SpanningRole, self.tableWidget)

        self.label_123 = QLabel(self.groupBox_11)
        self.label_123.setObjectName(u"label_123")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_123)

        self.lineEdit_11 = QLineEdit(self.groupBox_11)
        self.lineEdit_11.setObjectName(u"lineEdit_11")
        self.lineEdit_11.setEnabled(True)

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.lineEdit_11)

        self.label_110 = QLabel(self.groupBox_11)
        self.label_110.setObjectName(u"label_110")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.label_110)

        self.lineEdit1 = QLineEdit(self.groupBox_11)
        self.lineEdit1.setObjectName(u"lineEdit1")
        self.lineEdit1.setStyleSheet(u"")

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.lineEdit1)

        self.label_112 = QLabel(self.groupBox_11)
        self.label_112.setObjectName(u"label_112")

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.label_112)

        self.lineEdit2 = QLineEdit(self.groupBox_11)
        self.lineEdit2.setObjectName(u"lineEdit2")
        self.lineEdit2.setStyleSheet(u"")

        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.lineEdit2)

        self.label_111 = QLabel(self.groupBox_11)
        self.label_111.setObjectName(u"label_111")

        self.formLayout_2.setWidget(5, QFormLayout.LabelRole, self.label_111)

        self.lineEdit3 = QLineEdit(self.groupBox_11)
        self.lineEdit3.setObjectName(u"lineEdit3")
        self.lineEdit3.setStyleSheet(u"")

        self.formLayout_2.setWidget(5, QFormLayout.FieldRole, self.lineEdit3)

        self.pushButton_2 = QPushButton(self.groupBox_11)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setStyleSheet(u"\n"
"QPushButton:hover {\n"
"    font-size: 15px;\n"
"	\n"
"	background-color: rgb(255, 44, 44);\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	padding-left:5px;\n"
"	padding-top:5px;\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(53, 21, 21, 255), stop:0.55 rgba(235, 93, 44, 255), stop:0.98 rgba(146, 91, 9, 255), stop:1 rgba(0, 0, 0, 0));\n"
"}\n"
"")

        self.formLayout_2.setWidget(7, QFormLayout.SpanningRole, self.pushButton_2)

        self.verticalSpacer_21 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout_2.setItem(6, QFormLayout.SpanningRole, self.verticalSpacer_21)


        self.horizontalLayout_10.addWidget(self.groupBox_11)

        self.groupBox_4 = QGroupBox(self.widget_9)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setStyleSheet(u"QGroupBox {\n"
"    border: 1px solid rgba(128, 128, 128, 0.5); /* Ajusta la opacidad seg\u00fan tus necesidades */\n"
"    margin-top: 10px; /* Ajusta el margen superior seg\u00fan tus necesidades */\n"
"    padding-top: 20px; /* Ajusta el espaciado superior seg\u00fan tus necesidades */\n"
"	\n"
"	font: 600 12pt \"Bookman Old Style\";\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"    border: 1px solid rgb(189, 147, 249);\n"
"}\n"
"QLineEdit:focus{\n"
"    border: 1px solid rgb(189, 147, 249);\n"
"}\n"
"QLineEdit:focus{\n"
"    border: 1px solid rgb(189, 147, 249);\n"
"}")
        self.formLayout = QFormLayout(self.groupBox_4)
        self.formLayout.setObjectName(u"formLayout")
        self.label_113 = QLabel(self.groupBox_4)
        self.label_113.setObjectName(u"label_113")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_113)

        self.lineEdit_qg_bp1 = QLineEdit(self.groupBox_4)
        self.lineEdit_qg_bp1.setObjectName(u"lineEdit_qg_bp1")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEdit_qg_bp1)

        self.label_114 = QLabel(self.groupBox_4)
        self.label_114.setObjectName(u"label_114")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_114)

        self.lineEdit_lv_bp1 = QLineEdit(self.groupBox_4)
        self.lineEdit_lv_bp1.setObjectName(u"lineEdit_lv_bp1")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineEdit_lv_bp1)

        self.label_115 = QLabel(self.groupBox_4)
        self.label_115.setObjectName(u"label_115")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_115)

        self.lineEdit_v_bp1 = QLineEdit(self.groupBox_4)
        self.lineEdit_v_bp1.setObjectName(u"lineEdit_v_bp1")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.lineEdit_v_bp1)

        self.label_116 = QLabel(self.groupBox_4)
        self.label_116.setObjectName(u"label_116")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_116)

        self.lineEdit_lm_bp1 = QLineEdit(self.groupBox_4)
        self.lineEdit_lm_bp1.setObjectName(u"lineEdit_lm_bp1")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.lineEdit_lm_bp1)

        self.label_117 = QLabel(self.groupBox_4)
        self.label_117.setObjectName(u"label_117")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_117)

        self.lineEdit_qs_bp1 = QLineEdit(self.groupBox_4)
        self.lineEdit_qs_bp1.setObjectName(u"lineEdit_qs_bp1")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.lineEdit_qs_bp1)

        self.label_118 = QLabel(self.groupBox_4)
        self.label_118.setObjectName(u"label_118")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_118)

        self.lineEdit_lvt_bp1 = QLineEdit(self.groupBox_4)
        self.lineEdit_lvt_bp1.setObjectName(u"lineEdit_lvt_bp1")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.lineEdit_lvt_bp1)

        self.label_119 = QLabel(self.groupBox_4)
        self.label_119.setObjectName(u"label_119")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_119)

        self.lineEdit_lvm_bp1 = QLineEdit(self.groupBox_4)
        self.lineEdit_lvm_bp1.setObjectName(u"lineEdit_lvm_bp1")

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.lineEdit_lvm_bp1)

        self.label_120 = QLabel(self.groupBox_4)
        self.label_120.setObjectName(u"label_120")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.label_120)

        self.lineEdit_k_bp1 = QLineEdit(self.groupBox_4)
        self.lineEdit_k_bp1.setObjectName(u"lineEdit_k_bp1")

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.lineEdit_k_bp1)

        self.label_121 = QLabel(self.groupBox_4)
        self.label_121.setObjectName(u"label_121")

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.label_121)

        self.lineEdit_k1_bp1 = QLineEdit(self.groupBox_4)
        self.lineEdit_k1_bp1.setObjectName(u"lineEdit_k1_bp1")

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.lineEdit_k1_bp1)

        self.label_122 = QLabel(self.groupBox_4)
        self.label_122.setObjectName(u"label_122")

        self.formLayout.setWidget(9, QFormLayout.LabelRole, self.label_122)

        self.lineEdit_s_bp1 = QLineEdit(self.groupBox_4)
        self.lineEdit_s_bp1.setObjectName(u"lineEdit_s_bp1")

        self.formLayout.setWidget(9, QFormLayout.FieldRole, self.lineEdit_s_bp1)

        self.label_125 = QLabel(self.groupBox_4)
        self.label_125.setObjectName(u"label_125")

        self.formLayout.setWidget(10, QFormLayout.LabelRole, self.label_125)

        self.lineEdit_A1_bp1 = QLineEdit(self.groupBox_4)
        self.lineEdit_A1_bp1.setObjectName(u"lineEdit_A1_bp1")

        self.formLayout.setWidget(10, QFormLayout.FieldRole, self.lineEdit_A1_bp1)

        self.label_126 = QLabel(self.groupBox_4)
        self.label_126.setObjectName(u"label_126")

        self.formLayout.setWidget(11, QFormLayout.LabelRole, self.label_126)

        self.lineEdit_A2_bp1 = QLineEdit(self.groupBox_4)
        self.lineEdit_A2_bp1.setObjectName(u"lineEdit_A2_bp1")

        self.formLayout.setWidget(11, QFormLayout.FieldRole, self.lineEdit_A2_bp1)

        self.verticalSpacer_18 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout.setItem(12, QFormLayout.FieldRole, self.verticalSpacer_18)

        self.widget_2 = QWidget(self.groupBox_4)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy12 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy12.setHorizontalStretch(0)
        sizePolicy12.setVerticalStretch(30)
        sizePolicy12.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy12)
        self.widget_2.setMinimumSize(QSize(0, 30))
        self.widget_2.setStyleSheet(u"QPushButton{\n"
"    border: 1px solid red;\n"
"}")
        self.horizontalLayout_28 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(-1, 0, -1, 0)

        self.formLayout.setWidget(13, QFormLayout.SpanningRole, self.widget_2)

        self.pushButton_bandas_cal_1 = QPushButton(self.groupBox_4)
        self.pushButton_bandas_cal_1.setObjectName(u"pushButton_bandas_cal_1")
        self.pushButton_bandas_cal_1.setStyleSheet(u"\n"
"QPushButton:hover {\n"
"    font-size: 15px;\n"
"	\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(0, 255, 69);\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	padding-left:5px;\n"
"	padding-top:5px;\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(211, 255, 102, 255), stop:0.55 rgba(139, 235, 44, 255), stop:0.98 rgba(9, 146, 76, 149), stop:1 rgba(0, 0, 0, 0));\n"
"}")

        self.formLayout.setWidget(14, QFormLayout.SpanningRole, self.pushButton_bandas_cal_1)


        self.horizontalLayout_10.addWidget(self.groupBox_4)


        self.verticalLayout_25.addWidget(self.widget_9)

        self.stackedWidget_2.addWidget(self.Parte_1)
        self.Parte_2 = QWidget()
        self.Parte_2.setObjectName(u"Parte_2")
        self.verticalLayout_26 = QVBoxLayout(self.Parte_2)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.widget_10 = QWidget(self.Parte_2)
        self.widget_10.setObjectName(u"widget_10")
        self.horizontalLayout_11 = QHBoxLayout(self.widget_10)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.groupBox_13 = QGroupBox(self.widget_10)
        self.groupBox_13.setObjectName(u"groupBox_13")
        self.groupBox_13.setStyleSheet(u"QGroupBox {\n"
"    border: 1px solid rgba(128, 128, 128, 0.5); /* Ajusta la opacidad seg\u00fan tus necesidades */\n"
"    margin-top: 10px; /* Ajusta el margen superior seg\u00fan tus necesidades */\n"
"    padding-top: 20px; /* Ajusta el espaciado superior seg\u00fan tus necesidades */\n"
"	\n"
"	font: 600 12pt \"Bookman Old Style\";\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"    border: 1px solid rgb(189, 147, 249);\n"
"}\n"
"QLineEdit:focus{\n"
"    border: 1px solid rgb(189, 147, 249);\n"
"}")
        self.formLayout_3 = QFormLayout(self.groupBox_13)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.label_140 = QLabel(self.groupBox_13)
        self.label_140.setObjectName(u"label_140")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_140)

        self.comboBox_tb_bp2 = QComboBox(self.groupBox_13)
        self.comboBox_tb_bp2.addItem("")
        self.comboBox_tb_bp2.addItem("")
        self.comboBox_tb_bp2.setObjectName(u"comboBox_tb_bp2")

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.comboBox_tb_bp2)

        self.label_128 = QLabel(self.groupBox_13)
        self.label_128.setObjectName(u"label_128")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.label_128)

        self.lineEdit_fu_bp2 = QLineEdit(self.groupBox_13)
        self.lineEdit_fu_bp2.setObjectName(u"lineEdit_fu_bp2")

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.lineEdit_fu_bp2)

        self.label_129 = QLabel(self.groupBox_13)
        self.label_129.setObjectName(u"label_129")

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.label_129)

        self.lineEdit_l_bp2 = QLineEdit(self.groupBox_13)
        self.lineEdit_l_bp2.setObjectName(u"lineEdit_l_bp2")

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.lineEdit_l_bp2)

        self.label_131 = QLabel(self.groupBox_13)
        self.label_131.setObjectName(u"label_131")

        self.formLayout_3.setWidget(3, QFormLayout.LabelRole, self.label_131)

        self.lineEdit_cq_bp2 = QLineEdit(self.groupBox_13)
        self.lineEdit_cq_bp2.setObjectName(u"lineEdit_cq_bp2")

        self.formLayout_3.setWidget(3, QFormLayout.FieldRole, self.lineEdit_cq_bp2)

        self.label_132 = QLabel(self.groupBox_13)
        self.label_132.setObjectName(u"label_132")

        self.formLayout_3.setWidget(4, QFormLayout.LabelRole, self.label_132)

        self.lineEdit_ct_bp2 = QLineEdit(self.groupBox_13)
        self.lineEdit_ct_bp2.setObjectName(u"lineEdit_ct_bp2")

        self.formLayout_3.setWidget(4, QFormLayout.FieldRole, self.lineEdit_ct_bp2)

        self.label_133 = QLabel(self.groupBox_13)
        self.label_133.setObjectName(u"label_133")

        self.formLayout_3.setWidget(5, QFormLayout.LabelRole, self.label_133)

        self.lineEdit_f_bp2 = QLineEdit(self.groupBox_13)
        self.lineEdit_f_bp2.setObjectName(u"lineEdit_f_bp2")

        self.formLayout_3.setWidget(5, QFormLayout.FieldRole, self.lineEdit_f_bp2)

        self.label_134 = QLabel(self.groupBox_13)
        self.label_134.setObjectName(u"label_134")

        self.formLayout_3.setWidget(6, QFormLayout.LabelRole, self.label_134)

        self.lineEdit_qb_bp2 = QLineEdit(self.groupBox_13)
        self.lineEdit_qb_bp2.setObjectName(u"lineEdit_qb_bp2")

        self.formLayout_3.setWidget(6, QFormLayout.FieldRole, self.lineEdit_qb_bp2)

        self.label_135 = QLabel(self.groupBox_13)
        self.label_135.setObjectName(u"label_135")

        self.formLayout_3.setWidget(7, QFormLayout.LabelRole, self.label_135)

        self.lineEdit_qg_bp2 = QLineEdit(self.groupBox_13)
        self.lineEdit_qg_bp2.setObjectName(u"lineEdit_qg_bp2")

        self.formLayout_3.setWidget(7, QFormLayout.FieldRole, self.lineEdit_qg_bp2)

        self.label_136 = QLabel(self.groupBox_13)
        self.label_136.setObjectName(u"label_136")

        self.formLayout_3.setWidget(8, QFormLayout.LabelRole, self.label_136)

        self.lineEdit_qru_bp2 = QLineEdit(self.groupBox_13)
        self.lineEdit_qru_bp2.setObjectName(u"lineEdit_qru_bp2")

        self.formLayout_3.setWidget(8, QFormLayout.FieldRole, self.lineEdit_qru_bp2)

        self.label_137 = QLabel(self.groupBox_13)
        self.label_137.setObjectName(u"label_137")

        self.formLayout_3.setWidget(9, QFormLayout.LabelRole, self.label_137)

        self.lineEdit_qro_bp2 = QLineEdit(self.groupBox_13)
        self.lineEdit_qro_bp2.setObjectName(u"lineEdit_qro_bp2")

        self.formLayout_3.setWidget(9, QFormLayout.FieldRole, self.lineEdit_qro_bp2)

        self.label_138 = QLabel(self.groupBox_13)
        self.label_138.setObjectName(u"label_138")

        self.formLayout_3.setWidget(10, QFormLayout.LabelRole, self.label_138)

        self.lineEdit_h_bp2 = QLineEdit(self.groupBox_13)
        self.lineEdit_h_bp2.setObjectName(u"lineEdit_h_bp2")

        self.formLayout_3.setWidget(10, QFormLayout.FieldRole, self.lineEdit_h_bp2)

        self.label_141 = QLabel(self.groupBox_13)
        self.label_141.setObjectName(u"label_141")

        self.formLayout_3.setWidget(11, QFormLayout.LabelRole, self.label_141)

        self.lineEdit_v_bp2 = QLineEdit(self.groupBox_13)
        self.lineEdit_v_bp2.setObjectName(u"lineEdit_v_bp2")

        self.formLayout_3.setWidget(11, QFormLayout.FieldRole, self.lineEdit_v_bp2)

        self.label_142 = QLabel(self.groupBox_13)
        self.label_142.setObjectName(u"label_142")

        self.formLayout_3.setWidget(12, QFormLayout.LabelRole, self.label_142)

        self.lineEdit_n_bp2 = QLineEdit(self.groupBox_13)
        self.lineEdit_n_bp2.setObjectName(u"lineEdit_n_bp2")

        self.formLayout_3.setWidget(12, QFormLayout.FieldRole, self.lineEdit_n_bp2)

        self.label_139 = QLabel(self.groupBox_13)
        self.label_139.setObjectName(u"label_139")

        self.formLayout_3.setWidget(13, QFormLayout.LabelRole, self.label_139)

        self.lineEdit_p_bp2 = QLineEdit(self.groupBox_13)
        self.lineEdit_p_bp2.setObjectName(u"lineEdit_p_bp2")

        self.formLayout_3.setWidget(13, QFormLayout.FieldRole, self.lineEdit_p_bp2)


        self.horizontalLayout_11.addWidget(self.groupBox_13)

        self.groupBox_14 = QGroupBox(self.widget_10)
        self.groupBox_14.setObjectName(u"groupBox_14")
        self.verticalLayout_19 = QVBoxLayout(self.groupBox_14)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.scrollArea = QScrollArea(self.groupBox_14)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"QscrollArea {\n"
"border: 2px;\n"
"}")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 423, 471))
        self.formLayout_6 = QFormLayout(self.scrollAreaWidgetContents_2)
        self.formLayout_6.setObjectName(u"formLayout_6")
        self.lineEdit_pprs_bp2 = QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit_pprs_bp2.setObjectName(u"lineEdit_pprs_bp2")

        self.formLayout_6.setWidget(0, QFormLayout.FieldRole, self.lineEdit_pprs_bp2)

        self.label_143 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_143.setObjectName(u"label_143")

        self.formLayout_6.setWidget(1, QFormLayout.LabelRole, self.label_143)

        self.lineEdit_ao_bp2 = QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit_ao_bp2.setObjectName(u"lineEdit_ao_bp2")

        self.formLayout_6.setWidget(1, QFormLayout.FieldRole, self.lineEdit_ao_bp2)

        self.label_144 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_144.setObjectName(u"label_144")

        self.formLayout_6.setWidget(2, QFormLayout.LabelRole, self.label_144)

        self.lineEdit_ppri_bp2 = QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit_ppri_bp2.setObjectName(u"lineEdit_ppri_bp2")

        self.formLayout_6.setWidget(2, QFormLayout.FieldRole, self.lineEdit_ppri_bp2)

        self.label_145 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_145.setObjectName(u"label_145")

        self.formLayout_6.setWidget(3, QFormLayout.LabelRole, self.label_145)

        self.lineEdit_au_bp2 = QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit_au_bp2.setObjectName(u"lineEdit_au_bp2")

        self.formLayout_6.setWidget(3, QFormLayout.FieldRole, self.lineEdit_au_bp2)

        self.label_146 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_146.setObjectName(u"label_146")

        self.formLayout_6.setWidget(4, QFormLayout.LabelRole, self.label_146)

        self.lineEdit_t1_bp2 = QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit_t1_bp2.setObjectName(u"lineEdit_t1_bp2")

        self.formLayout_6.setWidget(4, QFormLayout.FieldRole, self.lineEdit_t1_bp2)

        self.label_147 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_147.setObjectName(u"label_147")

        self.formLayout_6.setWidget(5, QFormLayout.LabelRole, self.label_147)

        self.lineEdit_t2_bp2 = QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit_t2_bp2.setObjectName(u"lineEdit_t2_bp2")

        self.formLayout_6.setWidget(5, QFormLayout.FieldRole, self.lineEdit_t2_bp2)

        self.label_148 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_148.setObjectName(u"label_148")

        self.formLayout_6.setWidget(6, QFormLayout.LabelRole, self.label_148)

        self.lineEdit_fa_bp2 = QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit_fa_bp2.setObjectName(u"lineEdit_fa_bp2")

        self.formLayout_6.setWidget(6, QFormLayout.FieldRole, self.lineEdit_fa_bp2)

        self.label_149 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_149.setObjectName(u"label_149")

        self.formLayout_6.setWidget(7, QFormLayout.LabelRole, self.label_149)

        self.lineEdit_cw_bp2 = QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit_cw_bp2.setObjectName(u"lineEdit_cw_bp2")

        self.formLayout_6.setWidget(7, QFormLayout.FieldRole, self.lineEdit_cw_bp2)

        self.label_180 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_180.setObjectName(u"label_180")

        self.formLayout_6.setWidget(8, QFormLayout.LabelRole, self.label_180)

        self.lineEdit_t3_bp2 = QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit_t3_bp2.setObjectName(u"lineEdit_t3_bp2")

        self.formLayout_6.setWidget(8, QFormLayout.FieldRole, self.lineEdit_t3_bp2)

        self.label_181 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_181.setObjectName(u"label_181")

        self.formLayout_6.setWidget(9, QFormLayout.LabelRole, self.label_181)

        self.lineEdit_fr_bp2 = QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit_fr_bp2.setObjectName(u"lineEdit_fr_bp2")

        self.formLayout_6.setWidget(9, QFormLayout.FieldRole, self.lineEdit_fr_bp2)

        self.label_182 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_182.setObjectName(u"label_182")

        self.formLayout_6.setWidget(11, QFormLayout.LabelRole, self.label_182)

        self.lineEdit_tg_bp2 = QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit_tg_bp2.setObjectName(u"lineEdit_tg_bp2")

        self.formLayout_6.setWidget(11, QFormLayout.FieldRole, self.lineEdit_tg_bp2)

        self.label_183 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_183.setObjectName(u"label_183")

        self.formLayout_6.setWidget(12, QFormLayout.LabelRole, self.label_183)

        self.lineEdit_lc_bp2 = QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit_lc_bp2.setObjectName(u"lineEdit_lc_bp2")

        self.formLayout_6.setWidget(12, QFormLayout.FieldRole, self.lineEdit_lc_bp2)

        self.label_184 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_184.setObjectName(u"label_184")

        self.formLayout_6.setWidget(13, QFormLayout.LabelRole, self.label_184)

        self.lineEdit_ht_bp2 = QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit_ht_bp2.setObjectName(u"lineEdit_ht_bp2")

        self.formLayout_6.setWidget(13, QFormLayout.FieldRole, self.lineEdit_ht_bp2)

        self.label_185 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_185.setObjectName(u"label_185")

        self.formLayout_6.setWidget(14, QFormLayout.LabelRole, self.label_185)

        self.lineEdit_tumax_bp2 = QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit_tumax_bp2.setObjectName(u"lineEdit_tumax_bp2")

        self.formLayout_6.setWidget(14, QFormLayout.FieldRole, self.lineEdit_tumax_bp2)

        self.label_186 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_186.setObjectName(u"label_186")

        self.formLayout_6.setWidget(15, QFormLayout.LabelRole, self.label_186)

        self.lineEdit_tmax_bp2 = QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit_tmax_bp2.setObjectName(u"lineEdit_tmax_bp2")

        self.formLayout_6.setWidget(15, QFormLayout.FieldRole, self.lineEdit_tmax_bp2)

        self.label_187 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_187.setObjectName(u"label_187")

        self.formLayout_6.setWidget(16, QFormLayout.LabelRole, self.label_187)

        self.lineEdit_N_bp2 = QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit_N_bp2.setObjectName(u"lineEdit_N_bp2")

        self.formLayout_6.setWidget(16, QFormLayout.FieldRole, self.lineEdit_N_bp2)

        self.label_195 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_195.setObjectName(u"label_195")

        self.formLayout_6.setWidget(10, QFormLayout.LabelRole, self.label_195)

        self.lineEdit_t0_bp2 = QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit_t0_bp2.setObjectName(u"lineEdit_t0_bp2")

        self.formLayout_6.setWidget(10, QFormLayout.FieldRole, self.lineEdit_t0_bp2)

        self.label_130 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_130.setObjectName(u"label_130")

        self.formLayout_6.setWidget(0, QFormLayout.LabelRole, self.label_130)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_19.addWidget(self.scrollArea)

        self.widget_22 = QWidget(self.groupBox_14)
        self.widget_22.setObjectName(u"widget_22")
        sizePolicy13 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy13.setHorizontalStretch(0)
        sizePolicy13.setVerticalStretch(25)
        sizePolicy13.setHeightForWidth(self.widget_22.sizePolicy().hasHeightForWidth())
        self.widget_22.setSizePolicy(sizePolicy13)
        self.widget_22.setMinimumSize(QSize(0, 40))
        self.horizontalLayout_35 = QHBoxLayout(self.widget_22)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.pushButton_4 = QPushButton(self.widget_22)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setStyleSheet(u"\n"
"QPushButton:hover {\n"
"    font-size: 15px;\n"
"	\n"
"	background-color: rgb(255, 44, 44);\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	padding-left:5px;\n"
"	padding-top:5px;\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(53, 21, 21, 255), stop:0.55 rgba(235, 93, 44, 255), stop:0.98 rgba(146, 91, 9, 255), stop:1 rgba(0, 0, 0, 0));\n"
"}\n"
"")

        self.horizontalLayout_35.addWidget(self.pushButton_4)

        self.pushButton_bandas_cal_2 = QPushButton(self.widget_22)
        self.pushButton_bandas_cal_2.setObjectName(u"pushButton_bandas_cal_2")
        self.pushButton_bandas_cal_2.setStyleSheet(u"\n"
"QPushButton:hover {\n"
"    font-size: 15px;\n"
"	\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(0, 255, 69);\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	padding-left:5px;\n"
"	padding-top:5px;\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(211, 255, 102, 255), stop:0.55 rgba(139, 235, 44, 255), stop:0.98 rgba(9, 146, 76, 149), stop:1 rgba(0, 0, 0, 0));\n"
"}")

        self.horizontalLayout_35.addWidget(self.pushButton_bandas_cal_2)


        self.verticalLayout_19.addWidget(self.widget_22)


        self.horizontalLayout_11.addWidget(self.groupBox_14)


        self.verticalLayout_26.addWidget(self.widget_10)

        self.stackedWidget_2.addWidget(self.Parte_2)
        self.Parte_3 = QWidget()
        self.Parte_3.setObjectName(u"Parte_3")
        self.verticalLayout_27 = QVBoxLayout(self.Parte_3)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.widget_11 = QWidget(self.Parte_3)
        self.widget_11.setObjectName(u"widget_11")
        self.horizontalLayout_12 = QHBoxLayout(self.widget_11)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.groupBox_15 = QGroupBox(self.widget_11)
        self.groupBox_15.setObjectName(u"groupBox_15")
        self.groupBox_15.setStyleSheet(u"QGroupBox {\n"
"    border: 1px solid rgba(128, 128, 128, 0.5); /* Ajusta la opacidad seg\u00fan tus necesidades */\n"
"    margin-top: 10px; /* Ajusta el margen superior seg\u00fan tus necesidades */\n"
"    padding-top: 10px; /* Ajusta el espaciado superior seg\u00fan tus necesidades */\n"
"	\n"
"	font: 600 12pt \"Bookman Old Style\";\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"    border: 1px solid rgb(189, 147, 249);\n"
"}\n"
"QLineEdit:focus{\n"
"    border: 1px solid rgb(189, 147, 249);\n"
"}")
        self.formLayout_4 = QFormLayout(self.groupBox_15)
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.label_152 = QLabel(self.groupBox_15)
        self.label_152.setObjectName(u"label_152")

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.label_152)

        self.lineEdit_mif_bp3 = QLineEdit(self.groupBox_15)
        self.lineEdit_mif_bp3.setObjectName(u"lineEdit_mif_bp3")

        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.lineEdit_mif_bp3)

        self.label_150 = QLabel(self.groupBox_15)
        self.label_150.setObjectName(u"label_150")

        self.formLayout_4.setWidget(1, QFormLayout.LabelRole, self.label_150)

        self.lineEdit_mf_bp3 = QLineEdit(self.groupBox_15)
        self.lineEdit_mf_bp3.setObjectName(u"lineEdit_mf_bp3")

        self.formLayout_4.setWidget(1, QFormLayout.FieldRole, self.lineEdit_mf_bp3)

        self.label_153 = QLabel(self.groupBox_15)
        self.label_153.setObjectName(u"label_153")

        self.formLayout_4.setWidget(2, QFormLayout.LabelRole, self.label_153)

        self.lineEdit_mt_bp3 = QLineEdit(self.groupBox_15)
        self.lineEdit_mt_bp3.setObjectName(u"lineEdit_mt_bp3")

        self.formLayout_4.setWidget(2, QFormLayout.FieldRole, self.lineEdit_mt_bp3)

        self.label_154 = QLabel(self.groupBox_15)
        self.label_154.setObjectName(u"label_154")

        self.formLayout_4.setWidget(3, QFormLayout.LabelRole, self.label_154)

        self.lineEdit_w_bp3 = QLineEdit(self.groupBox_15)
        self.lineEdit_w_bp3.setObjectName(u"lineEdit_w_bp3")

        self.formLayout_4.setWidget(3, QFormLayout.FieldRole, self.lineEdit_w_bp3)

        self.label_155 = QLabel(self.groupBox_15)
        self.label_155.setObjectName(u"label_155")

        self.formLayout_4.setWidget(4, QFormLayout.LabelRole, self.label_155)

        self.lineEdit_u_bp3 = QLineEdit(self.groupBox_15)
        self.lineEdit_u_bp3.setObjectName(u"lineEdit_u_bp3")

        self.formLayout_4.setWidget(4, QFormLayout.FieldRole, self.lineEdit_u_bp3)

        self.label_156 = QLabel(self.groupBox_15)
        self.label_156.setObjectName(u"label_156")

        self.formLayout_4.setWidget(5, QFormLayout.LabelRole, self.label_156)

        self.lineEdit_d_bp3 = QLineEdit(self.groupBox_15)
        self.lineEdit_d_bp3.setObjectName(u"lineEdit_d_bp3")

        self.formLayout_4.setWidget(5, QFormLayout.FieldRole, self.lineEdit_d_bp3)

        self.label_157 = QLabel(self.groupBox_15)
        self.label_157.setObjectName(u"label_157")

        self.formLayout_4.setWidget(6, QFormLayout.LabelRole, self.label_157)

        self.lineEdit_cp_bp3 = QLineEdit(self.groupBox_15)
        self.lineEdit_cp_bp3.setObjectName(u"lineEdit_cp_bp3")

        self.formLayout_4.setWidget(6, QFormLayout.FieldRole, self.lineEdit_cp_bp3)

        self.label_158 = QLabel(self.groupBox_15)
        self.label_158.setObjectName(u"label_158")

        self.formLayout_4.setWidget(7, QFormLayout.LabelRole, self.label_158)

        self.lineEdit_t1_bp3 = QLineEdit(self.groupBox_15)
        self.lineEdit_t1_bp3.setObjectName(u"lineEdit_t1_bp3")

        self.formLayout_4.setWidget(7, QFormLayout.FieldRole, self.lineEdit_t1_bp3)

        self.label_159 = QLabel(self.groupBox_15)
        self.label_159.setObjectName(u"label_159")

        self.formLayout_4.setWidget(8, QFormLayout.LabelRole, self.label_159)

        self.lineEdit_t2_bp3 = QLineEdit(self.groupBox_15)
        self.lineEdit_t2_bp3.setObjectName(u"lineEdit_t2_bp3")

        self.formLayout_4.setWidget(8, QFormLayout.FieldRole, self.lineEdit_t2_bp3)

        self.label_160 = QLabel(self.groupBox_15)
        self.label_160.setObjectName(u"label_160")

        self.formLayout_4.setWidget(9, QFormLayout.LabelRole, self.label_160)

        self.lineEdit_qt_bp3 = QLineEdit(self.groupBox_15)
        self.lineEdit_qt_bp3.setObjectName(u"lineEdit_qt_bp3")

        self.formLayout_4.setWidget(9, QFormLayout.FieldRole, self.lineEdit_qt_bp3)

        self.label_161 = QLabel(self.groupBox_15)
        self.label_161.setObjectName(u"label_161")

        self.formLayout_4.setWidget(10, QFormLayout.LabelRole, self.label_161)

        self.lineEdit_p_bp3 = QLineEdit(self.groupBox_15)
        self.lineEdit_p_bp3.setObjectName(u"lineEdit_p_bp3")

        self.formLayout_4.setWidget(10, QFormLayout.FieldRole, self.lineEdit_p_bp3)

        self.label_162 = QLabel(self.groupBox_15)
        self.label_162.setObjectName(u"label_162")

        self.formLayout_4.setWidget(11, QFormLayout.LabelRole, self.label_162)

        self.lineEdit_n_bp3 = QLineEdit(self.groupBox_15)
        self.lineEdit_n_bp3.setObjectName(u"lineEdit_n_bp3")

        self.formLayout_4.setWidget(11, QFormLayout.FieldRole, self.lineEdit_n_bp3)

        self.label_163 = QLabel(self.groupBox_15)
        self.label_163.setObjectName(u"label_163")

        self.formLayout_4.setWidget(12, QFormLayout.LabelRole, self.label_163)

        self.lineEdit_cpr_bp3 = QLineEdit(self.groupBox_15)
        self.lineEdit_cpr_bp3.setObjectName(u"lineEdit_cpr_bp3")

        self.formLayout_4.setWidget(12, QFormLayout.FieldRole, self.lineEdit_cpr_bp3)

        self.label_164 = QLabel(self.groupBox_15)
        self.label_164.setObjectName(u"label_164")

        self.formLayout_4.setWidget(13, QFormLayout.LabelRole, self.label_164)

        self.lineEdit_ft_bp3 = QLineEdit(self.groupBox_15)
        self.lineEdit_ft_bp3.setObjectName(u"lineEdit_ft_bp3")

        self.formLayout_4.setWidget(13, QFormLayout.FieldRole, self.lineEdit_ft_bp3)

        self.label_165 = QLabel(self.groupBox_15)
        self.label_165.setObjectName(u"label_165")

        self.formLayout_4.setWidget(14, QFormLayout.LabelRole, self.label_165)

        self.lineEdit_ao_bp3 = QLineEdit(self.groupBox_15)
        self.lineEdit_ao_bp3.setObjectName(u"lineEdit_ao_bp3")

        self.formLayout_4.setWidget(14, QFormLayout.FieldRole, self.lineEdit_ao_bp3)

        self.label_179 = QLabel(self.groupBox_15)
        self.label_179.setObjectName(u"label_179")

        self.formLayout_4.setWidget(15, QFormLayout.LabelRole, self.label_179)

        self.lineEdit_au_bp3 = QLineEdit(self.groupBox_15)
        self.lineEdit_au_bp3.setObjectName(u"lineEdit_au_bp3")

        self.formLayout_4.setWidget(15, QFormLayout.FieldRole, self.lineEdit_au_bp3)

        self.label_193 = QLabel(self.groupBox_15)
        self.label_193.setObjectName(u"label_193")

        self.formLayout_4.setWidget(16, QFormLayout.LabelRole, self.label_193)

        self.lineEdit_qb_bp3 = QLineEdit(self.groupBox_15)
        self.lineEdit_qb_bp3.setObjectName(u"lineEdit_qb_bp3")

        self.formLayout_4.setWidget(16, QFormLayout.FieldRole, self.lineEdit_qb_bp3)


        self.horizontalLayout_12.addWidget(self.groupBox_15)

        self.groupBox_16 = QGroupBox(self.widget_11)
        self.groupBox_16.setObjectName(u"groupBox_16")
        self.gridLayout_21 = QGridLayout(self.groupBox_16)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.widget_23 = QWidget(self.groupBox_16)
        self.widget_23.setObjectName(u"widget_23")
        self.horizontalLayout_36 = QHBoxLayout(self.widget_23)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.pushButton_5 = QPushButton(self.widget_23)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setStyleSheet(u"\n"
"QPushButton:hover {\n"
"    font-size: 15px;\n"
"	\n"
"	background-color: rgb(255, 44, 44);\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	padding-left:5px;\n"
"	padding-top:5px;\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(53, 21, 21, 255), stop:0.55 rgba(235, 93, 44, 255), stop:0.98 rgba(146, 91, 9, 255), stop:1 rgba(0, 0, 0, 0));\n"
"}\n"
"")

        self.horizontalLayout_36.addWidget(self.pushButton_5)

        self.pushButton_bandas_cal_3 = QPushButton(self.widget_23)
        self.pushButton_bandas_cal_3.setObjectName(u"pushButton_bandas_cal_3")
        self.pushButton_bandas_cal_3.setStyleSheet(u"\n"
"\n"
"QPushButton:hover {\n"
"    font-size: 15px;\n"
"	\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(0, 255, 69);\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	padding-left:5px;\n"
"	padding-top:5px;\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(211, 255, 102, 255), stop:0.55 rgba(139, 235, 44, 255), stop:0.98 rgba(9, 146, 76, 149), stop:1 rgba(0, 0, 0, 0));\n"
"}")

        self.horizontalLayout_36.addWidget(self.pushButton_bandas_cal_3)


        self.gridLayout_21.addWidget(self.widget_23, 1, 0, 1, 1)

        self.scrollArea_2 = QScrollArea(self.groupBox_16)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 533, 579))
        self.formLayout_7 = QFormLayout(self.scrollAreaWidgetContents_3)
        self.formLayout_7.setObjectName(u"formLayout_7")
        self.label_194 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_194.setObjectName(u"label_194")

        self.formLayout_7.setWidget(1, QFormLayout.LabelRole, self.label_194)

        self.lineEdit_lv_bp3 = QLineEdit(self.scrollAreaWidgetContents_3)
        self.lineEdit_lv_bp3.setObjectName(u"lineEdit_lv_bp3")

        self.formLayout_7.setWidget(1, QFormLayout.FieldRole, self.lineEdit_lv_bp3)

        self.label_151 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_151.setObjectName(u"label_151")

        self.formLayout_7.setWidget(2, QFormLayout.LabelRole, self.label_151)

        self.lineEdit_c_bp3 = QLineEdit(self.scrollAreaWidgetContents_3)
        self.lineEdit_c_bp3.setObjectName(u"lineEdit_c_bp3")

        self.formLayout_7.setWidget(2, QFormLayout.FieldRole, self.lineEdit_c_bp3)

        self.label_166 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_166.setObjectName(u"label_166")

        self.formLayout_7.setWidget(3, QFormLayout.LabelRole, self.label_166)

        self.lineEdit_ot_bp3 = QLineEdit(self.scrollAreaWidgetContents_3)
        self.lineEdit_ot_bp3.setObjectName(u"lineEdit_ot_bp3")

        self.formLayout_7.setWidget(3, QFormLayout.FieldRole, self.lineEdit_ot_bp3)

        self.label_167 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_167.setObjectName(u"label_167")

        self.formLayout_7.setWidget(4, QFormLayout.LabelRole, self.label_167)

        self.lineEdit_ag_bp3 = QLineEdit(self.scrollAreaWidgetContents_3)
        self.lineEdit_ag_bp3.setObjectName(u"lineEdit_ag_bp3")

        self.formLayout_7.setWidget(4, QFormLayout.FieldRole, self.lineEdit_ag_bp3)

        self.label_168 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_168.setObjectName(u"label_168")

        self.formLayout_7.setWidget(5, QFormLayout.LabelRole, self.label_168)

        self.lineEdit_ee_bp3 = QLineEdit(self.scrollAreaWidgetContents_3)
        self.lineEdit_ee_bp3.setObjectName(u"lineEdit_ee_bp3")

        self.formLayout_7.setWidget(5, QFormLayout.FieldRole, self.lineEdit_ee_bp3)

        self.label_169 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_169.setObjectName(u"label_169")

        self.formLayout_7.setWidget(6, QFormLayout.LabelRole, self.label_169)

        self.lineEdit_j_bp3 = QLineEdit(self.scrollAreaWidgetContents_3)
        self.lineEdit_j_bp3.setObjectName(u"lineEdit_j_bp3")

        self.formLayout_7.setWidget(6, QFormLayout.FieldRole, self.lineEdit_j_bp3)

        self.label_170 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_170.setObjectName(u"label_170")

        self.formLayout_7.setWidget(7, QFormLayout.LabelRole, self.label_170)

        self.lineEdit_n_bp3_2 = QLineEdit(self.scrollAreaWidgetContents_3)
        self.lineEdit_n_bp3_2.setObjectName(u"lineEdit_n_bp3_2")

        self.formLayout_7.setWidget(7, QFormLayout.FieldRole, self.lineEdit_n_bp3_2)

        self.label_171 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_171.setObjectName(u"label_171")

        self.formLayout_7.setWidget(8, QFormLayout.LabelRole, self.label_171)

        self.lineEdit_v_bp3 = QLineEdit(self.scrollAreaWidgetContents_3)
        self.lineEdit_v_bp3.setObjectName(u"lineEdit_v_bp3")

        self.formLayout_7.setWidget(8, QFormLayout.FieldRole, self.lineEdit_v_bp3)

        self.label_172 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_172.setObjectName(u"label_172")

        self.formLayout_7.setWidget(9, QFormLayout.LabelRole, self.label_172)

        self.lineEdit_D_bp3 = QLineEdit(self.scrollAreaWidgetContents_3)
        self.lineEdit_D_bp3.setObjectName(u"lineEdit_D_bp3")

        self.formLayout_7.setWidget(9, QFormLayout.FieldRole, self.lineEdit_D_bp3)

        self.label_173 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_173.setObjectName(u"label_173")

        self.formLayout_7.setWidget(10, QFormLayout.LabelRole, self.label_173)

        self.lineEdit_Ca_bp3 = QLineEdit(self.scrollAreaWidgetContents_3)
        self.lineEdit_Ca_bp3.setObjectName(u"lineEdit_Ca_bp3")

        self.formLayout_7.setWidget(10, QFormLayout.FieldRole, self.lineEdit_Ca_bp3)

        self.label_174 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_174.setObjectName(u"label_174")

        self.formLayout_7.setWidget(11, QFormLayout.LabelRole, self.label_174)

        self.lineEdit_Ca1_bp3 = QLineEdit(self.scrollAreaWidgetContents_3)
        self.lineEdit_Ca1_bp3.setObjectName(u"lineEdit_Ca1_bp3")

        self.formLayout_7.setWidget(11, QFormLayout.FieldRole, self.lineEdit_Ca1_bp3)

        self.label_189 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_189.setObjectName(u"label_189")

        self.formLayout_7.setWidget(12, QFormLayout.LabelRole, self.label_189)

        self.lineEdit_ca_bp3 = QLineEdit(self.scrollAreaWidgetContents_3)
        self.lineEdit_ca_bp3.setObjectName(u"lineEdit_ca_bp3")

        self.formLayout_7.setWidget(12, QFormLayout.FieldRole, self.lineEdit_ca_bp3)

        self.label_175 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_175.setObjectName(u"label_175")

        self.formLayout_7.setWidget(13, QFormLayout.LabelRole, self.label_175)

        self.lineEdit_fd_bp3 = QLineEdit(self.scrollAreaWidgetContents_3)
        self.lineEdit_fd_bp3.setObjectName(u"lineEdit_fd_bp3")

        self.formLayout_7.setWidget(13, QFormLayout.FieldRole, self.lineEdit_fd_bp3)

        self.label_176 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_176.setObjectName(u"label_176")

        self.formLayout_7.setWidget(14, QFormLayout.LabelRole, self.label_176)

        self.lineEdit_fs_bp3 = QLineEdit(self.scrollAreaWidgetContents_3)
        self.lineEdit_fs_bp3.setObjectName(u"lineEdit_fs_bp3")

        self.formLayout_7.setWidget(14, QFormLayout.FieldRole, self.lineEdit_fs_bp3)

        self.label_177 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_177.setObjectName(u"label_177")

        self.formLayout_7.setWidget(15, QFormLayout.LabelRole, self.label_177)

        self.lineEdit_fm_bp3 = QLineEdit(self.scrollAreaWidgetContents_3)
        self.lineEdit_fm_bp3.setObjectName(u"lineEdit_fm_bp3")

        self.formLayout_7.setWidget(15, QFormLayout.FieldRole, self.lineEdit_fm_bp3)

        self.label_178 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_178.setObjectName(u"label_178")

        self.formLayout_7.setWidget(16, QFormLayout.LabelRole, self.label_178)

        self.lineEdit_fp_bp3 = QLineEdit(self.scrollAreaWidgetContents_3)
        self.lineEdit_fp_bp3.setObjectName(u"lineEdit_fp_bp3")

        self.formLayout_7.setWidget(16, QFormLayout.FieldRole, self.lineEdit_fp_bp3)

        self.label_188 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_188.setObjectName(u"label_188")

        self.formLayout_7.setWidget(17, QFormLayout.LabelRole, self.label_188)

        self.lineEdit_fv_bp3 = QLineEdit(self.scrollAreaWidgetContents_3)
        self.lineEdit_fv_bp3.setObjectName(u"lineEdit_fv_bp3")

        self.formLayout_7.setWidget(17, QFormLayout.FieldRole, self.lineEdit_fv_bp3)

        self.label_190 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_190.setObjectName(u"label_190")

        self.formLayout_7.setWidget(18, QFormLayout.LabelRole, self.label_190)

        self.lineEdit_Cr_bp3 = QLineEdit(self.scrollAreaWidgetContents_3)
        self.lineEdit_Cr_bp3.setObjectName(u"lineEdit_Cr_bp3")

        self.formLayout_7.setWidget(18, QFormLayout.FieldRole, self.lineEdit_Cr_bp3)

        self.label_191 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_191.setObjectName(u"label_191")

        self.formLayout_7.setWidget(19, QFormLayout.LabelRole, self.label_191)

        self.lineEdit_Cr1_bp3 = QLineEdit(self.scrollAreaWidgetContents_3)
        self.lineEdit_Cr1_bp3.setObjectName(u"lineEdit_Cr1_bp3")

        self.formLayout_7.setWidget(19, QFormLayout.FieldRole, self.lineEdit_Cr1_bp3)

        self.label_192 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_192.setObjectName(u"label_192")

        self.formLayout_7.setWidget(20, QFormLayout.LabelRole, self.label_192)

        self.lineEdit_cr_bp3 = QLineEdit(self.scrollAreaWidgetContents_3)
        self.lineEdit_cr_bp3.setObjectName(u"lineEdit_cr_bp3")

        self.formLayout_7.setWidget(20, QFormLayout.FieldRole, self.lineEdit_cr_bp3)

        self.lineEdit_b_bp3 = QLineEdit(self.scrollAreaWidgetContents_3)
        self.lineEdit_b_bp3.setObjectName(u"lineEdit_b_bp3")

        self.formLayout_7.setWidget(0, QFormLayout.FieldRole, self.lineEdit_b_bp3)

        self.label_196 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_196.setObjectName(u"label_196")

        self.formLayout_7.setWidget(0, QFormLayout.LabelRole, self.label_196)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_3)

        self.gridLayout_21.addWidget(self.scrollArea_2, 0, 0, 1, 1)


        self.horizontalLayout_12.addWidget(self.groupBox_16)


        self.verticalLayout_27.addWidget(self.widget_11)

        self.stackedWidget_2.addWidget(self.Parte_3)
        self.Parte_4 = QWidget()
        self.Parte_4.setObjectName(u"Parte_4")
        self.verticalLayout_28 = QVBoxLayout(self.Parte_4)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.widget_12 = QWidget(self.Parte_4)
        self.widget_12.setObjectName(u"widget_12")
        self.horizontalLayout_13 = QHBoxLayout(self.widget_12)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.groupBox_17 = QGroupBox(self.widget_12)
        self.groupBox_17.setObjectName(u"groupBox_17")

        self.horizontalLayout_13.addWidget(self.groupBox_17)

        self.groupBox_18 = QGroupBox(self.widget_12)
        self.groupBox_18.setObjectName(u"groupBox_18")

        self.horizontalLayout_13.addWidget(self.groupBox_18)


        self.verticalLayout_28.addWidget(self.widget_12)

        self.stackedWidget_2.addWidget(self.Parte_4)
        self.Parte_5 = QWidget()
        self.Parte_5.setObjectName(u"Parte_5")
        self.verticalLayout_29 = QVBoxLayout(self.Parte_5)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.widget_13 = QWidget(self.Parte_5)
        self.widget_13.setObjectName(u"widget_13")
        self.horizontalLayout_14 = QHBoxLayout(self.widget_13)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.groupBox_19 = QGroupBox(self.widget_13)
        self.groupBox_19.setObjectName(u"groupBox_19")

        self.horizontalLayout_14.addWidget(self.groupBox_19)

        self.groupBox_20 = QGroupBox(self.widget_13)
        self.groupBox_20.setObjectName(u"groupBox_20")

        self.horizontalLayout_14.addWidget(self.groupBox_20)


        self.verticalLayout_29.addWidget(self.widget_13)

        self.stackedWidget_2.addWidget(self.Parte_5)

        self.verticalLayout_18.addWidget(self.stackedWidget_2)


        self.verticalLayout_17.addWidget(self.widget_8)

        self.stackedWidget.addWidget(self.bandas)
        self.zarandas = QWidget()
        self.zarandas.setObjectName(u"zarandas")
        self.horizontalLayout_7 = QHBoxLayout(self.zarandas)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.widget_7 = QWidget(self.zarandas)
        self.widget_7.setObjectName(u"widget_7")
        self.horizontalLayout_15 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.groupBox_9 = QGroupBox(self.widget_7)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.groupBox_9.setStyleSheet(u"QGroupBox {\n"
"    \n"
"	font: 600 24pt \"Bookman Old Style\";\n"
"    border: 2px;\n"
"	\n"
"    margin-top: 10px; /* Ajusta el margen superior seg\u00fan tus necesidades */\n"
"	/*font: 350 20pt \"Yu Gothic UI Semilight\";*/\n"
"    padding-top: 30px; /* Ajusta el espaciado superior seg\u00fan tus necesidades */\n"
"}\n"
"\n"
"")
        self.groupBox_9.setAlignment(Qt.AlignCenter)
        self.gridLayout_14 = QGridLayout(self.groupBox_9)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.groupBox_2 = QGroupBox(self.groupBox_9)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setStyleSheet(u"QGroupBox {\n"
"    border: 1px solid rgba(128, 128, 128, 0.5); /* Ajusta la opacidad seg\u00fan tus necesidades */\n"
"    margin-top: 10px; /* Ajusta el margen superior seg\u00fan tus necesidades */\n"
"    padding-top: 20px; /* Ajusta el espaciado superior seg\u00fan tus necesidades */\n"
"	\n"
"	font: 600 12pt \"Bookman Old Style\";\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"    border: 1px solid rgb(189, 147, 249);\n"
"}")
        self.gridLayout_6 = QGridLayout(self.groupBox_2)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_90 = QLabel(self.groupBox_2)
        self.label_90.setObjectName(u"label_90")

        self.gridLayout_6.addWidget(self.label_90, 1, 0, 1, 1)

        self.lineEditAreaUtil = QLineEdit(self.groupBox_2)
        self.lineEditAreaUtil.setObjectName(u"lineEditAreaUtil")

        self.gridLayout_6.addWidget(self.lineEditAreaUtil, 7, 1, 1, 1)

        self.label_97 = QLabel(self.groupBox_2)
        self.label_97.setObjectName(u"label_97")

        self.gridLayout_6.addWidget(self.label_97, 9, 0, 1, 1)

        self.label_89 = QLabel(self.groupBox_2)
        self.label_89.setObjectName(u"label_89")

        self.gridLayout_6.addWidget(self.label_89, 0, 0, 1, 1)

        self.label_95 = QLabel(self.groupBox_2)
        self.label_95.setObjectName(u"label_95")

        self.gridLayout_6.addWidget(self.label_95, 7, 0, 1, 1)

        self.lineEditEficiencia = QLineEdit(self.groupBox_2)
        self.lineEditEficiencia.setObjectName(u"lineEditEficiencia")

        self.gridLayout_6.addWidget(self.lineEditEficiencia, 8, 1, 1, 1)

        self.lineEditPorcentajePeso = QLineEdit(self.groupBox_2)
        self.lineEditPorcentajePeso.setObjectName(u"lineEditPorcentajePeso")

        self.gridLayout_6.addWidget(self.lineEditPorcentajePeso, 3, 1, 1, 1)

        self.label_91 = QLabel(self.groupBox_2)
        self.label_91.setObjectName(u"label_91")

        self.gridLayout_6.addWidget(self.label_91, 2, 0, 1, 1)

        self.lineEditDensidadMaterial = QLineEdit(self.groupBox_2)
        self.lineEditDensidadMaterial.setObjectName(u"lineEditDensidadMaterial")

        self.gridLayout_6.addWidget(self.lineEditDensidadMaterial, 6, 1, 1, 1)

        self.lineEditSizeParticula = QLineEdit(self.groupBox_2)
        self.lineEditSizeParticula.setObjectName(u"lineEditSizeParticula")

        self.gridLayout_6.addWidget(self.lineEditSizeParticula, 2, 1, 1, 1)

        self.lineEditPorcentajeMaterialRetenido = QLineEdit(self.groupBox_2)
        self.lineEditPorcentajeMaterialRetenido.setObjectName(u"lineEditPorcentajeMaterialRetenido")

        self.gridLayout_6.addWidget(self.lineEditPorcentajeMaterialRetenido, 4, 1, 1, 1)

        self.comboBoxNumeroPisos = QComboBox(self.groupBox_2)
        self.comboBoxNumeroPisos.addItem("")
        self.comboBoxNumeroPisos.addItem("")
        self.comboBoxNumeroPisos.addItem("")
        self.comboBoxNumeroPisos.addItem("")
        self.comboBoxNumeroPisos.setObjectName(u"comboBoxNumeroPisos")
        self.comboBoxNumeroPisos.setCursor(QCursor(Qt.PointingHandCursor))
        self.comboBoxNumeroPisos.setStyleSheet(u"QComboBox QAbstractItemView {\n"
"	background: transparent;\n"
"    background-color: #FFFFFF; /* Cambia el color de fondo de las opciones\n"
"	 desplegadas a blanco */\n"
"	color: #000000; /* Cambia el color del texto a negro */\n"
"}")

        self.gridLayout_6.addWidget(self.comboBoxNumeroPisos, 9, 1, 1, 1)

        self.lineEditCapacidadZaranda = QLineEdit(self.groupBox_2)
        self.lineEditCapacidadZaranda.setObjectName(u"lineEditCapacidadZaranda")

        self.gridLayout_6.addWidget(self.lineEditCapacidadZaranda, 0, 1, 1, 1)

        self.label_106 = QLabel(self.groupBox_2)
        self.label_106.setObjectName(u"label_106")

        self.gridLayout_6.addWidget(self.label_106, 4, 0, 1, 1)

        self.comboBoxTipoMalla = QComboBox(self.groupBox_2)
        self.comboBoxTipoMalla.addItem("")
        self.comboBoxTipoMalla.addItem("")
        self.comboBoxTipoMalla.addItem("")
        self.comboBoxTipoMalla.addItem("")
        self.comboBoxTipoMalla.setObjectName(u"comboBoxTipoMalla")
        self.comboBoxTipoMalla.setCursor(QCursor(Qt.PointingHandCursor))
        self.comboBoxTipoMalla.setStyleSheet(u"QComboBox QAbstractItemView {\n"
"	background: transparent;\n"
"    background-color: #FFFFFF; /* Cambia el color de fondo de las opciones\n"
"	 desplegadas a blanco */\n"
"	color: #000000; /* Cambia el color del texto a negro */\n"
"}")

        self.gridLayout_6.addWidget(self.comboBoxTipoMalla, 10, 1, 1, 1)

        self.label_92 = QLabel(self.groupBox_2)
        self.label_92.setObjectName(u"label_92")

        self.gridLayout_6.addWidget(self.label_92, 3, 0, 1, 1)

        self.label_93 = QLabel(self.groupBox_2)
        self.label_93.setObjectName(u"label_93")

        self.gridLayout_6.addWidget(self.label_93, 5, 0, 1, 1)

        self.label_108 = QLabel(self.groupBox_2)
        self.label_108.setObjectName(u"label_108")

        self.gridLayout_6.addWidget(self.label_108, 10, 0, 1, 1)

        self.label_88 = QLabel(self.groupBox_2)
        self.label_88.setObjectName(u"label_88")

        self.gridLayout_6.addWidget(self.label_88, 6, 0, 1, 1)

        self.lineEditSizeMalla = QLineEdit(self.groupBox_2)
        self.lineEditSizeMalla.setObjectName(u"lineEditSizeMalla")

        self.gridLayout_6.addWidget(self.lineEditSizeMalla, 1, 1, 1, 1)

        self.label_96 = QLabel(self.groupBox_2)
        self.label_96.setObjectName(u"label_96")

        self.gridLayout_6.addWidget(self.label_96, 8, 0, 1, 1)

        self.lineEditPorcentajeHalfsize = QLineEdit(self.groupBox_2)
        self.lineEditPorcentajeHalfsize.setObjectName(u"lineEditPorcentajeHalfsize")

        self.gridLayout_6.addWidget(self.lineEditPorcentajeHalfsize, 5, 1, 1, 1)

        self.verticalSpacer_22 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer_22, 11, 1, 1, 1)


        self.gridLayout_14.addWidget(self.groupBox_2, 0, 0, 1, 1)

        self.pushButton_3 = QPushButton(self.groupBox_9)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet(u"\n"
"QPushButton:hover {\n"
"    font-size: 15px;\n"
"	\n"
"	\n"
"	background-color: rgb(106, 200, 243);\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	padding-left:5px;\n"
"	padding-top:5px;\n"
"	\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(69, 193, 151, 255), stop:0.528409 rgba(100, 191, 195, 216), stop:1 rgba(29, 135, 219, 255));\n"
"}\n"
"")

        self.gridLayout_14.addWidget(self.pushButton_3, 1, 0, 1, 1)

        self.groupBox_5 = QGroupBox(self.groupBox_9)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setStyleSheet(u"QGroupBox {\n"
"    border: 1px solid rgba(128, 128, 128, 0.5); /* Ajusta la opacidad seg\u00fan tus necesidades */\n"
"    margin-top: 10px; /* Ajusta el margen superior seg\u00fan tus necesidades */\n"
"    padding-top: 0px; /* Ajusta el espaciado superior seg\u00fan tus necesidades */\n"
"	\n"
"	font: 600 12pt \"Bookman Old Style\";\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"    border: 1px solid rgb(189, 147, 249);\n"
"}")
        self.gridLayout_7 = QGridLayout(self.groupBox_5)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(-1, 27, -1, -1)
        self.lineEditFactorD = QLineEdit(self.groupBox_5)
        self.lineEditFactorD.setObjectName(u"lineEditFactorD")

        self.gridLayout_7.addWidget(self.lineEditFactorD, 3, 1, 1, 1)

        self.label_101 = QLabel(self.groupBox_5)
        self.label_101.setObjectName(u"label_101")
        self.label_101.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_7.addWidget(self.label_101, 3, 0, 1, 1)

        self.label_94 = QLabel(self.groupBox_5)
        self.label_94.setObjectName(u"label_94")
        self.label_94.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_7.addWidget(self.label_94, 6, 0, 1, 1)

        self.label_99 = QLabel(self.groupBox_5)
        self.label_99.setObjectName(u"label_99")
        self.label_99.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_7.addWidget(self.label_99, 1, 0, 1, 1)

        self.lineEdit_12 = QLineEdit(self.groupBox_5)
        self.lineEdit_12.setObjectName(u"lineEdit_12")

        self.gridLayout_7.addWidget(self.lineEdit_12, 4, 1, 1, 1)

        self.label_105 = QLabel(self.groupBox_5)
        self.label_105.setObjectName(u"label_105")
        self.label_105.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_7.addWidget(self.label_105, 9, 0, 1, 1)

        self.label_98 = QLabel(self.groupBox_5)
        self.label_98.setObjectName(u"label_98")
        self.label_98.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_7.addWidget(self.label_98, 0, 0, 1, 1)

        self.lineEditFactorJ = QLineEdit(self.groupBox_5)
        self.lineEditFactorJ.setObjectName(u"lineEditFactorJ")

        self.gridLayout_7.addWidget(self.lineEditFactorJ, 8, 1, 1, 1)

        self.label_104 = QLabel(self.groupBox_5)
        self.label_104.setObjectName(u"label_104")
        self.label_104.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_7.addWidget(self.label_104, 8, 0, 1, 1)

        self.lineEditFactorG = QLineEdit(self.groupBox_5)
        self.lineEditFactorG.setObjectName(u"lineEditFactorG")

        self.gridLayout_7.addWidget(self.lineEditFactorG, 6, 1, 1, 1)

        self.lineEditFactorB = QLineEdit(self.groupBox_5)
        self.lineEditFactorB.setObjectName(u"lineEditFactorB")

        self.gridLayout_7.addWidget(self.lineEditFactorB, 1, 1, 1, 1)

        self.label_100 = QLabel(self.groupBox_5)
        self.label_100.setObjectName(u"label_100")
        self.label_100.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_7.addWidget(self.label_100, 2, 0, 1, 1)

        self.lineEditFactorH = QLineEdit(self.groupBox_5)
        self.lineEditFactorH.setObjectName(u"lineEditFactorH")

        self.gridLayout_7.addWidget(self.lineEditFactorH, 7, 1, 1, 1)

        self.label_124 = QLabel(self.groupBox_5)
        self.label_124.setObjectName(u"label_124")
        self.label_124.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_7.addWidget(self.label_124, 4, 0, 1, 1)

        self.lineEditFactorC = QLineEdit(self.groupBox_5)
        self.lineEditFactorC.setObjectName(u"lineEditFactorC")

        self.gridLayout_7.addWidget(self.lineEditFactorC, 2, 1, 1, 1)

        self.label_103 = QLabel(self.groupBox_5)
        self.label_103.setObjectName(u"label_103")
        self.label_103.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_7.addWidget(self.label_103, 7, 0, 1, 1)

        self.lineEditFactorF = QLineEdit(self.groupBox_5)
        self.lineEditFactorF.setObjectName(u"lineEditFactorF")

        self.gridLayout_7.addWidget(self.lineEditFactorF, 5, 1, 1, 1)

        self.label_102 = QLabel(self.groupBox_5)
        self.label_102.setObjectName(u"label_102")
        self.label_102.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_7.addWidget(self.label_102, 5, 0, 1, 1)

        self.lineEditAreaZaranda = QLineEdit(self.groupBox_5)
        self.lineEditAreaZaranda.setObjectName(u"lineEditAreaZaranda")

        self.gridLayout_7.addWidget(self.lineEditAreaZaranda, 9, 1, 1, 1)

        self.lineEditFactorA = QLineEdit(self.groupBox_5)
        self.lineEditFactorA.setObjectName(u"lineEditFactorA")

        self.gridLayout_7.addWidget(self.lineEditFactorA, 0, 1, 1, 1)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_7.addItem(self.verticalSpacer_9, 10, 0, 1, 1)


        self.gridLayout_14.addWidget(self.groupBox_5, 0, 1, 1, 1)

        self.boton_calcular6 = QPushButton(self.groupBox_9)
        self.boton_calcular6.setObjectName(u"boton_calcular6")
        sizePolicy14 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy14.setHorizontalStretch(0)
        sizePolicy14.setVerticalStretch(0)
        sizePolicy14.setHeightForWidth(self.boton_calcular6.sizePolicy().hasHeightForWidth())
        self.boton_calcular6.setSizePolicy(sizePolicy14)
        self.boton_calcular6.setCursor(QCursor(Qt.PointingHandCursor))
        self.boton_calcular6.setStyleSheet(u"\n"
"QPushButton:hover {\n"
"    font-size: 15px;\n"
"	\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(0, 255, 69);\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	padding-left:5px;\n"
"	padding-top:5px;\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(211, 255, 102, 255), stop:0.55 rgba(139, 235, 44, 255), stop:0.98 rgba(9, 146, 76, 149), stop:1 rgba(0, 0, 0, 0));\n"
"}")

        self.gridLayout_14.addWidget(self.boton_calcular6, 2, 0, 1, 1)

        self.boton_limpiar6 = QPushButton(self.groupBox_9)
        self.boton_limpiar6.setObjectName(u"boton_limpiar6")
        sizePolicy14.setHeightForWidth(self.boton_limpiar6.sizePolicy().hasHeightForWidth())
        self.boton_limpiar6.setSizePolicy(sizePolicy14)
        self.boton_limpiar6.setCursor(QCursor(Qt.PointingHandCursor))
        self.boton_limpiar6.setStyleSheet(u"\n"
"QPushButton:hover {\n"
"    font-size: 15px;\n"
"	\n"
"	background-color: rgb(255, 44, 44);\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	padding-left:5px;\n"
"	padding-top:5px;\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(53, 21, 21, 255), stop:0.55 rgba(235, 93, 44, 255), stop:0.98 rgba(146, 91, 9, 255), stop:1 rgba(0, 0, 0, 0));\n"
"}\n"
"")

        self.gridLayout_14.addWidget(self.boton_limpiar6, 1, 1, 1, 1)


        self.horizontalLayout_15.addWidget(self.groupBox_9)


        self.horizontalLayout_7.addWidget(self.widget_7)

        self.stackedWidget.addWidget(self.zarandas)

        self.verticalLayout_15.addWidget(self.stackedWidget)


        self.horizontalLayout_4.addWidget(self.pagesContainer)

        self.extraRightBox = QFrame(self.content)
        self.extraRightBox.setObjectName(u"extraRightBox")
        self.extraRightBox.setMinimumSize(QSize(0, 0))
        self.extraRightBox.setMaximumSize(QSize(0, 16777215))
        self.extraRightBox.setCursor(QCursor(Qt.ArrowCursor))
        self.extraRightBox.setStyleSheet(u"\n"
"\n"
"QFrame #extraRightBox{\n"
"background-color: rgb(255, 255, 255);\n"
"	border-color: rgb(111, 111, 111);\n"
"\n"
"    border: 0.5px solid gray;  /* Grosor del borde y color (puedes ajustarlos) */\n"
"	\n"
"    border-radius: 5px;  /* Borde redondeado (opcional) */\n"
"}\n"
"\n"
"")
        self.extraRightBox.setFrameShape(QFrame.NoFrame)
        self.extraRightBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.extraRightBox)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.themeSettingsTopDetail = QFrame(self.extraRightBox)
        self.themeSettingsTopDetail.setObjectName(u"themeSettingsTopDetail")
        self.themeSettingsTopDetail.setMaximumSize(QSize(16777215, 3))
        self.themeSettingsTopDetail.setFrameShape(QFrame.NoFrame)
        self.themeSettingsTopDetail.setFrameShadow(QFrame.Raised)

        self.verticalLayout_7.addWidget(self.themeSettingsTopDetail)

        self.contentSettings = QFrame(self.extraRightBox)
        self.contentSettings.setObjectName(u"contentSettings")
        sizePolicy.setHeightForWidth(self.contentSettings.sizePolicy().hasHeightForWidth())
        self.contentSettings.setSizePolicy(sizePolicy)
        self.contentSettings.setMinimumSize(QSize(0, 0))
        self.contentSettings.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.contentSettings.setFrameShape(QFrame.NoFrame)
        self.contentSettings.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.contentSettings)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.topMenus = QFrame(self.contentSettings)
        self.topMenus.setObjectName(u"topMenus")
        sizePolicy.setHeightForWidth(self.topMenus.sizePolicy().hasHeightForWidth())
        self.topMenus.setSizePolicy(sizePolicy)
        self.topMenus.setMinimumSize(QSize(0, 0))
        self.topMenus.setStyleSheet(u"QPushButton:hover {\n"
"    font-size: 15px;\n"
"	background-color: rgb(204, 232, 255);\n"
"\n"
"}")
        self.topMenus.setFrameShape(QFrame.NoFrame)
        self.topMenus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.topMenus)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.label_197 = QLabel(self.topMenus)
        self.label_197.setObjectName(u"label_197")
        self.label_197.setStyleSheet(u"color:rgb(125, 205, 243);\n"
"font:14px")
        self.label_197.setAlignment(Qt.AlignCenter)
        self.label_197.setMargin(5)

        self.verticalLayout_14.addWidget(self.label_197)

        self.btn_manual_zaranda = QPushButton(self.topMenus)
        self.btn_manual_zaranda.setObjectName(u"btn_manual_zaranda")
        sizePolicy1.setHeightForWidth(self.btn_manual_zaranda.sizePolicy().hasHeightForWidth())
        self.btn_manual_zaranda.setSizePolicy(sizePolicy1)
        self.btn_manual_zaranda.setMinimumSize(QSize(0, 45))
        self.btn_manual_zaranda.setFont(font1)
        self.btn_manual_zaranda.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_manual_zaranda.setLayoutDirection(Qt.LeftToRight)
        self.btn_manual_zaranda.setStyleSheet(u"background-image: url(:/icons/images/icons/informacion.png);")

        self.verticalLayout_14.addWidget(self.btn_manual_zaranda)

        self.btn_manual_elevador = QPushButton(self.topMenus)
        self.btn_manual_elevador.setObjectName(u"btn_manual_elevador")
        sizePolicy1.setHeightForWidth(self.btn_manual_elevador.sizePolicy().hasHeightForWidth())
        self.btn_manual_elevador.setSizePolicy(sizePolicy1)
        self.btn_manual_elevador.setMinimumSize(QSize(0, 45))
        self.btn_manual_elevador.setFont(font1)
        self.btn_manual_elevador.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_manual_elevador.setLayoutDirection(Qt.LeftToRight)
        self.btn_manual_elevador.setStyleSheet(u"background-image: url(:/icons/images/icons/informacion.png);")

        self.verticalLayout_14.addWidget(self.btn_manual_elevador)

        self.btn_manual_molino = QPushButton(self.topMenus)
        self.btn_manual_molino.setObjectName(u"btn_manual_molino")
        sizePolicy1.setHeightForWidth(self.btn_manual_molino.sizePolicy().hasHeightForWidth())
        self.btn_manual_molino.setSizePolicy(sizePolicy1)
        self.btn_manual_molino.setMinimumSize(QSize(0, 45))
        self.btn_manual_molino.setFont(font1)
        self.btn_manual_molino.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_manual_molino.setLayoutDirection(Qt.LeftToRight)
        self.btn_manual_molino.setStyleSheet(u"background-image: url(:/icons/images/icons/informacion.png);")

        self.verticalLayout_14.addWidget(self.btn_manual_molino)

        self.btn_manual_banda = QPushButton(self.topMenus)
        self.btn_manual_banda.setObjectName(u"btn_manual_banda")
        self.btn_manual_banda.setMinimumSize(QSize(0, 45))
        self.btn_manual_banda.setStyleSheet(u"background-image: url(:/icons/images/icons/informacion.png);")

        self.verticalLayout_14.addWidget(self.btn_manual_banda)

        self.btn_manual_tornillo = QPushButton(self.topMenus)
        self.btn_manual_tornillo.setObjectName(u"btn_manual_tornillo")
        self.btn_manual_tornillo.setMinimumSize(QSize(0, 45))
        self.btn_manual_tornillo.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_manual_tornillo.setStyleSheet(u"background-image: url(:/icons/images/icons/informacion.png);")

        self.verticalLayout_14.addWidget(self.btn_manual_tornillo)

        self.btn_manual_zaranda.raise_()
        self.btn_manual_molino.raise_()
        self.btn_manual_elevador.raise_()
        self.btn_manual_banda.raise_()
        self.label_197.raise_()
        self.btn_manual_tornillo.raise_()

        self.verticalLayout_13.addWidget(self.topMenus, 0, Qt.AlignTop)


        self.verticalLayout_7.addWidget(self.contentSettings)


        self.horizontalLayout_4.addWidget(self.extraRightBox)


        self.verticalLayout_6.addWidget(self.content)

        self.bottomBar = QFrame(self.contentBottom)
        self.bottomBar.setObjectName(u"bottomBar")
        self.bottomBar.setMinimumSize(QSize(0, 22))
        self.bottomBar.setMaximumSize(QSize(16777215, 22))
        self.bottomBar.setStyleSheet(u"")
        self.bottomBar.setFrameShape(QFrame.NoFrame)
        self.bottomBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.bottomBar)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.creditsLabel = QLabel(self.bottomBar)
        self.creditsLabel.setObjectName(u"creditsLabel")
        self.creditsLabel.setMaximumSize(QSize(16777215, 16))
        font6 = QFont()
        font6.setFamilies([u"Segoe UI"])
        font6.setBold(False)
        font6.setItalic(False)
        self.creditsLabel.setFont(font6)
        self.creditsLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.creditsLabel)

        self.version = QLabel(self.bottomBar)
        self.version.setObjectName(u"version")
        self.version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.version)

        self.frame_size_grip = QFrame(self.bottomBar)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMinimumSize(QSize(20, 0))
        self.frame_size_grip.setMaximumSize(QSize(20, 16777215))
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_size_grip)


        self.verticalLayout_6.addWidget(self.bottomBar)


        self.verticalLayout_2.addWidget(self.contentBottom)


        self.appLayout.addWidget(self.contentBox)


        self.horizontalLayout_8.addWidget(self.bgApp)

        MainWindow.setCentralWidget(self.styleSheet)
        QWidget.setTabOrder(self.toggleButton, self.btn_home)
        QWidget.setTabOrder(self.btn_home, self.btn_zarandas)
        QWidget.setTabOrder(self.btn_zarandas, self.btn_elevadores)
        QWidget.setTabOrder(self.btn_elevadores, self.btn_molino)
        QWidget.setTabOrder(self.btn_molino, self.btn_bandas)
        QWidget.setTabOrder(self.btn_bandas, self.btn_tornillo)
        QWidget.setTabOrder(self.btn_tornillo, self.toggleLeftBox)
        QWidget.setTabOrder(self.toggleLeftBox, self.extraCloseColumnBtn)
        QWidget.setTabOrder(self.extraCloseColumnBtn, self.btn_share)
        QWidget.setTabOrder(self.btn_share, self.btn_adjustments)
        QWidget.setTabOrder(self.btn_adjustments, self.btn_more)
        QWidget.setTabOrder(self.btn_more, self.textEdit)
        QWidget.setTabOrder(self.textEdit, self.settingsTopBtn)
        QWidget.setTabOrder(self.settingsTopBtn, self.minimizeAppBtn)
        QWidget.setTabOrder(self.minimizeAppBtn, self.maximizeRestoreAppBtn)
        QWidget.setTabOrder(self.maximizeRestoreAppBtn, self.closeAppBtn)
        QWidget.setTabOrder(self.closeAppBtn, self.reset_elevador)
        QWidget.setTabOrder(self.reset_elevador, self.reset_button_tornillo)
        QWidget.setTabOrder(self.reset_button_tornillo, self.modos_tornillo)
        QWidget.setTabOrder(self.modos_tornillo, self.bton_home_zaranda)
        QWidget.setTabOrder(self.bton_home_zaranda, self.bton_home_cangilon)
        QWidget.setTabOrder(self.bton_home_cangilon, self.bton_home_tornillo)
        QWidget.setTabOrder(self.bton_home_tornillo, self.bton_home_banda)
        QWidget.setTabOrder(self.bton_home_banda, self.bton_home_molino)
        QWidget.setTabOrder(self.bton_home_molino, self.pushButton_17)
        QWidget.setTabOrder(self.pushButton_17, self.menu_molino_rodillo)
        QWidget.setTabOrder(self.menu_molino_rodillo, self.menu_molino_cono)
        QWidget.setTabOrder(self.menu_molino_cono, self.menu_molino_bola)
        QWidget.setTabOrder(self.menu_molino_bola, self.menu_molino_mandibula)
        QWidget.setTabOrder(self.menu_molino_mandibula, self.lineEdit_D_tornillo)
        QWidget.setTabOrder(self.lineEdit_D_tornillo, self.comboBox_lambda_tornillo)
        QWidget.setTabOrder(self.comboBox_lambda_tornillo, self.lineEdit_t_tornillo)
        QWidget.setTabOrder(self.lineEdit_t_tornillo, self.lineEdit_n_tornillo)
        QWidget.setTabOrder(self.lineEdit_n_tornillo, self.comboBox_k_tornillo)
        QWidget.setTabOrder(self.comboBox_k_tornillo, self.lineEdit_y_tornillo)
        QWidget.setTabOrder(self.lineEdit_y_tornillo, self.lineEdit_L_tornillo)
        QWidget.setTabOrder(self.lineEdit_L_tornillo, self.lineEdit_H_tornillo)
        QWidget.setTabOrder(self.lineEdit_H_tornillo, self.comboBox_Co_tornillo)
        QWidget.setTabOrder(self.comboBox_Co_tornillo, self.lineEdit_s_tornillo)
        QWidget.setTabOrder(self.lineEdit_s_tornillo, self.lineEdit_v_tornillo)
        QWidget.setTabOrder(self.lineEdit_v_tornillo, self.lineEdit_Q_tornillo)
        QWidget.setTabOrder(self.lineEdit_Q_tornillo, self.lineEdit_pst_tornillo)
        QWidget.setTabOrder(self.lineEdit_pst_tornillo, self.lineEdit_PN_tornillo)
        QWidget.setTabOrder(self.lineEdit_PN_tornillo, self.lineEdit_PH_tornillo)
        QWidget.setTabOrder(self.lineEdit_PH_tornillo, self.lineEdit_P_tornillo)
        QWidget.setTabOrder(self.lineEdit_P_tornillo, self.pushButton)
        QWidget.setTabOrder(self.pushButton, self.pushButton_8)
        QWidget.setTabOrder(self.pushButton_8, self.lineEdit_i_elevador)
        QWidget.setTabOrder(self.lineEdit_i_elevador, self.lineEdit_p_elevador)
        QWidget.setTabOrder(self.lineEdit_p_elevador, self.lineEdit_j_elevador)
        QWidget.setTabOrder(self.lineEdit_j_elevador, self.lineEdit_v_elevador)
        QWidget.setTabOrder(self.lineEdit_v_elevador, self.comboBox_tipo_elevador)
        QWidget.setTabOrder(self.comboBox_tipo_elevador, self.comboBox_Tparticula_elevador)
        QWidget.setTabOrder(self.comboBox_Tparticula_elevador, self.lineEdit_h_elevador)
        QWidget.setTabOrder(self.lineEdit_h_elevador, self.lineEdit_pp_elevador)
        QWidget.setTabOrder(self.lineEdit_pp_elevador, self.lineEdit_cte_elevador)
        QWidget.setTabOrder(self.lineEdit_cte_elevador, self.lineEdit_tc_elevador)
        QWidget.setTabOrder(self.lineEdit_tc_elevador, self.lineEdit_t_elevador)
        QWidget.setTabOrder(self.lineEdit_t_elevador, self.lineEdit_H_elevador)
        QWidget.setTabOrder(self.lineEdit_H_elevador, self.comboBox_sistema_elevador)
        QWidget.setTabOrder(self.comboBox_sistema_elevador, self.lineEdit_n_elevador)
        QWidget.setTabOrder(self.lineEdit_n_elevador, self.lineEdit_Pc_elevador)
        QWidget.setTabOrder(self.lineEdit_Pc_elevador, self.lineEdit_q_elevador)
        QWidget.setTabOrder(self.lineEdit_q_elevador, self.lineEdit_Na_elevador)
        QWidget.setTabOrder(self.lineEdit_Na_elevador, self.lineEdit_Fa_elevador)
        QWidget.setTabOrder(self.lineEdit_Fa_elevador, self.lineEdit_FR_elevador)
        QWidget.setTabOrder(self.lineEdit_FR_elevador, self.lineEdit_m_elevador)
        QWidget.setTabOrder(self.lineEdit_m_elevador, self.lineEdit_Ta_elevador)
        QWidget.setTabOrder(self.lineEdit_Ta_elevador, self.comboBox_k_elevador)
        QWidget.setTabOrder(self.comboBox_k_elevador, self.lineEdit_D_elevador)
        QWidget.setTabOrder(self.lineEdit_D_elevador, self.lineEdit_Nc_elevador)
        QWidget.setTabOrder(self.lineEdit_Nc_elevador, self.lineEdit_sh_elevador)
        QWidget.setTabOrder(self.lineEdit_sh_elevador, self.lineEdit_sv_elevador)
        QWidget.setTabOrder(self.lineEdit_sv_elevador, self.lineEdit_a_elevador)
        QWidget.setTabOrder(self.lineEdit_a_elevador, self.lineEdit_s_elevador)
        QWidget.setTabOrder(self.lineEdit_s_elevador, self.lineEdit_alfa_elevador)
        QWidget.setTabOrder(self.lineEdit_alfa_elevador, self.lineEdit_R_elevador)
        QWidget.setTabOrder(self.lineEdit_R_elevador, self.combo_modos_elevador)
        QWidget.setTabOrder(self.combo_modos_elevador, self.calculate_elevador)
        QWidget.setTabOrder(self.calculate_elevador, self.btn_molinobola)
        QWidget.setTabOrder(self.btn_molinobola, self.btn_molino_rodillo)
        QWidget.setTabOrder(self.btn_molino_rodillo, self.pushButton_trituradora_mand)
        QWidget.setTabOrder(self.pushButton_trituradora_mand, self.pushButton_trituradora_cono)
        QWidget.setTabOrder(self.pushButton_trituradora_cono, self.lineEditSizeAlimento)
        QWidget.setTabOrder(self.lineEditSizeAlimento, self.lineEditSizeProducto)
        QWidget.setTabOrder(self.lineEditSizeProducto, self.lineEditDensidadAlimento)
        QWidget.setTabOrder(self.lineEditDensidadAlimento, self.lineEditDensidadBolas)
        QWidget.setTabOrder(self.lineEditDensidadBolas, self.lineEditDiametroMolino)
        QWidget.setTabOrder(self.lineEditDiametroMolino, self.lineEditLongitudMolino)
        QWidget.setTabOrder(self.lineEditLongitudMolino, self.lineEditPorosidadLecho)
        QWidget.setTabOrder(self.lineEditPorosidadLecho, self.lineEditMasaRocas)
        QWidget.setTabOrder(self.lineEditMasaRocas, self.lineEditMasaBolas)
        QWidget.setTabOrder(self.lineEditMasaBolas, self.lineEditNumeroLevantadores)
        QWidget.setTabOrder(self.lineEditNumeroLevantadores, self.lineEditSizeBolas)
        QWidget.setTabOrder(self.lineEditSizeBolas, self.lineEditFraccionRocas)
        QWidget.setTabOrder(self.lineEditFraccionRocas, self.lineEditFraccionBolas)
        QWidget.setTabOrder(self.lineEditFraccionBolas, self.lineEditConstanteMolino)
        QWidget.setTabOrder(self.lineEditConstanteMolino, self.lineEditFrecuenciaMolienda_2)
        QWidget.setTabOrder(self.lineEditFrecuenciaMolienda_2, self.lineEditFrecuenciaCritica_2)
        QWidget.setTabOrder(self.lineEditFrecuenciaCritica_2, self.lineEditFraccionFrecuenciaC)
        QWidget.setTabOrder(self.lineEditFraccionFrecuenciaC, self.lineEditIndiceAbrasion)
        QWidget.setTabOrder(self.lineEditIndiceAbrasion, self.lineEditIndiceBond)
        QWidget.setTabOrder(self.lineEditIndiceBond, self.lineEditFactorCorrecionCapacidad)
        QWidget.setTabOrder(self.lineEditFactorCorrecionCapacidad, self.comboBoxTipoMolienda)
        QWidget.setTabOrder(self.comboBoxTipoMolienda, self.lineEditDesgasteBolas)
        QWidget.setTabOrder(self.lineEditDesgasteBolas, self.lineEditCapacidadMolino)
        QWidget.setTabOrder(self.lineEditCapacidadMolino, self.lineEditPotenciaMolino)
        QWidget.setTabOrder(self.lineEditPotenciaMolino, self.botonCalcular)
        QWidget.setTabOrder(self.botonCalcular, self.lineEditAlimentoRodillo)
        QWidget.setTabOrder(self.lineEditAlimentoRodillo, self.lineEditProductoRodillo)
        QWidget.setTabOrder(self.lineEditProductoRodillo, self.lineEditTamaoMaximo)
        QWidget.setTabOrder(self.lineEditTamaoMaximo, self.lineEditDensidadRodillo)
        QWidget.setTabOrder(self.lineEditDensidadRodillo, self.lineEditTortaSalida)
        QWidget.setTabOrder(self.lineEditTortaSalida, self.lineEditGrosorTorta)
        QWidget.setTabOrder(self.lineEditGrosorTorta, self.lineEditCoeficienteFriccion)
        QWidget.setTabOrder(self.lineEditCoeficienteFriccion, self.lineEditAnguloApertura)
        QWidget.setTabOrder(self.lineEditAnguloApertura, self.lineEditAnguloFractura)
        QWidget.setTabOrder(self.lineEditAnguloFractura, self.lineEditAnguloCompresion)
        QWidget.setTabOrder(self.lineEditAnguloCompresion, self.lineEditWidthRodillos)
        QWidget.setTabOrder(self.lineEditWidthRodillos, self.lineEditDiametroRodillos)
        QWidget.setTabOrder(self.lineEditDiametroRodillos, self.lineEditk1)
        QWidget.setTabOrder(self.lineEditk1, self.lineEditk2)
        QWidget.setTabOrder(self.lineEditk2, self.lineEditk3)
        QWidget.setTabOrder(self.lineEditk3, self.lineEditk4)
        QWidget.setTabOrder(self.lineEditk4, self.lineEditTorqueMolienda)
        QWidget.setTabOrder(self.lineEditTorqueMolienda, self.lineEditFuerzaEspecifica)
        QWidget.setTabOrder(self.lineEditFuerzaEspecifica, self.lineEditDistanciaRodillos)
        QWidget.setTabOrder(self.lineEditDistanciaRodillos, self.lineEditVelocidadRodillos)
        QWidget.setTabOrder(self.lineEditVelocidadRodillos, self.lineEditCapacidadRodillos)
        QWidget.setTabOrder(self.lineEditCapacidadRodillos, self.lineEditSizePotenciaRodillos)
        QWidget.setTabOrder(self.lineEditSizePotenciaRodillos, self.botonCalcular_5)
        QWidget.setTabOrder(self.botonCalcular_5, self.botonLimpiar_5)
        QWidget.setTabOrder(self.botonLimpiar_5, self.lineEditSizeAlimento_2)
        QWidget.setTabOrder(self.lineEditSizeAlimento_2, self.lineEditSizeProducto_2)
        QWidget.setTabOrder(self.lineEditSizeProducto_2, self.lineEditSizeMayor_2)
        QWidget.setTabOrder(self.lineEditSizeMayor_2, self.lineEditSetCono)
        QWidget.setTabOrder(self.lineEditSetCono, self.lineEditGape_2)
        QWidget.setTabOrder(self.lineEditGape_2, self.lineEditDiametroBowl)
        QWidget.setTabOrder(self.lineEditDiametroBowl, self.lineEditDensidadAlimento_2)
        QWidget.setTabOrder(self.lineEditDensidadAlimento_2, self.lineEditLminCono)
        QWidget.setTabOrder(self.lineEditLminCono, self.lineEditLmax)
        QWidget.setTabOrder(self.lineEditLmax, self.lineEditFactorK)
        QWidget.setTabOrder(self.lineEditFactorK, self.lineEditRelacionR)
        QWidget.setTabOrder(self.lineEditRelacionR, self.lineEditCapacidadCono)
        QWidget.setTabOrder(self.lineEditCapacidadCono, self.lineEditOtroIndiceCono)
        QWidget.setTabOrder(self.lineEditOtroIndiceCono, self.lineEditPotenciaCono)
        QWidget.setTabOrder(self.lineEditPotenciaCono, self.lineEditSizeMayor)
        QWidget.setTabOrder(self.lineEditSizeMayor, self.lineEditSizeMenor)
        QWidget.setTabOrder(self.lineEditSizeMenor, self.lineEditDensidad)
        QWidget.setTabOrder(self.lineEditDensidad, self.lineEditLmin)
        QWidget.setTabOrder(self.lineEditLmin, self.lineEditFrecuenciaMolienda)
        QWidget.setTabOrder(self.lineEditFrecuenciaMolienda, self.lineEditSet)
        QWidget.setTabOrder(self.lineEditSet, self.lineEditGape)
        QWidget.setTabOrder(self.lineEditGape, self.lineEditAlturaTriturador)
        QWidget.setTabOrder(self.lineEditAlturaTriturador, self.lineEditWidth)
        QWidget.setTabOrder(self.lineEditWidth, self.lineEditThrow)
        QWidget.setTabOrder(self.lineEditThrow, self.lineEditCapacidadTrituradora)
        QWidget.setTabOrder(self.lineEditCapacidadTrituradora, self.lineEditFrecuenciaCritica)
        QWidget.setTabOrder(self.lineEditFrecuenciaCritica, self.lineEditCapacidadReal)
        QWidget.setTabOrder(self.lineEditCapacidadReal, self.lineEditRelacionReduccion)
        QWidget.setTabOrder(self.lineEditRelacionReduccion, self.lineEditOtroIndiceTrituradora)
        QWidget.setTabOrder(self.lineEditOtroIndiceTrituradora, self.lineEditPotenciaTrituradora)
        QWidget.setTabOrder(self.lineEditPotenciaTrituradora, self.botonCalcularMandibula)
        QWidget.setTabOrder(self.botonCalcularMandibula, self.lineEditCapacidadZaranda)
        QWidget.setTabOrder(self.lineEditCapacidadZaranda, self.lineEditSizeMalla)
        QWidget.setTabOrder(self.lineEditSizeMalla, self.lineEditSizeParticula)
        QWidget.setTabOrder(self.lineEditSizeParticula, self.lineEditPorcentajePeso)
        QWidget.setTabOrder(self.lineEditPorcentajePeso, self.lineEditPorcentajeMaterialRetenido)
        QWidget.setTabOrder(self.lineEditPorcentajeMaterialRetenido, self.lineEditPorcentajeHalfsize)
        QWidget.setTabOrder(self.lineEditPorcentajeHalfsize, self.lineEditDensidadMaterial)
        QWidget.setTabOrder(self.lineEditDensidadMaterial, self.lineEditAreaUtil)
        QWidget.setTabOrder(self.lineEditAreaUtil, self.lineEditEficiencia)
        QWidget.setTabOrder(self.lineEditEficiencia, self.comboBoxNumeroPisos)
        QWidget.setTabOrder(self.comboBoxNumeroPisos, self.comboBoxTipoMalla)
        QWidget.setTabOrder(self.comboBoxTipoMalla, self.lineEditFactorA)
        QWidget.setTabOrder(self.lineEditFactorA, self.lineEditFactorB)
        QWidget.setTabOrder(self.lineEditFactorB, self.lineEditFactorC)
        QWidget.setTabOrder(self.lineEditFactorC, self.lineEditFactorD)
        QWidget.setTabOrder(self.lineEditFactorD, self.lineEdit_12)
        QWidget.setTabOrder(self.lineEdit_12, self.lineEditFactorF)
        QWidget.setTabOrder(self.lineEditFactorF, self.lineEditFactorG)
        QWidget.setTabOrder(self.lineEditFactorG, self.lineEditFactorH)
        QWidget.setTabOrder(self.lineEditFactorH, self.lineEditFactorJ)
        QWidget.setTabOrder(self.lineEditFactorJ, self.lineEditAreaZaranda)
        QWidget.setTabOrder(self.lineEditAreaZaranda, self.boton_limpiar6)
        QWidget.setTabOrder(self.boton_limpiar6, self.lineEdit_lvt_bp1)
        QWidget.setTabOrder(self.lineEdit_lvt_bp1, self.lineEdit_lvm_bp1)
        QWidget.setTabOrder(self.lineEdit_lvm_bp1, self.lineEdit_k_bp1)
        QWidget.setTabOrder(self.lineEdit_k_bp1, self.lineEdit_k1_bp1)
        QWidget.setTabOrder(self.lineEdit_k1_bp1, self.lineEdit_s_bp1)
        QWidget.setTabOrder(self.lineEdit_s_bp1, self.lineEdit_A1_bp1)
        QWidget.setTabOrder(self.lineEdit_A1_bp1, self.lineEdit_A2_bp1)
        QWidget.setTabOrder(self.lineEdit_A2_bp1, self.comboBox_tb_bp2)
        QWidget.setTabOrder(self.comboBox_tb_bp2, self.lineEdit_fu_bp2)
        QWidget.setTabOrder(self.lineEdit_fu_bp2, self.lineEdit_l_bp2)
        QWidget.setTabOrder(self.lineEdit_l_bp2, self.lineEdit_cq_bp2)
        QWidget.setTabOrder(self.lineEdit_cq_bp2, self.lineEdit_ct_bp2)
        QWidget.setTabOrder(self.lineEdit_ct_bp2, self.lineEdit_f_bp2)
        QWidget.setTabOrder(self.lineEdit_f_bp2, self.lineEdit_qb_bp2)
        QWidget.setTabOrder(self.lineEdit_qb_bp2, self.lineEdit_qg_bp2)
        QWidget.setTabOrder(self.lineEdit_qg_bp2, self.lineEdit_qru_bp2)
        QWidget.setTabOrder(self.lineEdit_qru_bp2, self.lineEdit_qro_bp2)
        QWidget.setTabOrder(self.lineEdit_qro_bp2, self.lineEdit_h_bp2)
        QWidget.setTabOrder(self.lineEdit_h_bp2, self.lineEdit_v_bp2)
        QWidget.setTabOrder(self.lineEdit_v_bp2, self.lineEdit_n_bp2)
        QWidget.setTabOrder(self.lineEdit_n_bp2, self.lineEdit_p_bp2)
        QWidget.setTabOrder(self.lineEdit_p_bp2, self.scrollArea)
        QWidget.setTabOrder(self.scrollArea, self.lineEdit_pprs_bp2)
        QWidget.setTabOrder(self.lineEdit_pprs_bp2, self.lineEdit_ao_bp2)
        QWidget.setTabOrder(self.lineEdit_ao_bp2, self.lineEdit_ppri_bp2)
        QWidget.setTabOrder(self.lineEdit_ppri_bp2, self.lineEdit_au_bp2)
        QWidget.setTabOrder(self.lineEdit_au_bp2, self.lineEdit_t1_bp2)
        QWidget.setTabOrder(self.lineEdit_t1_bp2, self.lineEdit_t2_bp2)
        QWidget.setTabOrder(self.lineEdit_t2_bp2, self.lineEdit_fa_bp2)
        QWidget.setTabOrder(self.lineEdit_fa_bp2, self.lineEdit_cw_bp2)
        QWidget.setTabOrder(self.lineEdit_cw_bp2, self.lineEdit_t3_bp2)
        QWidget.setTabOrder(self.lineEdit_t3_bp2, self.lineEdit_fr_bp2)
        QWidget.setTabOrder(self.lineEdit_fr_bp2, self.lineEdit_tg_bp2)
        QWidget.setTabOrder(self.lineEdit_tg_bp2, self.lineEdit_lc_bp2)
        QWidget.setTabOrder(self.lineEdit_lc_bp2, self.lineEdit_ht_bp2)
        QWidget.setTabOrder(self.lineEdit_ht_bp2, self.lineEdit_tumax_bp2)
        QWidget.setTabOrder(self.lineEdit_tumax_bp2, self.lineEdit_tmax_bp2)
        QWidget.setTabOrder(self.lineEdit_tmax_bp2, self.lineEdit_N_bp2)
        QWidget.setTabOrder(self.lineEdit_N_bp2, self.lineEdit_t0_bp2)
        QWidget.setTabOrder(self.lineEdit_t0_bp2, self.pushButton_4)
        QWidget.setTabOrder(self.pushButton_4, self.pushButton_bandas_cal_2)
        QWidget.setTabOrder(self.pushButton_bandas_cal_2, self.lineEdit_mif_bp3)
        QWidget.setTabOrder(self.lineEdit_mif_bp3, self.lineEdit_mf_bp3)
        QWidget.setTabOrder(self.lineEdit_mf_bp3, self.lineEdit_mt_bp3)
        QWidget.setTabOrder(self.lineEdit_mt_bp3, self.lineEdit_w_bp3)
        QWidget.setTabOrder(self.lineEdit_w_bp3, self.lineEdit_u_bp3)
        QWidget.setTabOrder(self.lineEdit_u_bp3, self.lineEdit_d_bp3)
        QWidget.setTabOrder(self.lineEdit_d_bp3, self.lineEdit_cp_bp3)
        QWidget.setTabOrder(self.lineEdit_cp_bp3, self.lineEdit_t1_bp3)
        QWidget.setTabOrder(self.lineEdit_t1_bp3, self.lineEdit_t2_bp3)
        QWidget.setTabOrder(self.lineEdit_t2_bp3, self.lineEdit_qt_bp3)
        QWidget.setTabOrder(self.lineEdit_qt_bp3, self.lineEdit_p_bp3)
        QWidget.setTabOrder(self.lineEdit_p_bp3, self.lineEdit_n_bp3)
        QWidget.setTabOrder(self.lineEdit_n_bp3, self.lineEdit_cpr_bp3)
        QWidget.setTabOrder(self.lineEdit_cpr_bp3, self.lineEdit_ft_bp3)
        QWidget.setTabOrder(self.lineEdit_ft_bp3, self.lineEdit_ao_bp3)
        QWidget.setTabOrder(self.lineEdit_ao_bp3, self.lineEdit_au_bp3)
        QWidget.setTabOrder(self.lineEdit_au_bp3, self.lineEdit_qb_bp3)
        QWidget.setTabOrder(self.lineEdit_qb_bp3, self.pushButton_5)
        QWidget.setTabOrder(self.pushButton_5, self.pushButton_bandas_cal_3)
        QWidget.setTabOrder(self.pushButton_bandas_cal_3, self.scrollArea_2)
        QWidget.setTabOrder(self.scrollArea_2, self.lineEdit_lv_bp3)
        QWidget.setTabOrder(self.lineEdit_lv_bp3, self.lineEdit_c_bp3)
        QWidget.setTabOrder(self.lineEdit_c_bp3, self.lineEdit_ot_bp3)
        QWidget.setTabOrder(self.lineEdit_ot_bp3, self.lineEdit_ag_bp3)
        QWidget.setTabOrder(self.lineEdit_ag_bp3, self.lineEdit_ee_bp3)
        QWidget.setTabOrder(self.lineEdit_ee_bp3, self.lineEdit_j_bp3)
        QWidget.setTabOrder(self.lineEdit_j_bp3, self.lineEdit_n_bp3_2)
        QWidget.setTabOrder(self.lineEdit_n_bp3_2, self.lineEdit_v_bp3)
        QWidget.setTabOrder(self.lineEdit_v_bp3, self.lineEdit_D_bp3)
        QWidget.setTabOrder(self.lineEdit_D_bp3, self.lineEdit_Ca_bp3)
        QWidget.setTabOrder(self.lineEdit_Ca_bp3, self.lineEdit_Ca1_bp3)
        QWidget.setTabOrder(self.lineEdit_Ca1_bp3, self.lineEdit_ca_bp3)
        QWidget.setTabOrder(self.lineEdit_ca_bp3, self.lineEdit_fd_bp3)
        QWidget.setTabOrder(self.lineEdit_fd_bp3, self.lineEdit_fs_bp3)
        QWidget.setTabOrder(self.lineEdit_fs_bp3, self.lineEdit_fm_bp3)
        QWidget.setTabOrder(self.lineEdit_fm_bp3, self.lineEdit_fp_bp3)
        QWidget.setTabOrder(self.lineEdit_fp_bp3, self.lineEdit_fv_bp3)
        QWidget.setTabOrder(self.lineEdit_fv_bp3, self.lineEdit_Cr_bp3)
        QWidget.setTabOrder(self.lineEdit_Cr_bp3, self.lineEdit_Cr1_bp3)
        QWidget.setTabOrder(self.lineEdit_Cr1_bp3, self.lineEdit_cr_bp3)
        QWidget.setTabOrder(self.lineEdit_cr_bp3, self.lineEdit_b_bp3)
        QWidget.setTabOrder(self.lineEdit_b_bp3, self.comboBox)
        QWidget.setTabOrder(self.comboBox, self.parte1)
        QWidget.setTabOrder(self.parte1, self.botonLimpiar)
        QWidget.setTabOrder(self.botonLimpiar, self.comboBox_3)
        QWidget.setTabOrder(self.comboBox_3, self.comboBox_2)
        QWidget.setTabOrder(self.comboBox_2, self.opcionesMolinoRodillo)
        QWidget.setTabOrder(self.opcionesMolinoRodillo, self.parte2)
        QWidget.setTabOrder(self.parte2, self.botonCalcular_3)
        QWidget.setTabOrder(self.botonCalcular_3, self.parte3)
        QWidget.setTabOrder(self.parte3, self.botonLimpiar_3)
        QWidget.setTabOrder(self.botonLimpiar_3, self.botonLimpiarMandibula)
        QWidget.setTabOrder(self.botonLimpiarMandibula, self.pushButton_3)
        QWidget.setTabOrder(self.pushButton_3, self.lineEdit1)
        QWidget.setTabOrder(self.lineEdit1, self.lineEdit2)
        QWidget.setTabOrder(self.lineEdit2, self.lineEdit_v_bp1)
        QWidget.setTabOrder(self.lineEdit_v_bp1, self.lineEdit_qg_bp1)
        QWidget.setTabOrder(self.lineEdit_qg_bp1, self.tableWidget)
        QWidget.setTabOrder(self.tableWidget, self.lineEdit_lv_bp1)
        QWidget.setTabOrder(self.lineEdit_lv_bp1, self.lineEdit_11)
        QWidget.setTabOrder(self.lineEdit_11, self.lineEdit3)
        QWidget.setTabOrder(self.lineEdit3, self.lineEdit_lm_bp1)
        QWidget.setTabOrder(self.lineEdit_lm_bp1, self.searchBar)
        QWidget.setTabOrder(self.searchBar, self.boton_calcular6)
        QWidget.setTabOrder(self.boton_calcular6, self.lineEdit_qs_bp1)
        QWidget.setTabOrder(self.lineEdit_qs_bp1, self.btn_manual_zaranda)
        QWidget.setTabOrder(self.btn_manual_zaranda, self.btn_manual_elevador)
        QWidget.setTabOrder(self.btn_manual_elevador, self.btn_manual_molino)
        QWidget.setTabOrder(self.btn_manual_molino, self.btn_manual_banda)
        QWidget.setTabOrder(self.btn_manual_banda, self.btn_manual_tornillo)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(3)
        self.stackedWidget_3.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.styleSheet.setToolTip(QCoreApplication.translate("MainWindow", u"expand", None))
#endif // QT_CONFIG(tooltip)
        self.titleLeftApp.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>ChemSolid</p></body></html>", None))
        self.titleLeftDescription.setText(QCoreApplication.translate("MainWindow", u"Modern GUI / Flat Style", None))
#if QT_CONFIG(tooltip)
        self.toggleButton.setToolTip(QCoreApplication.translate("MainWindow", u"expand", None))
#endif // QT_CONFIG(tooltip)
        self.toggleButton.setText(QCoreApplication.translate("MainWindow", u"Hide", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_zarandas.setText(QCoreApplication.translate("MainWindow", u"Vibrating screens", None))
        self.btn_elevadores.setText(QCoreApplication.translate("MainWindow", u"Bucket Elevators", None))
        self.btn_molino.setText(QCoreApplication.translate("MainWindow", u"Grinding Mills", None))
        self.btn_bandas.setText(QCoreApplication.translate("MainWindow", u"Conveyor belts", None))
        self.btn_tornillo.setText(QCoreApplication.translate("MainWindow", u"Endless Screw", None))
#if QT_CONFIG(tooltip)
        self.toggleLeftBox.setToolTip(QCoreApplication.translate("MainWindow", u"more", None))
#endif // QT_CONFIG(tooltip)
        self.toggleLeftBox.setText(QCoreApplication.translate("MainWindow", u"Left Box", None))
        self.extraLabel.setText(QCoreApplication.translate("MainWindow", u"Left Box", None))
#if QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close left box", None))
#endif // QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setText("")
        self.btn_share.setText(QCoreApplication.translate("MainWindow", u"Share", None))
        self.btn_adjustments.setText(QCoreApplication.translate("MainWindow", u"Adjustments", None))
        self.btn_more.setText(QCoreApplication.translate("MainWindow", u"Credits", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">ChemSolid</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#000000;\">Solid handling equipment sizing application</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12p"
                        "x; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#000000;\">Interface created using Python and PySide (support for PyQt) .</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#000000;\">MIT License</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#bd93f9;\">Modified by: Kaleth Padilla, Et al</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-l"
                        "eft:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt;\"><br /></p></body></html>", None))
        self.titleRightInfo.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>ChemSolid</p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.settingsTopBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Manuals", None))
#endif // QT_CONFIG(tooltip)
        self.settingsTopBtn.setText("")
#if QT_CONFIG(tooltip)
        self.minimizeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.closeAppBtn.setText("")
        self.groupBox_36.setTitle("")
        self.bton_home_cangilon.setText("")
        self.bton_home_tornillo.setText("")
        self.pushButton_17.setText("")
        self.bton_home_zaranda.setText("")
        self.bton_home_banda.setText("")
        self.bton_home_molino.setText("")
        self.groupBox_12.setTitle("")
        self.menu_molino_mandibula.setText("")
        self.menu_molino_rodillo.setText("")
        self.menu_molino_bola.setText("")
        self.menu_molino_cono.setText("")
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Desing of Screw Conveyors: Mode", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Operating parameters", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Flow Reduction Factor (k): ", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Installation length (m): ", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Material Resistance Coefficient: ", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Screw Diameter (m): ", None))
        self.comboBox_lambda_tornillo.setItemText(0, QCoreApplication.translate("MainWindow", u"Unspecified", None))
        self.comboBox_lambda_tornillo.setItemText(1, QCoreApplication.translate("MainWindow", u"Heavy and abrasive ( \u03bb=0.125)", None))
        self.comboBox_lambda_tornillo.setItemText(2, QCoreApplication.translate("MainWindow", u"Heavy and not very abrasive  (\u03bb=0.25)", None))
        self.comboBox_lambda_tornillo.setItemText(3, QCoreApplication.translate("MainWindow", u"Not very abrasive (\u03bb=0.32)", None))
        self.comboBox_lambda_tornillo.setItemText(4, QCoreApplication.translate("MainWindow", u"Light, non-abrasive (\u03bb=0.4)", None))

        self.comboBox_k_tornillo.setItemText(0, QCoreApplication.translate("MainWindow", u"Unspecified", None))
        self.comboBox_k_tornillo.setItemText(1, QCoreApplication.translate("MainWindow", u"Gutter inclination of 0\u00b0", None))
        self.comboBox_k_tornillo.setItemText(2, QCoreApplication.translate("MainWindow", u"Gutter inclination of 5\u00b0", None))
        self.comboBox_k_tornillo.setItemText(3, QCoreApplication.translate("MainWindow", u"Gutter inclination of 10\u00b0", None))
        self.comboBox_k_tornillo.setItemText(4, QCoreApplication.translate("MainWindow", u"Gutter inclination of 15\u00b0", None))
        self.comboBox_k_tornillo.setItemText(5, QCoreApplication.translate("MainWindow", u"Gutter inclination of 20\u00b0", None))

        self.label_2.setText(QCoreApplication.translate("MainWindow", u"S: Gutter Filling Area (m\u00b2): ", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Q: Material Flow (t/h)", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Screw Pitch (m): ", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"PH: Material Transport Power (kW):", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"PN: Vacuum Screw Drive (kW): ", None))
        self.reset_button_tornillo.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"V: Conveyor speed (m/s): ", None))
        self.label_25.setText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Filling Coefficient (\u03bb): ", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Screw Rotation Speed (rpm): ", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"P: Net Power Required (kW): ", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Calculate", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Pst: Power of inclined screw conveyor (kW)", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Material density (t/m3): ", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Installation height (m)", None))
        self.comboBox_Co_tornillo.setItemText(0, QCoreApplication.translate("MainWindow", u"Unspecified", None))
        self.comboBox_Co_tornillo.setItemText(1, QCoreApplication.translate("MainWindow", u"flours, sawdust, granular products", None))
        self.comboBox_Co_tornillo.setItemText(2, QCoreApplication.translate("MainWindow", u"Peat, soda ash, coal dust", None))
        self.comboBox_Co_tornillo.setItemText(3, QCoreApplication.translate("MainWindow", u"Anthracite, coal, rock salt", None))
        self.comboBox_Co_tornillo.setItemText(4, QCoreApplication.translate("MainWindow", u"Gypsum, dry clay, fine soil, cement, lime, sand", None))

        self.groupBox_10.setTitle("")
        self.pushButton_8.setText("")
        self.modos_tornillo.setItemText(0, QCoreApplication.translate("MainWindow", u"General", None))
        self.modos_tornillo.setItemText(1, QCoreApplication.translate("MainWindow", u"S: Gutter Filling Area (m\u00b2): ", None))
        self.modos_tornillo.setItemText(2, QCoreApplication.translate("MainWindow", u"Screw Rotation Speed (rpm): ", None))
        self.modos_tornillo.setItemText(3, QCoreApplication.translate("MainWindow", u"Q: Material Flow (t/h)", None))
        self.modos_tornillo.setItemText(4, QCoreApplication.translate("MainWindow", u"Pst: Power of inclined screw conveyor (kW)", None))
        self.modos_tornillo.setItemText(5, QCoreApplication.translate("MainWindow", u"PN: Vacuum Screw Drive (kW): ", None))
        self.modos_tornillo.setItemText(6, QCoreApplication.translate("MainWindow", u"PH: Material Transport Power (kW):", None))
        self.modos_tornillo.setItemText(7, QCoreApplication.translate("MainWindow", u"P: Net Power Required (kW): ", None))

        self.groupBox_30.setTitle(QCoreApplication.translate("MainWindow", u"Bucket Elevador Mode:", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"Desing parameters", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"t: Bucket Pitch: ", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"\u03b7: Motor Performance: ", None))
        self.comboBox_tipo_elevador.setItemText(0, QCoreApplication.translate("MainWindow", u"Unspecified", None))
        self.comboBox_tipo_elevador.setItemText(1, QCoreApplication.translate("MainWindow", u"Normal bucket", None))
        self.comboBox_tipo_elevador.setItemText(2, QCoreApplication.translate("MainWindow", u"Scoop bucket", None))
        self.comboBox_tipo_elevador.setItemText(3, QCoreApplication.translate("MainWindow", u"Chain bucket", None))

        self.label_35.setText(QCoreApplication.translate("MainWindow", u"j: Fill Coeficiente: ", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"Bucket Type: ", None))
        self.comboBox_sistema_elevador.setItemText(0, QCoreApplication.translate("MainWindow", u"Unspecified", None))
        self.comboBox_sistema_elevador.setItemText(1, QCoreApplication.translate("MainWindow", u"From hopper", None))
        self.comboBox_sistema_elevador.setItemText(2, QCoreApplication.translate("MainWindow", u"By dredging", None))

        self.label_33.setText(QCoreApplication.translate("MainWindow", u"i : Bucket Volume (L): ", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"H: Elevation Height (m): ", None))
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"t chain: Chain Pitch: ", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"Pitch Constant: ", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"Material size: ", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"h: Bucket Height (m): ", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"v: Bucket elevator speed (m/h): ", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"\u03c1: Load Density (kg/L): ", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"Loading System: ", None))
        self.comboBox_Tparticula_elevador.setItemText(0, QCoreApplication.translate("MainWindow", u"Unspecified", None))
        self.comboBox_Tparticula_elevador.setItemText(1, QCoreApplication.translate("MainWindow", u"Small", None))
        self.comboBox_Tparticula_elevador.setItemText(2, QCoreApplication.translate("MainWindow", u"Medium", None))
        self.comboBox_Tparticula_elevador.setItemText(3, QCoreApplication.translate("MainWindow", u"Big", None))

        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Normal Bucket Pitch Ratio (2h-3h): ", None))
        self.calculate_elevador.setText(QCoreApplication.translate("MainWindow", u"Calculate", None))
        self.reset_elevador.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.combo_modos_elevador.setItemText(0, QCoreApplication.translate("MainWindow", u"General", None))
        self.combo_modos_elevador.setItemText(1, QCoreApplication.translate("MainWindow", u"Weight of transported material ", None))
        self.combo_modos_elevador.setItemText(2, QCoreApplication.translate("MainWindow", u"Flow of transported material", None))
        self.combo_modos_elevador.setItemText(3, QCoreApplication.translate("MainWindow", u"Motor Power", None))
        self.combo_modos_elevador.setItemText(4, QCoreApplication.translate("MainWindow", u"Maximum Belt Tension", None))
        self.combo_modos_elevador.setItemText(5, QCoreApplication.translate("MainWindow", u"Bucket Diameter", None))
        self.combo_modos_elevador.setItemText(6, QCoreApplication.translate("MainWindow", u"Number of buckets", None))
        self.combo_modos_elevador.setItemText(7, QCoreApplication.translate("MainWindow", u"Belt travel speed", None))

        self.groupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"Design calculations", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Pc: Weight of transported material (kg): ", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Q: Flow of transported material ( kg/h)", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Na: Drive Motor Power (CV): ", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"Fa: Force required to move the conveyor belt (kg):", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Fr: Net force from material discharge (N)", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"m: Weight of the load (kg): ", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"Ta: Maximum Belt Tension (kg): ", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"K: Drum dependent Coefficient: ", None))
        self.comboBox_k_elevador.setItemText(0, QCoreApplication.translate("MainWindow", u"Unspecified", None))
        self.comboBox_k_elevador.setItemText(1, QCoreApplication.translate("MainWindow", u"Drum Condition: Smooth Wet", None))
        self.comboBox_k_elevador.setItemText(2, QCoreApplication.translate("MainWindow", u"Drum Condition: Smooth Dry", None))
        self.comboBox_k_elevador.setItemText(3, QCoreApplication.translate("MainWindow", u"Drum Condition: Wet coating", None))
        self.comboBox_k_elevador.setItemText(4, QCoreApplication.translate("MainWindow", u"Drum Condition: Dry coating", None))

        self.label_198.setText(QCoreApplication.translate("MainWindow", u"D: Drum Diameter (m): ", None))
        self.label_199.setText(QCoreApplication.translate("MainWindow", u"Number of buckets per hour (Nc/h): ", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"sh: Horizontal displacement (m): ", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"sv: Vertical Displacement (m):", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"a: Acceleration (m/s2): ", None))
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"S: Material trajectory (m): ", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"\u03b1: Inclination angle (\u00b0): ", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"R: Drum Radius (m): ", None))
        self.btn_molinobola.setText(QCoreApplication.translate("MainWindow", u"Ball mill", None))
        self.btn_molino_rodillo.setText(QCoreApplication.translate("MainWindow", u"Roll mill", None))
        self.pushButton_trituradora_mand.setText(QCoreApplication.translate("MainWindow", u"Jaw crusher", None))
        self.pushButton_trituradora_cono.setText(QCoreApplication.translate("MainWindow", u"Cone Crusher", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("MainWindow", u"Ball Mill Mode: ", None))
        self.groupBox_32.setTitle(QCoreApplication.translate("MainWindow", u"Operating conditions", None))
        self.label_225.setText(QCoreApplication.translate("MainWindow", u"Abrasion index (Ai): ", None))
        self.comboBoxTipoMolienda.setItemText(0, QCoreApplication.translate("MainWindow", u"Dry grinding ", None))
        self.comboBoxTipoMolienda.setItemText(1, QCoreApplication.translate("MainWindow", u"Wet grinding", None))

        self.label_226.setText(QCoreApplication.translate("MainWindow", u"Grinding type: ", None))
        self.label_233.setText(QCoreApplication.translate("MainWindow", u"Mill constant (k): ", None))
        self.label_231.setText(QCoreApplication.translate("MainWindow", u"Mill power (kW):  ", None))
        self.label_229.setText(QCoreApplication.translate("MainWindow", u"Bond index (Wi) (kWh/t): ", None))
        self.label_227.setText(QCoreApplication.translate("MainWindow", u"Ball wear (kg/kWh): ", None))
        self.label_72.setText(QCoreApplication.translate("MainWindow", u"Critical Frequency (rpm): ", None))
        self.label_230.setText(QCoreApplication.translate("MainWindow", u"Capacity correction factor (CF): ", None))
        self.label_73.setText(QCoreApplication.translate("MainWindow", u"Fraction of critical frequency (%):  ", None))
        self.label_228.setText(QCoreApplication.translate("MainWindow", u"Mill capacity (t/h):  ", None))
        self.label_71.setText(QCoreApplication.translate("MainWindow", u"Grinding frequency (rpm): ", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"General", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"Ball and Mill Diameter", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("MainWindow", u"Ball Wearing", None))
        self.comboBox_2.setItemText(3, QCoreApplication.translate("MainWindow", u"Mill Power", None))
        self.comboBox_2.setItemText(4, QCoreApplication.translate("MainWindow", u"Mill Capacity", None))

        self.botonLimpiar.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.groupBox_21.setTitle(QCoreApplication.translate("MainWindow", u"Dimensions of the mill", None))
        self.label_68.setText(QCoreApplication.translate("MainWindow", u"Feed particle size (F80) (\u00b5m): ", None))
        self.label_69.setText(QCoreApplication.translate("MainWindow", u"Product particle size (P80) (\u00b5m): ", None))
        self.label_70.setText(QCoreApplication.translate("MainWindow", u"Feed density (t/m3): ", None))
        self.label_218.setText(QCoreApplication.translate("MainWindow", u"Ball density (t/m3): ", None))
        self.label_74.setText(QCoreApplication.translate("MainWindow", u"Mill diameter (m): ", None))
        self.label_232.setText(QCoreApplication.translate("MainWindow", u"Mill width (m): ", None))
        self.label_219.setText(QCoreApplication.translate("MainWindow", u"Bed porosity: ", None))
        self.label_220.setText(QCoreApplication.translate("MainWindow", u"Mass of rock used (t): ", None))
        self.label_221.setText(QCoreApplication.translate("MainWindow", u"Mass of balls used (t): ", None))
        self.label_222.setText(QCoreApplication.translate("MainWindow", u"Number of lifters: ", None))
        self.label_234.setText(QCoreApplication.translate("MainWindow", u"Balls diameter (m): ", None))
        self.label_223.setText(QCoreApplication.translate("MainWindow", u"Fraction occupied by rocks (%): ", None))
        self.label_224.setText(QCoreApplication.translate("MainWindow", u"Fraction occupied by balls (%): ", None))
        self.botonCalcular.setText(QCoreApplication.translate("MainWindow", u"Calculate", None))
        self.groupBox_26.setTitle(QCoreApplication.translate("MainWindow", u"Cone Crusher Mode: ", None))
        self.groupBox_29.setTitle(QCoreApplication.translate("MainWindow", u"Crusher capacity", None))
        self.label_237.setText(QCoreApplication.translate("MainWindow", u"Statistical Factor (K): ", None))
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"Reduction ratio (gape/set):", None))
        self.label_67.setText(QCoreApplication.translate("MainWindow", u"Crusher capacity (ton/h):", None))
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"Bond Index (kWh/t): ", None))
        self.label_64.setText(QCoreApplication.translate("MainWindow", u"Crusher Power (kWh):", None))
        self.comboBox_3.setItemText(0, QCoreApplication.translate("MainWindow", u"General", None))
        self.comboBox_3.setItemText(1, QCoreApplication.translate("MainWindow", u"Bowl Diameter", None))
        self.comboBox_3.setItemText(2, QCoreApplication.translate("MainWindow", u"Mill Capacity ", None))
        self.comboBox_3.setItemText(3, QCoreApplication.translate("MainWindow", u"Mill Power", None))

        self.groupBox_27.setTitle(QCoreApplication.translate("MainWindow", u"Dimensions and other parameters", None))
        self.label_61.setText(QCoreApplication.translate("MainWindow", u"Lmax (m): ", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Gape - Feed Opening (m): ", None))
        self.label_236.setText(QCoreApplication.translate("MainWindow", u"Product particle size (P80) (\u00b5m): ", None))
        self.label_63.setText(QCoreApplication.translate("MainWindow", u"Bowl diameter (m): ", None))
        self.label_62.setText(QCoreApplication.translate("MainWindow", u"Largest particle size (\u00b5m):", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Set - Crusher Opening (m): ", None))
        self.label_235.setText(QCoreApplication.translate("MainWindow", u"Feed particle size (F80) (\u00b5m): ", None))
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"Lmin (m): ", None))
        self.label_238.setText(QCoreApplication.translate("MainWindow", u"Feed density (kg/m3): ", None))
        self.botonLimpiar_3.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.botonCalcular_3.setText(QCoreApplication.translate("MainWindow", u"Calculate", None))
        self.groupBox_24.setTitle(QCoreApplication.translate("MainWindow", u"Roller Mill Mode: ", None))
        self.groupBox_28.setTitle(QCoreApplication.translate("MainWindow", u"Design calculations", None))
        self.label_212.setText(QCoreApplication.translate("MainWindow", u"Specific Grinding Force (N/mm2): ", None))
        self.label_209.setText(QCoreApplication.translate("MainWindow", u"Material Constant - K2: ", None))
        self.label_215.setText(QCoreApplication.translate("MainWindow", u"Mill Capacity (t/h): ", None))
        self.label_211.setText(QCoreApplication.translate("MainWindow", u"Material Constant - K4: ", None))
        self.label_214.setText(QCoreApplication.translate("MainWindow", u"Rolls Distance (m): ", None))
        self.label_210.setText(QCoreApplication.translate("MainWindow", u"Material Constant - K3: ", None))
        self.label_213.setText(QCoreApplication.translate("MainWindow", u"Rolls Speed (m/s)", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Mill Power (kWh):  ", None))
        self.label_204.setText(QCoreApplication.translate("MainWindow", u"Material Constant - K1: ", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Grinding Torque (N m)", None))
        self.botonLimpiar_5.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.groupBox_25.setTitle(QCoreApplication.translate("MainWindow", u"Mill Dimensions ", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Surface Friction Coefficient (\u00b5): ", None))
        self.label_206.setText(QCoreApplication.translate("MainWindow", u"Compacted Cake Density (t/m3): ", None))
        self.label_203.setText(QCoreApplication.translate("MainWindow", u"Largest Particle Size (m): ", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Rolls Diameter (m): ", None))
        self.label_207.setText(QCoreApplication.translate("MainWindow", u"\u03b8sp: Angle of nip for single particle breakage(\u00b0): ", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Feed Particle Size (m): ", None))
        self.label_208.setText(QCoreApplication.translate("MainWindow", u"\u03b8ip:  Angle of nip for interparticle breakage(\u00b0): ", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Product Particle Size (m): ", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Angle of Nip (\u00b0): ", None))
        self.label_216.setText(QCoreApplication.translate("MainWindow", u"Rolls Width (m) ", None))
        self.label_205.setText(QCoreApplication.translate("MainWindow", u"Mineral Feed Density (t/m3): ", None))
        self.label_217.setText(QCoreApplication.translate("MainWindow", u"Thickness of the Compacted Cake (m): ", None))
        self.opcionesMolinoRodillo.setItemText(0, QCoreApplication.translate("MainWindow", u"General", None))
        self.opcionesMolinoRodillo.setItemText(1, QCoreApplication.translate("MainWindow", u"Design angles", None))
        self.opcionesMolinoRodillo.setItemText(2, QCoreApplication.translate("MainWindow", u"Gap and Roll Diameter", None))
        self.opcionesMolinoRodillo.setItemText(3, QCoreApplication.translate("MainWindow", u"Rolls speed", None))
        self.opcionesMolinoRodillo.setItemText(4, QCoreApplication.translate("MainWindow", u"Mill Capacity ", None))
        self.opcionesMolinoRodillo.setItemText(5, QCoreApplication.translate("MainWindow", u"Mill Power ", None))

        self.botonCalcular_5.setText(QCoreApplication.translate("MainWindow", u"Calculate", None))
        self.groupBox_22.setTitle(QCoreApplication.translate("MainWindow", u"Jaw Crusher Mode: ", None))
        self.botonLimpiarMandibula.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.botonCalcularMandibula.setText(QCoreApplication.translate("MainWindow", u"Calculate", None))
        self.groupBox_23.setTitle(QCoreApplication.translate("MainWindow", u"Crusher dimensions", None))
        self.label_86.setText(QCoreApplication.translate("MainWindow", u"Grinding Frequency (rpm): ", None))
        self.label_79.setText(QCoreApplication.translate("MainWindow", u"Jaw Width (m):", None))
        self.label_201.setText(QCoreApplication.translate("MainWindow", u"Smallest Particle Size (m): ", None))
        self.label_76.setText(QCoreApplication.translate("MainWindow", u"Lmin (m): ", None))
        self.label_78.setText(QCoreApplication.translate("MainWindow", u"Vertical Height of the Crusher (m): ", None))
        self.label_87.setText(QCoreApplication.translate("MainWindow", u"Gape - Feed opening (m): ", None))
        self.label_200.setText(QCoreApplication.translate("MainWindow", u"Largest Particle Size (m): ", None))
        self.label_75.setText(QCoreApplication.translate("MainWindow", u"Set - Crusher outlet opening (m): ", None))
        self.label_77.setText(QCoreApplication.translate("MainWindow", u"Material Density (kg/m3):", None))
        self.label_80.setText(QCoreApplication.translate("MainWindow", u"Throw (m): ", None))
        self.groupBox_33.setTitle(QCoreApplication.translate("MainWindow", u"Design calculations", None))
        self.label_82.setText(QCoreApplication.translate("MainWindow", u"Maximum capacity (t/h):", None))
        self.label_83.setText(QCoreApplication.translate("MainWindow", u"Critical Frequency (rpm): ", None))
        self.label_202.setText(QCoreApplication.translate("MainWindow", u"Operation capacity (t/h): ", None))
        self.label_81.setText(QCoreApplication.translate("MainWindow", u"Reduction ratio (gape/set):", None))
        self.label_84.setText(QCoreApplication.translate("MainWindow", u"Bond Work Index (kWh/t): ", None))
        self.label_85.setText(QCoreApplication.translate("MainWindow", u"Operating Power (kWh/t):", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"General", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Mill Geometrical Parameters", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Mill Capacity", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Mill Power", None))

        self.parte1.setText(QCoreApplication.translate("MainWindow", u"Section 1", None))
        self.parte2.setText(QCoreApplication.translate("MainWindow", u"Section 2", None))
        self.parte3.setText(QCoreApplication.translate("MainWindow", u"Section 3", None))
        self.label_4.setText("")
        self.groupBox_11.setTitle(QCoreApplication.translate("MainWindow", u"Material Properties", None))
        self.label_109.setText(QCoreApplication.translate("MainWindow", u"Insert the material: ", None))
        self.searchBar.setText("")
        self.searchBar.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter the  material", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Material name", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Specific weight ( t/m3)", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Specific weight (lb/f )", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Angle of repose", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem4 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Alumina", None));
        ___qtablewidgetitem5 = self.tableWidget.item(0, 1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"0.80-1.04", None));
        ___qtablewidgetitem6 = self.tableWidget.item(0, 2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"50-65", None));
        ___qtablewidgetitem7 = self.tableWidget.item(0, 3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"22", None));
        ___qtablewidgetitem8 = self.tableWidget.item(1, 0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Mineral or rock asbestos", None));
        ___qtablewidgetitem9 = self.tableWidget.item(1, 1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"1.296", None));
        ___qtablewidgetitem10 = self.tableWidget.item(1, 2)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"81", None));
        ___qtablewidgetitem11 = self.tableWidget.item(2, 0)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Antracite", None));
        ___qtablewidgetitem12 = self.tableWidget.item(2, 1)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"0.95", None));
        ___qtablewidgetitem13 = self.tableWidget.item(2, 2)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"61", None));
        ___qtablewidgetitem14 = self.tableWidget.item(2, 3)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"27", None));
        ___qtablewidgetitem15 = self.tableWidget.item(3, 0)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Fine dry clay", None));
        ___qtablewidgetitem16 = self.tableWidget.item(3, 1)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"1.60-1.92", None));
        ___qtablewidgetitem17 = self.tableWidget.item(3, 2)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"100-120", None));
        ___qtablewidgetitem18 = self.tableWidget.item(3, 3)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"35", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.label_123.setText(QCoreApplication.translate("MainWindow", u"Select material: ", None))
        self.label_110.setText(QCoreApplication.translate("MainWindow", u"Specific weight ( t/m3):", None))
        self.label_112.setText(QCoreApplication.translate("MainWindow", u"Specific weight: ( lbs/Cu-ft):", None))
        self.label_111.setText(QCoreApplication.translate("MainWindow", u"Angle of repose (\u00b0): ", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u".", None))
        self.label_113.setText(QCoreApplication.translate("MainWindow", u"qG: weight of material per linear meter (kg/m):", None))
        self.label_114.setText(QCoreApplication.translate("MainWindow", u"Lv: Transport Capacity (m/h): ", None))
        self.label_115.setText(QCoreApplication.translate("MainWindow", u"v: Belt speed (m/s): ", None))
        self.label_116.setText(QCoreApplication.translate("MainWindow", u"IM: Volumetric transport capacities (m3/h):", None))
        self.label_117.setText(QCoreApplication.translate("MainWindow", u"qs: Specific weight of the material (t/m3):", None))
        self.label_118.setText(QCoreApplication.translate("MainWindow", u"IvT: Theoretical capacity in volume (m3/h): ", None))
        self.label_119.setText(QCoreApplication.translate("MainWindow", u"IvM: corrected volumetric transport capacities (m3/h):", None))
        self.label_120.setText(QCoreApplication.translate("MainWindow", u"K: Inclination Factor:", None))
        self.label_121.setText(QCoreApplication.translate("MainWindow", u"K1: Correction Factor: ", None))
        self.label_122.setText(QCoreApplication.translate("MainWindow", u"S: Section area of the transported material (m2):", None))
        self.label_125.setText(QCoreApplication.translate("MainWindow", u"A1: Circular sector area (m2): ", None))
        self.label_126.setText(QCoreApplication.translate("MainWindow", u"A2: Trapezius area (m2): ", None))
        self.pushButton_bandas_cal_1.setText(QCoreApplication.translate("MainWindow", u"Calculate", None))
        self.groupBox_13.setTitle(QCoreApplication.translate("MainWindow", u"Design Parameters", None))
        self.label_140.setText(QCoreApplication.translate("MainWindow", u"Type of section in the band: ", None))
        self.comboBox_tb_bp2.setItemText(0, QCoreApplication.translate("MainWindow", u"Ascending belt section", None))
        self.comboBox_tb_bp2.setItemText(1, QCoreApplication.translate("MainWindow", u"Descending belt section", None))

        self.label_128.setText(QCoreApplication.translate("MainWindow", u"Fu: Total Tangential Stress (daN): ", None))
        self.label_129.setText(QCoreApplication.translate("MainWindow", u"L: Distances between transported axles (m): ", None))
        self.label_131.setText(QCoreApplication.translate("MainWindow", u"Cq: Fixed resistance coefficient: ", None))
        self.label_132.setText(QCoreApplication.translate("MainWindow", u"Ct: Passive resistance coefficient due temperature: ", None))
        self.label_133.setText(QCoreApplication.translate("MainWindow", u"f: Internal friction coefficient of rotating parts:", None))
        self.label_134.setText(QCoreApplication.translate("MainWindow", u"qb: Belt weight per linear meter (kg/m):", None))
        self.label_135.setText(QCoreApplication.translate("MainWindow", u"qG=Material weight transported per linear meter (kg/m):", None))
        self.label_136.setText(QCoreApplication.translate("MainWindow", u"qRU: Weight lower rotating parts refered to station pass (kg/m):", None))
        self.label_137.setText(QCoreApplication.translate("MainWindow", u"qRO: Weight upper rotating parts refered to station pass (kg/m):", None))
        self.label_138.setText(QCoreApplication.translate("MainWindow", u"H: Conveyor belt unevenness (m):", None))
        self.label_141.setText(QCoreApplication.translate("MainWindow", u"v: Belt speed (m): ", None))
        self.label_142.setText(QCoreApplication.translate("MainWindow", u"\u03b7: Reducer performance", None))
        self.label_139.setText(QCoreApplication.translate("MainWindow", u"P: Minimum driving power (kW): ", None))
        self.groupBox_14.setTitle("")
        self.label_143.setText(QCoreApplication.translate("MainWindow", u"ao: Passing of the outgoing stations (m):", None))
        self.label_144.setText(QCoreApplication.translate("MainWindow", u"Ppri: Weight lower rotating parts (kg):", None))
        self.label_145.setText(QCoreApplication.translate("MainWindow", u"au: Passage of return stations (m): ", None))
        self.label_146.setText(QCoreApplication.translate("MainWindow", u"T1: Tight side tension (daN): ", None))
        self.label_147.setText(QCoreApplication.translate("MainWindow", u"T2: Slow side tension (daN): ", None))
        self.label_148.setText(QCoreApplication.translate("MainWindow", u"fa: Friction coefficient between belt and drum:", None))
        self.label_149.setText(QCoreApplication.translate("MainWindow", u"Cw: Huggin Factor: ", None))
        self.label_180.setText(QCoreApplication.translate("MainWindow", u"T3: Drum tension (not control): ", None))
        self.label_181.setText(QCoreApplication.translate("MainWindow", u"Fr: Tangential stress to move the belt (daN):", None))
        self.label_182.setText(QCoreApplication.translate("MainWindow", u"Tg: Belt tension at the counterweight point (daN):", None))
        self.label_183.setText(QCoreApplication.translate("MainWindow", u"lc: Distance drive drum and counterweight center (m):", None))
        self.label_184.setText(QCoreApplication.translate("MainWindow", u"Ht: Unevenness between the drum and the counterweight (m):", None))
        self.label_185.setText(QCoreApplication.translate("MainWindow", u"Tumax: Maximum unit tension of the band (daN/m):", None))
        self.label_186.setText(QCoreApplication.translate("MainWindow", u"Tmax: Tension at the point of maximum belt stress (daN):", None))
        self.label_187.setText(QCoreApplication.translate("MainWindow", u"N: Belt width (mm): ", None))
        self.label_195.setText(QCoreApplication.translate("MainWindow", u"T0: Minimum tail tension in the loading area (daN):", None))
        self.label_130.setText(QCoreApplication.translate("MainWindow", u"Pprs: Weight upper rotating parts (kg):", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.pushButton_bandas_cal_2.setText(QCoreApplication.translate("MainWindow", u"Calculate", None))
        self.groupBox_15.setTitle(QCoreApplication.translate("MainWindow", u"Design Parameters", None))
        self.label_152.setText(QCoreApplication.translate("MainWindow", u"Mif: ideal bending moment (daN*m):", None))
        self.label_150.setText(QCoreApplication.translate("MainWindow", u"Mf: Bending moment (daN*m):", None))
        self.label_153.setText(QCoreApplication.translate("MainWindow", u"Mt: Torque moment (daN*m): ", None))
        self.label_154.setText(QCoreApplication.translate("MainWindow", u"W: Resistance modulus (mm3):", None))
        self.label_155.setText(QCoreApplication.translate("MainWindow", u"\u03c3amm: Allowable Strength (daN/mm2):", None))
        self.label_156.setText(QCoreApplication.translate("MainWindow", u"d: Shaft/tree diameter (m): ", None))
        self.label_157.setText(QCoreApplication.translate("MainWindow", u"Cp: Load from forces on the drive drum axis (daN):", None))
        self.label_158.setText(QCoreApplication.translate("MainWindow", u"T1: Tight side tension (daN): ", None))
        self.label_159.setText(QCoreApplication.translate("MainWindow", u"T2: Slow side tension (daN): ", None))
        self.label_160.setText(QCoreApplication.translate("MainWindow", u"qt: Drum weight (kg): ", None))
        self.label_161.setText(QCoreApplication.translate("MainWindow", u"P:  Absorber Power (kW): ", None))
        self.label_162.setText(QCoreApplication.translate("MainWindow", u"n: Number of revolutions of the drum (giros min): ", None))
        self.label_163.setText(QCoreApplication.translate("MainWindow", u"Cpr: Load on the axis (daN/mm\u00b2)", None))
        self.label_164.setText(QCoreApplication.translate("MainWindow", u"ft: deflection of the axis of symmetry (mm): ", None))
        self.label_165.setText(QCoreApplication.translate("MainWindow", u"ao: Passing of the outgoing stations (m):", None))
        self.label_179.setText(QCoreApplication.translate("MainWindow", u"au: Passage of return stations (m): ", None))
        self.label_193.setText(QCoreApplication.translate("MainWindow", u"qb: weight of the belt per linear meter (kg/m): ", None))
        self.groupBox_16.setTitle("")
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.pushButton_bandas_cal_3.setText(QCoreApplication.translate("MainWindow", u"Calculate", None))
        self.label_194.setText(QCoreApplication.translate("MainWindow", u"lv: belt conveying capacity (material flow) (t/h): ", None))
        self.label_151.setText(QCoreApplication.translate("MainWindow", u"C: Distance between roller supports (m): ", None))
        self.label_166.setText(QCoreApplication.translate("MainWindow", u"\u03b1t: Symmetrical axis inclination (rotation) (\u00ba): ", None))
        self.label_167.setText(QCoreApplication.translate("MainWindow", u"ag: distance between support and drum flange (m):", None))
        self.label_168.setText(QCoreApplication.translate("MainWindow", u"E: Elastic modulus of steel (daN/mm2): ", None))
        self.label_169.setText(QCoreApplication.translate("MainWindow", u"J: Moment of inertia of the material section (mm4)", None))
        self.label_170.setText(QCoreApplication.translate("MainWindow", u"n: Number of revolutions (revs/min: ", None))
        self.label_171.setText(QCoreApplication.translate("MainWindow", u"v: Belt speed (m/s): ", None))
        self.label_172.setText(QCoreApplication.translate("MainWindow", u"D: Rolls diameter (m): ", None))
        self.label_173.setText(QCoreApplication.translate("MainWindow", u"Ca: Static charge at the outbound station (daN): ", None))
        self.label_174.setText(QCoreApplication.translate("MainWindow", u"Ca1: Dynamic load on the drive station (daN): ", None))
        self.label_189.setText(QCoreApplication.translate("MainWindow", u"ca: Load on the central roller of the drive station (daN): ", None))
        self.label_175.setText(QCoreApplication.translate("MainWindow", u"Fd: Impact factor:", None))
        self.label_176.setText(QCoreApplication.translate("MainWindow", u"Fs: Service Factor: ", None))
        self.label_177.setText(QCoreApplication.translate("MainWindow", u"Fm: Ambiental Factor: ", None))
        self.label_178.setText(QCoreApplication.translate("MainWindow", u"Fp: Participation factor", None))
        self.label_188.setText(QCoreApplication.translate("MainWindow", u"Fv: Speed Factor", None))
        self.label_190.setText(QCoreApplication.translate("MainWindow", u"Cr: Static charge at return station (daN): ", None))
        self.label_191.setText(QCoreApplication.translate("MainWindow", u"Cr1: Dynamic loading at the return station (daN): ", None))
        self.label_192.setText(QCoreApplication.translate("MainWindow", u"cr: Load on the roller of the return station (daN): ", None))
        self.label_196.setText(QCoreApplication.translate("MainWindow", u"\u03b2: Overload angle (\u00ba): ", None))
        self.groupBox_17.setTitle(QCoreApplication.translate("MainWindow", u"Parte 4", None))
        self.groupBox_18.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
        self.groupBox_19.setTitle(QCoreApplication.translate("MainWindow", u"Parte 5", None))
        self.groupBox_20.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
        self.groupBox_9.setTitle(QCoreApplication.translate("MainWindow", u"Desing of Vibrating Screens", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Operating conditions", None))
        self.label_90.setText(QCoreApplication.translate("MainWindow", u"Tyler Mesh Size (In):", None))
        self.label_97.setText(QCoreApplication.translate("MainWindow", u"Number of floors: ", None))
        self.label_89.setText(QCoreApplication.translate("MainWindow", u"Capacity (ton/h):", None))
        self.label_95.setText(QCoreApplication.translate("MainWindow", u"% Useful Area (%):", None))
        self.label_91.setText(QCoreApplication.translate("MainWindow", u"Particle Size (um):", None))
        self.comboBoxNumeroPisos.setItemText(0, QCoreApplication.translate("MainWindow", u"One", None))
        self.comboBoxNumeroPisos.setItemText(1, QCoreApplication.translate("MainWindow", u"Two", None))
        self.comboBoxNumeroPisos.setItemText(2, QCoreApplication.translate("MainWindow", u"Three", None))
        self.comboBoxNumeroPisos.setItemText(3, QCoreApplication.translate("MainWindow", u"Other", None))

        self.label_106.setText(QCoreApplication.translate("MainWindow", u"Percentaje of material passing (%):", None))
        self.comboBoxTipoMalla.setItemText(0, QCoreApplication.translate("MainWindow", u"Square", None))
        self.comboBoxTipoMalla.setItemText(1, QCoreApplication.translate("MainWindow", u"Cork groove", None))
        self.comboBoxTipoMalla.setItemText(2, QCoreApplication.translate("MainWindow", u"Long slot", None))
        self.comboBoxTipoMalla.setItemText(3, QCoreApplication.translate("MainWindow", u"Other", None))

        self.label_92.setText(QCoreApplication.translate("MainWindow", u"% Weight (%):", None))
        self.label_93.setText(QCoreApplication.translate("MainWindow", u"% Halfsize (%):", None))
        self.label_108.setText(QCoreApplication.translate("MainWindow", u"Mesh type: ", None))
        self.label_88.setText(QCoreApplication.translate("MainWindow", u"Material density (kg/m3): ", None))
        self.label_96.setText(QCoreApplication.translate("MainWindow", u"Efficiency (%):", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Interpolate factors", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Desing factors and results", None))
        self.label_101.setText(QCoreApplication.translate("MainWindow", u"Factor D: ", None))
        self.label_94.setText(QCoreApplication.translate("MainWindow", u"Factor G: ", None))
        self.label_99.setText(QCoreApplication.translate("MainWindow", u"Factor B: ", None))
        self.label_105.setText(QCoreApplication.translate("MainWindow", u"Screen area: (m2): ", None))
        self.label_98.setText(QCoreApplication.translate("MainWindow", u"Factor A: ", None))
        self.label_104.setText(QCoreApplication.translate("MainWindow", u"Factor J: ", None))
        self.label_100.setText(QCoreApplication.translate("MainWindow", u"Factor C: ", None))
        self.label_124.setText(QCoreApplication.translate("MainWindow", u"Factor E: ", None))
        self.label_103.setText(QCoreApplication.translate("MainWindow", u"Factor H: ", None))
        self.label_102.setText(QCoreApplication.translate("MainWindow", u"Factor F: ", None))
        self.boton_calcular6.setText(QCoreApplication.translate("MainWindow", u"Calculate", None))
        self.boton_limpiar6.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.label_197.setText(QCoreApplication.translate("MainWindow", u"User manuals", None))
        self.btn_manual_zaranda.setText(QCoreApplication.translate("MainWindow", u"Vibrating screens", None))
        self.btn_manual_elevador.setText(QCoreApplication.translate("MainWindow", u"Bucket Elevators", None))
        self.btn_manual_molino.setText(QCoreApplication.translate("MainWindow", u"Grinding Mills", None))
#if QT_CONFIG(whatsthis)
        self.btn_manual_banda.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:700; color:#bc56ae;\">Bandas transportadoras</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.btn_manual_banda.setText(QCoreApplication.translate("MainWindow", u"Conveyor belts", None))
        self.btn_manual_tornillo.setText(QCoreApplication.translate("MainWindow", u"Vibrating screens", None))
        self.creditsLabel.setText(QCoreApplication.translate("MainWindow", u"Modified By: Ronald Borja and Kaleth Padilla", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"v1.0.", None))
    # retranslateUi

