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



class Elevador(QMainWindow):
    def calculate_elevator(self): 
        widgets = self.ui

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

    def inhabilitar(self): 
        widgets = self.ui
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

    def reset_cangilones(self): 
        widgets = self.ui
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