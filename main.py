# ///////////////////////////////////////////////////////////////
#

# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.0.0
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////

# IMPORT / GUI AND MODULES AND WIDGETS
# ///////////////////////////////////////////////////////////////
import sys
import os
import platform
from typing import Optional
import PySide6.QtCore
import PySide6.QtWidgets
import sympy as sp
from sympy import cos
from sympy import exp
from PySide6 import QtCore 
from modules import *
from widgets import *
from resources.usar_creditos_solidos import *
from resources.using_credits import *
from modules.zarandas import Zarandas
from resources.splash_fondo import Ui_SplashScreen
from modules.mandibulas import Mandibula
from modules.rodillos import Rodillo
from modules.bolas import Bolas
from modules.conos import Cono
from modules.elevador import Elevador
from modules.tornillo import Tornillo
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from PySide6.QtCore import QUrl
from PySide6.QtGui import QDesktopServices
import os

os.environ["QT_FONT_DPI"] = "96" # FIX Problem for High DPI and Scale above 100%

# SET AS GLOBAL WIDGETS
# ///////////////////////////////////////////////////////////////
widgets = None
from PySide6 import QtCore as qtc

counter = 0

class CustomLineEdit(qtw.QLineEdit):
    def __init__(self, parent=None, expand=False):
        super().__init__(parent)
        self.original_width = self.width()
        self.clicked_width = self.original_width + 180
        self.expand = expand

    def focusInEvent(self, event):
        if self.expand:
            self.setFixedWidth(self.clicked_width)
        super().focusInEvent(event)

    def focusOutEvent(self, event):
        if self.expand:
            self.setFixedWidth(self.original_width)
        super().focusOutEvent(event)

# Pantalla inicial 
class SplashScreen(QMainWindow):
    def __init__(self): 
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)

        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0,0,0,60))
        self.ui.dropShadowFrame.setGraphicsEffect(self.shadow)

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        self.timer.start(35)

        self.show()

    def progress(self):
        global counter

        self.ui.progressBar.setValue(counter)

        # Cerrar la ventana 
        if counter > 100: 
            self.timer.stop()
            self.main = MainWindow()
            self.main.show()

            self.close()
        counter += 1
    
