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

# IMPORT / GUI AND MODULES AND WIDGETS
# ///////////////////////////////////////////////////////////////
from modules import *
from widgets import *
from resources.usar_creditos_solidos import *
from resources.using_credits import *
from modules.zarandas import Zarandas
from resources.splash_fondo import Ui_SplashScreen

## NUEVO ---------------------------- RONALD
from modules.mandibulas import Mandibula
from modules.rodillos import Rodillo
from modules.bolas import Bolas
from modules.conos import Cono

os.environ["QT_FONT_DPI"] = "96" # FIX Problem for High DPI and Scale above 100%

# SET AS GLOBAL WIDGETS
# ///////////////////////////////////////////////////////////////
widgets = None
from PySide6 import QtCore as qtc

counter = 0

#pdf

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from PySide6.QtCore import QUrl
from PySide6.QtGui import QDesktopServices
import os

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

        # Molinos -------------------- RONALD (Agregado) ------------------------------------------------------ 
        
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
        combox = self.sender()
        comboName = combox.objectName()
        if comboName=='comboBox_tipo_elevador':
            if widgets.comboBox_tipo_elevador.currentText() == "Normal bucket":
                widgets.lineEdit_pp_elevador.setEnabled(True)
                widgets.lineEdit_pp_elevador.setStyleSheet("background-color: transparent;")
                widgets.lineEdit_h_elevador.setEnabled(True)
                widgets.lineEdit_h_elevador.setStyleSheet("background-color: transparent;")

                widgets.lineEdit_h_elevador.setPlaceholderText('Enter the height')
                widgets.lineEdit_pp_elevador.setPlaceholderText('Enter the proportion constant')
                
                widgets.lineEdit_cte_elevador.setEnabled(False)
                widgets.lineEdit_tc_elevador.setEnabled(False)
            else:
                widgets.lineEdit_h_elevador.setText('')
                widgets.lineEdit_pp_elevador.setText('')
                widgets.lineEdit_h_elevador.setPlaceholderText('')
                widgets.lineEdit_pp_elevador.setPlaceholderText('')

                widgets.lineEdit_pp_elevador.setStyleSheet("background-color: lightgray;")
                widgets.lineEdit_h_elevador.setStyleSheet("background-color: lightgray;")


            if widgets.comboBox_tipo_elevador.currentText() == "Chain bucket":
                widgets.lineEdit_cte_elevador.setEnabled(True)
                widgets.lineEdit_tc_elevador.setEnabled(True)
                widgets.lineEdit_cte_elevador.setStyleSheet("background-color: transparent;")
                widgets.lineEdit_tc_elevador.setStyleSheet("background-color: transparent;")

                widgets.lineEdit_cte_elevador.setPlaceholderText('Enter the proportion constant')
                widgets.lineEdit_tc_elevador.setPlaceholderText('Enter the chain pitch')

                widgets.lineEdit_pp_elevador.setEnabled(False)
                widgets.lineEdit_h_elevador.setEnabled(False)
               

            else:
                widgets.lineEdit_cte_elevador.setText('')
                widgets.lineEdit_tc_elevador.setText('')
                widgets.lineEdit_cte_elevador.setPlaceholderText('')
                widgets.lineEdit_tc_elevador.setPlaceholderText(' ')
                widgets.lineEdit_cte_elevador.setStyleSheet("background-color: lightgray;")
                widgets.lineEdit_tc_elevador.setStyleSheet("background-color: lightgray;")

            if widgets.comboBox_tipo_elevador.currentText() == "Scoop bucket":


                widgets.lineEdit_h_elevador.setEnabled(True)
                widgets.lineEdit_h_elevador.setPlaceholderText('Enter the height')
                widgets.lineEdit_h_elevador.setStyleSheet("background-color: transparent;")

                widgets.lineEdit_pp_elevador.setEnabled(False)
                widgets.lineEdit_cte_elevador.setEnabled(False)
                widgets.lineEdit_tc_elevador.setEnabled(False)
            elif widgets.comboBox_tipo_elevador.currentText() == "Normal bucket":

                widgets.lineEdit_h_elevador.setText('')
                widgets.lineEdit_h_elevador.setPlaceholderText('Enter the height')
                widgets.lineEdit_tc_elevador.setStyleSheet("background-color: lightgray;")
                widgets.lineEdit_cte_elevador.setStyleSheet("background-color: lightgray;")

                

                

            if widgets.comboBox_tipo_elevador.currentText() == "Unspecified":
                widgets.lineEdit_pp_elevador.setEnabled(False)
                widgets.lineEdit_h_elevador.setEnabled(False)
                widgets.lineEdit_cte_elevador.setEnabled(False)
                widgets.lineEdit_tc_elevador.setEnabled(False)
                widgets.lineEdit_t_elevador.setText('')
                widgets.lineEdit_pp_elevador.setStyleSheet("background-color: lightgray;")
                widgets.lineEdit_h_elevador.setStyleSheet("background-color: lightgray;")
                widgets.lineEdit_cte_elevador.setStyleSheet("background-color: lightgray;")
                widgets.lineEdit_tc_elevador.setStyleSheet("background-color: lightgray;")


            

        if comboName=='comboBox_sistema_elevador':
            if  widgets.comboBox_sistema_elevador.currentText() == "From hopper":


                widgets.comboBox_Tparticula_elevador.setEnabled(False)
                widgets.comboBox_Tparticula_elevador.setCurrentIndex(0)
                widgets.comboBox_Tparticula_elevador.setStyleSheet("background-color: lightgray;")

            elif widgets.comboBox_sistema_elevador.currentText() == "By dredging":

                widgets.comboBox_Tparticula_elevador.setEnabled(True)
                widgets.comboBox_Tparticula_elevador.setStyleSheet("background-color: transparent;")


            else:
                widgets.comboBox_Tparticula_elevador.setEnabled(False)
                widgets.comboBox_Tparticula_elevador.setCurrentIndex(0)
                widgets.comboBox_Tparticula_elevador.setStyleSheet("background-color: lightgray;")




        #if comboName=='comboBox_tipo_elevador':
    def modos_tornillo(self):

        widgets = self.ui 
        combox = self.sender()
        comboName = combox.objectName()
        e=widgets
        all_lines=[
        e.lineEdit_s_tornillo, e.lineEdit_D_tornillo, e.lineEdit_t_tornillo, e.lineEdit_n_tornillo,
        e.lineEdit_v_tornillo,e.lineEdit_Q_tornillo,e.lineEdit_y_tornillo,e.lineEdit_pst_tornillo,
        e.lineEdit_PN_tornillo,e.lineEdit_PH_tornillo,e.lineEdit_L_tornillo,e.lineEdit_P_tornillo,
        e.comboBox_k_tornillo,e.comboBox_lambda_tornillo,
        e.comboBox_Co_tornillo,e.lineEdit_H_tornillo]


        area=[e.lineEdit_s_tornillo, e.lineEdit_D_tornillo,e.comboBox_lambda_tornillo]
        area_sin = [elemento for elemento in all_lines if elemento not in area]

        velocidad=[e.lineEdit_t_tornillo, e.lineEdit_n_tornillo,e.lineEdit_v_tornillo]
        velocidad_sin=[elemento for elemento in all_lines if elemento not in velocidad]

        flujo=[e.lineEdit_t_tornillo, e.lineEdit_n_tornillo,e.comboBox_k_tornillo,e.lineEdit_y_tornillo,e.lineEdit_D_tornillo,e.comboBox_lambda_tornillo,e.lineEdit_Q_tornillo]
        flujo_sin=[elemento for elemento in all_lines if elemento not in flujo]

        desplazamiento=[e.comboBox_Co_tornillo,e.lineEdit_L_tornillo,e.lineEdit_Q_tornillo,e.lineEdit_PH_tornillo]
        desplazamiento_sin=[elemento for elemento in all_lines if elemento not in desplazamiento]

        accionamiento_vacio=[e.lineEdit_D_tornillo,e.lineEdit_L_tornillo,e.lineEdit_PN_tornillo]
        accionamiento_vacio_sin=[elemento for elemento in all_lines if elemento not in accionamiento_vacio]

        inclinado=[e.lineEdit_H_tornillo,e.lineEdit_Q_tornillo,e.lineEdit_pst_tornillo]
        inclinado_sin=[elemento for elemento in all_lines if elemento not in inclinado]


        potencia=[e.lineEdit_Q_tornillo,e.comboBox_Co_tornillo,e.lineEdit_L_tornillo,e.lineEdit_H_tornillo,e.lineEdit_D_tornillo]
        potencia_sin=[elemento for elemento in all_lines if elemento not in potencia]


        widgets.widget_6.setStyleSheet('''
            QComboBox QAbstractItemView {
    background: #FFFFFF;
    background-color: #FFFFFF; /* Cambia el color de fondo de las opciones
     desplegadas a blanco */
    color: #000000; /* Cambia el color del texto a negro */
}

           ''')

        
        if comboName=='modos_tornillo':

            if widgets.modos_tornillo.currentText() == 'General':

                for i in all_lines:

                    i.setEnabled(True)
                    i.setStyleSheet('''background-color: #FFFFFF;
                                        background: #FFFFFF; ''')

                    self.reset_tornillo()

            elif widgets.modos_tornillo.currentText() == 'S: Gutter Filling Area (m²): ':
                self.reset_tornillo()
                for i in area:
                    i.setEnabled(True)
                    i.setStyleSheet('''background-color: #FFFFFF;
                                        background: #FFFFFF; ''')
                for i in area_sin:

                    i.setEnabled(False)
                    i.setStyleSheet("background-color: lightgray;")


            elif widgets.modos_tornillo.currentText() == 'Screw Rotation Speed (rpm): ':
                self.reset_tornillo()

                for i in velocidad:
                    i.setEnabled(True)
                    i.setStyleSheet('''background-color: #FFFFFF;
                                        background: #FFFFFF; ''')
                for i in velocidad_sin:

                    i.setEnabled(False)
                    i.setStyleSheet("background-color: lightgray;")


            elif widgets.modos_tornillo.currentText() == 'Q: Material Flow (t/h)':
                self.reset_tornillo()

                for i in flujo:
                    i.setEnabled(True)
                    i.setStyleSheet('''background-color: #FFFFFF;
                                                            background: #FFFFFF; ''')
                for i in flujo_sin:

                    i.setEnabled(False)
                    i.setStyleSheet("background-color: lightgray;")



            elif widgets.modos_tornillo.currentText() == 'Pst: Power of inclined screw conveyor (kW)':

                self.reset_tornillo()

                for i in inclinado:
                    i.setEnabled(True)
                    i.setStyleSheet('''background-color: #FFFFFF;
                                                            background: #FFFFFF; ''')
                for i in inclinado_sin:

                    i.setEnabled(False)
                    i.setStyleSheet("background-color: lightgray;")
            
            elif widgets.modos_tornillo.currentText() == 'PN: Vacuum Screw Drive (kW): ':
                self.reset_tornillo()

                for i in accionamiento_vacio:
                    i.setEnabled(True)
                    i.setStyleSheet('''background-color: #FFFFFF;
                                                            background: #FFFFFF; ''')

                for i in accionamiento_vacio_sin:

                    i.setEnabled(False)
                    i.setStyleSheet("background-color: lightgray;")

            elif widgets.modos_tornillo.currentText() == 'PH: Material Transport Power (kW):':
                self.reset_tornillo()

                for i in desplazamiento:
                    i.setEnabled(True)
                    i.setStyleSheet('''background-color: #FFFFFF;
                                                            background: #FFFFFF; ''')
                for i in desplazamiento_sin:

                    i.setEnabled(False)
                    i.setStyleSheet("background-color: lightgray;")
            
            elif widgets.modos_tornillo.currentText() == 'P: Net Power Required (kW): ':
                self.reset_tornillo()

                for i in potencia:
                    i.setEnabled(True)
                    i.setStyleSheet('''background-color: #FFFFFF;
                                                            background: #FFFFFF; ''')
                for i in potencia_sin:

                    i.setEnabled(False)
                    i.setStyleSheet("background-color: lightgray;")

            combo=[e.comboBox_k_tornillo,e.comboBox_lambda_tornillo,e.comboBox_Co_tornillo]

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


