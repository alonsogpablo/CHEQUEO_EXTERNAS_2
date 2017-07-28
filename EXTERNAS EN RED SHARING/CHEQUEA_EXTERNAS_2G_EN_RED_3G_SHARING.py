import sqlite3

db=sqlite3.connect('C:\\Desarrollo_Pablo\\CHEQUEO EXTERNAS\\dbext.db')
db.text_factory = str
cursor=db.cursor()

#EXT 2G_EN RED 3G SHARING
cursor.execute('''SELECT EXT2G_3GSHARING.EXTERNALGSMCELL, EXT2G_3GSHARING.cellidentity, EXT2G_3GSHARING.LAC, EXT2G_3GSHARING.MCC, EXT2G_3GSHARING.MNC, EXT2G_3GSHARING.NCC, EXT2G_3GSHARING.BCC, EXT2G_3GSHARING.BCCHFREQUENCY
FROM EXT2G_3GSHARING;''')

celdas=cursor.fetchall()

for celda in celdas:
    externa_valida=1
    def_ext_valida=1
    try:
        externa_eri=celda[0]
        ci_ext=int(celda[1])
        lac_ext=int(celda[2])
        mcc_ext=int(celda[3])
        mnc_ext=int(celda[4])
        ncc_ext=int(celda[5])
        bcc_ext=int(celda[6])
        bcch_ext=int(celda[7])

        externa_valida=1
    except:
        pass
        externa_valida=0
    cursor.execute('''
        SELECT ERI2G.GsmLocalCellName,  ERI2G.GsmCellId,ERI2G.Lac, ERI2G.Ncc, ERI2G.Bcc, ERI2G.Bcch,ERI2G.Mcc,ERI2G.Mnc, ERI2G.Bsc FROM ERI2G
         WHERE (((ERI2G.GsmLocalCellName)="'''+externa_eri+'"));')
    try:
        def_externa_eri=cursor.fetchone()
        def_externa_eri_ci = int(def_externa_eri[1])
        def_externa_eri_lac=int(def_externa_eri[2])
        def_externa_eri_ncc = int(def_externa_eri[3])
        def_externa_eri_bcc = int(def_externa_eri[4])
        def_externa_eri_bcch = int(def_externa_eri[5])
        def_externa_eri_mcc = int(def_externa_eri[6])
        def_externa_eri_mnc = int(def_externa_eri[7])
        def_externa_eri_mnc = int(def_externa_eri[8])
        def_ext_valida = 1
    except:
        pass
        def_ext_valida=0

    if externa_valida==1 and def_ext_valida==1:

        if bcch_ext-def_externa_eri_bcch<>0: print ' BCCH EN DEF EXTERNA: '+ celda[0],str(bcch_ext)+ '  BCCH EN RED: '+ externa_eri, def_externa_eri_bcch
        if lac_ext - def_externa_eri_lac <> 0: print  ' LAC EN DEF EXTERNA: ' + celda[0]+str(lac_ext) + '  LAC EN RED: ' + externa_eri, def_externa_eri_lac
        if ci_ext - def_externa_eri_ci <> 0: print ' CI EN DEF EXTERNA: ' + celda[0],str(celda[2]) + '  CI EN RED: ' + externa_eri, def_externa_eri_ci
        if ncc_ext - def_externa_eri_ncc <> 0: print  ' NCC EN DEF EXTERNA: ' + celda[0], str(celda[6]) + '  NCC EN RED: ' + externa_eri, def_externa_eri_ncc
        if bcc_ext - def_externa_eri_bcc <> 0: print ' BCC EN DEF EXTERNA: ' + celda[0], str(celda[7]) + '  BCC EN RED: ' + externa_eri, def_externa_eri_bcc
        if mcc_ext - def_externa_eri_mcc <> 0: print  ' MCC EN DEF EXTERNA: ' + celda[0], str(celda[4]) + '  MCC EN RED: ' + externa_eri, def_externa_eri_mcc
        if mnc_ext - def_externa_eri_mnc <> 0: print  ' MNC EN DEF EXTERNA: ' + celda[0], str(celda[5]) + '  MNC EN RED: ' + externa_eri, def_externa_eri_mnc


    cursor.execute('''
        SELECT HUA_2G.GsmLocalCellName,  HUA_2G.GsmLocalCellId,HUA_2G.LAC, HUA_2G.NCC, HUA_2G.BCC, HUA_2G.BCCH,HUA_2G.MCC,HUA_2G.MNC,HUA_2G.BSC FROM HUA_2G
         WHERE (((HUA_2G.GsmLocalCellName)="'''+externa_eri+'"));')
    try:
        def_externa_eri=cursor.fetchone()
        def_externa_eri_ci = int(def_externa_eri[1])
        def_externa_eri_lac=int(def_externa_eri[2])
        def_externa_eri_ncc = int(def_externa_eri[3])
        def_externa_eri_bcc = int(def_externa_eri[4])
        def_externa_eri_bcch = int(def_externa_eri[5])
        def_externa_eri_mcc = int(def_externa_eri[6])
        def_externa_eri_mnc = int(def_externa_eri[7])
        def_externa_eri_bsc = def_externa_eri[8]

        def_ext_valida = 1
    except:
        pass
        def_ext_valida=0

    if externa_valida==1 and def_ext_valida==1:

        if bcch_ext-def_externa_eri_bcch<>0: print  ' BCCH EN DEF EXTERNA: '+ celda[0],str(bcch_ext)+ '  BCCH EN RED: '+ externa_eri, def_externa_eri_bcch
        if lac_ext - def_externa_eri_lac <> 0: print ' LAC EN DEF EXTERNA: ' + celda[0]+str(lac_ext) + '  LAC EN RED: ' + externa_eri, def_externa_eri_lac
        if ci_ext - def_externa_eri_ci <> 0: print  ' CI EN DEF EXTERNA: ' + celda[0],str(celda[2]) + '  CI EN RED: ' + externa_eri, def_externa_eri_ci
        if ncc_ext - def_externa_eri_ncc <> 0: print  ' NCC EN DEF EXTERNA: ' + celda[0], str(celda[6]) + '  NCC EN RED: ' + externa_eri, def_externa_eri_ncc
        if bcc_ext - def_externa_eri_bcc <> 0: print ' BCC EN DEF EXTERNA: ' + celda[0], str(celda[7]) + '  BCC EN RED: ' + externa_eri, def_externa_eri_bcc
        if mcc_ext - def_externa_eri_mcc <> 0: print ' MCC EN DEF EXTERNA: ' + celda[0], str(celda[4]) + '  MCC EN RED: ' + externa_eri, def_externa_eri_mcc
        if mnc_ext - def_externa_eri_mnc <> 0: print  ' MCC EN DEF EXTERNA: ' + celda[0], str(celda[5]) + '  MNC EN RED: ' + externa_eri, def_externa_eri_mnc



db.commit()
db.close()