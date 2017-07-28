import sqlite3

db=sqlite3.connect('C:\\Desarrollo_Pablo\\CHEQUEO EXTERNAS\\dbext.db')
db.text_factory = str
cursor=db.cursor()

#EXT 2G_HUA2G
cursor.execute('''SELECT EXT_2G_HUA2G.ExternalGsmCellNameStandard, EXT_2G_HUA2G.TargetBscName, EXT_2G_HUA2G.ExternalGsmCellId, EXT_2G_HUA2G.ExternalGsmCellLAC, EXT_2G_HUA2G.ExternalGsmCellMCC, EXT_2G_HUA2G.ExternalGsmCellMNC, EXT_2G_HUA2G.ExternalGsmCellNcc, EXT_2G_HUA2G.ExternalGsmCellBcc, EXT_2G_HUA2G.ExternalGsmCellBcch,EXT_2G_HUA2G.GlobalVendor, EXT_2G_HUA2G.SourceBscName
FROM EXT_2G_HUA2G;''')

celdas=cursor.fetchall()

for celda in celdas:
    if celda[9]=='Huawei':
        externa_valida=1
        def_ext_valida=1
        try:
            externa_hua=celda[0]
            bsc_ext = celda[1]
            ci_ext=int(celda[2])
            lac_ext=int(celda[3])
            mcc_ext=int(celda[4])
            mnc_ext=int(celda[5])
            ncc_ext=int(celda[6])
            bcc_ext=int(celda[7])
            bcch_ext=int(celda[8])
            bsc_origen = celda[10]
            externa_valida=1
        except:
            pass
            externa_valida=0
        cursor.execute('''
        SELECT HUA_2G.GsmLocalCellName,  HUA_2G.GsmLocalCellId,HUA_2G.LAC, HUA_2G.NCC, HUA_2G.BCC, HUA_2G.BCCH,HUA_2G.MCC,HUA_2G.MNC,HUA_2G.BSC FROM HUA_2G
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
            def_externa_hua_bsc = def_externa_hua[8]
            def_ext_valida = 1
        except:
            pass
            def_ext_valida=0

        if externa_valida==1 and def_ext_valida==1:

            if bcch_ext - def_externa_hua_bcch <> 0: print 'BSC ORIGEN: '+bsc_origen+';BCCH EN DEF EXTERNA: ' + str(celda[0]), str(bcc_ext) + '  BCCH EN RED: ' + externa_hua, def_externa_hua_bcch
            if lac_ext - def_externa_hua_lac <> 0: print 'BSC ORIGEN: '+bsc_origen+';LAC EN DEF EXTERNA: ' + str(celda[0]), str(lac_ext) + '  LAC EN RED: ' + externa_hua, def_externa_hua_lac
            if ci_ext - def_externa_hua_ci <> 0: print 'BSC ORIGEN: '+bsc_origen+';CI EN DEF EXTERNA: ' + str(celda[0]), str(ci_ext) + '  CI EN RED: ' + externa_hua, def_externa_hua_ci
            if ncc_ext - def_externa_hua_ncc <> 0: print 'BSC ORIGEN: '+bsc_origen+';NCC EN DEF EXTERNA: ' + str(celda[0]), str(ncc_ext) + '  NCC EN RED: ' + externa_hua, def_externa_hua_ncc
            if bcc_ext - def_externa_hua_bcc <> 0: print 'BSC ORIGEN: '+bsc_origen+';BCC EN DEF EXTERNA: ' + str(celda[0]), str(bcc_ext) + '  BCC EN RED: ' + externa_hua, def_externa_hua_bcc
            if mcc_ext - def_externa_hua_mcc <> 0: print 'BSC ORIGEN: '+bsc_origen+';MCC EN DEF EXTERNA: ' + str(celda[0]), str(mcc_ext) + '  MCC EN RED: ' + externa_hua, def_externa_hua_mcc
            if mnc_ext - def_externa_hua_mnc <> 0: print 'BSC ORIGEN: '+bsc_origen+';MNC EN DEF EXTERNA: ' + str(celda[0]), str(mnc_ext) + '  MNC EN RED: ' + externa_hua, def_externa_hua_mnc
            if bsc_ext <> def_externa_hua_bsc <> 0: print 'BSC ORIGEN: '+bsc_origen+';BSC EN DEF EXTERNA: ' + str(celda[0]), str(bsc_ext) + '  BSC EN RED: ' + externa_hua, def_externa_hua_bsc
db.commit()
db.close()