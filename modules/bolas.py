#1. Importar los widgets y demás 
from modules import *
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
class Bolas(QMainWindow):

    def calcular_bolas(self): 
        widgets = self.ui 

        # Recuperación de valores ingresados por el usuario 
        tamañoAlimento = widgets.lineEditSizeAlimento.text()
        tamañoProducto = widgets.lineEditSizeProducto.text()
        densidadAlimento = widgets.lineEditDensidadAlimento.text()
        densidadBolas = widgets.lineEditDensidadBolas.text()
        frecuenciaMolienda = widgets.lineEditFrecuenciaMolienda_2.text()
        diametroMolino = widgets.lineEditDiametroMolino.text()
        porosidad = widgets.lineEditPorosidadLecho.text()
        masaRocas = widgets.lineEditMasaRocas.text()
        masaBolas = widgets.lineEditMasaBolas.text()
        numeroLevantadores = widgets.lineEditNumeroLevantadores.text()
        fraccionRocas = widgets.lineEditFraccionRocas.text()
        fraccionBolas = widgets.lineEditFraccionBolas.text()
        frecuenciaCritica = widgets.lineEditFrecuenciaCritica_2.text()
        fraccionFrecuencia = widgets.lineEditFraccionFrecuenciaC.text()
        indiceAbrasion = widgets.lineEditIndiceAbrasion.text()
        indiceBond = widgets.lineEditIndiceBond.text()
        cf = widgets.lineEditFactorCorrecionCapacidad.text()
        desgasteBolas = widgets.lineEditDesgasteBolas.text()
        capacidad = widgets.lineEditCapacidadMolino.text()
        potencia = widgets.lineEditPotenciaMolino.text()
        ancho = widgets.lineEditLongitudMolino.text()
        k = widgets.lineEditConstanteMolino.text()
        diametroBolas = widgets.lineEditSizeBolas.text()

        # Creación de variables simbolicas 
        if (tamañoAlimento == ''): 
            tamañoAlimento = sp.Symbol('tamañoAlimento')

        else: 
            tamañoAlimento = float(tamañoAlimento)

        if (tamañoProducto == ''): 
            tamañoProducto = sp.Symbol('tamañoProducto')

        else: 
            tamañoProducto = float(tamañoProducto)

        if (densidadAlimento == ''):
            densidadAlimento = sp.Symbol('densidadAlimento')

        else: 
            densidadAlimento = float(densidadAlimento)

        if (densidadBolas == ''): 
            densidadBolas = sp.Symbol('densidadBolas')

        else: 
            densidadBolas = float(densidadBolas)

        if (frecuenciaMolienda == ''): 
            frecuenciaMolienda = sp.Symbol('frecuenciaMolienda')

        else: 
            frecuenciaMolienda = float(frecuenciaMolienda)

        if (diametroMolino == ''): 
            diametroMolino = sp.Symbol('diametroMolino')

        else: 
            diametroMolino = float(diametroMolino)

        if (porosidad == ''): 
            porosidad = sp.Symbol('porosidad')

        else: 
            porosidad = float(porosidad)

        if (masaRocas == ''): 
            masaRocas = sp.Symbol('masaRocas')

        else: 
            masaRocas = float(masaRocas)

        if (masaBolas == ''): 
            masaBolas = sp.Symbol('masaBolas')

        else: 
            masaBolas = float(masaBolas)

        if (numeroLevantadores == ''): 
            numeroLevantadores = sp.Symbol('numeroLevantadores')

        else: 
            numeroLevantadores = float(numeroLevantadores)

        if (fraccionRocas == ''): 
            fraccionRocas = sp.Symbol('fraccionRocas')

        else: 
            fraccionRocas = float(fraccionRocas)

        if (fraccionBolas == ''): 
            fraccionBolas = sp.Symbol('fraccionBolas')

        else: 
            fraccionBolas = float(fraccionBolas)

        if (frecuenciaCritica == ''): 
            frecuenciaCritica = sp.Symbol('frecuenciaCritica')

        else: 
            frecuenciaCritica = float(frecuenciaCritica)

        if (indiceAbrasion == ''): 
            indiceAbrasion = sp.Symbol('indiceAbrasion')

        else: 
            indiceAbrasion = float(indiceAbrasion)

        if (indiceBond == ''):
            indiceBond = sp.Symbol('indiceBond')

        else: 
            indiceBond = float(indiceBond)

        if (cf == ''): 
            cf = sp.Symbol('cf')

        else: 
            cf = float(cf)

        if (desgasteBolas == ''):
            desgasteBolas = sp.Symbol('desgasteBolas')

        else: 
            desgasteBolas = float(desgasteBolas)

        if (capacidad == ''):
            capacidad = sp.Symbol('capacidad')

        else: 
            capacidad = float(capacidad)

        if (potencia == ''): 
            potencia = sp.Symbol('potencia')

        else: 
            potencia = float(potencia)

        if (ancho == ''):
            ancho = sp.Symbol('ancho')

        else:
            ancho = float(ancho)

        if (k == ''): 
            k = sp.Symbol('k')
        
        else: 
            k = float(k)

        if (fraccionFrecuencia == ''): 
            fraccionFrecuencia = sp.Symbol('fraccionFrecuencia')

        else: 
            fraccionFrecuencia = float(fraccionFrecuencia)

        if (diametroBolas == ''): 
            diametroBolas = sp.Symbol('diametroBolas')

        else: 
            diametroBolas = float(diametroBolas)

        
        # Ecuación #1: Densidad de bolas
        vars_eq1 = [densidadBolas, densidadAlimento]
        vars_des1 = []

        for i in vars_eq1: 
            if isinstance(i, sp.core.symbol.Symbol):
                vars_des1.append(i)

        ecuacion1 = str(((0.016*densidadAlimento**2 + 20*densidadAlimento)**0.5 - 0.4*densidadAlimento) - densidadBolas)
        ecSimpeada1 = sp.parse_expr(ecuacion1)      

        if len(vars_des1) == 1: 
            sln1 = sp.solve((ecSimpeada1), vars_des1[0])
            
            if vars_des1[0] == densidadBolas: 
                widgets.lineEditDensidadBolas.setText(str(round(sln1[0], 4)))
                densidadBolas = sln1[0]

            elif vars_des1[0] == densidadAlimento: 
                widgets.lineEditDensidadAlimento.setText(str(round(sln1[0],4)))
                densidadAlimento = sln1[0]

        # Ecuación #2: Numero de levantadores. 
        vars_eq2 = [numeroLevantadores, diametroMolino]
        vars_des2 = []

        for i in vars_eq2: 
            if isinstance(i, sp.core.symbol.Symbol):
                vars_des2.append(i)

        ecuacion2 = str(3.3*pi*diametroMolino - numeroLevantadores)
        ecSimpeada2 = sp.parse_expr(ecuacion2)      

        if len(vars_des2) == 1: 
            sln2 = sp.solve((ecSimpeada2), vars_des2[0])
            
            if vars_des2[0] == numeroLevantadores: 
                widgets.lineEditNumeroLevantadores.setText(str(round(sln2[0], 4)))
                numeroLevantadores = sln2[0]

            elif vars_des2[0] == diametroMolino: 
                widgets.lineEditDiametroMolino.setText(str(round(sln2[0],4)))
                diametroMolino = sln2[0]   

        # Ecuación #3: Fracción ocupara por las rocas
        vars_eq3 = [masaRocas, densidadAlimento, diametroMolino, ancho, fraccionRocas, porosidad]
        vars_des3 = []

        for i in vars_eq3: 
            if isinstance(i, sp.core.symbol.Symbol):
                vars_des3.append(i)

        ecuacion3 = str(((masaRocas/densidadAlimento)/(pi*(diametroMolino/2)**2*ancho))*(1/(1-porosidad)) - fraccionRocas)
        ecSimpeada3 = sp.parse_expr(ecuacion3)  

        if len(vars_des3) == 1: 
            sln3 = sp.solve((ecSimpeada3), vars_des3[0])
            
            if vars_des3[0] == masaRocas: 
                widgets.lineEditMasaRocas.setText(str(round(sln3[0], 4)))
                masaRocas = sln3[0]

            elif vars_des3[0] == densidadAlimento: 
                widgets.lineEditDensidadAlimento.setText(str(round(sln3[0], 4))) 
                densidadAlimento = sln3[0]

            elif vars_des3[0] == diametroMolino: 
                widgets.lineEditDiametroMolino.setText(str(round(sln3[0], 4))) 
                diametroMolino = sln3[0]

            elif vars_des3[0] == ancho: 
                widgets.lineEditLongitudMolino.setText(str(round(sln3[0], 4))) 
                ancho = sln3[0]

            elif vars_des3[0] == fraccionRocas: 
                widgets.lineEditFraccionRocas.setText(str(round(sln3[0], 4))) 
                fraccionRocas = sln3[0]

            elif vars_des3[0] == porosidad: 
                widgets.lineEditPorosidadLecho.setText(str(round(sln3[0], 4))) 
                porosidad = sln3[0]

        # Ecuación #4: Fracción ocupada por las bolas
        vars_eq4 = [masaBolas, densidadBolas, diametroMolino, fraccionBolas, porosidad, ancho]
        vars_des4 = []

        for i in vars_eq4: 
            if isinstance(i, sp.core.symbol.Symbol):
                vars_des4.append(i)

        ecuacion4 = str(((masaBolas/densidadBolas)/(pi*(diametroMolino/2)**2*ancho))*(1/(1-porosidad)) - fraccionBolas)
        ecSimpeada4 = sp.parse_expr(ecuacion4)  

        if len(vars_des4) == 1: 
            sln4 = sp.solve((ecSimpeada4), vars_des4[0])
            
            if vars_des4[0] == masaBolas: 
                widgets.lineEditMasaBolas.setText(str(round(sln4[0], 4)))
                masaBolas = sln4[0]

            elif vars_des4[0] == densidadBolas: 
                widgets.lineEditDensidadBolas.setText(str(round(sln4[0], 4))) 
                densidadBolas = sln4[0]

            elif vars_des4[0] == diametroMolino: 
                widgets.lineEditDiametroMolino.setText(str(round(sln4[0], 4))) 
                diametroMolino = sln4[0]

            elif vars_des4[0] == fraccionBolas: 
                widgets.lineEditFraccionBolas.setText(str(round(sln4[0], 4))) 
                fraccionBolas = sln4[0]

            elif vars_des4[0] == porosidad: 
                widgets.lineEditPorosidadLecho.setText(str(round(sln4[0], 4))) 
                porosidad = sln4[0]

            elif vars_des4[0] == ancho: 
                widgets.lineEditLongitudMolino.setText(str(round(sln4[0], 4))) 
                ancho = sln4[0]

        # Ecuación 5: Diametro bolas
        vars_eq5 = [tamañoAlimento, k, indiceBond, fraccionFrecuencia, diametroMolino, densidadAlimento, diametroBolas]
        vars_des5 = []

        for i in vars_eq5: 
            if isinstance(i, sp.core.symbol.Symbol):
                vars_des5.append(i)

        ecuacion5 = str((25.4*((tamañoAlimento/k)**0.5)*((densidadAlimento*indiceBond)/(fraccionFrecuencia*(3.281*diametroMolino)**0.5))**0.33) - diametroBolas)
        ecSimpeada5 = sp.parse_expr(ecuacion5)  

        if len(vars_des5) == 1: 
            sln5 = sp.solve((ecSimpeada5), vars_des5[0])

            if vars_des5[0] == tamañoAlimento: 
                widgets.lineEditSizeAlimento.setText(str(round(sln5[0], 4)))
                tamañoAlimento = sln5[0]

            elif vars_des5[0] == k: 
                widgets.lineEditConstanteMolino.setText(str(round(sln5[0], 4))) 
                k = sln5[0]

            elif vars_des5[0] == indiceBond: 
                widgets.lineEditIndiceBond.setText(str(round(sln5[0], 4))) 
                indiceBond = sln5[0]

            elif vars_des5[0] == fraccionFrecuencia: 
                widgets.lineEditFraccionFrecuenciaC.setText(str(round(sln5[0], 4))) 
                fraccionFrecuencia = sln5[0]

            elif vars_des5[0] == diametroMolino: 
                widgets.lineEditDiametroMolino.setText(str(round(sln5[0], 4))) 
                diametroMolino = sln5[0]

            elif vars_des5[0] == densidadAlimento: 
                widgets.lineEditDensidadAlimento.setText(str(round(sln5[0], 4))) 
                densidadAlimento = sln5[0]

            elif vars_des5[0] == diametroBolas: 
                widgets.lineEditSizeBolas.setText(str(round(sln5[0]*(1/1000), 4))) 
                diametroBolas = sln5[0]

        # Ecuación #6: Frecuencia crítica 
        vars_eq6 = [frecuenciaCritica, diametroMolino, diametroBolas]
        vars_des6 = []

        for i in vars_eq6: 
            if isinstance(i, sp.core.symbol.Symbol):
                vars_des6.append(i)

        ecuacion6 = str(42.3/(sp.sqrt(diametroMolino - diametroBolas)) - frecuenciaCritica)
        ecSimpeada6 = sp.parse_expr(ecuacion6)

        if len(vars_des6) == 1: 
            sln6 = sp.solve((ecSimpeada6), vars_des6[0])

            if vars_des6[0] == frecuenciaCritica: 
                widgets.lineEditFrecuenciaCritica_2.setText(str(round(sln6[0], 4)))
                frecuenciaCritica = sln6[0]

            elif vars_des6[0] == diametroMolino: 
                widgets.lineEditDiametroMolino.setText(str(round(sln6[0], 4))) 
                diametroMolino = sln6[0]

            elif vars_des6[0] == diametroBolas: 
                widgets.lineEditSizeBolas.setText(str(round(sln6[0], 4))) 
                diametroBolas = sln6[0]

        # Ecuación 7: Fracción frecuencia crítica (Pendiente): 
        vars_eq7 = [frecuenciaCritica, frecuenciaMolienda, fraccionFrecuencia]
        vars_des7 = []

        for i in vars_eq7: 
            if isinstance(i, sp.core.symbol.Symbol):
                vars_des7.append(i)

        ecuacion7 = str(frecuenciaMolienda/frecuenciaCritica - fraccionFrecuencia)
        ecSimpeada7 = sp.parse_expr(ecuacion7)

        if len(vars_des7) == 1: 
            sln7 = sp.solve((ecSimpeada7), vars_des7[0])
            
            if vars_des7[0] == frecuenciaCritica: 
                widgets.lineEditFrecuenciaCritica_2.setText(str(round(sln7[0], 4)))
                frecuenciaCritica = sln7[0]
                
            elif vars_des7[0] == frecuenciaMolienda: 
                widgets.lineEditFrecuenciaMolienda_2.setText(str(round(sln7[0], 4))) 
                frecuenciaMolienda = sln7[0]

            elif vars_des7[0] == fraccionFrecuencia: 
                widgets.lineEditFraccionFrecuenciaC.setText(str(round(sln7[0], 4))) 
                fraccionFrecuencia = sln7[0]
            

        # Ecuación 9: Desgaste de las bolas
        if (widgets.comboBoxTipoMolienda.currentText() == "Dry grinding"): 
            vars_eq9 = [indiceAbrasion, desgasteBolas]
            vars_des9 = []
            
            for i in vars_eq9: 
                if isinstance(i, sp.core.symbol.Symbol):
                    vars_des9.append(i)
            
            ecuacion9 = str(0.023*indiceAbrasion - desgasteBolas)
            ecSimpeada9 = sp.parse_expr(ecuacion9)

            if len(vars_des9) == 1: 
                sln9 = sp.solve((ecSimpeada9), vars_des9[0])
                
                if vars_des9[0] == indiceAbrasion: 
                    widgets.lineEditIndiceAbrasion.setText(str(round(sln9[0], 4)))
                    indiceAbrasion = sln9[0]

                elif vars_des9[0] == desgasteBolas: 
                    widgets.lineEditDesgasteBolas.setText(str(round(sln9[0], 4)))
                    desgasteBolas = sln9[0]
                
        elif (widgets.comboBoxTipoMolienda.currentText() == "Wet grinding"): 
            vars_eq9_1 = [indiceAbrasion, desgasteBolas]
            vars_des9_1 = []
            
            for i in vars_eq9_1: 
                if isinstance(i, sp.core.symbol.Symbol):
                    vars_des9_1.append(i)
            
            ecuacion9_1 = str(0.16*(indiceAbrasion - 0.015)**0.33 - desgasteBolas)
            ecSimpeada9_1 = sp.parse_expr(ecuacion9_1)

            if len(vars_des9_1) == 1: 
                sln9_1 = sp.solve((ecSimpeada9_1), vars_des9_1[0])
                
                if vars_des9_1[0] == indiceAbrasion: 
                    widgets.lineEditIndiceAbrasion.setText(str(round(sln9_1[0], 4)))
                    indiceAbrasion = sln9_1[0]

                elif vars_des9_1[0] == desgasteBolas: 
                    widgets.lineEditDesgasteBolas.setText(str(round(sln9_1[0], 4)))
                    desgasteBolas = sln9_1[0]


        # Capacidad del molino (Por realizar): 
        if (diametroMolino <= 3.81): 
            vars_eq8 = [diametroMolino, ancho, densidadBolas, fraccionBolas, fraccionFrecuencia, indiceBond, tamañoProducto, tamañoAlimento, cf, capacidad]
            vars_des8 = []

            for i in vars_eq8: 
                if isinstance(i, sp.core.symbol.Symbol):
                    vars_des8.append(i)

            ecuacion8 = str((((6.13*(diametroMolino**3.5))*(ancho/diametroMolino)*densidadBolas*(fraccionBolas - 0.937*(fraccionBolas**2))*(fraccionFrecuencia - (0.1*fraccionFrecuencia)/(2**(9-10*fraccionFrecuencia))))/(cf*indiceBond*10*(1/sqrt(tamañoProducto) - 1/sqrt(tamañoAlimento)))) - capacidad)
            ecSimpeada8 = sp.parse_expr(ecuacion8)
            
            if len(vars_des8) == 1: 
                sln8 = sp.solve((ecSimpeada8), (vars_des8[0]))

                if (vars_des8[0] == diametroMolino): 
                    widgets.lineEditDiametroMolino.setText(str(round(sln8[0], 4)))
                    diametroMolino = sln8[0]

                elif (vars_des8[0] == ancho): 
                    widgets.lineEditLongitudMolino.setText(str(round(sln8[0], 4)))
                    ancho = sln8[0]

                elif (vars_des8[0] == densidadBolas): 
                    widgets.lineEditDensidadBolas.setText(str(round(sln8[0], 4)))
                    densidadBolas = sln8[0]      

                elif (vars_des8[0] == fraccionBolas): 
                    widgets.lineEditFraccionBolas.setText(str(round(sln8[0], 4)))
                    fraccionBolas = sln8[0]

                elif (vars_des8[0] == fraccionFrecuencia): 
                    widgets.lineEditFraccionFrecuenciaC.setText(str(round(sln8[0], 4)))
                    fraccionFrecuencia = sln8[0]

                elif (vars_des8[0] == indiceBond): 
                    widgets.lineEditIndiceBond.setText(str(round(sln8[0], 4)))
                    indiceBond = sln8[0]

                elif (vars_des8[0] == tamañoProducto): 
                    widgets.lineEditSizeProducto.setText(str(round(sln8[0], 4)))
                    tamañoProducto = sln8[0]

                elif (vars_des8[0] == tamañoAlimento): 
                    widgets.lineEditSizeAlimento.setText(str(round(sln8[0], 4)))
                    tamañoAlimento = sln8[0]

                elif (vars_des8[0] == cf): 
                    widgets.lineEditFactorCorrecionCapacidad.setText(str(round(sln8[0], 4)))
                    cf = sln8[0]

                elif (vars_des8[0] == capacidad): 
                    widgets.lineEditCapacidadMolino.setText(str(round(sln8[0], 4)))
                    capacidad = sln8[0]


        elif (diametroMolino > 3.81): 
            vars_eq8_1 = [diametroMolino, ancho, densidadBolas, fraccionBolas, fraccionFrecuencia, indiceBond, tamañoProducto, tamañoAlimento, cf, capacidad]
            vars_des8_1 = []

            for i in vars_eq8_1: 
                if isinstance(i, sp.core.symbol.Symbol):
                    vars_des8_1.append(i)

            ecuacion8_1 = str((((8.01*(diametroMolino**3.3))*(ancho/diametroMolino)*densidadBolas*(fraccionBolas - 0.937*(fraccionBolas**2))*(fraccionFrecuencia - (0.1*fraccionFrecuencia)/(2**(9-10*fraccionFrecuencia))))/(cf*indiceBond*10*(1/sqrt(tamañoProducto) - 1/sqrt(tamañoAlimento)))) - capacidad)
            ecSimpeada8_1 = sp.parse_expr(ecuacion8)
            
            if len(vars_des8) == 1: 
                sln8_1 = sp.solve((ecSimpeada8_1), (vars_des8_1[0]))

                if (vars_des8_1[0] == diametroMolino): 
                    widgets.lineEditDiametroMolino.setText(str(round(sln8_1[0], 4)))
                    diametroMolino = sln8_1[0]

                elif (vars_des8_1[0] == ancho): 
                    widgets.lineEditLongitudMolino.setText(str(round(sln8_1[0], 4)))
                    ancho = sln8_1[0]

                elif (vars_des8_1[0] == densidadBolas): 
                    widgets.lineEditDensidadBolas.setText(str(round(sln8_1[0], 4)))
                    densidadBolas = sln8_1[0]      

                elif (vars_des8_1[0] == fraccionBolas): 
                    widgets.lineEditFraccionBolas.setText(str(round(sln8_1[0], 4)))
                    fraccionBolas = sln8_1[0]

                elif (vars_des8_1[0] == fraccionFrecuencia): 
                    widgets.lineEditFraccionFrecuenciaC.setText(str(round(sln8_1[0], 4)))
                    fraccionFrecuencia = sln8_1[0]

                elif (vars_des8_1[0] == indiceBond): 
                    widgets.lineEditIndiceBond.setText(str(round(sln8_1[0], 4)))
                    indiceBond = sln8_1[0]

                elif (vars_des8_1[0] == tamañoProducto): 
                    widgets.lineEditSizeProducto.setText(str(round(sln8_1[0], 4)))
                    tamañoProducto = sln8_1[0]

                elif (vars_des8_1[0] == tamañoAlimento): 
                    widgets.lineEditSizeAlimento.setText(str(round(sln8_1[0], 4)))
                    tamañoAlimento = sln8_1[0]

                elif (vars_des8_1[0] == cf): 
                    widgets.lineEditFactorCorrecionCapacidad.setText(str(round(sln8_1[0], 4)))
                    cf = sln8_1[0]

                elif (vars_des8_1[0] == capacidad): 
                    widgets.lineEditCapacidadMolino.setText(str(round(sln8_1[0], 4)))
                    capacidad = sln8_1[0] 
            
        # Potencia del molino 
        vars_eq10 = [potencia, capacidad, tamañoAlimento, tamañoProducto, indiceBond]
        vars_des10 = []

        for i in vars_eq10: 
            if isinstance(i, sp.core.symbol.Symbol):
                vars_des10.append(i)

        ecuacion10 = str(10*indiceBond*(1/sp.sqrt(tamañoProducto) - 1/sp.sqrt(tamañoAlimento))*capacidad - potencia)
        ecSimpeada10 = sp.parse_expr(ecuacion10)

        if len(vars_des10) == 1: 
            sln10 = sp.solve((ecSimpeada10), vars_des10[0])
            
            if vars_des10[0] == potencia: 
                widgets.lineEditPotenciaMolino.setText(str(round(sln10[0], 4)))
                potencia = sln10[0]

            elif vars_des10[0] == capacidad: 
                widgets.lineEditCapacidadMolino.setText(str(round(sln10[0], 4))) 
                capacidad = sln10[0]

            elif vars_des10[0] == tamañoAlimento: 
                widgets.lineEditSizeAlimento.setText(str(round(sln10[0], 4))) 
                tamañoAlimento = sln10[0]

            elif vars_des10[0] == tamañoProducto: 
                widgets.lineEditSizeProducto.setText(str(round(sln10[0], 4))) 
                tamañoProducto = sln10[0]

            elif vars_des10[0] == indiceBond: 
                widgets.lineEditIndiceBond.setText(str(round(sln10[0], 4))) 
                indiceBond = sln10[0]

    def limpiar_bolas(self): 
        widgets = self.ui

        lineEdit = [
            widgets.lineEditSizeAlimento, 
            widgets.lineEditSizeProducto, 
            widgets.lineEditDensidadAlimento,
            widgets.lineEditDensidadBolas, 
            widgets.lineEditDiametroMolino, 
            widgets.lineEditLongitudMolino, 
            widgets.lineEditPorosidadLecho, 
            widgets.lineEditMasaRocas, 
            widgets.lineEditMasaBolas, 
            widgets.lineEditNumeroLevantadores, 
            widgets.lineEditSizeBolas, 
            widgets.lineEditFraccionRocas,
            widgets.lineEditFraccionBolas, 
            widgets.lineEditConstanteMolino, 
            widgets.lineEditFrecuenciaMolienda_2,
            widgets.lineEditFrecuenciaCritica_2, 
            widgets.lineEditFraccionFrecuenciaC,
            widgets.lineEditIndiceAbrasion, 
            widgets.lineEditIndiceBond, 
            widgets.lineEditFactorCorrecionCapacidad,
            widgets.lineEditDesgasteBolas, 
            widgets.lineEditCapacidadMolino, 
            widgets.lineEditPotenciaMolino
        ]

        for i in lineEdit:
            i.clear()

        

            