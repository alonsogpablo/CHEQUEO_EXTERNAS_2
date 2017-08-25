import os
from os.path import join

path='C:\\CHEQUEO EXTERNAS'

from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]

for file in onlyfiles:
    if file.endswith(".csv"):
        newname=file[10:][:-22]+'.csv'
        os.rename(os.path.join(path, file), os.path.join(path, newname))