import csv,sqlite3,pandas

db=sqlite3.connect('C:\\Desarrollo_Pablo\\CHEQUEO EXTERNAS\\dbext.db')
db.text_factory = str
cursor=db.cursor()


#IMPORTA EXTERNAS


#IMPORTA EXT2G_ERI2G
df = pandas.read_csv('C:\\Desarrollo_Pablo\\CHEQUEO EXTERNAS\\Ericsson_2G_External_Gsm_Cells.csv',sep=';')
try:cursor.execute('''DROP TABLE EXT_2G_ERI2G''')
except:pass
df.to_sql('EXT_2G_ERI2G', db, if_exists='append', index=False)

#IMPORTA EXT3G_ERI2G
df = pandas.read_csv('C:\\Desarrollo_Pablo\\CHEQUEO EXTERNAS\\Ericsson_2G_External_Utran_Cells.csv',sep=';')
try: cursor.execute('''DROP TABLE EXT_3G_ERI2G''')
except:pass
df.to_sql('EXT_3G_ERI2G', db, if_exists='append', index=False)

#IMPORTA ERI_2G
df = pandas.read_csv('C:\\Desarrollo_Pablo\\CHEQUEO EXTERNAS\\Ericsson_2G_GSM_Cells.csv',sep=';')
try:cursor.execute('''DROP TABLE ERI2G''')
except:pass
df.to_sql('ERI2G', db, if_exists='append', index=False)

#IMPORTA ERI_2G_RS
df = pandas.read_csv('C:\\Desarrollo_Pablo\\CHEQUEO EXTERNAS\\Orange-Ericsson_2G_GSM_Cells.csv',sep=';')
try:cursor.execute('''DROP TABLE ERI2G_RS''')
except:pass
df.to_sql('ERI2G_RS', db, if_exists='append', index=False)


#IMPORTA EXT2G_ERI3G
df = pandas.read_csv('C:\\Desarrollo_Pablo\\CHEQUEO EXTERNAS\\Ericsson_3G_External_Gsm_Cells.csv',sep=';')
try:cursor.execute('''DROP TABLE EXT_2G_ERI3G''')
except:pass
df.to_sql('EXT_2G_ERI3G', db, if_exists='append', index=False)

#IMPORTA EXT3G_ERI3G
df = pandas.read_csv('C:\\Desarrollo_Pablo\\CHEQUEO EXTERNAS\\Ericsson_3G_External_Utran_Cells.csv',sep=';')
try:cursor.execute('''DROP TABLE EXT_3G_ERI3G''')
except:pass
df.to_sql('EXT_3G_ERI3G', db, if_exists='append', index=False)

#IMPORTA EXT2G_HUA3G
df = pandas.read_csv('C:\\Desarrollo_Pablo\\CHEQUEO EXTERNAS\\Huawei_3G_External_Gsm_Cells.csv',sep=';')
try:cursor.execute('''DROP TABLE EXT_2G_HUA3G''')
except:pass
df.to_sql('EXT_2G_HUA3G', db, if_exists='append', index=False)

#IMPORTA EXT3G_HUA3G
df = pandas.read_csv('C:\\Desarrollo_Pablo\\CHEQUEO EXTERNAS\\Huawei_3G_External_Utran_Cells.csv',sep=';')
try:cursor.execute('''DROP TABLE EXT_3G_HUA3G''')
except:pass
df.to_sql('EXT_3G_HUA3G', db, if_exists='append', index=False)

#IMPORTA EXT2G_HUA2G
df = pandas.read_csv('C:\\Desarrollo_Pablo\\CHEQUEO EXTERNAS\\Huawei_2G_All_GSM_External_Cells.csv',sep=';')
try:cursor.execute('''DROP TABLE EXT_2G_HUA2G''')
except:pass
df.to_sql('EXT_2G_HUA2G', db, if_exists='append', index=False)

