from __future__ import division #esta libreria nos ayuda a incluir punto decimal en las diviciones enteras

from sklearn.feature_extraction.text import CountVectorizer#esta libreria nos permite extraer las caracteristicas de las noticias formando un espacio vectorial por cada una 
 
import pandas as pd #esta libreria nos permite extraer datos de archivos csv

from sklearn.linear_model import LogisticRegression #esta libreria nos permite entrenar el algoritmo Regresion logistica


data=pd.read_csv('../../../NoticiasPrueba/UnionPrueba.txt', sep='&&&&&',engine='python') #se cargan los datos de archivo csv

noticias=data['noticia']# se extrae todas las noticias de la columna noticia
seccion=data['seccion']# se extraen las secciones correspondientes a cada noticia

#print (data)
#print(noticias)

vectorizer=CountVectorizer(binary=0)
X=vectorizer.fit_transform(noticias[0:324])# se extraer las caracteristicas de 325 noticias 
Y=seccion[0:324]#Se extraen las secciones de las primeras 325 noticias

Y_prueba=data.loc[325:350,'seccion']# secciones correspondientes a la prueba
X_prueba=vectorizer.transform(noticias[325:350])# se extraen las caracteristicas de las noticias con las cuales se va a probar el modelo 

#0-Deportes
#1-Economia
#2-Politica
#3-Culutura
#4-Ciencia y tecnologia


clf=LogisticRegression(random_state=0,solver='sag',multi_class='multinomial',max_iter=2000)
clf.fit(X,Y) #se crea el modelo del algoritmo, donde X es el espacio vectorial de las noticias de entrenamiento, y Y es la secciona la cula pertenece cada espacio vectorial

X_resultado=clf.predict(X_prueba)
#print (X_resultado) #Se precide las noticias de prueba
contador=0
numNoticias=25

for i in range(numNoticias):

 if Y_prueba[325+i]==X_resultado[i]:
  contador=contador+1
# print X_resultado[i],
# print Y_prueba[325+i],

exactitud=100*contador/numNoticias
print("Exactitud",exactitud)


#print( data[325:350])# se muestran las nooticias de prueba

