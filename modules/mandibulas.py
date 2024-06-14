# Clase para manejar trituradoras de mandibula 

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
from sympy import log, cos, pi


# Clase con los calculos de bandas
class Mandibula(QMainWindow):

    def calcular_mandibula(self): 
        widgets = self.ui 

        # Recuperamos los valores ingresados por el usuario: 
        tamañoParticulaMayor = widgets.lineEditSizeMayor.text()
        tamañoParticulaMenor = widgets.lineEditSizeMenor.text()
        gape = widgets.lineEditGape.text()
        set_mand = widgets.lineEditSet.text()
        Lmin = widgets.lineEditLmin.text()
        densidadMaterial = widgets.lineEditDensidad.text()
        alturaVertical = widgets.lineEditAlturaTriturador.text()
        width = widgets.lineEditWidth.text()
        Lt = widgets.lineEditThrow.text()
        R = widgets.lineEditRelacionReduccion.text()
        vc = widgets.lineEditFrecuenciaCritica.text()
        capacidad = widgets.lineEditCapacidadTrituradora.text()
        Wi = widgets.lineEditOtroIndiceTrituradora.text()
        potencia = widgets.lineEditPotenciaTrituradora.text() 
        Throw = widgets.lineEditThrow.text()
        frecuencia = widgets.lineEditFrecuenciaMolienda.text()
        Qa = widgets.lineEditCapacidadReal.text()

        # Creación de variables simbolicas 

        # TamañoParticulaMayor
        if (tamañoParticulaMayor == ''): 
            tamañoParticulaMayor = sp.Symbol('tamañoParticulaMayor')

        else: 
            tamañoParticulaMayor = float(tamañoParticulaMayor)

        # TamañoParticulaMenor
        if (tamañoParticulaMenor == ''): 
            tamañoParticulaMenor = sp.Symbol('tamañoParticulaMenor')

        else: 
            tamañoParticulaMenor = float(tamañoParticulaMenor)

        # Gape
        if (gape == ''): 
            gape = sp.Symbol('gape')

        else:
            gape = float(gape)

        # Set
        if (set_mand == ''): 
            set_mand = sp.Symbol('set_mand')

        else: 
            set_mand = float(set_mand)

        # Lmin
        if (Lmin == ''): 
            Lmin = sp.Symbol('Lmin')

        else: 
            Lmin = float(Lmin)

        # Trhow 
        if (Throw == ''): 
            Throw = sp.Symbol('Throw')
        
        else: 
            Throw = float(Throw)

        # DensidadMaterial
        if (densidadMaterial == ''): 
            densidadMaterial = sp.Symbol('densidadMaterial')

        else: 
            densidadMaterial = float(densidadMaterial)

        # AlturaVertical
        if (alturaVertical == ''): 
            alturaVertical = sp.Symbol('alturaVertical')
        
        else: 
            alturaVertical = float(alturaVertical)

        #Width
        if (width == ''): 
            width = sp.Symbol('width')

        else: 
            width = float(width)

        # Lt
        if (Lt == ''): 
            Lt = sp.Symbol('Lt')

        else: 
            Lt = float(Lt)

        # Relación reducción
        if (R == ''): 
            R = sp.Symbol('R')

        else: 
            R = float(R)

        # Freq crítica
        if (vc == ''): 
            vc = sp.Symbol('vc')
        
        else: 
            vc = float(vc)

        # Capacidad
        if (capacidad == ''): 
            capacidad = sp.Symbol('capacidad')

        else: 
            capacidad = float(capacidad)

        # Indice Bond
        if (Wi == ''): 
            Wi = sp.Symbol('Wi')

        else: 
            Wi = float(Wi)

        # Potencia 
        if (potencia == ''): 
            potencia = sp.Symbol('potencia')

        else: 
            potencia = float(potencia)


        # Ecuaciones a resolver -> Tamaño de particula y gape 
        vars_eq1 = [tamañoParticulaMayor, gape]
        vars_des1 = []

        for i in vars_eq1: 
            if isinstance(i, sp.core.symbol.Symbol):
                vars_des1.append(i)

        ecuacion1 = str(0.9*gape - tamañoParticulaMayor)
        ecSimpeada1 = sp.parse_expr(ecuacion1) 

        if len(vars_des1) == 1: 
            sln1 = sp.solve((ecSimpeada1), vars_des1[0])
            
            if vars_des1[0] == gape: 
                widgets.lineEditGape.setText(str(round(sln1[0], 4)))
                gape = sln1[0]

            elif vars_des1[0] == tamañoParticulaMayor: 
                widgets.lineEditSizeMayor.setText(str(round(sln1[0],4)))
                tamañoParticulaMayor = sln1[0]

        # Ecuación #2: 
        vars_eq2 = [width, gape]
        vars_des2 = []

        for i in vars_eq2: 
            if isinstance(i, sp.core.symbol.Symbol):
                vars_des2.append(i)

        ecuacion2 = str(1.3*gape - width)
        ecSimpeada2 = sp.parse_expr(ecuacion2)

        if len(vars_des2) == 1: 
            sln2 = sp.solve((ecSimpeada2), vars_des2[0])

            if vars_des2[0] == gape: 
                widgets.lineEditGape.setText(str(round(sln2[0], 4)))
                gape = sln2[0]

            elif vars_des2[0] == width: 
                widgets.lineEditWidth.setText(str(round(sln2[0], 4)))
                width = sln2[0]
                
        # Ecuacion #3: 
        vars_eq3 = [alturaVertical, gape]
        vars_des3 = []

        for i in vars_eq3: 
            if isinstance(i, sp.core.symbol.Symbol):
                vars_des3.append(i)

        ecuacion3 = str(2*gape - alturaVertical)
        ecSimpeada3 = sp.parse_expr(ecuacion3)

        if len(vars_des3) == 1: 
            sln3 = sp.solve((ecSimpeada3), vars_des3[0])

            if vars_des3[0] == gape: 
                widgets.lineEditGape.setText(str(round(sln3[0], 4)))
                gape = sln3[0]

            elif vars_des3[0] == alturaVertical: 
                widgets.lineEditAlturaTriturador.setText(str(round(sln3[0], 4)))
                alturaVertical = sln3[0]

        # Ecuación #4 
        vars_eq4 = [Throw, gape]
        vars_des4 = []

        for i in vars_eq4: 
            if isinstance(i, sp.core.symbol.Symbol):
                vars_des4.append(i)

        ecuacion4 = str(0.0502*(gape**0.85) - Throw)
        ecSimpeada4 = sp.parse_expr(ecuacion4)

        if len(vars_des4) == 1: 
            sln4 = sp.solve((ecSimpeada4), vars_des4[0])

            if vars_des4[0] == gape: 
                widgets.lineEditGape.setText(str(round(sln4[0], 4)))
                gape = sln4[0]

            elif vars_des4[0] == Throw: 
                widgets.lineEditThrow.setText(str(round(sln4[0], 4)))   
                Throw = sln4[0]          

        # Ecuación #5: 
        vars_eq5 = [R, gape, set_mand]
        vars_des5 = []

        for i in vars_eq5: 
            if isinstance(i, sp.core.symbol.Symbol):
                vars_des5.append(i)

        ecuacion5 = str(gape/set_mand - R)
        ecSimpeada5 = sp.parse_expr(ecuacion5)

        if len(vars_des5) == 1: 
            sln5 = sp.solve((ecSimpeada5), vars_des5[0])

            if vars_des5[0] == gape: 
                widgets.lineEditGape.setText(str(round(sln5[0], 4)))
                gape = sln5[0]

            elif vars_des5[0] == set_mand: 
                widgets.lineEditSet.setText(str(round(sln5[0], 4)))
                set_mand = sln5[0]

            elif vars_des5[0] == R: 
                widgets.lineEditRelacionReduccion.setText(str(round(sln5[0], 4)))  
                R = sln5[0]

        # Ecuación #6. --> Frecuencia crítica 
        vars_eq6 = [Throw, R, vc]
        vars_des6 = [] 

        for i in vars_eq6: 
            if isinstance(i, sp.core.symbol.Symbol):
                vars_des6.append(i)

        ecuacion6 = str(((47/Throw**0.5)*((R-1)/R)**0.5) - vc)
        ecSimpeada6 = sp.parse_expr(ecuacion6)

        if len(vars_des6) == 1: 
            sln6 = sp.solve((ecSimpeada6), vars_des6[0])

            if vars_des6[0] == Throw: 
                widgets.lineEditThrow.setText(str(round(sln6[0], 4)))
                Throw = sln6[0]

            elif vars_des6[0] == R: 
                widgets.lineEditRelacionReduccion.setText(str(round(sln6[0], 4)))
                R = sln6[0]

            elif vars_des6[0] == vc: 
                widgets.lineEditFrecuenciaCritica.setText(str(round(sln6[0], 4)))  
                vc = sln6[0]    

        # Ecuación 7.  
        Dpromedio = (tamañoParticulaMenor + tamañoParticulaMayor)/2
        pK = (tamañoParticulaMayor - tamañoParticulaMenor)/Dpromedio
        
        if (pK <= 0.25):
            fpK = 0.4 

        else: 
            fpK = 0.9944*pK**3 - 2.9964*pK**2 + 3.0359*pK - 0.1884 


        vars_eq7 = [Throw, width, Lmin, R, densidadMaterial, capacidad]
        vars_des7 = [] 
        
        for i in vars_eq7: 
            if isinstance(i, sp.core.symbol.Symbol):
                vars_des7.append(i)

        ecuacion7 = str((2820*(Throw**0.5)*width*(2*Lmin + Throw)*(R/(R-1))**0.5*densidadMaterial*fpK)*(1/1000) - capacidad)
        ecSimpeada7 = sp.parse_expr(ecuacion7)

        if len(vars_des7) == 1: 
            sln7 = sp.solve((ecSimpeada7), vars_des7[0])

            if vars_des7[0] == Throw: 
                widgets.lineEditThrow.setText(str(round(sln7[0], 4)))
                Throw = sln7[0]

            elif vars_des7[0] == Lmin: 
                widgets.lineEditLmin.setText(str(round(sln7[0], 4)))
                Lmin = sln7[0]

            elif vars_des7[0] == R: 
                widgets.lineEditRelacionReduccion.setText(str(round(sln7[0], 4)))
                R = sln7[0]  

            elif vars_des7[0] == densidadMaterial: 
                widgets.lineEditDensidad.setText(str(round(sln7[0], 4)))
                densidadMaterial = sln7[0]

            elif vars_des7[0] == capacidad: 
                widgets.lineEditCapacidadTrituradora.setText(str(round(sln7[0], 4)))
                capacidad = sln7[0]

        frecuencia = float(frecuencia)

        if (frecuencia < vc): 
            Qa = capacidad*(frecuencia/vc)
            widgets.lineEditCapacidadReal.setText(str(round(Qa, 4)))

        else: 
            Qa = capacidad*(vc/frecuencia)
            widgets.lineEditCapacidadReal.setText(str(round(Qa, 4)))


        # Ecuación 8 
        vars_eq8 = [Wi, gape, Lmin, Throw, potencia]
        vars_des8 = []

        for i in vars_eq8: 
            if isinstance(i, sp.core.symbol.Symbol):
                vars_des8.append(i)

        ecuacion8 = str(0.01195*Wi*Qa*((gape)**0.5 - 1.054*(Lmin + Throw)**0.5)/((gape)**0.5*(Lmin + Throw)**0.5) - potencia)
        ecSimpeada8 = sp.parse_expr(ecuacion8) 

        if len(vars_des8) == 1: 
            sln8 = sp.solve((ecSimpeada8), vars_des8[0])

            if vars_des8[0] == Wi: 
                widgets.lineEditOtroIndiceTrituradora.setText(str(round(sln8[0], 4)))
                Wi = sln8[0]
            
            elif vars_des8[0] == Throw: 
                widgets.lineEditThrow.setText(str(round(sln8[0], 4)))
                Throw = sln8[0]

            elif vars_des8[0] == Lmin: 
                widgets.lineEditLmin.setText(str(round(sln8[0], 4)))
                Lmin = sln8[0]

            elif vars_des8[0] == gape: 
                widgets.lineEditGape.setText(str(round(sln8[0], 4)))
                gape = sln8[0]

            elif vars_des8[0] == potencia: 
                widgets.lineEditPotenciaTrituradora.setText(str(round(sln8[0], 4)))
                potencia = sln8[0]

    def limpiar_mandibulas(self): 
        widgets = self.ui

        lineEdit = [
            widgets.lineEditSizeMayor,
            widgets.lineEditSizeMenor,
            widgets.lineEditDensidad,
            widgets.lineEditLmin, 
            widgets.lineEditFrecuenciaMolienda,
            widgets.lineEditSet, 
            widgets.lineEditGape, 
            widgets.lineEditAlturaTriturador, 
            widgets.lineEditWidth, 
            widgets.lineEditThrow, 
            widgets.lineEditRelacionReduccion, 
            widgets.lineEditFrecuenciaCritica, 
            widgets.lineEditCapacidadTrituradora,
            widgets.lineEditCapacidadReal,
            widgets.lineEditOtroIndiceTrituradora,
            widgets.lineEditPotenciaTrituradora
        ]

        for i in lineEdit:
            i.clear()

    

        



            

        

        

            

        