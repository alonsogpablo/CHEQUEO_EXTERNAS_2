import os
from os.path import join

path='C:\\Desarrollo_Pablo\\CHEQUEO EXTERNAS'

from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]

for file in onlyfiles:
    newname=file[10:][:-22]+'.csv'
    os.rename(os.path.join(path, file), os.path.join(path, newname))