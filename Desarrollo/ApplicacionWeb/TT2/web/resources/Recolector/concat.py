import os
import glob
import pandas as pd
from os.path import join

#Get current pathfile
os.chdir(os.getcwd())
extension = 'csv'
files = [i for i in glob.glob('*.{}'.format(extension))]

print(len(files))
while(len(files) <7):
	files = [i for i in glob.glob('*.{}'.format(extension))]

allFiles = pd.concat([pd.read_csv(f) for f in files])

allFiles.to_csv( "noticias.csv", index=False)