# MainWindow
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # SET AS GLOBAL WIDGETS
        # ///////////////////////////////////////////////////////////////
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        global widgets
        widgets = self.ui

        # USE CUSTOM TITLE BAR | USE AS "False" FOR MAC OR LINUX
        # ///////////////////////////////////////////////////////////////
        Settings.ENABLE_CUSTOM_TITLE_BAR = True

        # APP NAME
        # ///////////////////////////////////////////////////////////////
        title = "Chem Solid - Modern GUI"
        description = "ChemSolid - Desing your solid handling equipment"
        # APPLY TEXTS
        self.setWindowTitle(title)
        widgets.titleRightInfo.setText(description)

        # TOGGLE MENU
        # ///////////////////////////////////////////////////////////////
        widgets.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))

        # SET UI DEFINITIONS
        # ///////////////////////////////////////////////////////////////
        UIFunctions.uiDefinitions(self)

        # QTableWidget PARAMETERS
        # ///////////////////////////////////////////////////////////////
        #widgets.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # BUTTONS CLICK
        # ///////////////////////////////////////////////////////////////

        # LEFT MENUS
        widgets.btn_home.clicked.connect(self.buttonClick)
        widgets.btn_tornillo.clicked.connect(self.buttonClick)
        widgets.btn_elevadores.clicked.connect(self.buttonClick)
        widgets.btn_molino.clicked.connect(self.buttonClick)
        widgets.btn_bandas.clicked.connect(self.buttonClick)
        widgets.btn_zarandas.clicked.connect(self.buttonClick)
        widgets.pushButton.clicked.connect(self.calculate_tornillo)
        widgets.reset_button_tornillo.clicked.connect(self.reset_tornillo)
        widgets.btn_molinobola.clicked.connect(self.buttonClick)
        widgets.btn_molino_rodillo.clicked.connect(self.buttonClick)
        widgets.pushButton_trituradora_mand.clicked.connect(self.buttonClick)
        widgets.combo_modos_elevador.currentIndexChanged.connect(self.modos_cangilones)
        widgets.modos_tornillo.currentIndexChanged.connect(self.modos_tornillo)
        widgets.btn_manual_zaranda.clicked.connect(self.abrir_pdf)
        widgets.btn_manual_tornillo.clicked.connect(self.abrir_pdf)
        widgets.btn_manual_molino.clicked.connect(self.abrir_pdf)
        widgets.btn_manual_elevador.clicked.connect(self.abrir_pdf)
        widgets.btn_manual_banda.clicked.connect(self.abrir_pdf)
        widgets.pushButton_trituradora_cono.clicked.connect(self.buttonClick)
        widgets.reset_elevador.clicked.connect(self.reset_cangilones)
        widgets.calculate_elevador.clicked.connect(self.calculate_elevador)
        widgets.comboBox_tipo_elevador.currentIndexChanged.connect(self.inhalitar)
        widgets.comboBox_sistema_elevador.currentIndexChanged.connect(self.inhalitar)
        widgets.parte1.clicked.connect(self.buttonClick)
        widgets.parte2.clicked.connect(self.buttonClick)
        widgets.parte3.clicked.connect(self.buttonClick)
        #widgets.parte4.clicked.connect(self.buttonClick)
        #widgets.parte5.clicked.connect(self.buttonClick)
        widgets.searchBar.textChanged.connect(self.onSearchTextChanged)
        widgets.tableWidget.itemSelectionChanged.connect(self.onTableItemSelected)
        widgets.tableWidget.setSelectionBehavior(QTableWidget.SelectRows)  # Seleccionar filas completas
        widgets.tableWidget.setSelectionMode(QTableWidget.SingleSelection)  # Solo permitir selección de una fila a la vez
        widgets.tableWidget.setColumnWidth(0, 250)  # Ajustar el ancho de la segunda columna
        widgets.pushButton_bandas_cal_1.clicked.connect(self.actbandas1)
        widgets.pushButton_bandas_cal_2.clicked.connect(self.actbandas2)
        widgets.pushButton_bandas_cal_3.clicked.connect(self.actbandas3)

        #nuevos botones
        widgets.bton_home_zaranda.clicked.connect(self.buttonClick)
        widgets.bton_home_cangilon.clicked.connect(self.buttonClick)
        widgets.bton_home_tornillo.clicked.connect(self.buttonClick)
        widgets.bton_home_banda.clicked.connect(self.buttonClick)
        widgets.bton_home_molino.clicked.connect(self.buttonClick)

        #botones de molino menu
        widgets.menu_molino_rodillo.clicked.connect(self.buttonClick)
        widgets.menu_molino_cono.clicked.connect(self.buttonClick)
        widgets.menu_molino_bola.clicked.connect(self.buttonClick)
        widgets.menu_molino_mandibula.clicked.connect(self.buttonClick)


        widgets.btn_more.clicked.connect(self.abrir_creditos)

         # Zarandas vibratorias: 
        widgets.boton_calcular6.clicked.connect(self.calcularZarandas)
        widgets.pushButton_3.clicked.connect(self.botonInterpolar)
        widgets.pushButton_3.clicked.connect(self.chequeo)
        widgets.boton_limpiar6.clicked.connect(self.limpiarZarandas)

        self.botonPresionado = False 
        
        # Trituradora de mandibula
        widgets.botonCalcularMandibula.clicked.connect(self.calcularMandibula)
        widgets.botonLimpiarMandibula.clicked.connect(self.limpiarMandibula)
        widgets.comboBox.currentIndexChanged.connect(self.inhabilitar_mandibulas)


        # Triturador de rodillo 
        widgets.botonCalcular_5.clicked.connect(self.calcularRodillos)
        widgets.botonLimpiar_5.clicked.connect(self.limpiarRodillos)
        widgets.opcionesMolinoRodillo.currentIndexChanged.connect(self.inhabilitar_rodillo)


        # Molino de bolas 
        widgets.botonCalcular.clicked.connect(self.calcularBolas)
        widgets.botonLimpiar.clicked.connect(self.limpiarBolas)
        widgets.comboBox_2.currentIndexChanged.connect(self.inhabilitar_bolas)


        # Trituradora de conos 
        widgets.botonCalcular_3.clicked.connect(self.calcularConos)
        widgets.botonLimpiar_3.clicked.connect(self.limpiarConos)
        widgets.comboBox_3.currentIndexChanged.connect(self.inhabilitar_conos)


        # EXTRA LEFT BOX
        def openCloseLeftBox():
            UIFunctions.toggleLeftBox(self, True)
        widgets.toggleLeftBox.clicked.connect(openCloseLeftBox)
        widgets.extraCloseColumnBtn.clicked.connect(openCloseLeftBox)

        # EXTRA RIGHT BOX
        def openCloseRightBox():
            UIFunctions.toggleRightBox(self, True)
        widgets.settingsTopBtn.clicked.connect(openCloseRightBox)

        # SHOW APP
        # ///////////////////////////////////////////////////////////////
        self.show()

        # SET CUSTOM THEME
        # ///////////////////////////////////////////////////////////////
        useCustomTheme =False
        themeFile = "themes\py_dracula_light.qss"

        # SET THEME AND HACKS
        if useCustomTheme:
            # LOAD AND APPLY STYLE
            UIFunctions.theme(self, themeFile, True)

            # SET HACKS
            AppFunctions.setThemeHack(self)

        # SET HOME PAGE AND SELECT MENU
        # ///////////////////////////////////////////////////////////////
        widgets.stackedWidget.setCurrentWidget(widgets.home)
        widgets.btn_home.setStyleSheet(UIFunctions.selectMenu(widgets.btn_home.styleSheet()))
    def onSearchTextChanged(self, text):
        text = text.strip().lower()

        for row in range(widgets.tableWidget.rowCount()):
            item = widgets.tableWidget.item(row, 0)
            if item is not None:
                itemText = item.text().lower()
                if text in itemText:
                    widgets.tableWidget.setRowHidden(row, False)
                else:
                    widgets.tableWidget.setRowHidden(row, True)

    def onTableItemSelected(self):
        selectedRows = widgets.tableWidget.selectionModel().selectedRows()
        if selectedRows:
            row = selectedRows[0].row()
            item1 = widgets.tableWidget.item(row, 1)
            item2 = widgets.tableWidget.item(row, 2)
            item3 = widgets.tableWidget.item(row, 3)
            item4 = widgets.tableWidget.item(row, 0)

            if item1 and item2:
                value1 = item1.text()
                value2 = item2.text()
                value3 = item3.text()
                value4 = item4.text()

                widgets.lineEdit1.setText(value1)
                widgets.lineEdit2.setText(value2)
                widgets.lineEdit3.setText(value3)
                widgets.lineEdit_11.setText(value4)
            else:
                widgets.lineEdit1.setText("")
                widgets.lineEdit2.setText("")
                widgets.lineEdit3.setText("")
                widgets.lineEdit_11.setText("")

    def buttonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        # SHOW HOME PAGE
        if btnName == "btn_home":
            widgets.stackedWidget.setCurrentWidget(widgets.home)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))
    # BUTTONS CLICK
    # Post here your functions for clicked buttons
    # ///////////////////////////////////////////////////////////////


        # SHOW WIDGETS PAGE
        if btnName == "btn_tornillo":
            widgets.stackedWidget.setCurrentWidget(widgets.tornillo)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        if btnName == "bton_home_tornillo":
            widgets.stackedWidget.setCurrentWidget(widgets.tornillo)
            UIFunctions.resetStyle(self, widgets.btn_tornillo)
            self.ui.btn_tornillo.setStyleSheet(UIFunctions.selectMenu(self.ui.btn_tornillo.styleSheet()))

        # SHOW NEW PAGE
        if btnName == "btn_elevadores":
            widgets.stackedWidget.setCurrentWidget(widgets.elevadores) # SET PAGE
            UIFunctions.resetStyle(self, btnName) # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet())) # SELECT MENU

        if btnName == "bton_home_cangilon":
            widgets.stackedWidget.setCurrentWidget(widgets.elevadores) # SET PAGE
            UIFunctions.resetStyle(self, widgets.btn_elevadores) # RESET ANOTHERS BUTTONS SELECTED
            self.ui.btn_elevadores.setStyleSheet(UIFunctions.selectMenu(self.ui.btn_elevadores.styleSheet())) # SELECT MENU

        if btnName == "btn_molino":
            widgets.stackedWidget.setCurrentWidget(widgets.molinos)  # SET PAGE
            UIFunctions.resetStyle(self, btnName)  # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))  # SELECT MENU

            widgets.stackedWidget_3.setCurrentWidget(widgets.molino_bola)
            UIFunctions.resetStyle_3(self, widgets.btn_molinobola)  # RESET ANOTHERS BUTTONS SELECTED
            self.ui.btn_molinobola.setStyleSheet(UIFunctions.selectMenu_3(self.ui.btn_molinobola.styleSheet()))  # SELECT MENU

        if btnName == "bton_home_molino":
            widgets.stackedWidget.setCurrentWidget(widgets.menu_molino)  # SET PAGE
            UIFunctions.resetStyle(self, widgets.btn_molino)  # RESET ANOTHERS BUTTONS SELECTED
            self.ui.btn_molino.setStyleSheet(UIFunctions.selectMenu(self.ui.btn_molino.styleSheet()))  # SELECT MENU  

        if btnName == "btn_bandas":
            widgets.stackedWidget.setCurrentWidget(widgets.bandas)  # SET PAGE
            UIFunctions.resetStyle(self, btnName)  # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))  # SELECT MENU
            
            widgets.stackedWidget_2.setCurrentWidget(widgets.Parte_1)
            UIFunctions.resetStyle_2(self,widgets.parte1)
            self.ui.parte1.setStyleSheet(UIFunctions.selectMenu_2(self.ui.parte1.styleSheet()))

        if btnName == "bton_home_banda":
            widgets.stackedWidget.setCurrentWidget(widgets.bandas)  # SET PAGE
            UIFunctions.resetStyle(self, widgets.btn_bandas)  # RESET ANOTHERS BUTTONS SELECTED
            self.ui.btn_bandas.setStyleSheet(UIFunctions.selectMenu(self.ui.btn_bandas.styleSheet()))  # SELECT MENU

            widgets.stackedWidget_2.setCurrentWidget(widgets.Parte_1)
            UIFunctions.resetStyle_2(self, widgets.parte1)
            self.ui.parte1.setStyleSheet(UIFunctions.selectMenu_2(self.ui.parte1.styleSheet()))

        if btnName == "btn_zarandas":
            widgets.stackedWidget.setCurrentWidget(widgets.zarandas)  # SET PAGE
            UIFunctions.resetStyle(self, btnName)  # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))  # SELECT MENU

        if btnName == "bton_home_zaranda":
            widgets.stackedWidget.setCurrentWidget(widgets.zarandas)  # SET PAGE
            UIFunctions.resetStyle(self, widgets.btn_zarandas)  # RESET ANOTHERS BUTTONS SELECTED
            self.ui.btn_zarandas.setStyleSheet(UIFunctions.selectMenu(self.ui.btn_zarandas.styleSheet()))  # SELECT MENU


        if btnName == "btn_molinobola":
            print(btnName)
            print(btn)
            widgets.stackedWidget_3.setCurrentWidget(widgets.molino_bola)  # SET PAGE

            UIFunctions.resetStyle_3(self, btnName)  # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu_3(btn.styleSheet()))  # SELECT MENU

        if btnName == "menu_molino_bola":
            widgets.stackedWidget.setCurrentWidget(widgets.molinos)
            widgets.stackedWidget_3.setCurrentWidget(widgets.molino_bola)

            UIFunctions.resetStyle_3(self, widgets.btn_molinobola)  # RESET ANOTHERS BUTTONS SELECTED
            self.ui.btn_molinobola.setStyleSheet(UIFunctions.selectMenu_3(self.ui.btn_molinobola.styleSheet()))  # SELECT MENU


        if btnName == "btn_molino_rodillo":
            widgets.stackedWidget_3.setCurrentWidget(widgets.molino_rodillo)  # SET PAGE
            UIFunctions.resetStyle_3(self, btnName)  # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu_3(btn.styleSheet()))
            print(btn.setStyleSheet(UIFunctions.selectMenu_3(btn.styleSheet())))  # SELECT MENU

        if btnName == "menu_molino_rodillo":
            widgets.stackedWidget.setCurrentWidget(widgets.molinos)
            widgets.stackedWidget_3.setCurrentWidget(widgets.molino_rodillo)  # SET PAGE

            UIFunctions.resetStyle_3(self, widgets.btn_molino_rodillo)  # RESET ANOTHERS BUTTONS SELECTED
            widgets.btn_molino_rodillo.setStyleSheet(UIFunctions.selectMenu_3(widgets.btn_molino_rodillo.styleSheet()))


        if btnName == "pushButton_trituradora_mand":
            widgets.stackedWidget_3.setCurrentWidget(widgets.molino_mandibula)  # SET PAGE
            UIFunctions.resetStyle_3(self, btnName)  # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu_3(btn.styleSheet()))  # SELECT MENU

        if btnName == "menu_molino_mandibula":
            widgets.stackedWidget.setCurrentWidget(widgets.molinos)  # SET PAGE
            widgets.stackedWidget_3.setCurrentWidget(widgets.molino_mandibula)

            UIFunctions.resetStyle_3(self, widgets.pushButton_trituradora_mand)  # RESET ANOTHERS BUTTONS SELECTED
            widgets.pushButton_trituradora_mand.setStyleSheet(UIFunctions.selectMenu_3(widgets.pushButton_trituradora_mand.styleSheet()))  # SELECT MENU

        if btnName == "pushButton_trituradora_cono":
            widgets.stackedWidget_3.setCurrentWidget(widgets.molino_cono)  # SET PAGE
            UIFunctions.resetStyle_3(self, btnName)  # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu_3(btn.styleSheet()))  # SELECT MENU

        if btnName == "menu_molino_cono":
            widgets.stackedWidget.setCurrentWidget(widgets.molinos)

            widgets.stackedWidget_3.setCurrentWidget(widgets.molino_cono)  # SET 
            
            UIFunctions.resetStyle_3(self, widgets.pushButton_trituradora_cono)  # RESET ANOTHERS BUTTONS SELECTED
            widgets.pushButton_trituradora_cono.setStyleSheet(UIFunctions.selectMenu_3(widgets.pushButton_trituradora_cono.styleSheet()))  # SELECT MENU


        if btnName == "parte1":
            widgets.stackedWidget_2.setCurrentWidget(widgets.Parte_1)  # SET PAGE
            UIFunctions.resetStyle_2(self, btnName)  # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu_2(btn.styleSheet()))  # SELECT MENU
        if btnName == "parte2":
            widgets.stackedWidget_2.setCurrentWidget(widgets.Parte_2)  # SET PAGE
            UIFunctions.resetStyle_2(self, btnName)  # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu_2(btn.styleSheet()))  # SELECT MENU
        if btnName == "parte3":
            widgets.stackedWidget_2.setCurrentWidget(widgets.Parte_3)  # SET PAGE
            UIFunctions.resetStyle_2(self, btnName)  # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu_2(btn.styleSheet()))  # SELECT MENU
        if btnName == "parte4":
            widgets.stackedWidget_2.setCurrentWidget(widgets.Parte_4)  # SET PAGE
            UIFunctions.resetStyle_2(self, btnName)  # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu_2(btn.styleSheet()))  # SELECT MENU
        if btnName == "parte5":
            widgets.stackedWidget_2.setCurrentWidget(widgets.Parte_5)  # SET PAGE
            UIFunctions.resetStyle_2(self, btnName)  # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu_2(btn.styleSheet()))  # SELECT MENU


        # PRINT BTN NAME
        print(f'Button "{btnName}" pressed!')

    def inhalitar(self, index):
        Elevador.inhabilitar(self)

        #if comboName=='comboBox_tipo_elevador':
    def modos_tornillo(self):
        Tornillo.modos_tornillo(self)

    # RESIZE EVENTS
    # ///////////////////////////////////////////////////////////////
    def resizeEvent(self, event):
        # Update Size Grips
        UIFunctions.resize_grips(self)
    def actbandas1(self):
        calculos_bandas_1.calculate_1(self)
    def actbandas2(self):
        calculos_bandas_1.calculate_2(self)
    def actbandas3(self):
        calculos_bandas_1.calculate_3(self)
    

