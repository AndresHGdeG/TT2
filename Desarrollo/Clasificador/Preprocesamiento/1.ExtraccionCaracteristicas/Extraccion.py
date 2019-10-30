import sys# permite leer argumentos de la linea de comandos

if len(sys.argv)<2:
	print ("Se debe ingresar el argumento <Ruta/nombreArchivo>")
	sys.exit(2)
	#python Modelo.py '../../Corpus/Pruebas/UnionPrueba.txt'

ruta=sys.argv[1]

from sklearn.feature_extraction.text import CountVectorizer 
import pandas as pd

import pickle




data=pd.read_csv(ruta, sep='&&&&&',engine='python')
noticias=data['noticia']
#print (data)
print(noticias)
vectorizer=CountVectorizer()
X=vectorizer.fit_transform(noticias)
#	#print(vectorizer.get_feature_names())
print("Proceso completado se estan creando 2 archivos donde se escriben las caracteristicas para visualizar el trabajo del algoritmos")
caracteristicas=str(vectorizer.get_feature_names());
#	#print(caracteristicas)
fCaracteristicas=open('caracteristicas.txt','w')
fCaracteristicas.write(caracteristicas)
fCaracteristicas.close()
#
#
f=open('vector.txt','w')
x=X.toarray()
#
for item in x:
	for num in item: 
		numT=str(num)
		f.write(numT)
		f.write(" ")

	f.write("\n\n")
#	
#	
#
#
f.close()
#
print(" se ha creado 2 archivos, 1 con las caracteristicas y otro con los vectores")


