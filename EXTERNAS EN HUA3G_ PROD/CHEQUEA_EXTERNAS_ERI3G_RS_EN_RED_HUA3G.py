import sqlite3

db=sqlite3.connect('C:\\Desarrollo_Pablo\\CHEQUEO EXTERNAS\\dbext.db')
db.text_factory = str
cursor=db.cursor()

#EXT 3G_HUA3G
cursor.execute('''SELECT EXT_3G_HUA3G.ExternalUtranCellNameStandard, EXT_3G_HUA3G.global_ControllerName, EXT_3G_HUA3G.ExternalUtranCellId, EXT_3G_HUA3G.ExternalUtranCellLAC, EXT_3G_HUA3G.ExternalUtranCellMcc, EXT_3G_HUA3G.ExternalUtranCellMnc, EXT_3G_HUA3G.ExternalUtranCellRac, EXT_3G_HUA3G.TargetPSC,EXT_3G_HUA3G.global_Vendor,EXT_3G_HUA3G.TargetUARFCN
FROM EXT_3G_HUA3G;''')

celdas=cursor.fetchall()

for celda in celdas:

    if celda[8]=='Orange-Ericsson':
        externa_valida=1
        def_ext_valida=1
        try:
            externa_eri=celda[0]
            rnc_ext = celda[1]
            ci_ext=int(celda[2])
            lac_ext=int(celda[3])
            mcc_ext=int(celda[4])
            mnc_ext=int(celda[5])
            rac_ext=int(celda[6])
            psc_ext=int(celda[7])
            vendor_ext=celda[8]
            dl_uarfcn_ext = int(celda[9])
            externa_valida=1
        except:
            pass
            externa_valida=0

        cursor.execute('''
        SELECT ERI_3G_RS.LocalCellName,  ERI_3G_RS.UtranCellId,ERI_3G_RS.Lac, ERI_3G_RS.PSC,ERI_3G_RS.Mcc,ERI_3G_RS.Mnc, ERI_3G_RS.UARFCN_DL, ERI_3G_RS.Rnc FROM ERI_3G_RS
         WHERE (((ERI_3G_RS.LocalCellName)="'''+externa_eri+'"));')
        try:
            def_externa_eri=cursor.fetchone()
            def_externa_eri_ci = int(def_externa_eri[1])
            def_externa_eri_lac=int(def_externa_eri[2])
            def_externa_eri_psc = int(def_externa_eri[3])
            def_externa_eri_mcc = int(def_externa_eri[4])
            def_externa_eri_mnc = int(def_externa_eri[5])
            def_externa_eri_uarfcndl = int(def_externa_eri[6])
            def_externa_eri_rnc = def_externa_eri[7]
            def_ext_valida = 1

        except:
            pass
            def_ext_valida=0

        if externa_valida==1 and def_ext_valida==1:

            if psc_ext-def_externa_eri_psc<>0: print 'PSC EN DEF EXTERNA: '+ externa_eri,str(psc_ext)+ '  PSC EN RED: '+ externa_eri, def_externa_eri_psc
            if lac_ext - def_externa_eri_lac <> 0: print 'LAC EN DEF EXTERNA: ' + externa_eri,str(lac_ext) + '  LAC EN RED: ' + externa_eri, def_externa_eri_lac
            if ci_ext - def_externa_eri_ci <> 0: print 'CI EN DEF EXTERNA: ' + externa_eri,str(ci_ext) + '  CI EN RED: ' + externa_eri, def_externa_eri_ci
            if mcc_ext - def_externa_eri_mcc <> 0: print 'MCC EN DEF EXTERNA: ' + externa_eri,str(mcc_ext) + '  MCC EN RED: ' + externa_eri, def_externa_eri_mcc
            if mnc_ext - def_externa_eri_mnc <> 0: print 'MNC EN DEF EXTERNA: ' + externa_eri,str(mnc_ext) + '  MNC EN RED: ' + externa_eri, def_externa_eri_mnc
            if rnc_ext <> def_externa_eri_rnc: print 'RNC EN DEF EXTERNA: ' + externa_eri, str(rnc_ext) + '  RNC EN RED: ' + externa_eri, def_externa_eri_rnc

db.commit()
db.close()