# Tornillos + Elevadores de Cangilones
    @qtc.Slot()
    def calculate_tornillo (self):
        if  widgets.lineEdit_s_tornillo.text()=='':
            s=widgets.lineEdit_s_tornillo.text()
        else:
            s=float(str(widgets.lineEdit_s_tornillo.text()))

    
        D=widgets.lineEdit_D_tornillo.text()
    
        t=widgets.lineEdit_t_tornillo.text()
        n=widgets.lineEdit_n_tornillo.text()
        v=widgets.lineEdit_v_tornillo.text()
        q=widgets.lineEdit_Q_tornillo.text()
        y=widgets.lineEdit_y_tornillo.text()
        #k=widgets.lineEdit_k_tornillo.text()
        pst=widgets.lineEdit_pst_tornillo.text()
        PN=widgets.lineEdit_PN_tornillo.text()
        PH=widgets.lineEdit_PH_tornillo.text()
        L=widgets.lineEdit_L_tornillo.text()
        P=widgets.lineEdit_P_tornillo.text()
        H=widgets.lineEdit_H_tornillo.text()

        if widgets.comboBox_lambda_tornillo.currentText() == "Heavy and abrasive ( λ=0.125)":
            lamda = 0.125
        elif widgets.comboBox_lambda_tornillo.currentText() == "Heavy and not very abrasive  (λ=0.25)":
            lamda = 0.25
        elif widgets.comboBox_lambda_tornillo.currentText() == "Not very abrasive (λ=0.32)":
            lamda = 0.32
        elif widgets.comboBox_lambda_tornillo.currentText() == "Light, non-abrasive (λ=0.4)":
            lamda = 0.4
        elif widgets.comboBox_lambda_tornillo.currentText() == "Unspecified":
            lamda = sp.symbols('lamda')


        if widgets.comboBox_k_tornillo.currentText() == "Unspecified":
            k = sp.symbols('k')
        elif widgets.comboBox_k_tornillo.currentText() == "Gutter inclination of 0°":
            k = 1
        elif widgets.comboBox_k_tornillo.currentText() == "Gutter inclination of 5°":
            k = 0.9
        elif widgets.comboBox_k_tornillo.currentText() == "Gutter inclination of 10°":
            k = 0.8
        elif widgets.comboBox_k_tornillo.currentText() == "Gutter inclination of 15°":
            k = 0.7
        elif widgets.comboBox_k_tornillo.currentText() == "Gutter inclination of 20°":
            k = 0.6


        if widgets.comboBox_Co_tornillo.currentText() == "flours, sawdust, granular products":
            Co = 1.2
            print('valor de Co: ', Co)
        elif widgets.comboBox_Co_tornillo.currentText() == "Peat, soda ash, coal dust":
            Co = 1.6
            print('valor de Co: ', Co)
        elif widgets.comboBox_Co_tornillo.currentText() == "Anthracite, coal, rock salt":
            Co = 2.5
            print('valor de Co: ', Co)
        elif widgets.comboBox_Co_tornillo.currentText() == "Gypsum, dry clay, fine soil, cement, lime, sand":
            Co = 4
            print('valor de Co: ', Co)
        elif widgets.comboBox_Co_tornillo.currentText() == "Unspecified":
        
            Co = sp.Symbol('Co')
            print('valor de Co: ', Co)

        if s=='':
            s=sp.symbols('s')
        else:
            s=float(widgets.lineEdit_s_tornillo.text())
        
        if D=='':
            D = sp.symbols('D')
        else:
            D=float(widgets.lineEdit_D_tornillo.text())

        if t=='':
            t = sp.symbols('s')
        else:
            t=float(widgets.lineEdit_t_tornillo.text())
        if n=='':
            n = sp.symbols('n')
        else:
            n=float(widgets.lineEdit_n_tornillo.text())

        if v=='':
            v = sp.symbols('v')

        else:
            v=float(widgets.lineEdit_v_tornillo.text())

        if q=='':
            q = sp.Symbol('q')

        else:
            q=float( widgets.lineEdit_Q_tornillo.text())

        if y=='':
            y = sp.symbols('y')

        else:
            y=float(widgets.lineEdit_y_tornillo.text())

        #if k=='':
            #k = sp.symbols('k')
        #else:
            #k=int(widgets.lineEdit_k_tornillo.text())
        if pst=='':
            pst = sp.symbols('pst')
        else:
            pst=float(widgets.lineEdit_pst_tornillo.text())

        if PN=='':
            PN = sp.symbols('PN')
        else:
            PN=float(widgets.lineEdit_PN_tornillo.text())

        if PH=='':

            PH = sp.symbols('PH')
        else:
            PH=float(widgets.lineEdit_PH_tornillo.text())

        if L=='':
            L = sp.symbols('L')
        else:
            L=float(widgets.lineEdit_L_tornillo.text())

        if H=='':
            H = sp.symbols('H')
        else:
            H=float(widgets.lineEdit_H_tornillo.text())
        
        
        if P=='':
            P = sp.symbols('P')
        else:
            P=float(widgets.lineEdit_P_tornillo.text())


    
        #widgets.label_25.setText(widgets.lineEdit_s_tornillo.text())

        primera_ecua=[s,D,lamda]
        segunda_ecua=[v,t ,n]
        tercera_ecua=[]
        c_p=0
        inc_p=0

        variables_primera=[]
        var_des_pe=[]

        for i in primera_ecua:
            
            if isinstance(i, sp.core.symbol.Symbol):
                inc_p+=1
              
                var_des_pe.append(i)
            else:
                c_p+=1
            
            dif=c_p-inc_p
        print('valor de dif')


        if i==primera_ecua[len(primera_ecua)-1]:
            print('ultima ronda')
            print('numero de variables: ', inc_p)
            print('numero de constantes: ', c_p)
        ec=str(((lamda*3.1416*D**2)/4)-s)
        expr1 = sp.parse_expr(ec)

        if  dif==1 :
            print('se puede resolver')
            

            var1=var_des_pe[0]
            print(var1)

            print('variables desconocidas: ',var1)

            
            # Resolver el sistema de ecuaciones
            sol = sp.solve((expr1), (var1))

            if var1 == D:
                widgets.lineEdit_D_tornillo.setText(str(sol[1]))
                D = float((sol[1]))

            if var1 == s:
                widgets.lineEdit_s_tornillo.setText(str(sol[0]))
                s = float(sol[0])

            # Imprimir la solución

            print(sol)


            
        else:
            print('no se puede resolver')


        c_s=0
        inc_s=0

        variables_seginda=[]
        var_des_se=[]

        for i in segunda_ecua:
            
            if isinstance(i, sp.core.symbol.Symbol):
                inc_s+=1
              
                var_des_se.append(i)
            else:
                c_s+=1
            
            dif2=c_s-inc_s
        ec2=str(((t*n)/60)-v)
        expr2 = sp.parse_expr(ec2)

        if  dif2==1 :
            print('se puede resolver')
            

            var2=var_des_se[0]
            print(var2)

            print('variables desconocidas: ',var2)

            
            # Resolver el sistema de ecuaciones
            sol = sp.solve((expr2), (var2))

            if var2 == t:
                widgets.lineEdit_t_tornillo.setText(str(sol[0]))
                t = float(sol[0])

            elif var2 == n:
                widgets.lineEdit_n_tornillo.setText(str(sol[0]))
                n = float(sol[0])
            elif var2 == v:

                widgets.lineEdit_v_tornillo.setText(str(sol[0]))
                v= float(sol[0])

            # Imprimir la solución

            print(sol)
            
        else:
            print('no se puede resolver')
        
        if widgets.lineEdit_s_tornillo.text()!='' and widgets.lineEdit_v_tornillo.text()!='' and isinstance(y, sp.core.symbol.Symbol)==False and isinstance(k, sp.core.symbol.Symbol)==False:
            q=(3600*((float(lamda)*3.1416*float(D)**2)/4)*((float(t)*float(n))/60)*float(y)*float(k))
            widgets.lineEdit_Q_tornillo.setText(str(q))


        print('numero de variables desconocida de la ec1 ( dif)',inc_p)
        print('numero de variables desconocida de la ec(dif 2)', inc_s)






        all_var=[s,D,lamda,n,t,v,q,y,k]
        print('es Q variable ? ', isinstance(q, sp.core.symbol.Symbol))
        print('el estado de las variables :', all_var)
        var_des_all=[]
        ec3=(3600*lamda*((3.1416*D**2)/4)*((t*n)/60)*y*k-q)
        print(q)
        print(ec3)
        expr3=sp.parse_expr(str(ec3))
        
        print('variables totales desconocidas: ', )

        for i in all_var:
            if isinstance(i, sp.core.symbol.Symbol):
                var_des_all.append(i)
        print('variables totales desconocidas: ',var_des_all )

        if inc_s==2 and len(var_des_all)==2:
            sol3 = sp.solve((expr2,expr3), (var_des_all[0],var_des_all[1]))
            print("ecuacion" , sol3)
            
            sol4=list(sol3.values())
            print('valores de los resultados:', sol4)

            if var_des_all[0]==n:
                widgets.lineEdit_n_tornillo.setText(str(sol4[0]))
            elif var_des_all[0]==t:
                widgets.lineEdit_t_tornillo.setText(str(sol4[0]))
            elif var_des_all[0]==v:
                widgets.lineEdit_v_tornillo.setText(str(sol4[0]))


            if var_des_all[1]==n:
                widgets.lineEdit_n_tornillo.setText(str(sol4[1]))
            elif var_des_all[1]==t:
                widgets.lineEdit_t_tornillo.setText(str(sol4[1]))
            elif var_des_all[1]==v:
                widgets.lineEdit_v_tornillo.setText(str(sol4[1]))


           

        elif inc_p==2 and len(var_des_all)==2:
            sol3 = sp.solve((expr1,expr3), (var_des_all[0],var_des_all[1]))
            print("ecuacion" , sol3)
            sol4=sol3[1]
            print('valores de los resultados:', sol4)
            if var_des_all[0]==s:
                widgets.lineEdit_s_tornillo.setText(str(sol4[0]))
            elif var_des_all[0]==D:
                widgets.lineEdit_D_tornillo.setText(str(sol4[0]))

            if var_des_all[1]==s:
                widgets.lineEdit_s_tornillo.setText(str(sol4[1]))
            elif var_des_all[1]==D:
                widgets.lineEdit_D_tornillo.setText(str(sol4[1]))
                

        ec4=str((Co*q*L/367)-PH)
        print("ecuacion4" , ec4) 
        expr4=sp.parse_expr(ec4)
        variables_cuarta=[Co,q,L,PH]
        print(variables_cuarta)
        var_des_ce=[]
        print("" , var_des_ce)  
        for i in variables_cuarta:
            if isinstance(i, sp.core.symbol.Symbol):
                var_des_ce.append(i)
        if len(var_des_ce)==1:
            sol5=sp.solve((expr4), (var_des_ce[0]))
            print('sol5', sol5)

            if var_des_ce[0]==Co:
                widgets.lineEdit_Co_tornillo.setText(str(sol5[0]))
            elif var_des_ce[0]==q:
                widgets.lineEdit_Q_tornillo.setText(str(sol5[0]))
            elif var_des_ce[0]==L:
                widgets.lineEdit_L_tornillo.setText(str(sol5[0]))
            elif var_des_ce[0]==PH:
                widgets.lineEdit_PH_tornillo.setText(str(sol5[0]))
            
        ec5=str((D*L/20)-PN)
        print("ecuacion5" , ec5) 
        expr5=sp.parse_expr(ec5)
        variables_quinta=[D,L,PN]
        print(variables_quinta)
        var_des_qe=[]
        print("" , var_des_qe)  
        for i in variables_quinta:
            if isinstance(i, sp.core.symbol.Symbol):
                var_des_qe.append(i)
        if len(var_des_qe)==1:
            sol6=sp.solve((expr5), (var_des_qe[0]))
            print('sol6', sol6)

            if var_des_qe[0]==D:
                widgets.lineEdit_D_tornillo.setText(str(sol6[0]))
            elif var_des_qe[0]==L:
                widgets.lineEdit_Q_tornillo.setText(str(sol6[0]))
            elif var_des_qe[0]==PN:
                widgets.lineEdit_PN_tornillo.setText(str(sol6[0]))
            
        ec6=str((q*H/367)-pst)
        print("ecuacion6" , ec6) 
        expr6=sp.parse_expr(ec6)
        variables_sexta=[q,H,pst]
        print(variables_sexta)
        var_des_sxe=[]
        print("" , var_des_sxe)  
        for i in variables_sexta:
            if isinstance(i, sp.core.symbol.Symbol):
                var_des_sxe.append(i)
        if len(var_des_sxe)==1:
            sol7=sp.solve((expr6), (var_des_sxe[0]))
            print('sol7', sol7)

            if var_des_sxe[0]==q:
                widgets.lineEdit_Q_tornillo.setText(str(sol7[0]))
            elif var_des_sxe[0]==H:
                widgets.lineEdit_H_tornillo.setText(str(sol7[0]))
            elif var_des_sxe[0]==pst:
                widgets.lineEdit_pst_tornillo.setText(str(sol7[0]))
            

        

        #for i in segunda_ecua:

        #for i in tercera_ecua   

       

        #print('el valor de l es : ', l)

        if isinstance(pst, sp.core.symbol.Symbol)==False and isinstance(PN, sp.core.symbol.Symbol)==False and  isinstance(PH, sp.core.symbol.Symbol)==False:
            P=float(pst)+float(PH)+float(PN)
            widgets.lineEdit_P_tornillo.setText(str(P))
    @qtc.Slot()
    def calculate_elevador(self):

        Pc=widgets.lineEdit_Pc_elevador.text()
        e=widgets.lineEdit_i_elevador.text()
        p=widgets.lineEdit_p_elevador.text()
        j=widgets.lineEdit_j_elevador.text()
        q=widgets.lineEdit_q_elevador.text()
        v=widgets.lineEdit_v_elevador.text()
        t=widgets.lineEdit_t_elevador.text()
        Fa=widgets.lineEdit_Fa_elevador.text()
        H=widgets.lineEdit_H_elevador.text()
        Na=widgets.lineEdit_Na_elevador.text()
        n=widgets.lineEdit_n_elevador.text()
        Ta=widgets.lineEdit_Ta_elevador.text()
        FR=widgets.lineEdit_FR_elevador.text()
        m=widgets.lineEdit_m_elevador.text()
        R=widgets.lineEdit_R_elevador.text()
        alfa=widgets.lineEdit_alfa_elevador.text()
        sh=widgets.lineEdit_sh_elevador.text()
        sv=widgets.lineEdit_sv_elevador.text()
        a=widgets.lineEdit_a_elevador.text()
        h=widgets.lineEdit_h_elevador.text()
        s=widgets.lineEdit_s_elevador.text()
        pp=widgets.lineEdit_pp_elevador.text()
        Nc=widgets.lineEdit_Nc_elevador.text()


        if pp=='':
            pp=sp.Symbol('pp')
        else:
            pp=float(widgets.lineEdit_pp_elevador.text())

        if Nc=='':
            Nc=sp.Symbol('Nc')
        else:
            Nc=float(widgets.lineEdit_Nc_elevador.text())

        if Pc=='':
            Pc=sp.Symbol('Pc')
        else:
            Pc=float(widgets.lineEdit_Pc_elevador.text())

        if e=='':
            e=sp.Symbol('e')
        else:
            e=float(widgets.lineEdit_i_elevador.text())
        
        if p=='':
            p=sp.Symbol('p')
        else:
            p=float(widgets.lineEdit_p_elevador.text())

        if j=='':
            j=sp.Symbol('j')
        else:
            j=float(widgets.lineEdit_j_elevador.text())

        if q=='':
            q=sp.Symbol('q')
        else:
            q=float(widgets.lineEdit_q_elevador.text())

        if v=='':
            v=sp.Symbol('v')
        else:
            v=float(widgets.lineEdit_v_elevador.text())

        if t=='':
            t=sp.Symbol('t')
        else:
            t=float(widgets.lineEdit_t_elevador.text())
        if Fa=='':
            Fa=sp.Symbol('Fa')
        else:
            Fa=float(widgets.lineEdit_Fa_elevador.text())
        if H=='':
            H=sp.Symbol('H')
        else:
            H=float(widgets.lineEdit_H_elevador.text())
        if Na=='':
            Na=sp.Symbol('Na')
        else:
            Na=float(widgets.lineEdit_Na_elevador.text())
        if n=='':
            n=sp.Symbol('n')
        else:
            n=float(widgets.lineEdit_n_elevador.text())
        if Ta=='':
            Ta=sp.Symbol('Ta')
        else:
            Ta=float(widgets.lineEdit_Ta_elevador.text())
        if FR=='':
            FR=sp.Symbol('FR')
        else:
            FR=float(widgets.lineEdit_FR_elevador.text())
        if m=='':
            m=sp.Symbol('m')
        else:
            m=float(widgets.lineEdit_m_elevador.text())
        if R=='':
            R=sp.Symbol('R')
        else:
            R=float(widgets.lineEdit_R_elevador.text())

        if  alfa=='':

            alfa=sp.Symbol('alfa')
        else:
            alfa=float(widgets.lineEdit_alfa_elevador.text())
        if sh=='':
            sh=sp.Symbol('sh')
        else:
            sh=float(widgets.lineEdit_sh_elevador.text())
        if sv=='':
            sv=sp.Symbol('sv')
        else:
            sv=float(widgets.lineEdit_sv_elevador.text())

        if a=='':
            a=sp.Symbol('a')
        else:
            a=float(widgets.lineEdit_a_elevador.text())
        
        if h=='':
            h=sp.Symbol('h')
        else:
            h=float(widgets.lineEdit_h_elevador.text())
        if s=='':
            s=sp.Symbol('s')
        else:
            s=float(widgets.lineEdit_s_elevador.text())

        
        if widgets.lineEdit_tc_elevador.text()=='':
            tc=sp.Symbol('tc')
        else:
            tc=float(widgets.lineEdit_tc_elevador.text())
        

        if widgets.lineEdit_cte_elevador.text()=='':
            cte=sp.Symbol('cte')
        else:
            cte=float(widgets.lineEdit_cte_elevador.text())
        



        if widgets.comboBox_sistema_elevador.currentText()=='From hopper':

            Ho=3.8
            print('valor de Ho: ', Ho)
        elif widgets.comboBox_sistema_elevador.currentText()=='By dredging':

            #widgets.comboBox_Tparticula_elevador.setEnabled(True)

            if widgets.comboBox_Tparticula_elevador.currentText()=='Small':
                Ho=7.6
                print('valor de Ho: ', Ho)
            elif widgets.comboBox_Tparticula_elevador.currentText()=='Medium':
                Ho=11.4
                print('valor de Ho: ', Ho)
            elif widgets.comboBox_Tparticula_elevador.currentText()=='Big':
                Ho=15.3
                print('valor de Ho: ', Ho)
            elif widgets.comboBox_Tparticula_elevador.currentText()=='Unspecified':
                Ho=sp.Symbol('Ho')
                print('valor de Ho: ', Ho)
        elif widgets.comboBox_sistema_elevador.currentText()=='Unspecified':
            Ho=sp.Symbol('Ho')
            print('valor de Ho: ', Ho)

        if widgets.comboBox_k_elevador.currentText()=='Unspecified':
            k=sp.Symbol("k")
        elif widgets.comboBox_k_elevador.currentText()=='Drum Condition: Smooth Wet':
            k=3.2
        elif widgets.comboBox_k_elevador.currentText()=='Drum Condition: Smooth Dry':
            k=1.64
        elif widgets.comboBox_k_elevador.currentText()=='Drum Condition: Wet coating':
            k=1.73
        elif widgets.comboBox_k_elevador.currentText()=='Drum Condition: Dry coating':
            k=1.49
        

        
        

        #if widgets.comboBox_tipo_elevador.currentText()=='cangilon normal':
            #t=pp*h
        #elif widgets.comboBox_tipo_elevador.currentText()=='cangilon de escamas':
            #t=h
        #elif widgets.comboBox_tipo_elevador.currentText()=='cangilon de escamas':
            #t=cte*tc


        var_primera=[e,p,j,Pc]
        print('variables', var_primera)

        var_des_pe=[]
        for i in var_primera:
            if isinstance(i, sp.core.symbol.Symbol):
                var_des_pe.append(i)
        
        print(e,p,j)
        print(e*p*j)
        eccc1=str((j*p*e)-Pc)
        print('la ecuacion 1:', eccc1)
        print('variable desconocida: ', var_des_pe)

        expr1=sp.parse_expr(eccc1)
        if len(var_des_pe)==1:
            sol=sp.solve((expr1),(var_des_pe[0]))
            print('valor de la incognita: ', sol)
            
            if var_des_pe[0]==e:
                widgets.lineEdit_i_elevador.setText(str(sol[0]))
            elif var_des_pe[0]==p:
                widgets.lineEdit_p_elevador.setText(str(sol[0]))
            elif var_des_pe[0]==j:
                widgets.lineEdit_j_elevador.setText(str(sol[0]))
            elif var_des_pe[0]==Pc:
                widgets.lineEdit_Pc_elevador.setText(str(sol[0]))
        
        #extructura
        #variables
        #vector vacio de incognitas
        #llenado de incognitas
        #ecuacion
        if  widgets.comboBox_tipo_elevador.currentText() == "Normal bucket":

            var_antesegunda=[t,pp,h]
            var_des_ase=[]
            for i in var_antesegunda:
                if isinstance(i, sp.core.symbol.Symbol):
                    var_des_ase.append(i)
            ec_1_5=str(pp*h-t)
            expr_1_5=sp.parse_expr(ec_1_5)

            if len(var_des_ase)==1:
                sol_1_5=sp.solve((expr_1_5),(var_des_ase[0]))
                if var_des_ase[0]==pp:
                    widgets.lineEdit_pp_elevador.setText(str(sol_1_5[0]))
                elif var_des_ase[0]==h:
                    widgets.lineEdit_h_elevador.setText(str(sol_1_5[0]))
                elif var_des_ase[0]==t:
                    widgets.lineEdit_t_elevador.setText(str(sol_1_5[0]))

        elif   widgets.comboBox_tipo_elevador.currentText() == "Scoop bucket":

            var_antesegunda=[t,h]
            var_des_ase=[]
            for i in var_antesegunda:
                if isinstance(i, sp.core.symbol.Symbol):
                    var_des_ase.append(i)
            ec_1_5=str(h-t)
            expr_1_5=sp.parse_expr(ec_1_5)

            if len(var_des_ase)==1:
                sol_1_5=sp.solve((expr_1_5),(var_des_ase[0]))
                if var_des_ase[0]==pp:
                    widgets.lineEdit_pp_elevador.setText(str(sol_1_5[0]))
                elif var_des_ase[0]==h:
                    widgets.lineEdit_h_elevador.setText(str(sol_1_5[0]))
                elif var_des_ase[0]==t:
                    widgets.lineEdit_t_elevador.setText(str(sol_1_5[0]))
            
        elif   widgets.comboBox_tipo_elevador.currentText() == "Chain bucket":

            var_antesegunda=[t,tc,cte]
            var_des_ase=[]
            for i in var_antesegunda:
                if isinstance(i, sp.core.symbol.Symbol):
                    var_des_ase.append(i)
            ec_1_5=str(tc*cte-t)
            expr_1_5=sp.parse_expr(ec_1_5)
            print('variables desconocidas de 1.5', var_des_ase)

            if len(var_des_ase)==1:

                sol_1_5=sp.solve((expr_1_5),(var_des_ase[0]))
                if var_des_ase[0]==cte:
                    widgets.lineEdit_cte_elevador.setText(str(round(sol_1_5[0],4)))
                elif var_des_ase[0]==t:
                    widgets.lineEdit_t_elevador.setText(str(round(sol_1_5[0],4)))
                elif var_des_ase[0]==tc:
                    widgets.lineEdit_tc_elevador.setText(str(round(sol_1_5[0],4)))
   
            
            


        var_segunda=[Pc,v,t,q]
        var_des_se=[]
        for i in var_segunda:
            if isinstance(i, sp.core.symbol.Symbol):
                var_des_se.append(i)
        ec2=(str(((3.6*Pc*v)/t)-q))
        expr2=sp.parse_expr(ec2)
        print('variables segunda ec', var_segunda)
        

        print ('variable a despejar de la ec2,',var_des_se  )

        if len(var_des_se)==1:
            sol2=sp.solve((expr2),(var_des_se[0]))
            print('sol2: ', sol2)
            if var_des_se[0]==q:
                widgets.lineEdit_q_elevador.setText(str(round(sol2[0],4)))
            elif var_des_se[0]==t:
                widgets.lineEdit_t_elevador.setText(str(round(sol2[0],4)))
            elif var_des_se[0]==v:
                widgets.lineEdit_v_elevador.setText(str(round(sol2[0],4)))
            elif var_des_se[0]==Pc:
                widgets.lineEdit_Pc_elevador.setText(str(round(sol2[0],4)))
            
            


        #------------------------------------
        var_tercera=[q,v,H,Ho,Fa]
        var_des_te=[]

        print('variables iniciales',var_tercera)
        for i in var_tercera:
            if isinstance(i, sp.core.symbol.Symbol):
                var_des_te.append(i)
        print('variable a despejar :', var_des_te)
        ec3=str((q/(3.6*v))*(H+Ho)-Fa)
        print("ecuacion3",ec3)
        expr3=sp.parse_expr(ec3)
        if len(var_des_te)==1:
            sol3=sp.solve((expr3), (var_des_te[0]))
            print('la solucion es: ', sol3)
            if var_des_te[0]==q:
                widgets.lineEdit_q_elevador.setText(str(sol3[0]))
            elif var_des_te[0]==v:
                widgets.lineEdit_v_elevador.setText(str(sol3[0]))
            elif var_des_te[0]==H:
                widgets.lineEdit_H_elevador.setText(str(sol3[0]))
            #elif var_des_te[0]==Ho:
                #widgets.lineEdit_v_elevador.setText(str(sol3[0]))
            elif var_des_te[0]==Fa:
                widgets.lineEdit_Fa_elevador.setText(str(sol3[0]))


        #extructura
        #variables
        #vector vacio de incognitas
        #llenado de incognitas
        #ecuacion

        var_cuarta=[Fa, v, n , Na]
        var_des_ce=[]
        for i in var_cuarta:
            if isinstance(i, sp.core.symbol.Symbol):
                var_des_ce.append(i)
        ec4=str(((Fa*v)/(75*n))-Na)
        expr4=sp.parse_expr(ec4)
        if len(var_des_ce)==1:
            sol4=sp.solve((expr4), (var_des_ce[0]))
            if var_des_ce[0]==Fa:
                widgets.lineEdit_Fa_elevador.setText(str(sol4[0]))
            elif var_des_ce[0]==v:
                widgets.lineEdit_v_elevador.setText(str(sol4[0]))
            elif var_des_ce[0]==n:
                widgets.lineEdit_n_elevador.setText(str(sol4[0]))
            elif var_des_ce[0]==Na:
                widgets.lineEdit_Na_elevador.setText(str(sol4[0]))

        #extructura
        #variables
        #vector vacio de incognitas
        #llenado de incognitas
        #ecuacion

        var_quinta=[Fa, k, Ta]
        var_des_qe=[]
        for i in var_quinta:
            if isinstance(i, sp.core.symbol.Symbol):
                var_des_qe.append(i)
        ec5=str(Fa*k-Ta)
        expr5=sp.parse_expr(ec5)
        if len(var_des_qe)==1:
            sol5=sp.solve((expr5), (var_des_qe[0]))
            if var_des_qe[0]==Fa:
                widgets.lineEdit_Fa_elevador.setText(str(sol5[0]))
            elif var_des_qe[0]==Ta:
                widgets.lineEdit_Ta_elevador.setText(str(sol5[0]))
        
        #extructura
        #variables
        #vector vacio de incognitas
        #llenado de incognitas
        #ecuacion

        var_sexta=[m, v, R, alfa, FR]
        var_des_sxe=[]
        for i in var_sexta:
            if isinstance(i, sp.core.symbol.Symbol):
                var_des_sxe.append(i)
        
        ec6=str(((m*v**2)/R)-m*127137600*cos(alfa)-FR)
        expr6=sp.parse_expr(ec6)

        if len(var_des_sxe)==1:
            sol6=sp.solve((expr6), (var_des_sxe[0]))

            sol6_5 = [i.evalf() if i.is_real else i for i in sol6]

            print(sol6_5)

            sol6_6 = []

            for i in sol6_5:
                if i.is_real and i > 0:
                    sol6_6.append(i)

            print('sol6', sol6)
            print('sol 6.6', sol6_6)

            for o in var_sexta:
                if o == var_des_sxe[0]:
                    eval(f"widgets.lineEdit_{o}_elevador.setText(str(round(sol6_6[0], 5)))")


            '''if var_des_sxe[0]==m:
        
                widgets.lineEdit_m_elevador.setText(str(sol6[0]))

            elif var_des_sxe[0]==v:
                widgets.lineEdit_v_elevador.setText(str(sol6[1]))

            elif var_des_sxe[0]==R:
                widgets.lineEdit_R_elevador.setText(str(sol6[0]))

            elif var_des_sxe[0]==alfa:
                widgets.lineEdit_alfa_elevador.setText(str(sol6[1]))

            elif var_des_sxe[0]==FR:
                widgets.lineEdit_FR_elevador.setText(str(sol6[0]))'''

            

        Fc=1
        Fg=1
        if Fc==Fg:
            var_octava=[v,R]
            var_des_oe=[]
            for i in var_octava:
                if isinstance(i, sp.core.symbol.Symbol):
                    var_des_oe.append(i)
            ec8=str((v**2/127137600)-R)  
            expr8=sp.parse_expr(ec8)

            if len(var_des_oe)==1:
                sol8=sp.solve((expr8),(var_des_oe[0]))
                print('sol8: ', sol8)
                if var_des_oe[0]==R:
                    widgets.lineEdit_R_elevador.setText(str(sol8[0]))
                    widgets.lineEdit_D_elevador.setText(str(sol8[0]*2))
                elif var_des_oe[0]==v:
                    widgets.lineEdit_v_elevador.setText(str(sol8[1]))
        #extructura
        #variables
        #vector vacio de incognitas
        #llenado de incognitas
        #ecuacion
    #------------------------------------
        var_novena=[v,t,sh]
        var_des_ne=[]
        for i in var_novena:
            if isinstance(i, sp.core.symbol.Symbol):
                var_des_ne.append(i)
        ec9=str(v*t*sh)
        expr9=sp.parse_expr(ec9)
    #----------------------------------
        var_decima=[a,t,sv]
        var_des_de=[]
        for i in var_decima:
            if isinstance(i, sp.core.symbol.Symbol):
                var_des_de.append(i)
        ec10=str(0.5*a*t**2-sv)
        expr10=sp.parse_expr(ec10)

    #---------------------------------

        var_undecima=[v,t,a,s,sh,sv]
        var_des_ue=[]
        for i in var_undecima:
            if isinstance(i, sp.core.symbol.Symbol):
                var_des_ue.append(i)
        ec11=str(v*t+0.5*a*t**2-s)
        expr11=sp.parse_expr(ec11)
        #------------------------------
        var_doceava=[sh,sv,s]
        var_des_doe=[]
        for i in  var_doceava:
            if isinstance(i, sp.core.symbol.Symbol):
                var_des_doe.append(i)
        ec12=str(sh+sv-s)
        expr12=sp.parse_expr(ec12)

        #------------------------------
        var_trece=[q,Pc,Nc]
        var_trece_des=[]
        for i in var_trece:
            if isinstance(i, sp.core.symbol.Symbol):
                var_trece_des.append(i)
        ec13=str((q/Pc)-Nc)

        expr13=sp.parse_expr(ec13)

        if len (var_trece_des)==1:
            sol13=sp.solve(expr13, var_trece_des[0])

            print('sol13: ', sol13)
            if var_trece_des[0]==q:
                widgets.lineEdit_q_elevador.setText(str(round(sol13[0],4)))
        
            elif var_trece_des[0]==Pc:
                widgets.lineEdit_Pc_elevador.setText(str(round(sol13[0],4)))

            elif var_trece_des[0]==Nc:
                widgets.lineEdit_Nc_elevador.setText(str(round(sol13[0],4)))
        

        #-------------------------------

        var_catorce=[v,t,Nc]
        var_catorce_des=[]
        for i in var_catorce:
            if isinstance(i, sp.core.symbol.Symbol):
                var_catorce_des.append(i)
        ec14=str(t*Nc-v)

        expr14=sp.parse_expr(ec14)

        if len (var_catorce_des)==1:
            sol14=sp.solve(expr14, var_catorce_des[0])

            print('sol14: ', sol14)
            if var_catorce_des[0]==v:
                widgets.lineEdit_v_elevador.setText(str(round(sol14[0],4)))
        
            elif var_catorce_des[0]==t:
                widgets.lineEdit_t_elevador.setText(str(round(sol14[0],4)))

            elif var_catorce_des[0]==Nc:
                widgets.lineEdit_Nc_elevador.setText(str(round(sol14[0],4)))



        



        if len(var_des_ne)==1:
            sol9=sp.solve((expr9), (var_des_ne[0]))
            print('sol9: ', sol9)
            if var_des_ne[0]==v:
                widgets.lineEdit_v_elevador.setText(str(sol9[0]))
            elif var_des_ne[0]==t:
                widgets.lineEdit_t_elevador.setText(str(sol9[0]))
            elif var_des_ne[0]==sh:
                widgets.lineEdit_sh_elevador.setText(str(sol9[0]))
        

        if len(var_des_de)==1:
            sol10=sp.solve((expr10), (var_des_de[0]))
            print('sol10: ', sol10)
            if var_des_de[0]==a:
                widgets.lineEdit_a_elevador.setText(str(sol10[0]))
            elif var_des_de[0]==t:
                widgets.lineEdit_t_elevador.setText(str(sol10[1]))
            elif var_des_de[0]==sv:
                widgets.lineEdit_sv_elevador.setText(str(sol10[0]))
        
        if len(var_des_ue)==2 and len  (var_des_ne):
            sol11_1=sp.solve((expr9,expr11), (var_des_ue[0],var_des_ue[1]))
            print('sol 11.1: ', sol11_1)

            if var_des_ue[0]==v:
                widgets.lineEdit_v_elevador.setText(str(sol11_1[0]))
            elif var_des_ue[0]==t:
                widgets.lineEdit_t_elevador.setText(str(sol11_1[0]))
            elif var_des_ue[0]==sh:
                widgets.lineEdit_sh_elevador.setText(str(sol11_1[0]))


            if var_des_ue[1]==v:
                widgets.lineEdit_v_elevador.setText(str(sol11_1[1]))
            elif var_des_ue[1]==t:
                widgets.lineEdit_t_elevador.setText(str(sol11_1[1]))
            elif var_des_ue[1]==sh:
                widgets.lineEdit_sh_elevador.setText(str(sol11_1[1]))

        elif len(var_des_ue)==2 and len(var_des_de)==2 :
            sol11_2=sp.solve((expr10,expr11), (var_des_ue[0],var_des_ue[1]))
        print('variables12,', var_doceava)
        print('var_doe', var_des_doe)

        if len ( var_des_doe)==1:
            sol12=sp.solve((expr12),(var_des_doe[0]))
            print('sol12', sol12)
            print(ec2)
            if var_des_doe[0]==sh:
                widgets.lineEdit_sh_elevador.setText(str(round(sol12[0],4)))
            elif var_des_doe[0]==sv:
                widgets.lineEdit_sv_elevador.setText(str(round(sol12[0],4)))
            elif var_des_doe[0]==s:
                widgets.lineEdit_s_elevador.setText(str(round(sol12[0],4)))


    def modos_cangilones(self):
        widgets = self.ui 
        combox = self.sender()
        comboName = combox.objectName()

        all_lines=[widgets.lineEdit_Pc_elevador,
        widgets.lineEdit_i_elevador,widgets.lineEdit_p_elevador,widgets.lineEdit_j_elevador,
        widgets.lineEdit_q_elevador,widgets.lineEdit_v_elevador,widgets.lineEdit_t_elevador,
        widgets.lineEdit_Fa_elevador,widgets.lineEdit_H_elevador,widgets.lineEdit_Na_elevador,
        widgets.lineEdit_n_elevador,widgets.lineEdit_Ta_elevador,widgets.lineEdit_FR_elevador,
        widgets.lineEdit_m_elevador,widgets.lineEdit_R_elevador,widgets.lineEdit_alfa_elevador,
        widgets.lineEdit_sh_elevador,widgets.lineEdit_sv_elevador,widgets.lineEdit_a_elevador,
        widgets.lineEdit_s_elevador, widgets.lineEdit_Nc_elevador,widgets.lineEdit_D_elevador,
        widgets.comboBox_sistema_elevador,widgets.comboBox_tipo_elevador,widgets.comboBox_k_elevador]

        peso_transporte=[widgets.lineEdit_Pc_elevador,widgets.lineEdit_i_elevador,widgets.lineEdit_p_elevador,widgets.lineEdit_j_elevador]
        peso_transporte_sin = [elemento for elemento in all_lines if elemento not in peso_transporte]

        flujo_transporte=[widgets.lineEdit_q_elevador,widgets.lineEdit_v_elevador,widgets.lineEdit_t_elevador,widgets.comboBox_tipo_elevador]
        flujo_transporte_sin=[elemento for elemento in all_lines if elemento not in flujo_transporte]

        potencia_motor=[widgets.lineEdit_Na_elevador,widgets.lineEdit_n_elevador,widgets.lineEdit_v_elevador,widgets.lineEdit_Fa_elevador]
        potencia_motor_sin=[elemento for elemento in all_lines if elemento not in potencia_motor]

        tension_banda=[widgets.lineEdit_Fa_elevador,widgets.lineEdit_Ta_elevador,widgets.comboBox_k_elevador]
        tension_banda_sin=[elemento for elemento in all_lines if elemento not in tension_banda]

        numero_cangilones=[widgets.lineEdit_Pc_elevador, widgets.lineEdit_q_elevador, widgets.lineEdit_Nc_elevador]
        numero_cangilones_sin=[elemento for elemento in all_lines if elemento not in numero_cangilones]

        velocidad=[widgets.lineEdit_Nc_elevador,widgets.lineEdit_v_elevador,widgets.lineEdit_t_elevador]
        velocidad_sin=[elemento for elemento in all_lines if elemento not in velocidad]

        diametro=[widgets.lineEdit_v_elevador,widgets.lineEdit_D_elevador]
        diametro_sin=[elemento for elemento in all_lines if elemento not in diametro]


        if comboName=='combo_modos_elevador':

            if widgets.combo_modos_elevador.currentText() == 'General': 
                for i in all_lines:
                    i.setEnabled(True)
                    i.setStyleSheet('''background-color: #FFFFFF;
                                        background: #FFFFFF; ''')
                widgets.comboBox_Tparticula_elevador.setCurrentIndex(0)
                widgets.comboBox_Tparticula_elevador.setCurrentIndex(0)
                #aqui llamo a la funcion reset para que borre todo , la funcion esta definida mas abajo y especifica que hace
                self.reset_cangilones()
            
            elif widgets.combo_modos_elevador.currentText() == 'Weight of transported material ': 
                print('funciona ?')
                self.reset_cangilones()

                for i in peso_transporte:

                    i.setEnabled(True)
                    i.setStyleSheet("background-color: transparent;")
                    i.setStyleSheet('''background-color: #FFFFFF;
                                        background: #FFFFFF; ''')

                for i in peso_transporte_sin:

                    i.setEnabled(False)
                    i.setStyleSheet("background-color: lightgray")


            elif widgets.combo_modos_elevador.currentText() == 'Flow of transported material':
                self.reset_cangilones()

                for i in flujo_transporte:

                    i.setEnabled(True)
                    i.setStyleSheet("background-color: transparent;")
                    i.setStyleSheet('''background-color: #FFFFFF;
                                        background: #FFFFFF; ''')

                for i in flujo_transporte_sin:

                    i.setEnabled(False)
                    i.setStyleSheet("background-color: lightgray")
            
            elif widgets.combo_modos_elevador.currentText() == 'Motor Power':
                self.reset_cangilones()

                for i in potencia_motor:

                    i.setEnabled(True)
                    i.setStyleSheet("background-color: transparent;")
                    i.setStyleSheet('''background-color: #FFFFFF;
                                        background: #FFFFFF; ''')
                    
                for i in potencia_motor_sin:

                    i.setEnabled(False)
                    i.setStyleSheet("background-color: lightgray")

            
            elif widgets.combo_modos_elevador.currentText() == 'Maximum Belt Tension':
                self.reset_cangilones()

                for i in tension_banda:

                    i.setEnabled(True)
                    i.setStyleSheet("background-color: transparent;")
                    i.setStyleSheet('''background-color: #FFFFFF;
                                        background: #FFFFFF; ''')
                    
                for i in tension_banda_sin:

                    i.setEnabled(False)
                    i.setStyleSheet("background-color: lightgray")


            elif widgets.combo_modos_elevador.currentText() == 'Number of buckets':
                self.reset_cangilones()
                for i in numero_cangilones:

                    i.setEnabled(True)
                    i.setStyleSheet("background-color: transparent;")
                    i.setStyleSheet('''background-color: #FFFFFF;
                                        background: #FFFFFF; ''')
                    
                for i in numero_cangilones_sin:
                    i.setEnabled(False)
                    i.setStyleSheet("background-color: lightgray")

            elif widgets.combo_modos_elevador.currentText() == 'Belt travel speed':
                self.reset_cangilones()
                for i in velocidad:

                    i.setEnabled(True)
                    i.setStyleSheet("background-color: transparent;")
                    i.setStyleSheet('''background-color: #FFFFFF;
                                        background: #FFFFFF; ''')
                for i in velocidad_sin:
                    i.setEnabled(False)
                    i.setStyleSheet("background-color: lightgray")

            elif widgets.combo_modos_elevador.currentText() == 'Bucket Diameter':

                self.reset_cangilones()
                for i in diametro:

                    i.setEnabled(True)
                    i.setStyleSheet("background-color: transparent;")
                    i.setStyleSheet('''background-color: #FFFFFF;
                                        background: #FFFFFF; ''')
                for i in diametro_sin:
                    i.setEnabled(False)
                    i.setStyleSheet("background-color: lightgray")




    @qtc.Slot()
    def reset_tornillo (self):
        widgets.lineEdit_s_tornillo.clear()
        widgets.lineEdit_D_tornillo.clear()
        widgets.lineEdit_t_tornillo.clear()
        widgets.lineEdit_n_tornillo.clear()
        widgets.lineEdit_v_tornillo.clear()
        widgets.lineEdit_Q_tornillo.clear()
        widgets.lineEdit_y_tornillo.clear()
        #widgets.lineEdit_k_tornillo.clear()
        widgets.lineEdit_pst_tornillo.clear()
        widgets.lineEdit_PN_tornillo.clear()
        widgets.lineEdit_PH_tornillo.clear()
        widgets.lineEdit_L_tornillo.clear()
        #widgets.label_25.clear()
        x=widgets.comboBox_Co_tornillo.currentText()
        widgets.lineEdit_P_tornillo.clear()
        widgets.comboBox_k_tornillo.setCurrentIndex(0)
        widgets.comboBox_lambda_tornillo.setCurrentIndex(0)
        widgets.comboBox_Co_tornillo.setCurrentIndex(0)
    @qtc.Slot()
    def reset_cangilones (self) :
        lineEdit=[widgets.lineEdit_Pc_elevador,widgets.lineEdit_i_elevador
        ,widgets.lineEdit_p_elevador,widgets.lineEdit_j_elevador,widgets.lineEdit_q_elevador
        ,widgets.lineEdit_v_elevador,widgets.lineEdit_t_elevador,widgets.lineEdit_Fa_elevador
        ,widgets.lineEdit_H_elevador,widgets.lineEdit_Na_elevador,widgets.lineEdit_n_elevador
        ,widgets.lineEdit_FR_elevador,widgets.lineEdit_m_elevador,widgets.lineEdit_R_elevador
        ,widgets.lineEdit_alfa_elevador,widgets.lineEdit_sv_elevador,widgets.lineEdit_sh_elevador
        ,widgets.lineEdit_a_elevador,widgets.lineEdit_Ta_elevador,widgets.lineEdit_h_elevador,
        widgets.lineEdit_pp_elevador,widgets.lineEdit_s_elevador, widgets.lineEdit_Nc_elevador,
        widgets.lineEdit_D_elevador]

        for i in lineEdit:
            i.clear()
        widgets.comboBox_tipo_elevador.setCurrentIndex(0)
        widgets.comboBox_sistema_elevador.setCurrentIndex(0)
        widgets.comboBox_Tparticula_elevador.setCurrentIndex(0)
        widgets.comboBox_k_elevador.setCurrentIndex(0)
    def chequeo(self):
        self.botonPresionado = True

