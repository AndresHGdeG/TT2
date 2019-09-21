
from sklearn.feature_extraction.text import CountVectorizer#esta libreria nos permite extraer las caracteristicas de las noticias formando un espacio vectorial por cada una 
 
import pandas as pd #esta libreria nos permite extraer datos de archivos csv

from sklearn.naive_bayes import MultinomialNB #esta libreria nos permite entrenar el algoritmo Naive bayes


data=pd.read_csv('../../NoticiasPrueba/UnionPrueba.txt', sep='&&&&&',engine='python') #se cargan los datos de archivo csv

noticias=data['noticia']# se extrae todas las noticias de la columna noticia
seccion=data['seccion']# se extraen las secciones correspondientes a cada noticia

#print (data)
#print(noticias)

vectorizer=CountVectorizer()
X=vectorizer.fit_transform(noticias[0:324])# se extraer las caracteristicas de 325 noticias 
Y=seccion[0:324]#Se extraen las secciones de las primeras 325 noticias

X_prueba=vectorizer.transform(noticias[325:350])# se extraen las caracteristicas de las noticias con las cuales se va a probar el modelo 
#0-Deportes
#1-Economia
#2-Politica
#3-Culutura
#4-Ciencia y tecnologia


clf=MultinomialNB()
clf.fit(X,Y) #se crea el modelo del algoritmo, donde X es el espacio vectorial de las noticias de entrenamiento, y Y es la secciona la cula pertenece cada espacio vectorial

print (clf.predict(X_prueba)) #Se precide las noticias de prueba

print( data[325:350])# se muestran las nooticias de prueba

