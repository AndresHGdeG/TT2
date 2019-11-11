import os
import glob
import pandas as pd
from os.path import join
import pandas.io.common



def CSVsinNoticias():

	file=open("Clasificador/tiempoagotado.txt","w+")
	file.write("Se ha agotado el tiempo de recolección, sin encontrar alguna")
	file.close()



#Get current pathfile
os.chdir(os.getcwd())
extension = 'csv'
files = [i for i in glob.glob('*.{}'.format(extension))]


#print(len(files))
#while(len(files) <7):
#	files = [i for i in glob.glob('*.{}'.format(extension))]
nonEmptyFiles=['']

if(len(files)>0):

	for f in files:

		try:
			nonEmptyFiles.append(pd.read_csv(f))
		except pandas.io.common.EmptyDataError:
			print(f, " is empty and has been skipped.")

	nonEmptyFiles.remove('')
	print(len(nonEmptyFiles))
	if (len(nonEmptyFiles)>0):

		allFiles = pd.concat([f for f in nonEmptyFiles])
		if(len(allFiles)>0):

			allFiles.to_csv( "Clasificador/noticias.csv", index=False)
		else:
 			CSVsinNoticias()

	else:
		CSVsinNoticias()

else:
	CSVsinNoticias()