# Zarandas --> Interpolación + Calculos + Reset 
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
        widgets = self.ui 
        combox = self.sender()
        comboName = combox.objectName()

        if comboName == 'opcionesMolinoRodillo': 
            if widgets.opcionesMolinoRodillo.currentText() == 'Design angles': 
                widgets.lineEditAlimentoRodillo.setEnabled(False)
                widgets.lineEditProductoRodillo.setEnabled(False)
                widgets.lineEditWidthRodillos.setEnabled(False)
                widgets.lineEditk1.setEnabled(False)
                widgets.lineEditk2.setEnabled(False)
                widgets.lineEditk3.setEnabled(False)
                widgets.lineEditk4.setEnabled(False)
                widgets.lineEditTorqueMolienda.setEnabled(False)
                widgets.lineEditFuerzaEspecifica.setEnabled(False)
                widgets.lineEditDistanciaRodillos.setEnabled(False)
                widgets.lineEditVelocidadRodillos.setEnabled(False)
                widgets.lineEditCapacidadRodillos.setEnabled(False)
                widgets.lineEditSizePotenciaRodillos.setEnabled(False)

                # Reactivar: 
                widgets.lineEditTamaoMaximo.setEnabled(True)
                widgets.lineEditGrosorTorta.setEnabled(True)
                widgets.lineEditDensidadRodillo.setEnabled(True)
                widgets.lineEditTortaSalida.setEnabled(True)
                widgets.lineEditDiametroRodillos.setEnabled(True)
                widgets.lineEditCoeficienteFriccion.setEnabled(True)
                widgets.lineEditAnguloApertura.setEnabled(True)
                widgets.lineEditAnguloCompresion.setEnabled(True)
                widgets.lineEditAnguloFractura.setEnabled(True)


                # Cambiar el color de fondo de los widgets desactivados a gris
                default_style = "QLineEdit { }"
                light_gray_style = "background-color: lightgray;"
                widgets.lineEditAlimentoRodillo.setStyleSheet(light_gray_style)
                widgets.lineEditProductoRodillo.setStyleSheet(light_gray_style)
                widgets.lineEditWidthRodillos.setStyleSheet(light_gray_style)
                widgets.lineEditk1.setStyleSheet(light_gray_style)
                widgets.lineEditk2.setStyleSheet(light_gray_style)
                widgets.lineEditk3.setStyleSheet(light_gray_style)
                widgets.lineEditk4.setStyleSheet(light_gray_style)
                widgets.lineEditTorqueMolienda.setStyleSheet(light_gray_style)
                widgets.lineEditFuerzaEspecifica.setStyleSheet(light_gray_style)
                widgets.lineEditDistanciaRodillos.setStyleSheet(light_gray_style)
                widgets.lineEditVelocidadRodillos.setStyleSheet(light_gray_style)
                widgets.lineEditCapacidadRodillos.setStyleSheet(light_gray_style)
                widgets.lineEditSizePotenciaRodillos.setStyleSheet(light_gray_style)

                widgets.lineEditTamaoMaximo.setStyleSheet(default_style)
                widgets.lineEditGrosorTorta.setStyleSheet(default_style)
                widgets.lineEditDensidadRodillo.setStyleSheet(default_style)
                widgets.lineEditTortaSalida.setStyleSheet(default_style)
                widgets.lineEditDiametroRodillos.setStyleSheet(default_style)
                widgets.lineEditCoeficienteFriccion.setStyleSheet(default_style)
                widgets.lineEditAnguloApertura.setStyleSheet(default_style)
                widgets.lineEditAnguloCompresion.setStyleSheet(default_style)
                widgets.lineEditAnguloFractura.setStyleSheet(default_style)
                self.limpiarRodillos()


            
            elif widgets.opcionesMolinoRodillo.currentText() == 'Gap and Roll Diameter':
                widgets.lineEditAlimentoRodillo.setEnabled(False)
                widgets.lineEditProductoRodillo.setEnabled(False)
                widgets.lineEditTamaoMaximo.setEnabled(False)
                widgets.lineEditDensidadRodillo.setEnabled(False)
                widgets.lineEditGrosorTorta.setEnabled(False)
                widgets.lineEditCoeficienteFriccion.setEnabled(False)
                widgets.lineEditAnguloApertura.setEnabled(False)
                widgets.lineEditAnguloFractura.setEnabled(False)
                widgets.lineEditAnguloFractura.setEnabled(False)
                widgets.lineEditAnguloCompresion.setEnabled(False)
                widgets.lineEditWidthRodillos.setEnabled(False)
                widgets.lineEditTorqueMolienda.setEnabled(False)
                widgets.lineEditFuerzaEspecifica.setEnabled(False)
                widgets.lineEditCapacidadRodillos.setEnabled(False)
                widgets.lineEditSizePotenciaRodillos.setEnabled(False) 
                widgets.lineEditTortaSalida.setEnabled(False)
                
                # Reactivar los necesarios 
                widgets.lineEditDistanciaRodillos.setEnabled(True)
                widgets.lineEditDiametroRodillos.setEnabled(True)
                widgets.lineEditFuerzaEspecifica.setEnabled(True)
                widgets.lineEditk1.setEnabled(True)
                widgets.lineEditk2.setEnabled(True)
                widgets.lineEditk3.setEnabled(True)
                widgets.lineEditk4.setEnabled(True)
                widgets.lineEditVelocidadRodillos.setEnabled(True)

                default_style = "QLineEdit { }"
                light_gray_style = "background-color: lightgray;"
                widgets.lineEditAlimentoRodillo.setStyleSheet(light_gray_style)
                widgets.lineEditProductoRodillo.setStyleSheet(light_gray_style)
                widgets.lineEditTamaoMaximo.setStyleSheet(light_gray_style)
                widgets.lineEditDensidadRodillo.setStyleSheet(light_gray_style)
                widgets.lineEditGrosorTorta.setStyleSheet(light_gray_style)
                widgets.lineEditCoeficienteFriccion.setStyleSheet(light_gray_style)
                widgets.lineEditAnguloApertura.setStyleSheet(light_gray_style)
                widgets.lineEditAnguloFractura.setStyleSheet(light_gray_style)
                widgets.lineEditAnguloCompresion.setStyleSheet(light_gray_style)
                widgets.lineEditWidthRodillos.setStyleSheet(light_gray_style)
                widgets.lineEditTorqueMolienda.setStyleSheet(light_gray_style)
                widgets.lineEditFuerzaEspecifica.setStyleSheet(light_gray_style)
                widgets.lineEditCapacidadRodillos.setStyleSheet(light_gray_style)
                widgets.lineEditSizePotenciaRodillos.setStyleSheet(light_gray_style)
                widgets.lineEditTortaSalida.setStyleSheet(light_gray_style)

                widgets.lineEditDistanciaRodillos.setStyleSheet(default_style)
                widgets.lineEditDiametroRodillos.setStyleSheet(default_style)
                widgets.lineEditFuerzaEspecifica.setStyleSheet(default_style)
                widgets.lineEditk1.setStyleSheet(default_style)
                widgets.lineEditk2.setStyleSheet(default_style)
                widgets.lineEditk3.setStyleSheet(default_style)
                widgets.lineEditk4.setStyleSheet(default_style)
                widgets.lineEditVelocidadRodillos.setStyleSheet(default_style)
                self.limpiarRodillos()

            elif widgets.opcionesMolinoRodillo.currentText() == 'General':
                widgets.lineEditAlimentoRodillo.setEnabled(True)
                widgets.lineEditProductoRodillo.setEnabled(True)
                widgets.lineEditTamaoMaximo.setEnabled(True)
                widgets.lineEditDensidadRodillo.setEnabled(True)
                widgets.lineEditGrosorTorta.setEnabled(True)
                widgets.lineEditCoeficienteFriccion.setEnabled(True)
                widgets.lineEditAnguloApertura.setEnabled(True)
                widgets.lineEditAnguloFractura.setEnabled(True)
                widgets.lineEditAnguloFractura.setEnabled(True)
                widgets.lineEditAnguloCompresion.setEnabled(True)
                widgets.lineEditWidthRodillos.setEnabled(True)
                widgets.lineEditTorqueMolienda.setEnabled(True)
                widgets.lineEditFuerzaEspecifica.setEnabled(True)
                widgets.lineEditCapacidadRodillos.setEnabled(True)
                widgets.lineEditSizePotenciaRodillos.setEnabled(True) 
                widgets.lineEditTortaSalida.setEnabled(True)
                widgets.lineEditDistanciaRodillos.setEnabled(True)
                widgets.lineEditDiametroRodillos.setEnabled(True)
                widgets.lineEditFuerzaEspecifica.setEnabled(True)
                widgets.lineEditk1.setEnabled(True)
                widgets.lineEditk2.setEnabled(True)
                widgets.lineEditk3.setEnabled(True)
                widgets.lineEditk4.setEnabled(True) 
                widgets.lineEditVelocidadRodillos.setEnabled(True)


                default_style = "QLineEdit { }"
                widgets.lineEditAlimentoRodillo.setStyleSheet(default_style)
                widgets.lineEditProductoRodillo.setStyleSheet(default_style)
                widgets.lineEditTamaoMaximo.setStyleSheet(default_style)
                widgets.lineEditDensidadRodillo.setStyleSheet(default_style)
                widgets.lineEditGrosorTorta.setStyleSheet(default_style)
                widgets.lineEditCoeficienteFriccion.setStyleSheet(default_style)
                widgets.lineEditAnguloApertura.setStyleSheet(default_style)
                widgets.lineEditAnguloFractura.setStyleSheet(default_style)
                widgets.lineEditAnguloFractura.setStyleSheet(default_style)
                widgets.lineEditAnguloCompresion.setStyleSheet(default_style)
                widgets.lineEditWidthRodillos.setStyleSheet(default_style)
                widgets.lineEditTorqueMolienda.setStyleSheet(default_style)
                widgets.lineEditFuerzaEspecifica.setStyleSheet(default_style)
                widgets.lineEditCapacidadRodillos.setStyleSheet(default_style)
                widgets.lineEditSizePotenciaRodillos.setStyleSheet(default_style) 
                widgets.lineEditTortaSalida.setStyleSheet(default_style)
                widgets.lineEditDistanciaRodillos.setStyleSheet(default_style)
                widgets.lineEditDiametroRodillos.setStyleSheet(default_style)
                widgets.lineEditFuerzaEspecifica.setStyleSheet(default_style)
                widgets.lineEditk1.setStyleSheet(default_style)
                widgets.lineEditk2.setStyleSheet(default_style)
                widgets.lineEditk3.setStyleSheet(default_style)
                widgets.lineEditk4.setStyleSheet(default_style)
                widgets.lineEditVelocidadRodillos.setStyleSheet(default_style)
                self.limpiarRodillos()


            elif widgets.opcionesMolinoRodillo.currentText() == 'Rolls speed': 
                widgets.lineEditAlimentoRodillo.setEnabled(False)
                widgets.lineEditProductoRodillo.setEnabled(False)
                widgets.lineEditTamaoMaximo.setEnabled(False)
                widgets.lineEditDensidadRodillo.setEnabled(False)
                widgets.lineEditGrosorTorta.setEnabled(False)
                widgets.lineEditCoeficienteFriccion.setEnabled(False)
                widgets.lineEditAnguloApertura.setEnabled(False)
                widgets.lineEditAnguloFractura.setEnabled(False)
                widgets.lineEditAnguloFractura.setEnabled(False)
                widgets.lineEditAnguloCompresion.setEnabled(False)
                widgets.lineEditWidthRodillos.setEnabled(False)
                widgets.lineEditTorqueMolienda.setEnabled(False)
                widgets.lineEditFuerzaEspecifica.setEnabled(False)
                widgets.lineEditCapacidadRodillos.setEnabled(False)
                widgets.lineEditSizePotenciaRodillos.setEnabled(False) 
                widgets.lineEditTortaSalida.setEnabled(False)
                widgets.lineEditDistanciaRodillos.setEnabled(False)
                widgets.lineEditDiametroRodillos.setEnabled(True)
                widgets.lineEditVelocidadRodillos.setEnabled(True)
                widgets.lineEditFuerzaEspecifica.setEnabled(False)
                widgets.lineEditk1.setEnabled(False)
                widgets.lineEditk2.setEnabled(False)
                widgets.lineEditk3.setEnabled(False)
                widgets.lineEditk4.setEnabled(False) 

                default_style = "QLineEdit { }"
                light_gray_style = "background-color: lightgray;"
                widgets.lineEditAlimentoRodillo.setStyleSheet(light_gray_style)
                widgets.lineEditProductoRodillo.setStyleSheet(light_gray_style)
                widgets.lineEditTamaoMaximo.setStyleSheet(light_gray_style)
                widgets.lineEditDensidadRodillo.setStyleSheet(light_gray_style)
                widgets.lineEditGrosorTorta.setStyleSheet(light_gray_style)
                widgets.lineEditCoeficienteFriccion.setStyleSheet(light_gray_style)
                widgets.lineEditAnguloApertura.setStyleSheet(light_gray_style)
                widgets.lineEditAnguloFractura.setStyleSheet(light_gray_style)
                widgets.lineEditAnguloFractura.setStyleSheet(light_gray_style)
                widgets.lineEditAnguloCompresion.setStyleSheet(light_gray_style)
                widgets.lineEditWidthRodillos.setStyleSheet(light_gray_style)
                widgets.lineEditTorqueMolienda.setStyleSheet(light_gray_style)
                widgets.lineEditFuerzaEspecifica.setStyleSheet(light_gray_style)
                widgets.lineEditCapacidadRodillos.setStyleSheet(light_gray_style)
                widgets.lineEditSizePotenciaRodillos.setStyleSheet(light_gray_style) 
                widgets.lineEditTortaSalida.setStyleSheet(light_gray_style)
                widgets.lineEditDistanciaRodillos.setStyleSheet(light_gray_style)
                widgets.lineEditDiametroRodillos.setStyleSheet(default_style)
                widgets.lineEditVelocidadRodillos.setStyleSheet(default_style)
                widgets.lineEditFuerzaEspecifica.setStyleSheet(light_gray_style)
                widgets.lineEditk1.setStyleSheet(light_gray_style)
                widgets.lineEditk2.setStyleSheet(light_gray_style)
                widgets.lineEditk3.setStyleSheet(light_gray_style)
                widgets.lineEditk4.setStyleSheet(light_gray_style)
                self.limpiarRodillos()


            elif widgets.opcionesMolinoRodillo.currentText() == 'Mill Capacity ':
                widgets.lineEditAlimentoRodillo.setEnabled(False)
                widgets.lineEditProductoRodillo.setEnabled(False)
                widgets.lineEditTamaoMaximo.setEnabled(False)
                widgets.lineEditDensidadRodillo.setEnabled(True) #y
                widgets.lineEditGrosorTorta.setEnabled(False)
                widgets.lineEditCoeficienteFriccion.setEnabled(False)
                widgets.lineEditAnguloApertura.setEnabled(False)
                widgets.lineEditAnguloFractura.setEnabled(False)
                widgets.lineEditAnguloFractura.setEnabled(False)
                widgets.lineEditAnguloCompresion.setEnabled(False)
                widgets.lineEditWidthRodillos.setEnabled(True) #y
                widgets.lineEditTorqueMolienda.setEnabled(False)
                widgets.lineEditFuerzaEspecifica.setEnabled(False)
                widgets.lineEditCapacidadRodillos.setEnabled(True)
                widgets.lineEditSizePotenciaRodillos.setEnabled(False) 
                widgets.lineEditTortaSalida.setEnabled(False)
                widgets.lineEditDistanciaRodillos.setEnabled(True) #y
                widgets.lineEditDiametroRodillos.setEnabled(False)
                widgets.lineEditVelocidadRodillos.setEnabled(True) #y
                widgets.lineEditFuerzaEspecifica.setEnabled(False)
                widgets.lineEditk1.setEnabled(False)
                widgets.lineEditk2.setEnabled(False)
                widgets.lineEditk3.setEnabled(False)
                widgets.lineEditk4.setEnabled(False) 

                # Reactivación 
                default_style = "QLineEdit { }"
                light_gray_style = "background-color: lightgray;"

                widgets.lineEditAlimentoRodillo.setStyleSheet(light_gray_style)
                widgets.lineEditProductoRodillo.setStyleSheet(light_gray_style)
                widgets.lineEditTamaoMaximo.setStyleSheet(light_gray_style)
                widgets.lineEditDensidadRodillo.setStyleSheet(default_style) #y
                widgets.lineEditGrosorTorta.setStyleSheet(light_gray_style)
                widgets.lineEditCoeficienteFriccion.setStyleSheet(light_gray_style)
                widgets.lineEditAnguloApertura.setStyleSheet(light_gray_style)
                widgets.lineEditAnguloFractura.setStyleSheet(light_gray_style)
                widgets.lineEditAnguloFractura.setStyleSheet(light_gray_style)
                widgets.lineEditAnguloCompresion.setStyleSheet(light_gray_style)
                widgets.lineEditWidthRodillos.setStyleSheet(default_style)
                widgets.lineEditTorqueMolienda.setStyleSheet(light_gray_style)
                widgets.lineEditFuerzaEspecifica.setStyleSheet(light_gray_style)
                widgets.lineEditCapacidadRodillos.setStyleSheet(default_style)
                widgets.lineEditSizePotenciaRodillos.setStyleSheet(light_gray_style) 
                widgets.lineEditTortaSalida.setStyleSheet(light_gray_style)
                widgets.lineEditDistanciaRodillos.setStyleSheet(default_style)
                widgets.lineEditDiametroRodillos.setStyleSheet(light_gray_style)
                widgets.lineEditVelocidadRodillos.setStyleSheet(default_style)
                widgets.lineEditFuerzaEspecifica.setStyleSheet(light_gray_style)
                widgets.lineEditk1.setStyleSheet(light_gray_style)
                widgets.lineEditk2.setStyleSheet(light_gray_style)
                widgets.lineEditk3.setStyleSheet(light_gray_style)
                widgets.lineEditk4.setStyleSheet(light_gray_style)
                self.limpiarRodillos()

            elif widgets.opcionesMolinoRodillo.currentText() == 'Mill Power ':
                widgets.lineEditAlimentoRodillo.setEnabled(False)
                widgets.lineEditProductoRodillo.setEnabled(False)
                widgets.lineEditTamaoMaximo.setEnabled(False)
                widgets.lineEditDensidadRodillo.setEnabled(False) 
                widgets.lineEditGrosorTorta.setEnabled(False)
                widgets.lineEditCoeficienteFriccion.setEnabled(False)
                widgets.lineEditAnguloApertura.setEnabled(False)
                widgets.lineEditAnguloFractura.setEnabled(False)
                widgets.lineEditAnguloFractura.setEnabled(False)
                widgets.lineEditAnguloCompresion.setEnabled(False)
                widgets.lineEditWidthRodillos.setEnabled(False) 
                widgets.lineEditTorqueMolienda.setEnabled(True) #y
                widgets.lineEditFuerzaEspecifica.setEnabled(False)
                widgets.lineEditCapacidadRodillos.setEnabled(False)
                widgets.lineEditSizePotenciaRodillos.setEnabled(True) #y
                widgets.lineEditTortaSalida.setEnabled(False)
                widgets.lineEditDistanciaRodillos.setEnabled(False) 
                widgets.lineEditDiametroRodillos.setEnabled(True) #y
                widgets.lineEditVelocidadRodillos.setEnabled(True) #y
                widgets.lineEditFuerzaEspecifica.setEnabled(False)
                widgets.lineEditk1.setEnabled(False)
                widgets.lineEditk2.setEnabled(False)
                widgets.lineEditk3.setEnabled(False)
                widgets.lineEditk4.setEnabled(False) 

                default_style = "QLineEdit { }"
                light_gray_style = "background-color: lightgray;"
                widgets.lineEditAlimentoRodillo.setStyleSheet(light_gray_style)
                widgets.lineEditProductoRodillo.setStyleSheet(light_gray_style)
                widgets.lineEditTamaoMaximo.setStyleSheet(light_gray_style)
                widgets.lineEditDensidadRodillo.setStyleSheet(light_gray_style)
                widgets.lineEditGrosorTorta.setStyleSheet(light_gray_style)
                widgets.lineEditCoeficienteFriccion.setStyleSheet(light_gray_style)
                widgets.lineEditAnguloApertura.setStyleSheet(light_gray_style)
                widgets.lineEditAnguloFractura.setStyleSheet(light_gray_style)
                widgets.lineEditAnguloFractura.setStyleSheet(light_gray_style)
                widgets.lineEditAnguloCompresion.setStyleSheet(light_gray_style)
                widgets.lineEditWidthRodillos.setStyleSheet(light_gray_style)
                widgets.lineEditTorqueMolienda.setStyleSheet(default_style) #y
                widgets.lineEditFuerzaEspecifica.setStyleSheet(light_gray_style)
                widgets.lineEditCapacidadRodillos.setStyleSheet(light_gray_style)
                widgets.lineEditSizePotenciaRodillos.setStyleSheet(default_style) #y
                widgets.lineEditTortaSalida.setStyleSheet(light_gray_style)
                widgets.lineEditDistanciaRodillos.setStyleSheet(light_gray_style) 
                widgets.lineEditDiametroRodillos.setStyleSheet(default_style) #y
                widgets.lineEditVelocidadRodillos.setStyleSheet(default_style) #y
                widgets.lineEditFuerzaEspecifica.setStyleSheet(light_gray_style)
                widgets.lineEditk1.setStyleSheet(light_gray_style)
                widgets.lineEditk2.setStyleSheet(light_gray_style)
                widgets.lineEditk3.setStyleSheet(light_gray_style)
                widgets.lineEditk4.setStyleSheet(light_gray_style)
                self.limpiarRodillos()
    def inhabilitar_bolas(self): 
        widgets = self.ui 
        combox = self.sender()
        comboName = combox.objectName()

        if comboName == 'comboBox_2': 
            if widgets.comboBox_2.currentText() == 'General': 
                widgets.lineEditSizeAlimento.setEnabled(True)
                widgets.lineEditSizeProducto.setEnabled(True)
                widgets.lineEditDensidadAlimento.setEnabled(True)
                widgets.lineEditDensidadBolas.setEnabled(True)
                widgets.lineEditDiametroMolino.setEnabled(True)
                widgets.lineEditLongitudMolino.setEnabled(True)
                widgets.lineEditPorosidadLecho.setEnabled(True)
                widgets.lineEditMasaRocas.setEnabled(True)
                widgets.lineEditMasaBolas.setEnabled(True)
                widgets.lineEditNumeroLevantadores.setEnabled(True)
                widgets.lineEditSizeBolas.setEnabled(True)
                widgets.lineEditFraccionRocas.setEnabled(True)
                widgets.lineEditFraccionBolas.setEnabled(True)
                widgets.lineEditConstanteMolino.setEnabled(True)
                widgets.lineEditFrecuenciaMolienda_2.setEnabled(True)
                widgets.lineEditFrecuenciaCritica_2.setEnabled(True)
                widgets.lineEditFraccionFrecuenciaC.setEnabled(True)
                widgets.lineEditIndiceAbrasion.setEnabled(True)
                widgets.lineEditIndiceBond.setEnabled(True)
                widgets.lineEditFactorCorrecionCapacidad.setEnabled(True)
                widgets.lineEditDesgasteBolas.setEnabled(True)
                widgets.lineEditCapacidadMolino.setEnabled(True)
                widgets.lineEditPotenciaMolino.setEnabled(True)

                default_style = "QLineEdit { }"
                widgets.lineEditSizeAlimento.setStyleSheet(default_style)
                widgets.lineEditSizeProducto.setStyleSheet(default_style)
                widgets.lineEditDensidadAlimento.setStyleSheet(default_style)
                widgets.lineEditDensidadBolas.setStyleSheet(default_style)
                widgets.lineEditDiametroMolino.setStyleSheet(default_style)
                widgets.lineEditLongitudMolino.setStyleSheet(default_style)
                widgets.lineEditPorosidadLecho.setStyleSheet(default_style)
                widgets.lineEditMasaRocas.setStyleSheet(default_style)
                widgets.lineEditMasaBolas.setStyleSheet(default_style)
                widgets.lineEditNumeroLevantadores.setStyleSheet(default_style)
                widgets.lineEditSizeBolas.setStyleSheet(default_style)
                widgets.lineEditFraccionRocas.setStyleSheet(default_style)
                widgets.lineEditFraccionBolas.setStyleSheet(default_style)
                widgets.lineEditConstanteMolino.setStyleSheet(default_style)
                widgets.lineEditFrecuenciaMolienda_2.setStyleSheet(default_style)
                widgets.lineEditFrecuenciaCritica_2.setStyleSheet(default_style)
                widgets.lineEditFraccionFrecuenciaC.setStyleSheet(default_style)
                widgets.lineEditIndiceAbrasion.setStyleSheet(default_style)
                widgets.lineEditIndiceBond.setStyleSheet(default_style)
                widgets.lineEditFactorCorrecionCapacidad.setStyleSheet(default_style)
                widgets.lineEditDesgasteBolas.setStyleSheet(default_style)
                widgets.lineEditCapacidadMolino.setStyleSheet(default_style)
                widgets.lineEditPotenciaMolino.setStyleSheet(default_style)
                self.limpiarBolas()

            elif widgets.comboBox_2.currentText() == 'Ball and Mill Diameter': 
                widgets.lineEditSizeAlimento.setEnabled(True) #y
                widgets.lineEditSizeProducto.setEnabled(False) 
                widgets.lineEditDensidadAlimento.setEnabled(True) #y
                widgets.lineEditDensidadBolas.setEnabled(False)  
                widgets.lineEditDiametroMolino.setEnabled(True) #y
                widgets.lineEditLongitudMolino.setEnabled(False) 
                widgets.lineEditPorosidadLecho.setEnabled(False) 
                widgets.lineEditMasaRocas.setEnabled(False) 
                widgets.lineEditMasaBolas.setEnabled(False) 
                widgets.lineEditNumeroLevantadores.setEnabled(False)
                widgets.lineEditSizeBolas.setEnabled(True) # y
                widgets.lineEditFraccionRocas.setEnabled(False) 
                widgets.lineEditFraccionBolas.setEnabled(False)
                widgets.lineEditConstanteMolino.setEnabled(True) #y
                widgets.lineEditFrecuenciaMolienda_2.setEnabled(True) #y
                widgets.lineEditFrecuenciaCritica_2.setEnabled(True) #y
                widgets.lineEditFraccionFrecuenciaC.setEnabled(True) #y
                widgets.lineEditIndiceAbrasion.setEnabled(False)
                widgets.lineEditIndiceBond.setEnabled(True) #y
                widgets.lineEditFactorCorrecionCapacidad.setEnabled(False)
                widgets.lineEditDesgasteBolas.setEnabled(False)
                widgets.lineEditCapacidadMolino.setEnabled(False)
                widgets.lineEditPotenciaMolino.setEnabled(False)

                default_style = "QLineEdit { }"
                light_gray_style = "background-color: lightgray;"

                widgets.lineEditSizeAlimento.setStyleSheet(default_style) #y
                widgets.lineEditSizeProducto.setStyleSheet(light_gray_style) 
                widgets.lineEditDensidadAlimento.setStyleSheet(default_style) #y
                widgets.lineEditDensidadBolas.setStyleSheet(light_gray_style) 
                widgets.lineEditDiametroMolino.setStyleSheet(default_style) #y
                widgets.lineEditLongitudMolino.setStyleSheet(light_gray_style)  
                widgets.lineEditPorosidadLecho.setStyleSheet(light_gray_style) 
                widgets.lineEditMasaRocas.setStyleSheet(light_gray_style) 
                widgets.lineEditMasaBolas.setStyleSheet(light_gray_style) 
                widgets.lineEditNumeroLevantadores.setStyleSheet(light_gray_style) 
                widgets.lineEditSizeBolas.setStyleSheet(default_style) #y
                widgets.lineEditFraccionRocas.setStyleSheet(light_gray_style) 
                widgets.lineEditFraccionBolas.setStyleSheet(light_gray_style) 
                widgets.lineEditConstanteMolino.setStyleSheet(default_style) #y
                widgets.lineEditFrecuenciaMolienda_2.setStyleSheet(default_style) #y
                widgets.lineEditFrecuenciaCritica_2.setStyleSheet(default_style) #y
                widgets.lineEditFraccionFrecuenciaC.setStyleSheet(default_style) #y
                widgets.lineEditIndiceAbrasion.setStyleSheet(light_gray_style) 
                widgets.lineEditIndiceBond.setStyleSheet(default_style) #y
                widgets.lineEditFactorCorrecionCapacidad.setStyleSheet(light_gray_style) #y
                widgets.lineEditDesgasteBolas.setStyleSheet(light_gray_style) #y
                widgets.lineEditCapacidadMolino.setStyleSheet(light_gray_style) #y
                widgets.lineEditPotenciaMolino.setStyleSheet(light_gray_style) #y
                self.limpiarBolas()

            elif widgets.comboBox_2.currentText() == 'Ball Wearing': 
                widgets.lineEditSizeAlimento.setEnabled(False) 
                widgets.lineEditSizeProducto.setEnabled(False) 
                widgets.lineEditDensidadAlimento.setEnabled(False) 
                widgets.lineEditDensidadBolas.setEnabled(False)  
                widgets.lineEditDiametroMolino.setEnabled(False) 
                widgets.lineEditLongitudMolino.setEnabled(False) 
                widgets.lineEditPorosidadLecho.setEnabled(False) 
                widgets.lineEditMasaRocas.setEnabled(False) 
                widgets.lineEditMasaBolas.setEnabled(False) 
                widgets.lineEditNumeroLevantadores.setEnabled(False)
                widgets.lineEditSizeBolas.setEnabled(False) 
                widgets.lineEditFraccionRocas.setEnabled(False) 
                widgets.lineEditFraccionBolas.setEnabled(False)
                widgets.lineEditConstanteMolino.setEnabled(False) 
                widgets.lineEditFrecuenciaMolienda_2.setEnabled(False) 
                widgets.lineEditFrecuenciaCritica_2.setEnabled(False) 
                widgets.lineEditFraccionFrecuenciaC.setEnabled(False) 
                widgets.lineEditIndiceAbrasion.setEnabled(True) #y
                widgets.lineEditIndiceBond.setEnabled(False) 
                widgets.lineEditFactorCorrecionCapacidad.setEnabled(False)
                widgets.lineEditDesgasteBolas.setEnabled(True) #y
                widgets.lineEditCapacidadMolino.setEnabled(False)
                widgets.lineEditPotenciaMolino.setEnabled(False)

                default_style = "QLineEdit { }"
                light_gray_style = "background-color: lightgray;"

                widgets.lineEditSizeAlimento.setStyleSheet(light_gray_style) 
                widgets.lineEditSizeProducto.setStyleSheet(light_gray_style) 
                widgets.lineEditDensidadAlimento.setStyleSheet(light_gray_style) 
                widgets.lineEditDensidadBolas.setStyleSheet(light_gray_style)   
                widgets.lineEditDiametroMolino.setStyleSheet(light_gray_style) 
                widgets.lineEditLongitudMolino.setStyleSheet(light_gray_style) 
                widgets.lineEditPorosidadLecho.setStyleSheet(light_gray_style) 
                widgets.lineEditMasaRocas.setStyleSheet(light_gray_style) 
                widgets.lineEditMasaBolas.setStyleSheet(light_gray_style) 
                widgets.lineEditNumeroLevantadores.setStyleSheet(light_gray_style) 
                widgets.lineEditSizeBolas.setStyleSheet(light_gray_style) 
                widgets.lineEditFraccionRocas.setStyleSheet(light_gray_style) 
                widgets.lineEditFraccionBolas.setStyleSheet(light_gray_style) 
                widgets.lineEditConstanteMolino.setStyleSheet(light_gray_style) 
                widgets.lineEditFrecuenciaMolienda_2.setStyleSheet(light_gray_style) 
                widgets.lineEditFrecuenciaCritica_2.setStyleSheet(light_gray_style) 
                widgets.lineEditFraccionFrecuenciaC.setStyleSheet(light_gray_style) 
                widgets.lineEditIndiceAbrasion.setStyleSheet(default_style) 
                widgets.lineEditIndiceBond.setStyleSheet(light_gray_style) 
                widgets.lineEditFactorCorrecionCapacidad.setStyleSheet(light_gray_style) 
                widgets.lineEditDesgasteBolas.setStyleSheet(default_style) 
                widgets.lineEditCapacidadMolino.setStyleSheet(light_gray_style) 
                widgets.lineEditPotenciaMolino.setStyleSheet(light_gray_style) 
                self.limpiarBolas()

            elif widgets.comboBox_2.currentText() == 'Mill Power': 
                widgets.lineEditSizeAlimento.setEnabled(True) #y
                widgets.lineEditSizeProducto.setEnabled(True) #y
                widgets.lineEditDensidadAlimento.setEnabled(False)  
                widgets.lineEditDensidadBolas.setEnabled(False)    
                widgets.lineEditDiametroMolino.setEnabled(False) 
                widgets.lineEditLongitudMolino.setEnabled(False) 
                widgets.lineEditPorosidadLecho.setEnabled(False) 
                widgets.lineEditMasaRocas.setEnabled(False) 
                widgets.lineEditMasaBolas.setEnabled(False) 
                widgets.lineEditNumeroLevantadores.setEnabled(False)
                widgets.lineEditSizeBolas.setEnabled(False) 
                widgets.lineEditFraccionRocas.setEnabled(False) 
                widgets.lineEditFraccionBolas.setEnabled(False)
                widgets.lineEditConstanteMolino.setEnabled(False) 
                widgets.lineEditFrecuenciaMolienda_2.setEnabled(False) 
                widgets.lineEditFrecuenciaCritica_2.setEnabled(False) 
                widgets.lineEditFraccionFrecuenciaC.setEnabled(False) 
                widgets.lineEditIndiceAbrasion.setEnabled(False) 
                widgets.lineEditIndiceBond.setEnabled(True) #y
                widgets.lineEditFactorCorrecionCapacidad.setEnabled(False)
                widgets.lineEditDesgasteBolas.setEnabled(False) 
                widgets.lineEditCapacidadMolino.setEnabled(True) #y
                widgets.lineEditPotenciaMolino.setEnabled(True)

                default_style = "QLineEdit { }"
                light_gray_style = "background-color: lightgray;"

                widgets.lineEditSizeAlimento.setStyleSheet(default_style)  #y
                widgets.lineEditSizeProducto.setStyleSheet(default_style) #y
                widgets.lineEditDensidadAlimento.setStyleSheet(light_gray_style)   
                widgets.lineEditDensidadBolas.setStyleSheet(light_gray_style)   
                widgets.lineEditDiametroMolino.setStyleSheet(light_gray_style)  
                widgets.lineEditLongitudMolino.setStyleSheet(light_gray_style)  
                widgets.lineEditPorosidadLecho.setStyleSheet(light_gray_style) 
                widgets.lineEditMasaRocas.setStyleSheet(light_gray_style)  
                widgets.lineEditMasaBolas.setStyleSheet(light_gray_style)  
                widgets.lineEditNumeroLevantadores.setStyleSheet(light_gray_style) 
                widgets.lineEditSizeBolas.setStyleSheet(light_gray_style) 
                widgets.lineEditFraccionRocas.setStyleSheet(light_gray_style)  
                widgets.lineEditFraccionBolas.setStyleSheet(light_gray_style) 
                widgets.lineEditConstanteMolino.setStyleSheet(light_gray_style)  
                widgets.lineEditFrecuenciaMolienda_2.setStyleSheet(light_gray_style)  
                widgets.lineEditFrecuenciaCritica_2.setStyleSheet(light_gray_style) 
                widgets.lineEditFraccionFrecuenciaC.setStyleSheet(light_gray_style) 
                widgets.lineEditIndiceAbrasion.setStyleSheet(light_gray_style) 
                widgets.lineEditIndiceBond.setStyleSheet(default_style) 
                widgets.lineEditFactorCorrecionCapacidad.setStyleSheet(light_gray_style) 
                widgets.lineEditDesgasteBolas.setStyleSheet(light_gray_style) 
                widgets.lineEditCapacidadMolino.setStyleSheet(default_style) 
                widgets.lineEditPotenciaMolino.setStyleSheet(default_style) 
                self.limpiarBolas()

            elif widgets.comboBox_2.currentText() == 'Mill Capacity': 
                widgets.lineEditSizeAlimento.setEnabled(True) #y
                widgets.lineEditSizeProducto.setEnabled(True) #y
                widgets.lineEditDensidadAlimento.setEnabled(False)  
                widgets.lineEditDensidadBolas.setEnabled(True) #y 
                widgets.lineEditDiametroMolino.setEnabled(True) #y
                widgets.lineEditLongitudMolino.setEnabled(True) #y
                widgets.lineEditPorosidadLecho.setEnabled(True) #y
                widgets.lineEditMasaRocas.setEnabled(False)
                widgets.lineEditMasaBolas.setEnabled(True) #y
                widgets.lineEditNumeroLevantadores.setEnabled(False)
                widgets.lineEditSizeBolas.setEnabled(False) 
                widgets.lineEditFraccionRocas.setEnabled(False) 
                widgets.lineEditFraccionBolas.setEnabled(True) #y
                widgets.lineEditConstanteMolino.setEnabled(False) 
                widgets.lineEditFrecuenciaMolienda_2.setEnabled(True) #y 
                widgets.lineEditFrecuenciaCritica_2.setEnabled(True)  #y
                widgets.lineEditFraccionFrecuenciaC.setEnabled(True) #y
                widgets.lineEditIndiceAbrasion.setEnabled(False) 
                widgets.lineEditIndiceBond.setEnabled(True) #y
                widgets.lineEditFactorCorrecionCapacidad.setEnabled(True) #y
                widgets.lineEditDesgasteBolas.setEnabled(False) 
                widgets.lineEditCapacidadMolino.setEnabled(True) #y
                widgets.lineEditPotenciaMolino.setEnabled(False)

                default_style = "QLineEdit { }"
                light_gray_style = "background-color: lightgray;"

                widgets.lineEditSizeAlimento.setStyleSheet(default_style) #y
                widgets.lineEditSizeProducto.setStyleSheet(default_style) #y
                widgets.lineEditDensidadAlimento.setStyleSheet(light_gray_style)
                widgets.lineEditDensidadBolas.setStyleSheet(default_style) #y 
                widgets.lineEditDiametroMolino.setStyleSheet(default_style) #y
                widgets.lineEditLongitudMolino.setStyleSheet(default_style) #y
                widgets.lineEditPorosidadLecho.setStyleSheet(default_style) #y
                widgets.lineEditMasaRocas.setStyleSheet(light_gray_style)
                widgets.lineEditMasaBolas.setStyleSheet(default_style) #y
                widgets.lineEditNumeroLevantadores.setStyleSheet(light_gray_style)
                widgets.lineEditSizeBolas.setStyleSheet(light_gray_style)
                widgets.lineEditFraccionRocas.setStyleSheet(light_gray_style)
                widgets.lineEditFraccionBolas.setStyleSheet(default_style) #y
                widgets.lineEditConstanteMolino.setStyleSheet(light_gray_style) 
                widgets.lineEditFrecuenciaMolienda_2.setStyleSheet(default_style) #y 
                widgets.lineEditFrecuenciaCritica_2.setStyleSheet(default_style) #y
                widgets.lineEditFraccionFrecuenciaC.setStyleSheet(default_style) #y
                widgets.lineEditIndiceAbrasion.setStyleSheet(light_gray_style)
                widgets.lineEditIndiceBond.setStyleSheet(default_style) #y
                widgets.lineEditFactorCorrecionCapacidad.setStyleSheet(default_style) #y
                widgets.lineEditDesgasteBolas.setStyleSheet(light_gray_style)
                widgets.lineEditCapacidadMolino.setStyleSheet(default_style) #y
                widgets.lineEditPotenciaMolino.setStyleSheet(light_gray_style)
                self.limpiarBolas()
    def inhabilitar_mandibulas(self): 
        widgets = self.ui 
        combox = self.sender()
        comboName = combox.objectName()

        if comboName == 'comboBox': 
            if widgets.comboBox.currentText() == 'General': 
                widgets.lineEditSizeMayor.setEnabled(True)
                widgets.lineEditSizeMenor.setEnabled(True)
                widgets.lineEditDensidad.setEnabled(True)
                widgets.lineEditLmin.setEnabled(True)
                widgets.lineEditFrecuenciaMolienda.setEnabled(True)
                widgets.lineEditSet.setEnabled(True)
                widgets.lineEditGape.setEnabled(True)
                widgets.lineEditAlturaTriturador.setEnabled(True)
                widgets.lineEditWidth.setEnabled(True)
                widgets.lineEditThrow.setEnabled(True)
                widgets.lineEditCapacidadTrituradora.setEnabled(True)
                widgets.lineEditFrecuenciaCritica.setEnabled(True)
                widgets.lineEditCapacidadReal.setEnabled(True)
                widgets.lineEditRelacionReduccion.setEnabled(True)
                widgets.lineEditOtroIndiceTrituradora.setEnabled(True)
                widgets.lineEditPotenciaTrituradora.setEnabled(True)

                default_style = "QLineEdit { }"
                light_gray_style = "background-color: lightgray;"

                widgets.lineEditSizeMayor.setStyleSheet(default_style)
                widgets.lineEditSizeMenor.setStyleSheet(default_style)
                widgets.lineEditDensidad.setStyleSheet(default_style)
                widgets.lineEditLmin.setStyleSheet(default_style)
                widgets.lineEditFrecuenciaMolienda.setStyleSheet(default_style)
                widgets.lineEditSet.setStyleSheet(default_style)
                widgets.lineEditGape.setStyleSheet(default_style)
                widgets.lineEditAlturaTriturador.setStyleSheet(default_style)
                widgets.lineEditWidth.setStyleSheet(default_style)
                widgets.lineEditThrow.setStyleSheet(default_style)
                widgets.lineEditCapacidadTrituradora.setStyleSheet(default_style)
                widgets.lineEditFrecuenciaCritica.setStyleSheet(default_style)
                widgets.lineEditCapacidadReal.setStyleSheet(default_style)
                widgets.lineEditRelacionReduccion.setStyleSheet(default_style)
                widgets.lineEditOtroIndiceTrituradora.setStyleSheet(default_style)
                widgets.lineEditPotenciaTrituradora.setStyleSheet(default_style)    
                self.limpiarMandibula() 

            elif widgets.comboBox.currentText() == 'Mill Geometrical Parameters': 
                widgets.lineEditSizeMayor.setEnabled(True) #y
                widgets.lineEditSizeMenor.setEnabled(False) 
                widgets.lineEditDensidad.setEnabled(False) 
                widgets.lineEditLmin.setEnabled(True) #y
                widgets.lineEditFrecuenciaMolienda.setEnabled(False)
                widgets.lineEditSet.setEnabled(True) #y
                widgets.lineEditGape.setEnabled(True) #y
                widgets.lineEditAlturaTriturador.setEnabled(True) #y
                widgets.lineEditWidth.setEnabled(True) #y
                widgets.lineEditThrow.setEnabled(True) #y
                widgets.lineEditCapacidadTrituradora.setEnabled(False)
                widgets.lineEditFrecuenciaCritica.setEnabled(False)
                widgets.lineEditCapacidadReal.setEnabled(False)
                widgets.lineEditRelacionReduccion.setEnabled(True) #y
                widgets.lineEditOtroIndiceTrituradora.setEnabled(False)
                widgets.lineEditPotenciaTrituradora.setEnabled(False)

                default_style = "QLineEdit { }"
                light_gray_style = "background-color: lightgray;"

                widgets.lineEditSizeMayor.setStyleSheet(default_style) #y
                widgets.lineEditSizeMenor.setStyleSheet(light_gray_style) 
                widgets.lineEditDensidad.setStyleSheet(light_gray_style) 
                widgets.lineEditLmin.setStyleSheet(default_style) #y
                widgets.lineEditFrecuenciaMolienda.setStyleSheet(light_gray_style)
                widgets.lineEditSet.setStyleSheet(default_style) #y
                widgets.lineEditGape.setStyleSheet(default_style) #y
                widgets.lineEditAlturaTriturador.setStyleSheet(default_style) #y
                widgets.lineEditWidth.setStyleSheet(default_style) #y
                widgets.lineEditThrow.setStyleSheet(default_style) #y
                widgets.lineEditCapacidadTrituradora.setStyleSheet(light_gray_style)
                widgets.lineEditFrecuenciaCritica.setStyleSheet(light_gray_style)
                widgets.lineEditCapacidadReal.setStyleSheet(light_gray_style)
                widgets.lineEditRelacionReduccion.setStyleSheet(default_style) #y
                widgets.lineEditOtroIndiceTrituradora.setStyleSheet(light_gray_style)
                widgets.lineEditPotenciaTrituradora.setStyleSheet(light_gray_style)
                self.limpiarMandibula()

            elif widgets.comboBox.currentText() == 'Mill Capacity': 
                widgets.lineEditSizeMayor.setEnabled(True) 
                widgets.lineEditSizeMenor.setEnabled(True) 
                widgets.lineEditDensidad.setEnabled(True) 
                widgets.lineEditLmin.setEnabled(True) 
                widgets.lineEditFrecuenciaMolienda.setEnabled(True)
                widgets.lineEditSet.setEnabled(True) 
                widgets.lineEditGape.setEnabled(True) 
                widgets.lineEditAlturaTriturador.setEnabled(True) 
                widgets.lineEditWidth.setEnabled(True) 
                widgets.lineEditThrow.setEnabled(True) 
                widgets.lineEditCapacidadTrituradora.setEnabled(True)
                widgets.lineEditFrecuenciaCritica.setEnabled(True)
                widgets.lineEditCapacidadReal.setEnabled(True)
                widgets.lineEditRelacionReduccion.setEnabled(True) 
                widgets.lineEditOtroIndiceTrituradora.setEnabled(False) #nel
                widgets.lineEditPotenciaTrituradora.setEnabled(False)   #nel

                default_style = "QLineEdit { }"
                light_gray_style = "background-color: lightgray;"

                widgets.lineEditSizeMayor.setStyleSheet(default_style) 
                widgets.lineEditSizeMenor.setStyleSheet(default_style) 
                widgets.lineEditDensidad.setStyleSheet(default_style) 
                widgets.lineEditLmin.setStyleSheet(default_style) 
                widgets.lineEditFrecuenciaMolienda.setStyleSheet(default_style) 
                widgets.lineEditSet.setStyleSheet(default_style) 
                widgets.lineEditGape.setStyleSheet(default_style)  
                widgets.lineEditAlturaTriturador.setStyleSheet(default_style) 
                widgets.lineEditWidth.setStyleSheet(default_style)  
                widgets.lineEditThrow.setStyleSheet(default_style) 
                widgets.lineEditCapacidadTrituradora.setStyleSheet(default_style) 
                widgets.lineEditFrecuenciaCritica.setStyleSheet(default_style) 
                widgets.lineEditCapacidadReal.setStyleSheet(default_style) 
                widgets.lineEditRelacionReduccion.setStyleSheet(default_style)  
                widgets.lineEditOtroIndiceTrituradora.setStyleSheet(light_gray_style)  #nel
                widgets.lineEditPotenciaTrituradora.setStyleSheet(light_gray_style)   #nel
                self.limpiarMandibula()

            elif widgets.comboBox.currentText() == 'Mill Power': 
                widgets.lineEditSizeMayor.setEnabled(True)
                widgets.lineEditSizeMenor.setEnabled(False) 
                widgets.lineEditDensidad.setEnabled(False) 
                widgets.lineEditLmin.setEnabled(True) #y
                widgets.lineEditFrecuenciaMolienda.setEnabled(False)
                widgets.lineEditSet.setEnabled(True)  #y
                widgets.lineEditGape.setEnabled(True) #y
                widgets.lineEditAlturaTriturador.setEnabled(False) 
                widgets.lineEditWidth.setEnabled(False) 
                widgets.lineEditThrow.setEnabled(True) #y
                widgets.lineEditCapacidadTrituradora.setEnabled(False)
                widgets.lineEditFrecuenciaCritica.setEnabled(False)
                widgets.lineEditCapacidadReal.setEnabled(True) #y
                widgets.lineEditRelacionReduccion.setEnabled(True) #y
                widgets.lineEditOtroIndiceTrituradora.setEnabled(True) #y
                widgets.lineEditPotenciaTrituradora.setEnabled(True)  #y

                default_style = "QLineEdit { }"
                light_gray_style = "background-color: lightgray;"

                widgets.lineEditSizeMayor.setStyleSheet(default_style) #y
                widgets.lineEditSizeMenor.setStyleSheet(light_gray_style)
                widgets.lineEditDensidad.setStyleSheet(light_gray_style)
                widgets.lineEditLmin.setStyleSheet(default_style)
                widgets.lineEditFrecuenciaMolienda.setStyleSheet(light_gray_style)
                widgets.lineEditSet.setStyleSheet(default_style)
                widgets.lineEditGape.setStyleSheet(default_style) #y
                widgets.lineEditAlturaTriturador.setStyleSheet(light_gray_style) 
                widgets.lineEditWidth.setStyleSheet(light_gray_style)
                widgets.lineEditThrow.setStyleSheet(default_style)
                widgets.lineEditCapacidadTrituradora.setStyleSheet(light_gray_style) 
                widgets.lineEditFrecuenciaCritica.setStyleSheet(light_gray_style) 
                widgets.lineEditCapacidadReal.setStyleSheet(default_style)
                widgets.lineEditRelacionReduccion.setStyleSheet(default_style)
                widgets.lineEditOtroIndiceTrituradora.setStyleSheet(default_style)
                widgets.lineEditPotenciaTrituradora.setStyleSheet(default_style)
                self.limpiarMandibula()
    def inhabilitar_conos(self): 
        widgets = self.ui 
        combox = self.sender()
        comboName = combox.objectName()

        if comboName == 'comboBox_3':
            if widgets.comboBox_3.currentText() == 'General': 
                widgets.lineEditSizeAlimento_2.setEnabled(True)
                widgets.lineEditSizeProducto_2.setEnabled(True)
                widgets.lineEditSizeMayor_2.setEnabled(True)
                widgets.lineEditSetCono.setEnabled(True)
                widgets.lineEditGape_2.setEnabled(True)
                widgets.lineEditDiametroBowl.setEnabled(True)
                widgets.lineEditDensidadAlimento_2.setEnabled(True)
                widgets.lineEditLminCono.setEnabled(True)
                widgets.lineEditLmax.setEnabled(True)
                widgets.lineEditFactorK.setEnabled(True)
                widgets.lineEditRelacionR.setEnabled(True)
                widgets.lineEditCapacidadCono.setEnabled(True)
                widgets.lineEditOtroIndiceCono.setEnabled(True)
                widgets.lineEditPotenciaCono.setEnabled(True)

                default_style = "QLineEdit { }"
                light_gray_style = "background-color: lightgray;"    

                widgets.lineEditSizeAlimento_2.setStyleSheet(default_style)
                widgets.lineEditSizeProducto_2.setStyleSheet(default_style)
                widgets.lineEditSetCono.setStyleSheet(default_style)
                widgets.lineEditSizeMayor_2.setStyleSheet(default_style)
                widgets.lineEditGape_2.setStyleSheet(default_style)
                widgets.lineEditDiametroBowl.setStyleSheet(default_style)
                widgets.lineEditDensidadAlimento_2.setStyleSheet(default_style)
                widgets.lineEditLminCono.setStyleSheet(default_style)
                widgets.lineEditLmax.setStyleSheet(default_style)
                widgets.lineEditFactorK.setStyleSheet(default_style)
                widgets.lineEditRelacionR.setStyleSheet(default_style)
                widgets.lineEditCapacidadCono.setStyleSheet(default_style)
                widgets.lineEditOtroIndiceCono.setStyleSheet(default_style)
                widgets.lineEditPotenciaCono.setStyleSheet(default_style)
                self.limpiarConos()

            elif  widgets.comboBox_3.currentText() == 'Bowl Diameter': 
                widgets.lineEditSizeAlimento_2.setEnabled(False) 
                widgets.lineEditSizeProducto_2.setEnabled(False)
                widgets.lineEditSizeMayor_2.setEnabled(True) #y
                widgets.lineEditSetCono.setEnabled(True) #y
                widgets.lineEditGape_2.setEnabled(True) #y
                widgets.lineEditDiametroBowl.setEnabled(True) #y
                widgets.lineEditDensidadAlimento_2.setEnabled(False) 
                widgets.lineEditLminCono.setEnabled(True) #y
                widgets.lineEditLmax.setEnabled(True)  #y
                widgets.lineEditFactorK.setEnabled(True) #y
                widgets.lineEditRelacionR.setEnabled(True) #y
                widgets.lineEditCapacidadCono.setEnabled(True) #y
                widgets.lineEditOtroIndiceCono.setEnabled(True) #y
                widgets.lineEditPotenciaCono.setEnabled(False)

                default_style = "QLineEdit { }"
                light_gray_style = "background-color: lightgray;"  

                widgets.lineEditSizeAlimento_2.setStyleSheet(light_gray_style) 
                widgets.lineEditSizeProducto_2.setStyleSheet(light_gray_style) 
                widgets.lineEditSizeMayor_2.setStyleSheet(default_style)  #y
                widgets.lineEditSetCono.setStyleSheet(default_style)  #y
                widgets.lineEditGape_2.setStyleSheet(default_style)  #y
                widgets.lineEditDiametroBowl.setStyleSheet(default_style)  #y
                widgets.lineEditDensidadAlimento_2.setStyleSheet(light_gray_style)  
                widgets.lineEditLminCono.setStyleSheet(default_style) #y
                widgets.lineEditLmax.setStyleSheet(default_style)  #y
                widgets.lineEditFactorK.setStyleSheet(default_style) #y
                widgets.lineEditRelacionR.setStyleSheet(default_style) #y
                widgets.lineEditCapacidadCono.setStyleSheet(default_style) #y
                widgets.lineEditOtroIndiceCono.setStyleSheet(default_style) #y
                widgets.lineEditPotenciaCono.setStyleSheet(light_gray_style) 
                self.limpiarConos()

            elif widgets.comboBox_3.currentText() == 'Mill Capacity ': 
                widgets.lineEditSizeAlimento_2.setEnabled(False) 
                widgets.lineEditSizeProducto_2.setEnabled(False)
                widgets.lineEditSizeMayor_2.setEnabled(True) #y
                widgets.lineEditSetCono.setEnabled(True) #y
                widgets.lineEditGape_2.setEnabled(True) #y
                widgets.lineEditDiametroBowl.setEnabled(True) #y
                widgets.lineEditDensidadAlimento_2.setEnabled(False) 
                widgets.lineEditLminCono.setEnabled(True) #y
                widgets.lineEditLmax.setEnabled(True)  #y
                widgets.lineEditFactorK.setEnabled(True) #y
                widgets.lineEditRelacionR.setEnabled(True) #y
                widgets.lineEditCapacidadCono.setEnabled(True) #y
                widgets.lineEditOtroIndiceCono.setEnabled(True) #y
                widgets.lineEditPotenciaCono.setEnabled(False)

                default_style = "QLineEdit { }"
                light_gray_style = "background-color: lightgray;"  

                widgets.lineEditSizeAlimento_2.setStyleSheet(light_gray_style) 
                widgets.lineEditSizeProducto_2.setStyleSheet(light_gray_style) 
                widgets.lineEditSizeMayor_2.setStyleSheet(default_style)  #y
                widgets.lineEditSetCono.setStyleSheet(default_style)  #y
                widgets.lineEditGape_2.setStyleSheet(default_style)  #y
                widgets.lineEditDiametroBowl.setStyleSheet(default_style)  #y
                widgets.lineEditDensidadAlimento_2.setStyleSheet(light_gray_style)  
                widgets.lineEditLminCono.setStyleSheet(default_style) #y
                widgets.lineEditLmax.setStyleSheet(default_style)  #y
                widgets.lineEditFactorK.setStyleSheet(default_style) #y
                widgets.lineEditRelacionR.setStyleSheet(default_style) #y
                widgets.lineEditCapacidadCono.setStyleSheet(default_style) #y
                widgets.lineEditOtroIndiceCono.setStyleSheet(default_style) #y
                widgets.lineEditPotenciaCono.setStyleSheet(light_gray_style)  
                self.limpiarConos()

            elif widgets.comboBox_3.currentText() == 'Mill Power': 
                widgets.lineEditSizeAlimento_2.setEnabled(True) #y
                widgets.lineEditSizeProducto_2.setEnabled(True) #y
                widgets.lineEditSizeMayor_2.setEnabled(False) 
                widgets.lineEditSetCono.setEnabled(False) 
                widgets.lineEditGape_2.setEnabled(False) 
                widgets.lineEditDiametroBowl.setEnabled(False)  
                widgets.lineEditDensidadAlimento_2.setEnabled(False) 
                widgets.lineEditLminCono.setEnabled(False) 
                widgets.lineEditLmax.setEnabled(False)  
                widgets.lineEditFactorK.setEnabled(False) 
                widgets.lineEditRelacionR.setEnabled(False) 
                widgets.lineEditCapacidadCono.setEnabled(True) #y
                widgets.lineEditOtroIndiceCono.setEnabled(True) #y
                widgets.lineEditPotenciaCono.setEnabled(True) #y

                default_style = "QLineEdit { }"
                light_gray_style = "background-color: lightgray;"  

                widgets.lineEditSizeAlimento_2.setStyleSheet(default_style) #y
                widgets.lineEditSizeProducto_2.setStyleSheet(default_style) #y
                widgets.lineEditSizeMayor_2.setStyleSheet(light_gray_style) 
                widgets.lineEditSetCono.setStyleSheet(light_gray_style) 
                widgets.lineEditGape_2.setStyleSheet(light_gray_style) 
                widgets.lineEditDiametroBowl.setStyleSheet(light_gray_style)  
                widgets.lineEditDensidadAlimento_2.setStyleSheet(light_gray_style) 
                widgets.lineEditLminCono.setStyleSheet(light_gray_style) 
                widgets.lineEditLmax.setStyleSheet(light_gray_style) 
                widgets.lineEditFactorK.setStyleSheet(light_gray_style) 
                widgets.lineEditRelacionR.setStyleSheet(light_gray_style) 
                widgets.lineEditCapacidadCono.setStyleSheet(default_style) #y
                widgets.lineEditOtroIndiceCono.setStyleSheet(default_style) #y
                widgets.lineEditPotenciaCono.setStyleSheet(default_style)#y
                self.limpiarConos()

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
