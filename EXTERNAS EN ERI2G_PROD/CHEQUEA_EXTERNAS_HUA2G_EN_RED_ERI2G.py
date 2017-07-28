import sqlite3

db=sqlite3.connect('C:\\Desarrollo_Pablo\\CHEQUEO EXTERNAS\\dbext.db')
db.text_factory = str
cursor=db.cursor()

#EXT 2G_ERI2G
cursor.execute('''SELECT EXT_2G_ERI2G.ExternalGsmCellName, EXT_2G_ERI2G.BSC, EXT_2G_ERI2G.LocalCellId, EXT_2G_ERI2G.Lac, EXT_2G_ERI2G.Mcc, EXT_2G_ERI2G.Mnc, EXT_2G_ERI2G.NCC, EXT_2G_ERI2G.BCC, EXT_2G_ERI2G.BCCH,EXT_2G_ERI2G.Vendor
FROM EXT_2G_ERI2G;''')

celdas=cursor.fetchall()

for celda in celdas:
    if celda[9]=='Huawei':
        externa_valida=1
        def_ext_valida=1
        try:
            externa_hua=celda[0]
            ci_ext=int(celda[2])
            lac_ext=int(celda[3])
            mcc_ext=int(celda[4])
            mnc_ext=int(celda[5])
            ncc_ext=int(celda[6])
            bcc_ext=int(celda[7])
            bcch_ext=int(celda[8])
            externa_valida=1
        except:
            pass
            externa_valida=0
        cursor.execute('''
        SELECT HUA_2G.GsmLocalCellName,  HUA_2G.GsmLocalCellId,HUA_2G.LAC, HUA_2G.NCC, HUA_2G.BCC, HUA_2G.BCCH,HUA_2G.MCC,HUA_2G.MNC FROM HUA_2G
         WHERE (((HUA_2G.GsmLocalCellName)="'''+externa_hua+'"));')
        try:
            def_externa_hua=cursor.fetchone()
            def_externa_hua_ci = int(def_externa_hua[1])
            def_externa_hua_lac=int(def_externa_hua[2])
            def_externa_hua_ncc = int(def_externa_hua[3])
            def_externa_hua_bcc = int(def_externa_hua[4])
            def_externa_hua_bcch = int(def_externa_hua[5])
            def_externa_hua_mcc = int(def_externa_hua[6])
            def_externa_hua_mnc = int(def_externa_hua[7])
            def_ext_valida = 1
        except:
            pass
            def_ext_valida=0

        if externa_valida==1 and def_ext_valida==1:

            if bcch_ext-def_externa_hua_bcch<>0: print 'BCCH EN DEF EXTERNA: '+ celda[0],celda[8]+ '  BCCH EN RED: '+ externa_hua, def_externa_hua_bcch
            if lac_ext - def_externa_hua_lac <> 0: print 'LAC EN DEF EXTERNA: ' + celda[0]+str(lac_ext) + '  LAC EN RED: ' + externa_hua, def_externa_hua_lac
            if ci_ext - def_externa_hua_ci <> 0: print 'CI EN DEF EXTERNA: ' + celda[0],celda[2] + '  CI EN RED: ' + externa_hua, def_externa_hua_ci
            if ncc_ext - def_externa_hua_ncc <> 0: print 'NCC EN DEF EXTERNA: ' + celda[0], celda[6] + '  NCC EN RED: ' + externa_hua, def_externa_hua_ncc
            if bcc_ext - def_externa_hua_bcc <> 0: print 'BCC EN DEF EXTERNA: ' + celda[0], celda[7] + '  BCC EN RED: ' + externa_hua, def_externa_hua_bcc
            if mcc_ext - def_externa_hua_mcc <> 0: print 'MCC EN DEF EXTERNA: ' + celda[0], celda[4] + '  MCC EN RED: ' + externa_hua, def_externa_hua_mcc
            if mnc_ext - def_externa_hua_mnc <> 0: print 'MCC EN DEF EXTERNA: ' + celda[0], celda[5] + '  MNC EN RED: ' + externa_hua, def_externa_hua_mnc
db.commit()
db.close()