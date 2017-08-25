import sqlite3
import csv

db=sqlite3.connect('C:\\CHEQUEO EXTERNAS\\dbext.db')
db.text_factory = str
cursor=db.cursor()

#EXT 2G_2G_SHARING
cursor.execute('''SELECT EXT2G_2GSHARING_HUA.EXT2GCELLNAME, EXT2G_2GSHARING_HUA.SUBSESSION_NEID, EXT2G_2GSHARING_HUA.CI, EXT2G_2GSHARING_HUA.LAC, EXT2G_2GSHARING_HUA.MCC, EXT2G_2GSHARING_HUA.MNC, EXT2G_2GSHARING_HUA.NCC, EXT2G_2GSHARING_HUA.BCC, EXT2G_2GSHARING_HUA.BCCH
FROM EXT2G_2GSHARING_HUA;''')

f=open('C:\\CHEQUEO EXTERNAS\\CORRECCIONES_EXT_ERI2G_EN_RED_HUA2G_SHARING.csv','wb')
writer=csv.writer(f,delimiter=',')
fila=['CONTROLLER DONDE SE DEFINE EXTERNA','EXTERNA','PARAMETRO','VALOR EN DEF EXTERNA','VALOR EN RED']
writer.writerow(fila)

celdas=cursor.fetchall()

for celda in celdas:
    externa_valida=1
    def_ext_valida=1
    try:
        externa_eri=celda[0]
        bsc_donde_se_define_ext=celda[1]
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

        if bcch_ext - def_externa_eri_bcch <> 0: writer.writerow([bsc_donde_se_define_ext, str(externa_eri), 'BCCH', str(bcch_ext), str(def_externa_eri_bcch)])
        if lac_ext - def_externa_eri_lac <> 0: writer.writerow([bsc_donde_se_define_ext, str(externa_eri), 'LAC', str(lac_ext), (def_externa_eri_lac)])
        if ci_ext - def_externa_eri_ci <> 0: writer.writerow([bsc_donde_se_define_ext, str(externa_eri), 'CI', str(ci_ext), (def_externa_eri_ci)])
        if ncc_ext - def_externa_eri_ncc <> 0: writer.writerow([bsc_donde_se_define_ext, str(externa_eri), 'NCC', str(ncc_ext), str(def_externa_eri_ncc)])
        if bcc_ext - def_externa_eri_bcc <> 0: writer.writerow([bsc_donde_se_define_ext, str(externa_eri), 'BCC', str(bcc_ext), str(def_externa_eri_bcc)])
        if mcc_ext - def_externa_eri_mcc <> 0: writer.writerow([bsc_donde_se_define_ext, str(externa_eri), 'MCC', str(mcc_ext), str(def_externa_eri_mcc)])
        if mnc_ext - def_externa_eri_mnc <> 0: writer.writerow([bsc_donde_se_define_ext, str(externa_eri), 'MNC', str(mnc_ext), str(def_externa_eri_mnc)])


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

        if bcch_ext - def_externa_eri_bcch <> 0: writer.writerow([bsc_donde_se_define_ext, str(externa_eri), 'BCCH', str(bcch_ext), str(def_externa_eri_bcch)])
        if lac_ext - def_externa_eri_lac <> 0: writer.writerow([bsc_donde_se_define_ext, str(externa_eri), 'LAC', str(lac_ext), (def_externa_eri_lac)])
        if ci_ext - def_externa_eri_ci <> 0: writer.writerow([bsc_donde_se_define_ext, str(externa_eri), 'CI', str(ci_ext), (def_externa_eri_ci)])
        if ncc_ext - def_externa_eri_ncc <> 0: writer.writerow([bsc_donde_se_define_ext, str(externa_eri), 'NCC', str(ncc_ext), str(def_externa_eri_ncc)])
        if bcc_ext - def_externa_eri_bcc <> 0: writer.writerow([bsc_donde_se_define_ext, str(externa_eri), 'BCC', str(bcc_ext), str(def_externa_eri_bcc)])
        if mcc_ext - def_externa_eri_mcc <> 0: writer.writerow([bsc_donde_se_define_ext, str(externa_eri), 'MCC', str(mcc_ext), str(def_externa_eri_mcc)])
        if mnc_ext - def_externa_eri_mnc <> 0: writer.writerow([bsc_donde_se_define_ext, str(externa_eri), 'MNC', str(mnc_ext), str(def_externa_eri_mnc)])

db.commit()
db.close()