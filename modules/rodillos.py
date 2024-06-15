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
class Rodillo(QMainWindow):
    def calcular_rodillos(self): 
        widgets = self.ui

        # Recuperación de los valores ingresados por el usuario 
        tamañoAlimento = widgets.lineEditAlimentoRodillo.text()
        tamañoProducto = widgets.lineEditProductoRodillo.text()
        tamañoMaximo = widgets.lineEditTamaoMaximo.text()
        densidadMat = widgets.lineEditDensidadRodillo.text()
        densidadTorta = widgets.lineEditTortaSalida.text()
        coeficienteFriccion = widgets.lineEditCoeficienteFriccion.text()
        anguloApertura = widgets.lineEditAnguloApertura.text()
        anguloFractura = widgets.lineEditAnguloFractura.text()
        anguloCompresion = widgets.lineEditAnguloCompresion.text()
        widthRodillos = widgets.lineEditWidthRodillos.text()
        diametroRodillos = widgets.lineEditDiametroRodillos.text()
        k1 = widgets.lineEditk1.text()
        k2 = widgets.lineEditk2.text()
        k3 = widgets.lineEditk3.text()
        k4 = widgets.lineEditk4.text()
        torque = widgets.lineEditTorqueMolienda.text()
        fuerzaEspecifica = widgets.lineEditFuerzaEspecifica.text()
        gap = widgets.lineEditDistanciaRodillos.text()
        velocidadRodillos = widgets.lineEditVelocidadRodillos.text()
        capacidadRodillos = widgets.lineEditCapacidadRodillos.text()
        potenciaRodillos = widgets.lineEditSizePotenciaRodillos.text()
        grosorTorta = widgets.lineEditGrosorTorta.text()

        # Creación de variables simbolicas 
        if (tamañoAlimento == ''): 
            tamañoAlimento = sp.Symbol('tamañoAlimento')
        else: 
            tamañoAlimento = float(tamañoAlimento)

        if (tamañoProducto == ''): 
            tamañoProducto = sp.Symbol('tamañoProducto')

        else: 
            tamañoProducto = float(tamañoProducto)

        if (tamañoMaximo == ''): 
            tamañoMaximo = sp.Symbol('tamañoMaximo')

        else: 
            tamañoMaximo = float(tamañoMaximo)

        if (densidadMat == ''): 
            densidadMat = sp.Symbol('densidadMat')

        else: 
            densidadMat = float(densidadMat)


        if (densidadTorta == ''): 
            densidadTorta = sp.Symbol('densidadTorta')

        else: 
            densidadTorta = float(densidadTorta)

        if (coeficienteFriccion == ''): 
            coeficienteFriccion = sp.Symbol('coeficienteFriccion')

        else: 
            coeficienteFriccion = float(coeficienteFriccion)

        if (anguloApertura == ''): 
            anguloApertura = sp.Symbol('anguloApertura')

        else: 
            anguloApertura = float(anguloApertura)

        if (anguloFractura == ''): 
            anguloFractura = sp.Symbol('anguloFractura')

        else: 
            anguloFractura = float(anguloFractura)

        # Pendiente --> Angulo Compresión 
        if (anguloCompresion == ''): 
            anguloCompresion = sp.Symbol('anguloComprension')

        else: 
            anguloCompresion = float(anguloCompresion)

        if (widthRodillos == ''): 
            widthRodillos = sp.Symbol('widthRodillos')

        else: 
            widthRodillos = float(widthRodillos)

        if (diametroRodillos == ''): 
            diametroRodillos = sp.Symbol('diametroRodillos')
        
        else: 
            diametroRodillos = float(diametroRodillos)

        if (k1 == ''): 
            k1 = sp.Symbol('k1')

        else: 
            k1 = float(k1) 

        if (k2 == ''): 
            k2 = sp.Symbol('k2')

        else: 
            k2 = float(k2)

        if (k3 == ''): 
            k3 = sp.Symbol('k3')

        else: 
            k3 = float(k3)

        if (k4 == ''): 
            k4 = sp.Symbol('k4')

        else: 
            k4 = float(k4)

        if (torque == ''): 
            torque = sp.Symbol('torque')

        else: 
            torque = float(torque)

        if (fuerzaEspecifica == ''): 
            fuerzaEspecifica = sp.Symbol('fuerzaEspecifica')

        else: 
            fuerzaEspecifica = float(fuerzaEspecifica)

        if (gap == ''): 
            gap = sp.Symbol('gap')

        else: 
            gap = float(gap)

        if (capacidadRodillos == ''): 
            capacidadRodillos = sp.Symbol('capacidadRodillos')

        else: 
            capacidadRodillos = float(capacidadRodillos)

        if (potenciaRodillos == ''): 
            potenciaRodillos = sp.Symbol('potenciaRodillos')

        else: 
            potenciaRodillos = float(potenciaRodillos)

        if (grosorTorta == ''): 
            grosorTorta = sp.Symbol('grosorTorta')

        else: 
            grosorTorta = float(grosorTorta)

        # Ecuacion #1: 
        vars_eq1_1 = [coeficienteFriccion, anguloApertura]
        vars_des1_1= []

        for i in vars_eq1_1: 
            if isinstance(i, sp.core.symbol.Symbol):
                vars_des1_1.append(i)

        ecuacion1_1 = str(coeficienteFriccion - sp.tan(sp.rad(anguloApertura)))
        ecSimpeada1_1 = sp.parse_expr(ecuacion1_1)

        if len(vars_des1_1) == 1: 
            sln1_1 = sp.solve((ecSimpeada1_1), vars_des1_1[0])

            if vars_des1_1[0] == coeficienteFriccion: 
                widgets.lineEditCoeficienteFriccion.setText(str(round(sln1_1[0], 4)))
                coeficienteFriccion = sln1_1[0]

            elif vars_des1_1[0] == anguloApertura: 
                widgets.lineEditAnguloApertura.setText(str(round(sln1_1[0], 4)))
                anguloApertura = sp.rad(sln1_1[0])

        # Ecuación #2: Diametro de los rodillos 
        vars_eq2_1 = [anguloApertura, diametroRodillos, gap, tamañoMaximo]
        vars_des2_1= []

        for i in vars_eq2_1: 
            if isinstance(i, sp.core.symbol.Symbol):
                vars_des2_1.append(i)

        ecuacion2_1 = str(((gap - tamañoMaximo*sp.cos(anguloApertura))/(sp.cos(anguloApertura) - 1)) - diametroRodillos)
        ecSimpeada2_1 = sp.parse_expr(ecuacion2_1)

        if len(vars_des2_1) == 1: 
            sln2_1 = sp.solve((ecSimpeada2_1), vars_des2_1[0])

            if vars_des2_1[0] == diametroRodillos: 
                widgets.lineEditDiametroRodillos.setText(str(round(sln2_1[0], 4)))
                diametroRodillos = sln2_1[0]

            elif vars_des2_1[0] == gap: 
                widgets.lineEditDistanciaRodillos.setText(str(round(sln2_1[0], 4)))
                gap = sln2_1[0]

            elif vars_des2_1[0] == anguloApertura: 
                widgets.lineEditAnguloApertura.setText(str(round(sln2_1[0], 4)))
                anguloApertura = sln2_1[0]

            elif vars_des2_1[0] == tamañoMaximo: 
                widgets.lineEditTamaoMaximo.setText(str(round(sln2_1[0], 4)))
                tamañoMaximo = sln2_1[0]     

        
        # Ecuacion 4: Angulos de compactación 
        vars_eq3_1 = [tamañoMaximo, diametroRodillos, grosorTorta, anguloFractura]
        vars_des3_1= []

        for i in vars_eq3_1: 
            if isinstance(i, sp.core.symbol.Symbol):
                vars_des3_1.append(i)

        ecuacion3_1 = str((1 - (tamañoMaximo/grosorTorta - 1)*(grosorTorta/(1000*diametroRodillos))) - sp.cos(sp.rad(anguloFractura)))
        ecSimpeada3_1 = sp.parse_expr(ecuacion3_1)

        if len(vars_des3_1) == 1: 
            sln3_1 = sp.solve((ecSimpeada3_1), vars_des3_1[0])

            if vars_des3_1[0] == tamañoMaximo: 
                widgets.lineEditTamaoMaximo.setText(str(round(sln3_1[0], 4)))
                tamañoMaximo = sln3_1[0]

            elif vars_des3_1[0] == diametroRodillos: 
                widgets.lineEditDiametroRodillos.setText(str(round(sln3_1[0], 4)))
                diametroRodillos = sln3_1[0]

            elif vars_des3_1[0] == grosorTorta: 
                widgets.lineEditGrosorTorta.setText(str(round(sln3_1[0], 4)))
                grosorTorta = sln3_1[0]

            elif vars_des3_1[0] == anguloFractura: 
                widgets.lineEditAnguloFractura.setText(str(round(sln3_1[0], 4)))
                anguloFractura = sp.rad(sln3_1[0])


        # Ecuación 5 - Angulo de compresión 
        vars_eq4_1 = [densidadMat, densidadTorta, grosorTorta, diametroRodillos, anguloCompresion]
        vars_des4_1= []

        for i in vars_eq4_1: 
            if isinstance(i, sp.core.symbol.Symbol):
                vars_des4_1.append(i)

        ecuacion4_1 = str((1 - (densidadTorta/densidadMat - 1)*(grosorTorta/(1000*diametroRodillos))) - sp.cos(sp.rad(anguloCompresion)))
        ecSimpeada4_1 = sp.parse_expr(ecuacion4_1)

        if len(vars_des4_1) == 1: 
            sln4_1 = sp.solve((ecSimpeada4_1), vars_des4_1[0])

            if vars_des4_1[0] == densidadMat: 
                widgets.lineEditDensidadRodillo.setText(str(round(sln4_1[0], 4)))
                densidadMat = sln4_1[0]

            elif vars_des4_1[0] == densidadTorta: 
                widgets.lineEdiTortaSalida.setText(str(round(sln4_1[0], 4)))
                densidadTorta = sln4_1[0]

            elif vars_des4_1[0] == grosorTorta: 
                widgets.lineEditGrosorTorta.setText(str(round(sln4_1[0], 4)))
                grosorTorta = sln4_1[0]

            elif vars_des4_1[0] == diametroRodillos: 
                widgets.lineEditDiametroRodillos.setText(str(round(sln4_1[0], 4)))
                diametroRodillos = sln4_1[0]

            elif vars_des4_1[0] == anguloCompresion: 
                widgets.lineEditAnguloCompresion.setText(str(round(sln4_1[0], 4)))
                anguloCompresion = sp.rad(sln4_1[0]) 

        # Ecuacion Velocidad de los rodillos 
        if (diametroRodillos < 2): 
            velocidadRodillos = 1.35*diametroRodillos
            velocidadAngular = (diametroRodillos/2)*velocidadRodillos
            widgets.lineEditVelocidadRodillos.setText(str(round(velocidadRodillos, 4)))

        else: 
            velocidadRodillos = diametroRodillos
            velocidadAngular = (diametroRodillos/2)*velocidadRodillos
            widgets.lineEditVelocidadRodillos.setText(str(round(velocidadRodillos, 4)))


        # Ecuación del gap o distancia entre rodillos 
        # vars_eq7_1 = [gap, velocidadRodillos, diametroRodillos, fuerzaEspecifica, k1, k2, k3, k4]
        # vars_des7_1= []

        # for i in vars_eq7_1: 
          #   if isinstance(i, sp.core.symbol.Symbol):
            #     vars_des7_1.append(i)

        # ecuacion7_1 = str(((k1*(velocidadRodillos**2)*(2/(9.81*diametroRodillos)) + k2*velocidadRodillos*sp.sqrt(2/(9.81*diametroRodillos)) + k3)*(1 + k4*sp.log(fuerzaEspecifica, 10)))*diametroRodillos - gap)
        # ecSimpeada7_1 = sp.parse_expr(ecuacion7_1)

        # if len(vars_des7_1) == 1: 
          #  sln7_1 = sp.solve((ecSimpeada7_1), vars_des7_1[0])

           # if vars_des7_1[0] == gap: 
              #  widgets.lineEditDistanciaRodillos.setText(str(round(sln7_1[0], 4)))
              #  gap = sln7_1[0]

            # elif vars_des7_1[0] == velocidadRodillos: 
              #  widgets.lineEditVelocidadRodillos.setText(str(round(sln7_1[0], 4)))
               #  velocidadRodillos = sln7_1[0]

            # elif vars_des7_1[0] == diametroRodillos: 
              #  widgets.lineEditDiametroRodillos.setText(str(round(sln7_1[0], 4)))
               #  diametroRodillos = sln7_1[0]

            # elif vars_des7_1[0] == fuerzaEspecifica: 
              #  widgets.lineEditFuerzaEspecifica.setText(str(round(sln7_1[0], 4)))
               #  fuerzaEspecifica = sln7_1[0]

            # elif vars_des7_1[0] == k1: 
              #  widgets.lineEditk1.setText(str(round(sln7_1[0], 4)))
               # k1 = sln7_1[0]
    
            # elif vars_des7_1[0] == k2: 
              #  widgets.lineEditk2.setText(str(round(sln7_1[0], 4)))
            #  k2 = sln7_1[0]

            # elif vars_des7_1[0] == k3: 
              #  widgets.lineEditk3.setText(str(round(sln7_1[0], 4)))
               #  k3 = sln7_1[0]

            #elif vars_des7_1[0] == k4: 
             #   widgets.lineEditk4.setText(str(round(sln7_1[0], 4)))
              #  k4 = sln7_1[0]

        # Calculo directo del gap 
        gap = ((k1*(velocidadRodillos**2)*(2/(9.81*diametroRodillos)) + k2*velocidadRodillos*sp.sqrt(2/(9.81*diametroRodillos)) + k3)*(1 + k4*sp.log(fuerzaEspecifica, 10)))*diametroRodillos
        widgets.lineEditDistanciaRodillos.setText(str(round(gap, 4)))


        # Ecuacion 6 - Capacidad. 
        vars_eq5_1 = [widthRodillos, gap, velocidadRodillos, densidadMat, capacidadRodillos]
        vars_des5_1= []

        for i in vars_eq5_1: 
            if isinstance(i, sp.core.symbol.Symbol):
                vars_des5_1.append(i)
        
        ecuacion5_1 = str(3.6*widthRodillos*(gap*1000)*velocidadRodillos*densidadMat - capacidadRodillos)
        ecSimpeada5_1 = sp.parse_expr(ecuacion5_1)

        if len(vars_des5_1) == 1: 
            sln5_1 = sp.solve((ecSimpeada5_1), vars_des5_1[0])

            if vars_des5_1[0] == widthRodillos: 
                widgets.lineEditWidthRodillos.setText(str(round(sln5_1[0], 4)))
                widthRodillos = sln5_1[0]

            elif vars_des5_1[0] == gap: 
                widgets.lineEditDistanciaRodillos.setText(str(round(sln5_1[0], 4)))
                gap = sln5_1[0]

            elif vars_des5_1[0] == velocidadRodillos: 
                widgets.lineEditVelocidadRodillos.setText(str(round(sln5_1[0], 4)))
                velocidadRodillos = sln5_1[0] 

            elif vars_des5_1[0] == densidadMat: 
                widgets.lineEditDensidadRodillo.setText(str(round(sln5_1[0], 4)))
                densidadMat = sln5_1[0]

            elif vars_des5_1[0] == capacidadRodillos:  
                widgets.lineEditCapacidadRodillos.setText(str(round(sln5_1[0], 4)))
                capacidadRodillos = sln5_1[0]


        # Ecuación - Potencia de Rodillos 
        vars_eq6_1 = [potenciaRodillos, torque, diametroRodillos, velocidadAngular]
        vars_des6_1= []

        for i in vars_eq6_1: 
            if isinstance(i, sp.core.symbol.Symbol):
                vars_des6_1.append(i)
        
        ecuacion6_1 = str((2*torque*velocidadAngular)/(diametroRodillos) - potenciaRodillos)
        ecSimpeada6_1 = sp.parse_expr(ecuacion6_1)

        if len(vars_des6_1) == 1: 
            sln6_1 = sp.solve((ecSimpeada6_1), vars_des6_1[0])

            if vars_des6_1[0] == potenciaRodillos: 
                widgets.lineEditSizePotenciaRodillos.setText(str(round(sln6_1[0], 4)))
                potenciaRodillos = sln6_1[0]

            elif vars_des6_1[0] == torque: 
                widgets.lineEditTorqueMolienda.setText(str(round(sln6_1[0], 4)))
                torque = sln6_1[0]

            elif vars_des6_1[0] == diametroRodillos: 
                widgets.lineEditDiametroRodillos.setText(str(round(sln6_1[0], 4)))
                diametroRodillos = sln6_1[0]

    def inhabilitar_rodillo(self, index): 
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


    def limpiar_rodillos(self): 
        widgets = self.ui

        lineEdit = [
            widgets.lineEditAlimentoRodillo,
            widgets.lineEditProductoRodillo, 
            widgets.lineEditTamaoMaximo, 
            widgets.lineEditDensidadRodillo, 
            widgets.lineEditTortaSalida, 
            widgets.lineEditGrosorTorta,
            widgets.lineEditCoeficienteFriccion, 
            widgets.lineEditAnguloApertura, 
            widgets.lineEditAnguloFractura,
            widgets.lineEditAnguloCompresion, 
            widgets.lineEditWidthRodillos, 
            widgets.lineEditDiametroRodillos,
            widgets.lineEditk1, 
            widgets.lineEditk2,
            widgets.lineEditk3,
            widgets.lineEditk4, 
            widgets.lineEditTorqueMolienda,
            widgets.lineEditFuerzaEspecifica, 
            widgets.lineEditDistanciaRodillos, 
            widgets.lineEditVelocidadRodillos, 
            widgets.lineEditCapacidadRodillos,
            widgets.lineEditSizePotenciaRodillos 
        ]

        for i in lineEdit:
            i.clear()

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
