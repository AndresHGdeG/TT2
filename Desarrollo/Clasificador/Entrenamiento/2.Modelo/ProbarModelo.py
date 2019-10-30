import sys
from sklearn.feature_extraction.text import CountVectorizer#esta libreria nos permite extraer las caracteristicas de las noticias formando un espacio vectorial por cada una  
import pandas as pd #esta libreria nos permite extraer datos de archivos csv

from sklearn.metrics import accuracy_score
import pickle


#--------------------------------------MAIN()----------------------------------#

if len(sys.argv)<3:
	print ("Se debe incluir <NombreAlgoritmo> <RutaNoticias> enla linea de comandos")
	sys.exit(2)

modelo=sys.argv[1]# Es el nombre del algoritmo, NaiveBayes, RegresionLogistica,RandomForest y MSV
ruta=sys.argv[2] #Es la ruta del corpus

vectorizer,clf=pickle.load(open(modelo,'rb'))#Se crea la instacia CLF quien genera el modelo del algoritmo

data=pd.read_csv(ruta, sep='&&&&&',engine='python') #se cargan los datos de archivo csv

noticias=data['noticia']# se extrae todas las noticias de la columna noticia
seccion=data['seccion']
#print (data)
#print(noticias)

X=vectorizer.transform(noticias) #se extraer las caracteristicas de las noticias 


X_test=clf.predict(X)
Y_test=seccion

accuracyP=accuracy_score(X_test,Y_test) # Se calcula la precicion

print("accuracyP: "+str(accuracyP))