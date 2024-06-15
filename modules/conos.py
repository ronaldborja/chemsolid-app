#1. Importar los widgets y demás 
from widgets import *  
from main import * 
from scipy import *
import numpy as np 
import sympy as sp 
import pandas as pd
from fractions import Fraction
from scipy.interpolate import interp1d
import math
from sympy import log, cos, pi, sqrt


# Clase con los calculos de bandas
class Cono(QMainWindow):

    def calcular_cono(self): 
        widgets = self.ui 

        # Recuperación de valores ingresados por el usuario 
        tamañoAlimento = widgets.lineEditSizeAlimento_2.text()
        tamañoProducto = widgets.lineEditSizeProducto_2.text()
        tamañoMayor = widgets.lineEditSizeMayor_2.text()
        set = widgets.lineEditSetCono.text()
        gape = widgets.lineEditGape_2.text()
        diametro = widgets.lineEditDiametroBowl.text()
        densidad = widgets.lineEditDensidadAlimento_2.text()
        Lmin = widgets.lineEditLminCono.text()
        Lmax = widgets.lineEditLmax.text()
        R = widgets.lineEditRelacionR.text()
        K = widgets.lineEditFactorK.text()
        capacidad = widgets.lineEditCapacidadCono.text()
        indiceBond = widgets.lineEditOtroIndiceCono.text()
        potencia = widgets.lineEditPotenciaCono.text()

        
        # Creación de variables simbolicas 
        if (tamañoAlimento == ''): 
            tamañoAlimento = sp.Symbol('tamañoAlimento')

        else: 
            tamañoAlimento = float(tamañoAlimento)

        if (tamañoProducto == ''): 
            tamañoProducto = sp.Symbol('tamañoProducto')

        else: 
            tamañoProducto = float(tamañoProducto)

        if (tamañoMayor == ''): 
            tamañoMayor = sp.Symbol('tamañoMayor')

        else:
            tamañoMayor = float(tamañoMayor)

        if (set == ''): 
            set = sp.Symbol('set')

        else: 
            set = float(set)

        if (gape == ''):
            gape = sp.Symbol('gape')

        else: 
            gape = float(gape)

        if (diametro == ''): 
            diametro = sp.Symbol('diametro')

        else: 
            diametro = float(diametro)

        if (densidad == ''):
            densidad = sp.Symbol('densidad')
        
        else: 
            densidad = float(densidad)
        
        if (Lmin == ''): 
            Lmin = sp.Symbol('Lmin')

        else: 
            Lmin = float(Lmin)

        if (Lmax == ''): 
            Lmax = sp.Symbol('Lmax')

        else: 
            Lmax = float(Lmax)

        if (R == ''): 
            R = sp.Symbol('R')

        else: 
            R = float(R)

        if (K == ''): 
            K = sp.Symbol('K')

        else: 
            K = float(K)

        if (capacidad == ''):
            capacidad = sp.Symbol('capacidad')

        else: 
            capacidad = float(capacidad)

        if (indiceBond == ''):
            indiceBond = sp.Symbol('indiceBond')

        else: 
            indiceBond = float(indiceBond)

        if (potencia == ''):
            potencia = sp.Symbol('potencia')

        else: 
            potencia = float(potencia)


        #Ecuación #1
        vars_eq1 = [gape, tamañoMayor]
        vars_des1 = []

        for i in vars_eq1: 
            if isinstance(i, sp.core.symbol.Symbol):
                vars_des1.append(i)

        ecuacion1 = str(1.1*tamañoMayor - gape)
        ecSimpeada1 = sp.parse_expr(ecuacion1) 

        if len(vars_des1) == 1: 
            sln1 = sp.solve((ecSimpeada1), vars_des1[0])
            
            if vars_des1[0] == gape: 
                widgets.lineEditGape_2.setText(str(round(sln1[0], 4)))
                gape = sln1[0]

            elif vars_des1[0] == tamañoMayor: 
                widgets.lineEditSizeMayor_2.setText(str(round(sln1[0],4)))
                tamañoMayor = sln1[0]

        # Ecuación #2: Relación de reducción 
        vars_eq2 = [gape, set, R]
        vars_des2 = []

        for i in vars_eq2: 
            if isinstance(i, sp.core.symbol.Symbol):
                vars_des2.append(i)

        ecuacion2 = str(gape/set - R)
        ecSimpeada2 = sp.parse_expr(ecuacion2) 

        if len(vars_des2) == 1: 
            sln2 = sp.solve((ecSimpeada2), vars_des2[0])
            
            if vars_des2[0] == gape: 
                widgets.lineEditGape_2.setText(str(round(sln2[0], 4)))
                gape = sln2[0]

            elif vars_des2[0] == set: 
                widgets.lineEditSetCono.setText(str(round(sln2[0],4)))
                set = sln2[0]

            elif vars_des2[0] == R: 
                widgets.lineEditRelacionR.setText(str(round(sln2[0],4)))
                R = sln2[0]
            

        # Capacidad del molino 
        vars_eq3 = [indiceBond, diametro, densidad, Lmin, Lmax, K, R, capacidad]
        vars_des3 = []

        for i in vars_eq3: 
            if isinstance(i, sp.core.symbol.Symbol):
                vars_des3.append(i)

        ecuacion3 = str((indiceBond*diametro*densidad*sp.sqrt(Lmax - Lmin)*(Lmax + Lmin)*K)/(2*sp.sqrt(R/(R-1))) - capacidad)
        ecSimpeada3 = sp.parse_expr(ecuacion3) 

        if len(vars_des3) == 1: 
            sln3 = sp.solve((ecSimpeada3), vars_des3[0])
            
            if vars_des3[0] == indiceBond: 
                widgets.lineEditOtroIndiceCono.setText(str(round(sln3[0], 4)))
                indiceBond = sln3[0]

            elif vars_des3[0] == diametro: 
                widgets.lineEditDiametroBowl.setText(str(round(sln3[0],4)))
                diametro = sln3[0]

            elif vars_des3[0] == densidad: 
                widgets.lineEditDensidadAlimento_2.setText(str(round(sln3[0],4)))
                densidad = sln3[0]

            elif vars_des3[0] == Lmin: 
                widgets.lineEditLminCono.setText(str(round(sln3[0],4)))
                Lmin = sln3[0]
            
            elif vars_des3[0] == Lmax: 
                widgets.lineEditLmax.setText(str(round(sln3[0],4)))
                Lmax = sln3[0]

            elif vars_des3[0] == K: 
                widgets.lineEditFactorK.setText(str(round(sln3[0],4)))
                K = sln3[0]

            elif vars_des3[0] == R: 
                widgets.lineEditRelacionR.setText(str(round(sln3[0],4)))
                R = sln3[0]

            elif vars_des3[0] == capacidad: 
                widgets.lineEditCapacidadCono.setText(str(round(sln3[0],4)))
                capacidad = sln3[0]

        # Potencia del molino
        vars_eq4 = [indiceBond, tamañoAlimento, tamañoProducto, capacidad, potencia]
        vars_des4 = []

        for i in vars_eq4: 
            if isinstance(i, sp.core.symbol.Symbol):
                vars_des4.append(i)

        ecuacion4 = str(indiceBond*capacidad*((sp.sqrt(tamañoAlimento) - sp.sqrt(tamañoProducto))/(sp.sqrt(tamañoAlimento)))*sp.sqrt(100/tamañoProducto) - potencia)
        ecSimpeada4 = sp.parse_expr(ecuacion4) 

        if len(vars_des4) == 1: 
            sln4 = sp.solve((ecSimpeada4), vars_des4[0])
            
            if vars_des4[0] == indiceBond: 
                widgets.lineEditOtroIndiceCono.setText(str(round(sln4[0], 4)))
                indiceBond = sln4[0]
         
            elif vars_des4[0] == tamañoAlimento: 
                widgets.lineEditSizeAlimento_2.setText(str(round(sln4[0], 4)))
                tamañoAlimento = sln4[0]

            elif vars_des4[0] == tamañoProducto: 
                widgets.lineEditSizeProducto_2.setText(str(round(sln4[0], 4)))
                tamañoProducto = sln4[0]

            elif vars_des4[0] == capacidad: 
                widgets.lineEditCapacidadCono.setText(str(round(sln4[0], 4)))
                capacidad = sln4[0]

            elif vars_des4[0] == potencia: 
                widgets.lineEditPotenciaCono.setText(str(round(sln4[0], 4)))
                potencia = sln4[0]

    def limpiar_conos(self): 
        widgets = self.ui

        lineEdit = [
            widgets.lineEditSizeAlimento_2, 
            widgets.lineEditSizeProducto_2,
            widgets.lineEditSizeMayor_2, 
            widgets.lineEditSetCono, 
            widgets.lineEditGape_2, 
            widgets.lineEditDiametroBowl, 
            widgets.lineEditDensidadAlimento_2,
            widgets.lineEditLminCono, 
            widgets.lineEditLmax,
            widgets.lineEditRelacionR,
            widgets.lineEditFactorK,
            widgets.lineEditCapacidadCono,
            widgets.lineEditOtroIndiceCono, 
            widgets.lineEditPotenciaCono 
        ]

        for i in lineEdit:
            i.clear()

    def innhabilitar_conos(self): 
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
