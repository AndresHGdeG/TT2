import os
import glob
import pandas as pd
from os.path import join

#Get current pathfile
os.chdir(os.getcwd())
extension = 'csv'
files = [i for i in glob.glob('*.{}'.format(extension))]

#print(len(files))
#while(len(files) <7):
#	files = [i for i in glob.glob('*.{}'.format(extension))]

if(len(files)>0):
	allFiles = pd.concat([pd.read_csv(f) for f in files])
	if(len(allFiles)>0):

		allFiles.to_csv( "Clasificador/noticias.csv", index=False)
	else:

		file=open("Clasificador/tiempoagotado.txt","w+")
		file.write("Se ha agotado el tiempo de recolección, sin encontrar alguna")
		file.close()

else:
		file=open("Clasificador/tiempoagotado.txt","w+")
		file.write("Se ha agotado el tiempo de recolección, sin encontrar alguna")
		file.close()
