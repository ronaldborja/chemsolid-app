#1. Importar los widgets y demás 
from modules import *
from widgets import * 


class Tornillo(QMainWindow):
    def calculate_tornillo(self): 
        widgets = self.ui
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

    def reset_tornillo(self):
        widgets = self.ui 
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