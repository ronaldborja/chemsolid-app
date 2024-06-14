from main import *

class calculos_bandas_1(MainWindow):
    def calculate_1(self):
        widget = self.ui
        
        #definicion de las variables
        qg=widget.lineEdit_qg_bp1.text()
        lv=widget.lineEdit_lv_bp1.text()
        v=widget.lineEdit_v_bp1.text()
        lm=widget.lineEdit_lm_bp1.text()
        qs=widget.lineEdit_qs_bp1.text()
        lvt=widget.lineEdit_lvt_bp1.text()
        lvm=widget.lineEdit_lvm_bp1.text()
        k=widget.lineEdit_k_bp1.text()
        k1=widget.lineEdit_k1_bp1.text()
        s=widget.lineEdit_s_bp1.text()
        A1=widget.lineEdit_A1_bp1.text()
        A2=widget.lineEdit_A2_bp1.text()


        #--------espacio para las demas variables

        if qg=='':
            qg=sp.Symbol('qg')
        else:
            qg=float(widget.lineEdit_qg_bp1.text())
        
        if lv=="":
            lv=sp.Symbol("lv")
        else:
            lv=float(widget.lineEdit_lv_bp1.text())


        if v=="":
            v=sp.Symbol("v")
        else:
            v=float(widget.lineEdit_v_bp1.text())
        

        if lm=="":
            lm=sp.Symbol("lm")
        else:
            lm=float(widget.lineEdit_lm_bp1.text())
        
        if qs=='':
            qs=sp.Symbol('qs')
        else:
            qs=float(widget.lineEdit_qs_bp1.text())


        if lvt=='':
            lvt=sp.Symbol('lvt')
        else:
            lvt=float(widget.lineEdit_lvt_bp1.text())

        if lvm=='':
            lvm=sp.Symbol('lvm')
        else:
            lvm=float(widget.lineEdit_lvm_bp1.text())


        if k=='':
            k=sp.Symbol('k')
        else:
            k=float(widget.lineEdit_k_bp1.text())

        if k1=='':
            k1=sp.Symbol('k1')
        else:
            k1=float(widget.lineEdit_k1_bp1.text())

        if s=='':
            s=sp.Symbol('s')
        else:
            s=float(widget.lineEdit_s_bp1.text())
        if A1=='':
            A1=sp.Symbol('A1')
        else:
            A1=float(widget.lineEdit_A1_bp1.text())

        if A2=='':
            A2=sp.Symbol('A2')
        else:
            A2=float(widget.lineEdit_A2_bp1.text())
        

        #definimos la primera ecuacion
        #variables implicadas
        #variables desconocidad
        #las metemos en un for i

        #escribimos la expresion de la ecuacion
        #resolvemos si es posible y seteamos en el lugar correspondiente


        var_primera=[s,lvt]
        var_des_pe=[]
        for i in var_primera:
            if  isinstance(i, sp.core.symbol.Symbol):
                var_des_pe.append(i)
        ec1=(lvt/3600)-s
        expr1=sp.parse_expr(str(ec1))
        if len(var_des_pe)==1:
            sol1=sp.solve(expr1,var_des_pe[0])
            print('sol1', sol1)
            if var_des_pe[0]==s:
                widget.lineEdit_s_bp1.setText(str(round(sol1[0],5)))
            elif var_des_pe[0]==lvt:
                widget.lineEdit_lvt_bp1.setText(str(round(sol1[0],5)))
        
        #segunda ecuacion

        var_segunda=[lv,v,qg]
        var_des_se=[]
        for i in var_segunda:
            if  isinstance(i, sp.core.symbol.Symbol):
                var_des_se.append(i)
        print("la ariable desconocida es ", var_des_se[0])
        ec2=(lv/(3.6*v))-qg
        expr2=sp.parse_expr(str(ec2))
        if len(var_des_se)==1:
            sol2=sp.solve(expr2, var_des_se[0])
            print('sol2', sol2)
            if var_des_se[0]==lv:
                widget.lineEdit_lv_bp1.setText(str(round(sol2[0],5)))
            elif var_des_se[0]==v:
                widget.lineEdit_v_bp1.setText(str(round(sol2[0],5)))
            elif var_des_se[0]==qg:
                widget.lineEdit_qg_bp1.setText(str(round(sol2[0],5)))
                widget.lineEdit_qg_bp2.setText(str(round(sol2[0],5)))
                

        #terceraecuacion

        var_tercera=[lm,lv,qs]
        var_des_te=[]
        for i in var_tercera:
            if  isinstance(i, sp.core.symbol.Symbol):
                var_des_te.append(i)
        print('variable des;' , var_des_te[0])

        ec3=(lv/qs)-lm
        expr3=(sp.parse_expr(str(ec3)))
        if len(var_des_te)==1:
            sol3=sp.solve(expr3, var_des_te[0])
            if var_des_te[0]==lm:
                widget.lineEdit_lm_bp1.setText(str(round(sol3[0],5)))
            elif var_des_te[0]==lv:
                widget.lineEdit_lv_bp1.setText(str(round(sol3[0],5)))
            elif var_des_te[0]==qs:
                widget.lineEdit_qs_bp1.setText(str(round(sol3[0],5)))
        
        #cuarta ecuacion

        var_cuarta=[lm,v,lvt]
        var_des_ce=[]
        for i in var_cuarta:
            if  isinstance(i, sp.core.symbol.Symbol):
                var_des_ce.append(i)
        ec4=(lm/v)-lvt
        expr4=(sp.parse_expr(str(ec4)))
        if len(var_des_ce)==1:
            sol4=sp.solve(expr4, var_des_ce[0])
            print('sol4', sol4)
            if var_des_ce[0]==lm:
                widget.lineEdit_lm_bp1.setText(str(round(sol4[0],5)))
            elif var_des_ce[0]==v:
                widget.lineEdit_v_bp1.setText(str(round(sol4[0],5)))

            elif var_des_ce[0]==lvt:
                widget.lineEdit_lvt_bp1.setText(str(round(sol4[0],5)))

            
        var_quinta=[lvt,k,k1,lvm]
        var_des_qe=[]

        for i in var_quinta:
            if  isinstance(i, sp.core.symbol.Symbol):
                var_des_qe.append(i)
        ec5=lvt*k*k1-lvm
        expr5=(sp.parse_expr(str(ec5)))
        
        if len(var_des_qe)==1:
            sol5=sp.solve(expr5, var_des_qe[0])
            if var_des_qe[0]==lvt:
                widget.lineEdit_lvt_bp1.setText(str(round(sol5[0],5)))
            
            elif var_des_qe[0]==k:
                widget.lineEdit_k_bp1.setText(str(round(sol5[0],5)))

            elif var_des_qe[0]==k1:
                widget.lineEdit_k1_bp1.setText(str(round(sol5[0],5)))
            
            elif var_des_qe[0]==lvm:
                widget.lineEdit_lvm_bp1.setText(str(round(sol5[0],5)))

        #sexta ecuacion
        var_sexta=[s,A1,A2]
        var_des_se=[]
        for i in var_sexta:
            if  isinstance(i, sp.core.symbol.Symbol):
                var_des_se.append(i)
        ec6=A1+A2-s
        expr6=sp.parse_expr(str(ec6))
        if len(var_des_se)==1:
            sol6=sp.solve(expr6,var_des_se[0])
            print('sol6', sol6)


            for i in var_sexta:
                if i==var_des_se[0]:
                    o=str(i)

                    eval(f"widget.lineEdit_{i}_bp1.setText(str(round(sol6[0], 5)))")





    def calculate_2(self):
        widget=self.ui

        fu=widget.lineEdit_fu_bp2.text()
        l=widget.lineEdit_l_bp2.text()
        cq=widget.lineEdit_cq_bp2.text()
        ct=widget.lineEdit_ct_bp2.text()
        f=widget.lineEdit_f_bp2.text()
        qb=widget.lineEdit_qb_bp2.text()
        qg=widget.lineEdit_qg_bp2.text()
        qru=widget.lineEdit_qru_bp2.text()
        qro=widget.lineEdit_qro_bp2.text()
        h=widget.lineEdit_h_bp2.text()
        v=widget.lineEdit_v_bp2.text()
        n=widget.lineEdit_n_bp2.text()
        p=widget.lineEdit_p_bp2.text()
        pprs=widget.lineEdit_pprs_bp2.text()
        ao=widget.lineEdit_ao_bp2.text()
        ppri=widget.lineEdit_ppri_bp2.text()
        au=widget.lineEdit_au_bp2.text()
        t1=widget.lineEdit_t1_bp2.text()
        t2=widget.lineEdit_t2_bp2.text()
        fa=widget.lineEdit_fa_bp2.text()
        cw=widget.lineEdit_cw_bp2.text()
        t3=widget.lineEdit_t3_bp2.text()




        if fu=='':
            fu=sp.Symbol('fu')
        else:
            fu=float(widget.lineEdit_fu_bp2.text())

        if l=='':
            l=sp.Symbol('l')
        else:
            l=float(widget.lineEdit_l_bp2.text())
        
        if cq=='':
            cq=sp.Symbol('cq')
        else:
            cq=float(widget.lineEdit_cq_bp2.text())
        
        if ct=='':
            ct=sp.Symbol('ct')
        else:
            ct=float(widget.lineEdit_ct_bp2.text())

        if f=='':
            f=sp.Symbol('f')
        else:
            f=float(widget.lineEdit_f_bp2.text())
        
        if qb=='':
            qb=sp.Symbol('qb')
        else:
            qb=float(widget.lineEdit_qb_bp2.text())

        if qg=='':
            qg=sp.Symbol('qg')
        else:
            qg=float(widget.lineEdit_qg_bp2.text())

        if qru=='':
            qru=sp.Symbol('qru')
        else:
            qru=float(widget.lineEdit_qru_bp2.text())
        
        if qro=='':
            qro=sp.Symbol('qro')
        else:
            qro=float(widget.lineEdit_qro_bp2.text())
        
        if h=='':
            h=sp.Symbol('h')
        else:
            h=float(widget.lineEdit_h_bp2.text())

        if v=='':
            v=sp.Symbol('v')
        else:
            v=float(widget.lineEdit_v_bp2.text())
        
        if n=='':
            n=sp.Symbol('n')
        else:
            n=float(widget.lineEdit_n_bp2.text())

        if p=='':
            p=sp.Symbol('p')
        else:
            p=float(widget.lineEdit_p_bp2.text())
        
        if pprs=='':
            pprs=sp.Symbol('pprs')
        else:
            pprs=float(widget.lineEdit_pprs_bp2.text())
        
        if ao=='':
            ao=sp.Symbol('ao')
        else:
            ao=float(widget.lineEdit_ao_bp2.text())
        
        if ppri=='':
            ppri=sp.Symbol('ppri')
        else:
            ppri=float(widget.lineEdit_ppri_bp2.text())
        
        if au=='':
            au=sp.Symbol('au')
        else:
            au=float(widget.lineEdit_au_bp2.text())

        if t1=='':
            t1=sp.Symbol('t1')
        else:
            t1=float(widget.lineEdit_t1_bp2.text())
        
        if t2=='':
            t2=sp.Symbol('t2')
        else:
            t2=float(widget.lineEdit_t2_bp2.text())
        
        if fa=='':
            fa=sp.Symbol('fa')
        else:
            fa=float(widget.lineEdit_fa_bp2.text())
        
        if cw=='':
            cw=sp.Symbol('cw')
        else:
            cw=float(widget.lineEdit_cw_bp2.text())


        if widget.lineEdit_t3_bp2.text()=='':
            t3=sp.Symbol('t3')
        else:
            t3=float(widget.lineEdit_t3_bp2.text())

        if widget.lineEdit_fr_bp2.text()=='':
            fr=sp.Symbol('fr')
        else:
            fr=float(widget.lineEdit_fr_bp2.text())

        if widget.lineEdit_t0_bp2.text()=='':
            t0=sp.Symbol('t0')
        else:
            t0=float(widget.lineEdit_t0_bp2.text())

        if widget.lineEdit_tg_bp2.text()=='':
            tg=sp.Symbol('tg')
        else:
            tg=float(widget.lineEdit_tg_bp2.text())

        if widget.lineEdit_lc_bp2.text()=='':
            lc=sp.Symbol('lc')
        else:
            lc=float(widget.lineEdit_lc_bp2.text())
        
        if widget.lineEdit_ht_bp2.text()=='':
            ht=sp.Symbol('ht')
        else:
            ht=float(widget.lineEdit_ht_bp2.text())
        
        if widget.lineEdit_tumax_bp2.text()=='':
            tumax=sp.Symbol('tumax')
        else:
            tumax=float(widget.lineEdit_tumax_bp2.text())
        
        if widget.lineEdit_tmax_bp2.text()=='':
            tmax=sp.Symbol('tmax')
        else:
            tmax=float(widget.lineEdit_tmax_bp2.text())

        if widget.lineEdit_N_bp2.text()=='':
            N=sp.Symbol('N')
        else:
            N=float(widget.lineEdit_N_bp2.text())
        




        #primera ecuacion

        var_primera=[fu,l,cq,ct,f,qb,qg,qru,qro,h]
        for i in var_primera:
            if isinstance(i, sp.core.symbol.Symbol):
                print ('es variable: ', i)
        

        var_des_pe=[]


        for i in var_primera:
            if isinstance(i, sp.core.symbol.Symbol):
                var_des_pe.append(i)
        if widget.comboBox_tb_bp2.currentText()=="tramo de banda ascendente":
            
            expr1 = sp.Eq(((l * cq * ct * f * (2.0 * qb + qg + qru + qro) + (qg * h)) ), fu)

        elif widget.comboBox_tb_bp2.currentText()=='tramo de banda descendente':
            
            expr1 = sp.Eq(((l * cq * ct * f * (2.0 * qb + qg + qru + qro) - (qg * h)) ), fu)
        
        if len(var_des_pe)==1:
            sol1=sp.solve(expr1, var_des_pe[0])

            for i in var_primera:
                if i==var_des_pe[0]:
                
                    eval(f"widget.lineEdit_{i}_bp2.setText(str(round(sol1[0], 5)))")

        #segunda ecuacion

        var_segunda=[p,fu,n,v]
        var_des_se=[]

        for i in var_segunda:
            if isinstance(i, sp.core.symbol.Symbol):
                var_des_se.append(i)
        ec2=((fu*v)/100*n)-p
        expr2=sp.Eq(((fu*v)/100*n),p)
        if len (var_des_se)==1:
            sol2=sp.solve(expr2, var_des_se[0])
            print('sol2', sol2)
            for i in var_segunda:
                if i==var_des_se[0]:  
                    eval(f"widget.lineEdit_{i}_bp2.setText(str(round(sol2[0], 5)))")

        #tercera ecuacion
        var_tercera=[qro,pprs,ao]
        var_des_te=[]

        for i in var_tercera:
            if isinstance(i, sp.core.symbol.Symbol):
                var_des_te.append(i)
        expr3=sp.Eq((pprs/ao),qro)

        if len (var_des_te)==1:
            sol3=sp.solve(expr3, var_des_te[0])
            print('sol3', sol3)
            for i in var_tercera:
                if i==var_des_te[0]:  
                    eval(f"widget.lineEdit_{i}_bp2.setText(str(round(sol3[0], 5)))")
        
        #cuarta ecuacion

        var_cuarta=[qru, ppri,au]
        var_des_ce=[]

        for i in var_cuarta:
            if isinstance(i, sp.core.symbol.Symbol):
                var_des_ce.append(i)
        expr4=sp.Eq((ppri/au), qru)
        if len (var_des_te)==1:
            sol4=sp.solve(expr4, var_des_ce[0])
            for i in var_tercera:
                if i==var_des_ce[0]:  
                    eval(f"widget.lineEdit_{i}_bp2.setText(str(round(sol4[0], 5)))")
                
        var_quinta=[t1,fu,t2]
        var_des_qe=[]
        expr5=sp.Eq((fu+t2),t1)

        ec6=[[fu+t2,t1],[t1,fu,t2]]
        ec7=[[(fu*(1/(exp(fa)-1))),t2],[fu,fa,t2]]
        ec8=[[((1/(exp(fa)-1))),t3],[fa,cw]]
        ec9=[[(6.25*(qb+qg)*ao*0.981),t0],[qb,qg,ao]]
        ec10=[[(2*t3),tg],[fa,cw]]
        ec11=[[((tmax*10)/N),tumax],[tmax,N,tumax]]
        
        


        #las agregamos a la lista
        lista=[ec6,ec7,ec8,ec9,ec10,ec11]
        print(lista)
        #el resto lo hace el algorimo

        contador=0
        for i in lista:
            contador+=1
            all=i
            variable=all[1]
            expr88=all[0][0]
           

            print('variables', variable)
            print('expresion', expr88)
            var_des_xe=[]
            expr11=sp.Eq(expr88,all[0][1])
            print('la expresion final es:', expr11)

            for e in variable:
                if isinstance(e, sp.core.symbol.Symbol):
                    var_des_xe.append(e)
            print('variable desconocida:', var_des_xe)

            if len(var_des_xe)==1:
                sol7=sp.solve(expr11,var_des_xe[0])
                print('sol7', sol7)

                for o in variable:
                    if o==var_des_xe[0]:  
                        eval(f"widget.lineEdit_{o}_bp2.setText(str(round(sol7[0], 5)))")
        

        print('variables recien agregadas ', t3,fr, t0,tg,lc,ht,tumax,tmax,N)

        var_doceaba=[t2,lc.cq,ct,f,qb,qru,tg]
        var_des_doceaba=[]


        if widget.comboBox_tb_bp2.currentText()=="tramo de banda ascendente":
            
            expr12=sp.Eq((2*t2+2*((lc*cq*ct*f)*(qb*qru)+(ht*qb))),tg)

        elif widget.comboBox_tb_bp2.currentText()=='tramo de banda descendente':
            
            expr12=sp.Eq((2*t2+2*((lc*cq*ct*f)*(qb*qru)+(ht*qb))),tg)

        for i in var_doceaba:
            if isinstance(i, sp.core.symbol.Symbol):
                var_des_doceaba.append(i)
        
        if len (var_des_doceaba)==1:
            sol12=sp.solve(expr12, var_des_doceaba[0])
            for i in var_doceaba:
                if i==var_des_doceaba[0]:  
                    eval(f"widget.lineEdit_{i}_bp2.setText(str(round(sol12[0], 5)))")
        
    def calculate_3(self):
        widget=self.ui

        mif=widget.lineEdit_mif_bp3.text()
        mf=widget.lineEdit_mf_bp3.text()
        mt=widget.lineEdit_mt_bp3.text()
        w=widget.lineEdit_w_bp3.text()
        u=widget.lineEdit_u_bp3.text()
        d=widget.lineEdit_d_bp3.text()
        cp=widget.lineEdit_cp_bp3.text()
        t1=widget.lineEdit_t1_bp3.text()
        t2=widget.lineEdit_t2_bp3.text()

        if widget.lineEdit_mif_bp3.text()=='':
            mif=sp.Symbol('mif')
        else:
            mif=widget.lineEdit_mif_bp3.text()
        
        if widget.lineEdit_mf_bp3.text()=='':
            mf=sp.Symbol('mf')
        else:
            mf=widget.lineEdit_mf_bp3.text()
        
        if widget.lineEdit_mt_bp3.text()=='':
            mt=sp.Symbol('mt')
        else:
            mt=widget.lineEdit_mt_bp3.text()

        if widget.lineEdit_w_bp3.text()=='':
            w=sp.Symbol('w')
        else:
            w=widget.lineEdit_w_bp3.text()
        
        if widget.lineEdit_u_bp3.text()=='':
            u=sp.Symbol('u')
        else:
            u=widget.lineEdit_u_bp3.text()

        if widget.lineEdit_d_bp3.text()=='':
            d=sp.Symbol('d')
        else:
            d=widget.lineEdit_d_bp3.text()
        
        if widget.lineEdit_cp_bp3.text()=='':
            cp=sp.Symbol('cp')
        else:
            cp=widget.lineEdit_cp_bp3.text()
        
        if widget.lineEdit_t1_bp3.text()=='':
            t1=sp.Symbol('t1')
        else:
            t1=widget.lineEdit_t1_bp3.text()

        
        if widget.lineEdit_t2_bp3.text()=='':
            t2=sp.Symbol('t2')
        else:
            t2=widget.lineEdit_t2_bp3.text()
        
        if widget.lineEdit_qt_bp3.text()=='':
            qt=sp.Symbol('qt')
        else:
            qt=widget.lineEdit_qt_bp3.text()
        
        if widget.lineEdit_p_bp3.text()=='':
            p=sp.Symbol('p')
        else:
            p=widget.lineEdit_p_bp3.text()
        

        if widget.lineEdit_n_bp3.text()=='':
            n=sp.Symbol('n')
        else:
            n=widget.lineEdit_n_bp3.text()
        
        if widget.lineEdit_cpr_bp3.text()=='':
            cpr=sp.Symbol('cpr')
        else:
            cpr=widget.lineEdit_cpr_bp3.text()
        
        if widget.lineEdit_ft_bp3.text()=='':
            ft=sp.Symbol('ft')
        else:
            ft=widget.lineEdit_ft_bp3.text()

        if widget.lineEdit_ao_bp3.text()=='':
            ao=sp.Symbol('ao')
        else:
            ao=widget.lineEdit_ao_bp3.text()
        
        if widget.lineEdit_au_bp3.text()=='':
            au=sp.Symbol('au')
        else:
            au=widget.lineEdit_au_bp3.text()
        
        if widget.lineEdit_qb_bp3.text()=='':
            qb=sp.Symbol('qb')
        else:
            qb=widget.lineEdit_qb_bp3.text()
        
        if widget.lineEdit_lv_bp3.text()=='':
            lv=sp.Symbol('lv')
        else:
            lv=widget.lineEdit_lv_bp3.text()
        
        if widget.lineEdit_c_bp3.text()=='':
            c=sp.Symbol('c')
        else:
            c=widget.lineEdit_c_bp3.text()

        if widget.lineEdit_ot_bp3.text()=='':
            ot=sp.Symbol('ot')
        else:
            ot=widget.lineEdit_ot_bp3.text()
        
        if widget.lineEdit_ag_bp3.text()=='':
            ag=sp.Symbol('ag')
        else:
            ag=widget.lineEdit_ag_bp3.text()
        
        if widget.lineEdit_ee_bp3.text()=='':
            ee=sp.Symbol('ee')
        else:
            ee=widget.lineEdit_ee_bp3.text()

        if widget.lineEdit_j_bp3.text()=='':
            j=sp.Symbol('j')
        else:
            j=widget.lineEdit_j_bp3.text()
        
        if widget.lineEdit_v_bp3.text()=='':
            v=sp.Symbol('v')
        else:
            v=widget.lineEdit_v_bp3.text()
        
        if widget.lineEdit_D_bp3.text()=='':
            D=sp.Symbol('D')
        else:
            D=widget.lineEdit_D_bp3.text()
        
        if widget.lineEdit_Ca_bp3.text()=='':
            Ca=sp.Symbol('Ca')
        else:
            CaD=widget.lineEdit_Ca_bp3.text()
        
        if widget.lineEdit_Ca1_bp3.text()=='':
            Ca1=sp.Symbol('Ca1')
        else:
            Ca1=widget.lineEdit_Ca1_bp3.text()
        
        if widget.lineEdit_ca_bp3.text()=='':
            ca=sp.Symbol('ca')
        else:
            ca=widget.lineEdit_ca_bp3.text()
        
        if widget.lineEdit_fd_bp3.text()=='':
            fd=sp.Symbol('fd')
        else:
            fd=widget.lineEdit_fd_bp3.text()

        if widget.lineEdit_fs_bp3.text()=='':
            fs=sp.Symbol('fs')
        else:
            fs=widget.lineEdit_fs_bp3.text()
        
        if widget.lineEdit_fm_bp3.text()=='':
            fm=sp.Symbol('fm')
        else:
            fm=widget.lineEdit_fm_bp3.text()
        
        if widget.lineEdit_fp_bp3.text()=='':
            fp=sp.Symbol('fp')
        else:
            fp=widget.lineEdit_fp_bp3.text()
        
        if widget.lineEdit_fv_bp3.text()=='':
            fv=sp.Symbol('fv')
        else:
            fv=widget.lineEdit_fv_bp3.text()
        
        if widget.lineEdit_Cr_bp3.text()=='':
            Cr=sp.Symbol('Cr')
        else:
            Cr=widget.lineEdit_Cr_bp3.text()
        
        if widget.lineEdit_Cr1_bp3.text()=='':
            Cr1=sp.Symbol('Cr1')
        else:
            Cr1=widget.lineEdit_Cr1_bp3.text()
        
        if widget.lineEdit_cr_bp3.text()=='':
            cr=sp.Symbol('cr')
        else:
            cr=widget.lineEdit_cr_bp3.text()
        

        if widget.lineEdit_b_bp3.text()=='':
            b=sp.Symbol('b')
        else:
            b=widget.lineEdit_b_bp3.text()

        ec1=[[sp.sqrt(sp.Pow(mf,2)+0.75*sp.Pow(mt,2)),mif],[mf,mt,mif]]
        ec2=[[((mif*1000)/u),w],[mif,u,w]]
        ec3=[[((3.1416/32)*sp.cbrt(d)),w],[d]]
        ec3=[[(sp.sqrt(sp.Pow(t1+t2,2)+sp.Pow(qt,2))),cp],[t1,t2,cp]]
        ec4=[[((cp/2)*ag),mf],[cp,ag,mf]]
        ec5=[[((p/n)*954.9),mt],[p,n,mt]]
        ec6=[[(cpr*ag/2),mf],[cpr,ag,mf]]
        ec7=[[(mf*1000/u),w],[mf,u,w]]
        ec8=[[(sp.cbrt(w*32/3.1416)),d],[d,w]]
        ec9=[[(((cpr/2)*ag/24*ee*j)*(3*(sp.Pow(b+2*ag,2))-4*sp.Pow(ag,2))),ft],[cpr,ag,ee,j,b,ft]]
        ec10=[[(((cpr/2)/2*ee*j)*ag*(c-ag)),ot],[cpr,ee,j,ag,c,ot]]
        ec11=[[((v*1000*60)/(D*3.1416)),n],[v,D,n]]
        ec12=[[(ao*(qb+(lv/3.6*v))*0.981),Ca],[ao,qb,lv,Ca]]
        ec13=[[(Ca*fd*fs*fm),Ca1],[Ca,fd,fs,fm,Ca1]]
        ec14=[[(Ca1*fp),ca],[Ca1,fp,ca]]
        ec15=[[(au*qb*0.981),Cr],[au,qb,Cr]]
        ec16=[[(Cr*fs*fm*fv),Cr1],[Cr,fs,fm,Cr1]]
        ec17=[[(Cr1*fp),cr],[Cr1,fp,cr]]

        #ec6=[[fu+t2,t1],[t1,fu,t2]]


        #las agregamos a la lista
        lista=[ec6,ec7,ec8,ec9,ec10,ec11]
        print(lista)
        #el resto lo hace el algorimo

        contador=0
        for i in lista:
            contador+=1
            all=i
            variable=all[1]
            expr88=all[0][0]
           

            print('variables', variable)
            print('expresion', expr88)
            var_des_xe=[]
            expr11=sp.Eq(expr88,all[0][1])
            print('la expresion final es:', expr11)

            for e in variable:
                if isinstance(e, sp.core.symbol.Symbol):
                    var_des_xe.append(e)
            print('variable desconocida:', var_des_xe)

            if len(var_des_xe)==1:
                sol1=sp.solve(expr11,var_des_xe[0])
                print('sol1', sol1)

                sol2 = [i.evalf() if i.is_real else i for i in sol1]

                print(sol2)

                sol3 = []

                for i in sol2:
                    if i.is_real and i > 0:
                        sol3.append(i)

                for o in variable:
                    if o==var_des_xe[0]:  
                        eval(f"widget.lineEdit_{o}_bp3.setText(str(round(sol3[0], 5)))")
        



        

        

        

        

        
        
        

        

        
        
        


        




        








        
        




        






        


        

        

        
        


        



        
        














                   
                


        



