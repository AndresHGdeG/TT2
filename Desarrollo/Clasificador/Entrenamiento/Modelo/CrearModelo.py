import sys
from sklearn.feature_extraction.text import CountVectorizer#esta libreria nos permite extraer las caracteristicas de las noticias formando un espacio vectorial por cada una  
import pandas as pd #esta libreria nos permite extraer datos de archivos csv

import pickle

#from joblib import dump#permite generar la persistencia del modelo entrenado
#from joblib import load#permite cargar el modelo entrenado
#pip install joblib:
#import joblib
#--------------------------------------FUNCIONES()-----------------------------#

def importarAlgoritmo(algoritmo):
	if algoritmo=="NaiveBayes":
		from sklearn.naive_bayes import MultinomialNB #esta libreria nos permite entrenar el algoritmo Naive bayesi
		clf=MultinomialNB()
	
	if algoritmo=="MSV":
		from sklearn.svm import SVC # Maquinas de soporte vectorial
		clf=SVC(kernel='rbf',gamma='scale')

	if algoritmo=="RegresionLogistica":
		from sklearn.linear_model import LogisticRegression # Regresion logistica
		clf=LogisticRegression(random_state=1,solver='sag',multi_class='multinomial',max_iter=500)
	
	if algoritmo=="RandomForest":
		from sklearn.ensemble import RandomForestClassifier # RandomForest
		clf=RandomForestClassifier(n_estimators=100, max_depth=10,random_state=4)
	
	return clf

#--------------------------------------MAIN()----------------------------------#

if len(sys.argv)<4:
	print ("Se debe incluir <NombreAlgoritmo> <RutaNoticias> <Modo Binario(1)/Frecuencia(0)> enla linea de comandos")
	sys.exit(2)

algoritmo=sys.argv[1]# Es el nombre del algoritmo, NaiveBayes, RegresionLogistica,RandomForest y MSV
ruta=sys.argv[2] #Es la ruta del corpus
modoBinario=sys.argv[3]

clf=importarAlgoritmo(algoritmo)#Se crea la instacia CLF quien genera el modelo del algoritmo

data=pd.read_csv(ruta, sep='&&&&&',engine='python') #se cargan los datos de archivo csv

noticias=data['noticia']# se extrae todas las noticias de la columna noticia
seccion=data['seccion']# se extraen las secciones correspondientes a cada noticia
 
#print (data)
#print(noticias)

vectorizer=CountVectorizer(binary=modoBinario)
X=vectorizer.fit_transform(noticias) #se extraer las caracteristicas de las noticias 
Y=seccion #Se extraen las secciones correspondientes a cada noticia

clf.fit(X,Y) #se crea el modelo del algoritmo, donde X es el espacio vectorial de las noticias de entrenamiento, y Y es la secciona la cula pertenece cada espacio vectoria

pickle.dump(clf,open('Modelo_'+algoritmo+'.save','wb'))

print ("Se ha generado el modelo")	
