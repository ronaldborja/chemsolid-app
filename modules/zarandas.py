# Clase para manejar zarandas 

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
from PySide6.QtWidgets import QApplication, QMainWindow


# Clase con los calculos de bandas
class Zarandas(QMainWindow):

    # Boton interpolar valores de tablas. 
    def interpolar_zaranda(self): 
        widgets = self.ui

        # Factor A
        sizeMalla = pd.Series([4, 3.5, 3, 2.75, 2.5, 2, 1.75, 1.5, 1.25, 1, 0.875, 0.75 
                                    ,0.625, 0.5, 0.375, 0.25, 0.1875, 0.125, 3/32, 1/16, 1/32]).astype(float)

        porcentajeAreaAbierta = pd.Series([75, 77, 74, 74, 72, 71, 68, 69, 66, 64, 63, 61 
                                    ,59 , 54, 51, 46, 45, 40, 45, 37, 41]).astype(float)

        STPHperft2 = pd.Series([7.69, 7.03, 6.17, 5.85, 5.52, 4.9, 4.51, 4.2, 3.89, 3.56, 3.38, 3.08 
                                    ,2.82 , 2.47, 2.08, 1.6, 1.27, 0.95, 0.76, 0.58, 0.39]).astype(float)
    
        dfFactorA = pd.DataFrame({"SizeMalla": sizeMalla, 
                                    "PorcentajeAreaAbierta": porcentajeAreaAbierta, 
                                    "STPHperft2": STPHperft2})

        # Factor B
        porcentajeTamañosRetenidos = pd.Series([5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60 
                                                    ,65, 70, 75, 80, 85, 90, 95])

        factoresB = pd.Series([1.21, 1.13, 1.08, 1.02, 1, 0.96, 0.92, 0.88, 0.84, 0.79, 0.75, 0.70 
                                                    ,0.66, 0.62, 0.58, 0.53, 0.5, 0.46, 0.33])

        dfFactorB = pd.DataFrame({"PorcentajeRetenidos": porcentajeTamañosRetenidos, 
                                    "FactorB": factoresB})


        # Factor C 
        porcentajeHalfSize = pd.Series([0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60 
                                                    ,65, 70, 75, 80, 85, 90])

        factoresC = pd.Series([0.40, 0.45, 0.50, 0.55, 0.60, 0.70, 0.80, 0.90, 1, 1.1, 1.2, 1.3, 1.4 
                                                    ,1.55, 1.70, 1.85, 2.00, 2.20, 2.40])

        dfFactorC = pd.DataFrame({"PorcentajeHalfSize": porcentajeHalfSize, 
                                    "FactorC": factoresC})


        #Factor E
        opening = pd.Series([1/32, 1/16, 1/8, 3/16, 1/4, 3/8, 1/2, 3/4, 1])
        factoresE = pd.Series([1, 1.25, 2, 2.5, 2, 1.75, 1.4, 1.3, 1.25])

        dfFactorE = pd.DataFrame({"opening": opening, 
                                    "FactorE": factoresE})             
            

        #Factor F
        densidadMaterial = pd.Series([150, 125, 100, 90, 80, 75, 70, 60, 50, 40, 30])
        factoresF = pd.Series([1.50, 1.25, 1.00, 0.90, 0.80, 0.75, 0.70, 0.60, 0.50, 0.40, 0.30])
        
        dfFactorF = pd.DataFrame({"Densidad": densidadMaterial, 
                                    "FactorF": factoresF}) 


        # Factor J
        eficienciaEsperada = pd.Series([95, 90, 85, 80, 75, 70])
        factoresJ = pd.Series([1, 1.15, 1.35, 1.5, 1.7, 1.9])

        dfFactorJ = pd.DataFrame({"Eficiencia": eficienciaEsperada, 
                                    "FactorJ": factoresJ}) 
        

        # Recuperamos los valores de la GUI
        capacidad = widgets.lineEditCapacidadZaranda.text()
        mallaTyler = widgets.lineEditSizeMalla.text()
        sizeParticula = widgets.lineEditSizeParticula.text()
        porcentajePeso = widgets.lineEditPorcentajePeso.text() 
        porcentajePasante = widgets.lineEditPorcentajeMaterialRetenido.text() #Realizar la correción en QT
        halfsize = widgets.lineEditPorcentajeHalfsize.text()
        densidad_material = widgets.lineEditDensidadMaterial.text()
        eficiencia_zaranda = widgets.lineEditEficiencia.text()
        areaZaranda = widgets.lineEditAreaZaranda.text()
        factorA = widgets.lineEditFactorA.text()
        factorB = widgets.lineEditFactorB.text()
        factorC = widgets.lineEditFactorC.text()
        factorD = widgets.lineEditFactorD.text()
        factorE = widgets.lineEdit_12.text()
        factorF = widgets.lineEditFactorF.text()
        factorG = widgets.lineEditFactorG.text()
        factorH = widgets.lineEditFactorH.text()
        factorJ = widgets.lineEditFactorJ.text()

                # Factor D -- (ComboBoxNumerodePisos)
        if (widgets.comboBoxNumeroPisos.currentText() == "Other"): 
            factorD = float(factorD)

        elif (widgets.comboBoxNumeroPisos.currentText() == "One"): 
            factorD = 1

        elif (widgets.comboBoxNumeroPisos.currentText() == "Two"): 
            factorD = 0.9 
            
        elif (widgets.comboBoxNumeroPisos.currentText() == "Three"):
            factorD = 0.8
     

        # Factor H - ComboBoxTipodeMalla
        if (widgets.comboBoxTipoMalla.currentText() == "Other"):
            factorH = float(factorH)

        if (widgets.comboBoxTipoMalla.currentText() == "Square"):
            factorH = 1 

        elif (widgets.comboBoxTipoMalla.currentText() == "Cork groove"):
            factorH = 1.15

        elif (widgets.comboBoxTipoMalla.currentText() == "Long slot"):
            factorH = 1.2

        factorG = float(widgets.lineEditAreaUtil.text()) 

        # Interpolación de los factores de diseño. 

            # -------------------------- FACTOR A ----------------------------------------------------
        mallaTyler = Fraction(mallaTyler) #Se convierte el sizeMalla a float
        mallaTyler = float(mallaTyler)


            # Funciones de interpolación. 
        fAreaAbierta = interp1d(dfFactorA["SizeMalla"], dfFactorA["PorcentajeAreaAbierta"])
        fSTPH = interp1d(dfFactorA["SizeMalla"], dfFactorA["STPHperft2"])

            # Utilizamos las funciones 
        areaAbiertaSelect = fAreaAbierta(mallaTyler)
        factorA = fSTPH(mallaTyler)

            # ------------------------ FACTOR B -------------------------------------------------------
        porcentajeRetenidoMalla = 100 - float(porcentajePasante)

            # Funciones interpolación 
        fB = interp1d(dfFactorB["PorcentajeRetenidos"], dfFactorB["FactorB"])

            # Uso de la función 
        factorB = fB(porcentajeRetenidoMalla)

            # ------------------------FACTOR C --------------------------------------------------------
        halfsize = float(halfsize) # Se convierte a flaot 
        fC = interp1d(dfFactorC["PorcentajeHalfSize"], dfFactorC["FactorC"])
            
            # Uso de la función
        factorC = fC(halfsize)

            # --------------------- Factor E ---------------------------------------------------------- 
            # Se interpola con el tamaño de la malla 
        fE = interp1d(dfFactorE["opening"], dfFactorE["FactorE"])
        factorE = fE(mallaTyler)

            # --------------------- FACTOR F -----------------------------------------------------------
        densidad_material = float(densidad_material)/16.0185 #lb/ft^3 
        fF = interp1d(dfFactorF["Densidad"], dfFactorF["FactorF"])
        factorF = fF(densidad_material)

            # ---------------------FACTOR J -------------------------------------------------------------
        eficiencia_zaranda = float(eficiencia_zaranda)
        fJ = interp1d(dfFactorJ["Eficiencia"], dfFactorJ["FactorJ"])
        factorJ = fJ(eficiencia_zaranda)

        # Seteamos los valores en la interfaz 
        widgets.lineEditFactorA.setText(str(np.round(factorA,4)))
        widgets.lineEditFactorB.setText(str(np.round(factorB,4)))
        widgets.lineEditFactorC.setText(str(np.round(factorC,4)))
        widgets.lineEditFactorD.setText(str(np.round(factorD,4)))
        widgets.lineEdit_12.setText(str(np.round(factorE,4)))
        widgets.lineEditFactorF.setText(str(np.round(factorF,4)))
        widgets.lineEditFactorG.setText(str(np.round(factorG,4)))
        widgets.lineEditFactorH.setText(str(factorH))
        widgets.lineEditFactorJ.setText(str(np.round(factorJ,4))) 
        widgets.pushButton_3.setChecked(True)

    # Método para hacer los calculos 
    def calcular_zarandas(self): 
        widgets = self.ui

        # Factor A
        sizeMalla = pd.Series([4, 3.5, 3, 2.75, 2.5, 2, 1.75, 1.5, 1.25, 1, 0.875, 0.75 
                                    ,0.625, 0.5, 0.375, 0.25, 0.1875, 0.125, 3/32, 1/16, 1/32]).astype(float)

        porcentajeAreaAbierta = pd.Series([75, 77, 74, 74, 72, 71, 68, 69, 66, 64, 63, 61 
                                    ,59 , 54, 51, 46, 45, 40, 45, 37, 41]).astype(float)

        STPHperft2 = pd.Series([7.69, 7.03, 6.17, 5.85, 5.52, 4.9, 4.51, 4.2, 3.89, 3.56, 3.38, 3.08 
                                    ,2.82 , 2.47, 2.08, 1.6, 1.27, 0.95, 0.76, 0.58, 0.39]).astype(float)
    
        dfFactorA = pd.DataFrame({"SizeMalla": sizeMalla, 
                                    "PorcentajeAreaAbierta": porcentajeAreaAbierta, 
                                    "STPHperft2": STPHperft2})

        # Factor B
        porcentajeTamañosRetenidos = pd.Series([5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60 
                                                    ,65, 70, 75, 80, 85, 90, 95])

        factoresB = pd.Series([1.21, 1.13, 1.08, 1.02, 1, 0.96, 0.92, 0.88, 0.84, 0.79, 0.75, 0.70 
                                                    ,0.66, 0.62, 0.58, 0.53, 0.5, 0.46, 0.33])

        dfFactorB = pd.DataFrame({"PorcentajeRetenidos": porcentajeTamañosRetenidos, 
                                    "FactorB": factoresB})


        # Factor C 
        porcentajeHalfSize = pd.Series([0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60 
                                                    ,65, 70, 75, 80, 85, 90])

        factoresC = pd.Series([0.40, 0.45, 0.50, 0.55, 0.60, 0.70, 0.80, 0.90, 1, 1.1, 1.2, 1.3, 1.4 
                                                    ,1.55, 1.70, 1.85, 2.00, 2.20, 2.40])

        dfFactorC = pd.DataFrame({"PorcentajeHalfSize": porcentajeHalfSize, 
                                    "FactorC": factoresC})


        #Factor E
        opening = pd.Series([1/32, 1/16, 1/8, 3/16, 1/4, 3/8, 1/2, 3/4, 1])
        factoresE = pd.Series([1, 1.25, 2, 2.5, 2, 1.75, 1.4, 1.3, 1.25])

        dfFactorE = pd.DataFrame({"opening": opening, 
                                    "FactorE": factoresE})             
            

        #Factor F
        densidadMaterial = pd.Series([150, 125, 100, 90, 80, 75, 70, 60, 50, 40, 30])
        factoresF = pd.Series([1.50, 1.25, 1.00, 0.90, 0.80, 0.75, 0.70, 0.60, 0.50, 0.40, 0.30])
        
        dfFactorF = pd.DataFrame({"Densidad": densidadMaterial, 
                                    "FactorF": factoresF}) 

        # Factor J
        eficienciaEsperada = pd.Series([95, 90, 85, 80, 75, 70])
        factoresJ = pd.Series([1, 1.15, 1.35, 1.5, 1.7, 1.9])

        dfFactorJ = pd.DataFrame({"Eficiencia": eficienciaEsperada, 
                                    "FactorJ": factoresJ}) 
        

        # Recuperamos los valores de la GUI
        capacidad = widgets.lineEditCapacidadZaranda.text()
        mallaTyler = widgets.lineEditSizeMalla.text()
        sizeParticula = widgets.lineEditSizeParticula.text()
        porcentajePeso = widgets.lineEditPorcentajePeso.text() 
        porcentajePasante = widgets.lineEditPorcentajeMaterialRetenido.text() #Realizar la correción en QT
        halfsize = widgets.lineEditPorcentajeHalfsize.text()
        densidad_material = widgets.lineEditDensidadMaterial.text()
        eficiencia_zaranda = widgets.lineEditEficiencia.text()
        areaZaranda = widgets.lineEditAreaZaranda.text()
        factorA = widgets.lineEditFactorA.text()
        factorB = widgets.lineEditFactorB.text()
        factorC = widgets.lineEditFactorC.text()
        factorD = widgets.lineEditFactorD.text()
        factorE = widgets.lineEdit_12.text()
        factorF = widgets.lineEditFactorF.text()
        factorG = widgets.lineEditFactorG.text()
        factorH = widgets.lineEditFactorH.text()
        factorJ = widgets.lineEditFactorJ.text()

                # Factor D -- (ComboBoxNumerodePisos)
        if (widgets.comboBoxNumeroPisos.currentText() == "Other"): 
            factorD = float(factorD)

        elif (widgets.comboBoxNumeroPisos.currentText() == "One"): 
            factorD = 1

        elif (widgets.comboBoxNumeroPisos.currentText() == "Two"): 
            factorD = 0.9 
            
        elif (widgets.comboBoxNumeroPisos.currentText() == "Three"):
            factorD = 0.8
     
        # Factor H - ComboBoxTipodeMalla
        if (widgets.comboBoxTipoMalla.currentText() == "Another"):
            factorH = float(factorH)

        if (widgets.comboBoxTipoMalla.currentText() == "Square"):
            factorH = 1 

        elif (widgets.comboBoxTipoMalla.currentText() == "Cork groove"):
            factorH = 1.15

        elif (widgets.comboBoxTipoMalla.currentText() == "Long slot"):
            factorH = 1.2

        factorG = float(widgets.lineEditAreaUtil.text()) 

        # Interpolación de los factores de diseño. 

            # -------------------------- FACTOR A ----------------------------------------------------
        mallaTyler = Fraction(mallaTyler) #Se convierte el sizeMalla a float
        mallaTyler = float(mallaTyler)


        # Funciones de interpolación. 
        fAreaAbierta = interp1d(dfFactorA["SizeMalla"], dfFactorA["PorcentajeAreaAbierta"])
        fSTPH = interp1d(dfFactorA["SizeMalla"], dfFactorA["STPHperft2"])

            # Utilizamos las funciones 
        areaAbiertaSelect = fAreaAbierta(mallaTyler)
        factorA = fSTPH(mallaTyler)

            # ------------------------ FACTOR B -------------------------------------------------------
        porcentajeRetenidoMalla = 100 - float(porcentajePasante)

            # Funciones interpolación 
        fB = interp1d(dfFactorB["PorcentajeRetenidos"], dfFactorB["FactorB"])

            # Uso de la función 
        factorB = fB(porcentajeRetenidoMalla)

            # ------------------------FACTOR C --------------------------------------------------------
        halfsize = float(halfsize) # Se convierte a flaot 
        fC = interp1d(dfFactorC["PorcentajeHalfSize"], dfFactorC["FactorC"])
            
            # Uso de la función
        factorC = fC(halfsize)

            # --------------------- Factor E ---------------------------------------------------------- 
            # Se interpola con el tamaño de la malla 
        fE = interp1d(dfFactorE["opening"], dfFactorE["FactorE"])
        factorE = fE(mallaTyler)

            # --------------------- FACTOR F -----------------------------------------------------------
        densidad_material = float(densidad_material)/16.0185 #lb/ft^3 
        fF = interp1d(dfFactorF["Densidad"], dfFactorF["FactorF"])
        factorF = fF(densidad_material)

            # ---------------------FACTOR J -------------------------------------------------------------
        eficiencia_zaranda = float(eficiencia_zaranda)
        fJ = interp1d(dfFactorJ["Eficiencia"], dfFactorJ["FactorJ"])
        factorJ = fJ(eficiencia_zaranda)


        # Creación sistema de ecuaciones. 
        if (widgets.lineEditCapacidadZaranda.text() == ''): 
            capacidad = sp.Symbol('capacidad')
            areaZaranda = float(areaZaranda)*10.764
            capacidad = (areaZaranda*factorA*factorB*factorC*factorD*factorE*factorF*factorG*factorH*factorJ)/1.10231
            widgets.lineEditCapacidadZaranda.setText(str(np.round(capacidad,4)))
            
        else: 
            capacidad = float(capacidad)

            
        if (areaZaranda == ''): 
            areaCalculada = ((capacidad*1.10231)/(factorA*factorB*factorC*factorD*factorE*factorF*factorG*factorH*factorJ))/(10.764)
            widgets.lineEditAreaZaranda.setText(str(np.round(areaCalculada,4)))
      
        else: 
            areaZaranda = float(areaZaranda)*10.764

    def calcular_zarandas_sin_interpolar(self):
        widgets = self.ui

        # Recuperamos los valores de la GUI
        capacidad = widgets.lineEditCapacidadZaranda.text()
        mallaTyler = widgets.lineEditSizeMalla.text()
        sizeParticula = widgets.lineEditSizeParticula.text()
        porcentajePeso = widgets.lineEditPorcentajePeso.text() 
        porcentajePasante = widgets.lineEditPorcentajeMaterialRetenido.text() #Realizar la correción en QT
        halfsize = widgets.lineEditPorcentajeHalfsize.text()
        densidad_material = widgets.lineEditDensidadMaterial.text()
        eficiencia_zaranda = widgets.lineEditEficiencia.text()
        areaZaranda = widgets.lineEditAreaZaranda.text()
        factorA = widgets.lineEditFactorA.text()
        factorB = widgets.lineEditFactorB.text()
        factorC = widgets.lineEditFactorC.text()
        factorD = widgets.lineEditFactorD.text()
        factorE = widgets.lineEdit_12.text()
        factorF = widgets.lineEditFactorF.text()
        factorG = widgets.lineEditFactorG.text()
        factorH = widgets.lineEditFactorH.text()
        factorJ = widgets.lineEditFactorJ.text()
            

        # Creación sistema de ecuaciones. 
        if (capacidad == ''): 
            capacidad = sp.Symbol('capacidad')

        else: 
            capacidad = float(capacidad)*1.10231


        if (factorA == ''): 
            factorA = sp.Symbol('factorA')

        else: 
            factorA = float(factorA)
            

        if (factorB == ''): 
            factorB = sp.Symbol('FactorB')

        else: 
            factorB = float(factorB)


        if (factorC == ''): 
            factorC = sp.Symbol("factorC")
            
        else:
            factorC = float(factorC)


        if (factorD == ''): 
            factorD = sp.Symbol("factorD")

        else: 
            factorD = float(factorD)
            

        if (factorE == ''):
            factorE = sp.Symbol("factorE")

        else: 
            factorE = float(factorE)


        if (factorF == ''): 
            factorF = sp.Symbol("factorF")

        else: 
            factorF = float(factorF)


        if (factorG == ''): 
            # Factor G - LineEdit 
            factorG = sp.Symbol('factorG')    

        else: 
            factorG = float(factorG)    


        if (factorH == ''): 
            factorH = sp.Symbol('factorH')

        else: 
            factorH = float(factorH) 


        if (factorJ == ''): 
            factorJ == sp.Symbol('factorJ')
            
        else: 
            factorJ = float(factorJ)


        if (areaZaranda == ''):
            areaZaranda = sp.Symbol('areaZaranda')

        else:
            areaZaranda = float(areaZaranda)*10.764

        variables_ecuacion = [areaZaranda, capacidad, factorA, factorB, factorC, factorD, factorE, factorF, 
                            factorG, factorH, factorJ]

        variables_despejar = []

        for i in variables_ecuacion: 
            if isinstance(i, sp.core.symbol.Symbol):
                variables_despejar.append(i)

        ecDiseñoZarandas = str(capacidad/(factorA*factorB*factorC*factorD*factorE*factorF*factorG*factorH*factorJ) - areaZaranda)
        ecSimpeada = sp.parse_expr(ecDiseñoZarandas)

        if len(variables_despejar) == 1: 
            sln = sp.solve((ecSimpeada), variables_despejar[0])
            
            if variables_despejar[0] == capacidad: 
                widgets.lineEditCapacidadZaranda.setText(str(round(sln[0], 4)))

            elif variables_despejar[0] == factorA:
                widgets.lineEditFactorA.setText(str(round(sln[0], 4)))

            elif variables_despejar[0] == factorB:
                widgets.lineEditFactorB.setText(str(round(sln[0], 4)))

            elif variables_despejar[0] == factorC:
                widgets.lineEditFactorC.setText(str(round(sln[0], 4)))

            elif variables_despejar[0] == factorD:
                widgets.lineEditFactorD.setText(str(round(sln[0], 4)))

            elif variables_despejar[0] == factorE:
                widgets.lineEdit_12.setText(str(round(sln[0], 4)))

            elif variables_despejar[0] == factorF:
                widgets.lineEditFactorF.setText(str(round(sln[0], 4)))

            elif variables_despejar[0] == factorG:
                widgets.lineEditFactorG.setText(str(round(sln[0], 4)))

            elif variables_despejar[0] == factorH:
                widgets.lineEditFactorH.setText(str(round(sln[0], 4)))

            elif variables_despejar[0] == factorJ:
                widgets.lineEditFactorJ.setText(str(round(sln[0], 4)))

            elif variables_despejar[0] == areaZaranda: 
                widgets.lineEditAreaZaranda.setText(str(round(sln[0]/10.764, 4)))

    def limpiarZarandas(self): 
        widgets = self.ui

        lineEdit = [widgets.lineEditCapacidadZaranda, 
        widgets.lineEditSizeMalla,
        widgets.lineEditSizeParticula,
        widgets.lineEditPorcentajePeso, 
        widgets.lineEditPorcentajeMaterialRetenido, #Realizar la correción en QT
        widgets.lineEditPorcentajeHalfsize,
        widgets.lineEditDensidadMaterial,
        widgets.lineEditEficiencia,
        widgets.lineEditAreaZaranda,
        widgets.lineEditAreaUtil,
        widgets.lineEditFactorA,
        widgets.lineEditFactorB,
        widgets.lineEditFactorC,
        widgets.lineEditFactorD,
        widgets.lineEdit_12,
        widgets.lineEditFactorF,
        widgets.lineEditFactorG,
        widgets.lineEditFactorH,
        widgets.lineEditFactorJ]

        for i in lineEdit:
            i.clear()