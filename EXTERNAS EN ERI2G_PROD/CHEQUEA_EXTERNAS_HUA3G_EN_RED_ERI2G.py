import sqlite3
import csv

db=sqlite3.connect('C:\\CHEQUEO EXTERNAS\\dbext.db')
db.text_factory = str
cursor=db.cursor()

f=open('C:\\CHEQUEO EXTERNAS\\CORRECCIONES_EXT_HUA3G_EN_RED_ERI2G.csv','wb')
writer=csv.writer(f,delimiter=',')
fila=['CONTROLLER DONDE SE DEFINE EXTERNA','EXTERNA','PARAMETRO','VALOR EN DEF EXTERNA','VALOR EN RED']
writer.writerow(fila)

#EXT 2G_ERI2G
cursor.execute('''SELECT EXT_3G_ERI2G.ExternalUtranCellName, EXT_3G_ERI2G.RNC, EXT_3G_ERI2G.LocalCellId, EXT_3G_ERI2G.Lac, EXT_3G_ERI2G.Mcc, EXT_3G_ERI2G.Mnc, EXT_3G_ERI2G.Rac, EXT_3G_ERI2G.PSC,EXT_3G_ERI2G.Vendor,EXT_3G_ERI2G.DlUarfcn,EXT_3G_ERI2G.BSC
FROM EXT_3G_ERI2G;''')

celdas=cursor.fetchall()

for celda in celdas:

    if celda[8]=='Huawei':
        externa_valida=1
        def_ext_valida=1
        try:
            externa_hua=celda[0]
            rnc_ext = celda[1]
            ci_ext=int(celda[2])
            lac_ext=int(celda[3])
            mcc_ext=int(celda[4])
            mnc_ext=int(celda[5])
            rac_ext=int(celda[6])
            psc_ext=int(celda[7])
            vendor_ext=celda[8]
            dl_uarfcn_ext = int(celda[9])
            bsc_donde_se_define_ext = celda[10]
            externa_valida=1
        except:
            pass
            externa_valida=0

        cursor.execute('''
        SELECT HUA_3G.LocalCellName,  HUA_3G.UtranCellId,HUA_3G.LAC, HUA_3G.PSC,HUA_3G.MCC,HUA_3G.MNC, HUA_3G.UARFCN_DL, HUA_3G.RNC FROM HUA_3G
         WHERE (((HUA_3G.LocalCellName)="'''+externa_hua+'"));')
        try:
            def_externa_hua=cursor.fetchone()
            def_externa_hua_ci = int(def_externa_hua[1])
            def_externa_hua_lac=int(def_externa_hua[2])
            def_externa_hua_psc = int(def_externa_hua[3])
            def_externa_hua_mcc = int(def_externa_hua[4])
            def_externa_hua_mnc = int(def_externa_hua[5])
            def_externa_hua_uarfcndl = int(def_externa_hua[6])
            def_externa_hua_rnc = def_externa_hua[7]
            def_ext_valida = 1

        except:
            pass
            def_ext_valida=0

        if externa_valida==1 and def_ext_valida==1:

            if psc_ext-def_externa_hua_psc<>0: writer.writerow([bsc_donde_se_define_ext,str(externa_hua),'PSC',str(psc_ext),str(def_externa_hua_psc)])
            if lac_ext - def_externa_hua_lac <> 0: writer.writerow([bsc_donde_se_define_ext,str(externa_hua),'LAC',str(lac_ext),str(def_externa_hua_lac)])
            if ci_ext - def_externa_hua_ci <> 0: writer.writerow([bsc_donde_se_define_ext,str(externa_hua),'CI',str(ci_ext),str(def_externa_hua_ci)])
            if mcc_ext - def_externa_hua_mcc <> 0: writer.writerow([bsc_donde_se_define_ext,str(externa_hua),'MCC',str(mcc_ext),str(def_externa_hua_mcc)])
            if mnc_ext - def_externa_hua_mnc <> 0: writer.writerow([bsc_donde_se_define_ext,str(externa_hua),'MNC',str(mnc_ext),str(def_externa_hua_mnc)])
            if rnc_ext <> def_externa_hua_rnc: print writer.writerow([bsc_donde_se_define_ext,str(externa_hua),'RNC',str(rnc_ext),str(def_externa_hua_rnc)])

db.commit()
db.close()