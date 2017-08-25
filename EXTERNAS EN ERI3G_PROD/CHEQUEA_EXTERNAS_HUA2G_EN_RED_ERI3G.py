import sqlite3
import csv

db=sqlite3.connect('C:\\CHEQUEO EXTERNAS\\dbext.db')
db.text_factory = str
cursor=db.cursor()

f=open('C:\\CHEQUEO EXTERNAS\\CORRECCIONES_EXT_HUA2G_EN_RED_ERI3G.csv','wb')
writer=csv.writer(f,delimiter=',')
fila=['CONTROLLER DONDE SE DEFINE EXTERNA','EXTERNA','PARAMETRO','VALOR EN DEF EXTERNA','VALOR EN RED']
writer.writerow(fila)

#EXT 2G_ERI3G
cursor.execute('''SELECT EXT_2G_ERI3G.ExternalGsmCell, EXT_2G_ERI3G.BSC, EXT_2G_ERI3G.CellId, EXT_2G_ERI3G.LAC, EXT_2G_ERI3G.MCC, EXT_2G_ERI3G.MNC, EXT_2G_ERI3G.NCC, EXT_2G_ERI3G.BCC, EXT_2G_ERI3G.BCCH,EXT_2G_ERI3G.Vendor
FROM EXT_2G_ERI3G;''')

celdas=cursor.fetchall()

for celda in celdas:
    if celda[9]=='Huawei':
        externa_valida=1
        def_ext_valida=1
        try:
            externa_hua=celda[0]
            bsc_donde_se_define_ext = celda[1]
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

            if bcch_ext-def_externa_hua_bcch<>0: writer.writerow(['',str(externa_hua),'BCCH',str(bcch_ext),str(def_externa_hua_bcch)])
            if lac_ext - def_externa_hua_lac <> 0: writer.writerow (['',str(externa_hua),'LAC',str(lac_ext),(def_externa_hua_lac)])
            if ci_ext - def_externa_hua_ci <> 0: writer.writerow(['',str(externa_hua),'CI',str(ci_ext),(def_externa_hua_ci)])
            if ncc_ext - def_externa_hua_ncc <> 0: writer.writerow(['',str(externa_hua),'NCC', str(ncc_ext), str(def_externa_hua_ncc)])
            if bcc_ext - def_externa_hua_bcc <> 0: writer.writerow(['',str(externa_hua),'BCC', str(bcc_ext),str(def_externa_hua_bcc)])
            if mcc_ext - def_externa_hua_mcc <> 0: writer.writerow(['',str(externa_hua),'MCC', str(mcc_ext),str(def_externa_hua_mcc)])
            if mnc_ext - def_externa_hua_mnc <> 0: writer.writerow(['',str(externa_hua),'MNC', str(mnc_ext),str(def_externa_hua_mnc)])

db.commit()
db.close()