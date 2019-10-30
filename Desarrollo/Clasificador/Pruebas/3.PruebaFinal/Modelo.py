import sys
from sklearn.feature_extraction.text import CountVectorizer#esta libreria nos permite extraer las caracteristicas de las noticias formando un espacio vectorial por cada una  
from sklearn.metrics import classification_report
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


Y_predic=clf.predict(X)
Y_real=seccion
etiquetas=['Deportes','Economía','Política','Cultura','Ciencia y Tecnología']

accuracyP=accuracy_score(Y_real,Y_predic) # Se calcula la precicion


print("accuracyP: "+str(accuracyP))
scores=classification_report(Y_real,Y_predic,target_names=etiquetas)

nombreTXT="Score_PruebaFinal.txt"
file=open(nombreTXT,'w+')
file.write(scores)
file.close

print(scores)