# Abrir manual de usuario 
    def abrir_creditos(self):
        self.form=creditos_solidos2()
        self.form.exec()          
    def obtener_ruta_actual(self):
        # Obtén el directorio del script en ejecución
        ruta_actual = os.path.dirname(os.path.abspath(__file__))
        return ruta_actual
    def abrir_pdf(self):

        btn = self.sender()
        btnName = btn.objectName()

        # SHOW HOME PAGE

        if btnName == "btn_manual_zaranda":
            numero_pagina = 4

        elif btnName == "btn_manual_molino":

            numero_pagina = 5
        
        elif btnName == "btn_manual_elevador":
            numero_pagina = 12

        elif btnName == "btn_manual_tornillo":
            numero_pagina = 14
        
        elif btnName == "btn_manual_banda":
            numero_pagina = 15

        # Obtiene la ruta del directorio actual
        ruta_directorio_actual = self.obtener_ruta_actual()

        # Construye la ruta completa al archivo PDF
        nombre_pdf = "Manual de usuario ChemSolid.pdf"
        ruta_pdf = os.path.join(ruta_directorio_actual, nombre_pdf)

        # Número de página que deseas abrir
        

        # Construir la URL con el fragmento de la página
        url_pdf = QUrl.fromLocalFile(ruta_pdf)
        url_pdf.setFragment(f"page={numero_pagina}")

        # Abrir el archivo PDF
        QDesktopServices.openUrl(url_pdf)

    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()

        # PRINT MOUSE EVENTS
        if event.buttons() == Qt.LeftButton:
            print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            print('Mouse click: RIGHT CLICK')


    # Tornillos Sin Fin
    @qtc.Slot()
    def calculate_tornillo (self):
        Tornillo.calculate_tornillo(self)
    @qtc.Slot()
    def reset_tornillo (self):
        Tornillo.reset_tornillo(self)

    # Elevadores de cangilones
    @qtc.Slot()
    def calculate_elevador(self):
        Elevador.calculate_elevator(self)
    def modos_cangilones(self):
        Elevador.modos_cangilones(self)
    @qtc.Slot()
    def reset_cangilones(self):
        Elevador.reset_cangilones(self)
    def chequeo(self):
        self.botonPresionado = True

    #  Zarandas --> Interpolación + Calculos + Reset 
    def botonInterpolar(self):
        Zarandas.interpolar_zaranda(self)
    def calcularZarandas(self):
        if (self.botonPresionado):
            Zarandas.calcular_zarandas(self)
        else:
            Zarandas.calcular_zarandas_sin_interpolar(self)
    def limpiarZarandas(self):
        Zarandas.limpiarZarandas(self)