#IMPORTA EXT3G_HUA2G
df = pandas.read_csv('C:\\Desarrollo_Pablo\\CHEQUEO EXTERNAS\\Huawei_2G_External_Utran_Cells.csv',sep=';')
try:cursor.execute('''DROP TABLE EXT_3G_HUA2G''')
except:pass
df.to_sql('EXT_3G_HUA2G', db, if_exists='append', index=False)


#IMPORTA DATOS DE RED

#IMPORTA HUA_2G
df = pandas.read_csv('C:\\Desarrollo_Pablo\\CHEQUEO EXTERNAS\\Huawei_2G_Gsm_Cells.csv',sep=';')
try:cursor.execute('''DROP TABLE HUA_2G''')
except:pass
df.to_sql('HUA_2G', db, if_exists='append', index=False)

#IMPORTA ERI_3G
df = pandas.read_csv('C:\\Desarrollo_Pablo\\CHEQUEO EXTERNAS\\Ericsson_3G_Utran_Cell.csv',sep=';')
try:cursor.execute('''DROP TABLE ERI_3G''')
except:pass
df.to_sql('ERI_3G', db, if_exists='append', index=False)

#IMPORTA HUA_3G
df = pandas.read_csv('C:\\Desarrollo_Pablo\\CHEQUEO EXTERNAS\\Huawei_3G_Utran_Cells.csv',sep=';')
try:cursor.execute('''DROP TABLE HUA_3G''')
except:pass
df.to_sql('HUA_3G', db, if_exists='append', index=False)

#IMPORTA ERI_3G_RS
df = pandas.read_csv('C:\\Desarrollo_Pablo\\CHEQUEO EXTERNAS\\Orange-Ericsson_3G_Utran_Cells.csv',sep=';')
try:cursor.execute('''DROP TABLE ERI_3G_RS''')
except:pass
df.to_sql('ERI_3G_RS', db, if_exists='append', index=False)

#IMPORTA HUA_3G_RS
df = pandas.read_csv('C:\\Desarrollo_Pablo\\CHEQUEO EXTERNAS\\Orange-Huawei_3G_Utran_Cells.csv',sep=';')
try:cursor.execute('''DROP TABLE HUA_3G_RS''')
except:pass
df.to_sql('HUA_3G_RS', db, if_exists='append', index=False)

#IMPORTA 2G EN 2G SHARING
df = pandas.read_csv('C:\\Desarrollo_Pablo\\CHEQUEO EXTERNAS\\EXT_2G_2G.csv',sep=',')
try:cursor.execute('''DROP TABLE EXT2G_2GSHARING''')
except:pass
df.to_sql('EXT2G_2GSHARING', db, if_exists='append', index=False)

#IMPORTA 2G EN 3G SHARING
df = pandas.read_csv('C:\\Desarrollo_Pablo\\CHEQUEO EXTERNAS\\EXT_3G_2G.csv',sep=',')
try:cursor.execute('''DROP TABLE EXT2G_3GSHARING''')
except:pass
df.to_sql('EXT2G_3GSHARING', db, if_exists='append', index=False)

#IMPORTA 3G EN 2G SHARING
df = pandas.read_csv('C:\\Desarrollo_Pablo\\CHEQUEO EXTERNAS\\EXT_2G_3G.csv',sep=',')
try:cursor.execute('''DROP TABLE EXT3G_2GSHARING''')
except:pass
df.to_sql('EXT3G_2GSHARING', db, if_exists='append', index=False)

#IMPORTA 3G EN 3G SHARING
df = pandas.read_csv('C:\\Desarrollo_Pablo\\CHEQUEO EXTERNAS\\EXT_3G_3G.csv',sep=',')
try:cursor.execute('''DROP TABLE EXT3G_3GSHARING''')
except:pass
df.to_sql('EXT3G_3GSHARING', db, if_exists='append', index=False)

db.commit()
db.close()