import sys
from sklearn.feature_extraction.text import CountVectorizer#esta libreria nos permite extraer las caracteristicas de las noticias formando un espacio vectorial por cada una  
import pandas as pd #esta libreria nos permite extraer datos de archivos csv

import pickle


#--------------------------------------MAIN()----------------------------------#

if len(sys.argv)<4:
	print ("Se debe incluir <NombreAlgoritmo> <RutaNoticias> <Modo Binario(1)/Frecuencia(0)> enla linea de comandos")
	sys.exit(2)

modelo=sys.argv[1]# Es el nombre del algoritmo, NaiveBayes, RegresionLogistica,RandomForest y MSV
ruta=sys.argv[2] #Es la ruta del corpus
modoBinario=int(sys.argv[3])

clf=pickle.load(open(modelo,'rb'))#Se crea la instacia CLF quien genera el modelo del algoritmo

data=pd.read_csv(ruta, sep='&&&&&',engine='python') #se cargan los datos de archivo csv

noticias=data['noticia']# se extrae todas las noticias de la columna noticia
seccion=data['seccion']# se extraen las secciones correspondientes a cada noticia
 
#print (data)
#print(noticias)

vectorizer=CountVectorizer(binary=modoBinario)
X=vectorizer.fit_transform(noticias) #se extraer las caracteristicas de las noticias 
Y=seccion #Se extraen las secciones correspondientes a cada noticia

