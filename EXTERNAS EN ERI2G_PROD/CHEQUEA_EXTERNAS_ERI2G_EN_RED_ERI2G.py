import sqlite3
import csv

db=sqlite3.connect('C:\\CHEQUEO EXTERNAS\\dbext.db')
db.text_factory = str
cursor=db.cursor()

f=open('C:\\CHEQUEO EXTERNAS\\CORRECCIONES_EXT_ERI2G_EN_RED_ERI2G.csv','wb')
writer=csv.writer(f,delimiter=',')
fila=['CONTROLLER DONDE SE DEFINE EXTERNA','EXTERNA','PARAMETRO','VALOR EN DEF EXTERNA','VALOR EN RED']
writer.writerow(fila)

#EXT 2G_ERI2G
cursor.execute('''SELECT EXT_2G_ERI2G.ExternalGsmCellName, EXT_2G_ERI2G.BSC, EXT_2G_ERI2G.LocalCellId, EXT_2G_ERI2G.Lac, EXT_2G_ERI2G.Mcc, EXT_2G_ERI2G.Mnc, EXT_2G_ERI2G.NCC, EXT_2G_ERI2G.BCC, EXT_2G_ERI2G.BCCH,EXT_2G_ERI2G.Vendor
FROM EXT_2G_ERI2G;''')

celdas=cursor.fetchall()

for celda in celdas:
    if celda[9]=='Ericsson':
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
        SELECT ERI2G.GsmLocalCellName,  ERI2G.GsmCellId,ERI2G.Lac, ERI2G.Ncc, ERI2G.Bcc, ERI2G.Bcch,ERI2G.Mcc,ERI2G.Mnc FROM ERI2G
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
            def_ext_valida = 1
        except:
            pass
            def_ext_valida=0

        if externa_valida==1 and def_ext_valida==1:




            if bcch_ext-def_externa_eri_bcch<>0: writer.writerow([bsc_donde_se_define_ext,str(externa_eri),'BCCH',str(bcch_ext),str(def_externa_eri_bcch)])
            if lac_ext - def_externa_eri_lac <> 0: writer.writerow ([bsc_donde_se_define_ext,str(externa_eri),'LAC',str(lac_ext),(def_externa_eri_lac)])
            if ci_ext - def_externa_eri_ci <> 0: writer.writerow([bsc_donde_se_define_ext,str(externa_eri),'CI',str(ci_ext),(def_externa_eri_ci)])
            if ncc_ext - def_externa_eri_ncc <> 0: writer.writerow([bsc_donde_se_define_ext,str(externa_eri),'NCC', str(ncc_ext), str(def_externa_eri_ncc)])
            if bcc_ext - def_externa_eri_bcc <> 0: writer.writerow([bsc_donde_se_define_ext,str(externa_eri),'BCC', str(bcc_ext),str(def_externa_eri_bcc)])
            if mcc_ext - def_externa_eri_mcc <> 0: writer.writerow([bsc_donde_se_define_ext,str(externa_eri),'MCC', str(mcc_ext),str(def_externa_eri_mcc)])
            if mnc_ext - def_externa_eri_mnc <> 0: writer.writerow([bsc_donde_se_define_ext,str(externa_eri),'MNC', str(mnc_ext),str(def_externa_eri_mnc)])


db.commit()
db.close()