# Molinos --> Calculos 
    def calcularMandibula(self): 
        Mandibula.calcular_mandibula(self)
    def limpiarMandibula(self): 
        Mandibula.limpiar_mandibulas(self)
    def calcularRodillos(self):
        Rodillo.calcular_rodillos(self)       
    def defaul_style(lista): 
        default_style = "QLineEdit { }"
        for i in lista: 
            i.setStyleSheet(default_style)
    def light_gray_style(lista): 
        light_gray_style = "background-color: lightgray;"
        for i in lista: 
            i.i.setStyleSheet(light_gray_style)

# Casos -> Molinos
    def inhabilitar_rodillo(self): 
        Rodillo.inhabilitar_rodillo(self)
    def inhabilitar_bolas(self): 
        Bolas.inhabilitar_bolas(self)
    def inhabilitar_mandibulas(self): 
        Mandibula.inhabilitar_mandibulas(self)
    def inhabilitar_conos(self): 
        Cono.innhabilitar_conos(self)
        
# Funcionalidad reset -> Molinos
    def limpiarRodillos(self): 
        Rodillo.limpiar_rodillos(self)
    def calcularBolas(self):
        Bolas.calcular_bolas(self)    
    def limpiarBolas(self): 
        Bolas.limpiar_bolas(self)
    def calcularConos(self): 
        Cono.calcular_cono(self)
    def limpiarConos(self): 
        Cono.limpiar_conos(self)
        
# Ejecutar la app
if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = SplashScreen()
    sys.exit(app.exec())