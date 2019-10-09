import sys# permite leer argumentos de la linea de comandos

if len(sys.argv)<2:
	print("Se debe ingresar el argumento <Ruta/nombreArchivo>")
	sys.exit(2)
	#python Modelo.py '../../../Corpus/Pruebas/UnionPrueba.txt'


ruta=sys.argv[1]

from sklearn.ensemble import RandomForestClassifier #esta libreria nos permite entrenar el algoritmo RamdonForest
clf=RandomForestClassifier(n_estimators=100,max_depth=10,random_state=4)


from sklearn.feature_extraction.text import CountVectorizer#esta libreria nos permite extraer las caracteristicas de las noticias formando un espacio vectorial por cada una  
import pandas as pd #esta libreria nos permite extraer datos de archivos csv


from sklearn.linear_model import LogisticRegression #esta libreria nos permite entrenar el algoritmo Regresion logistica
from sklearn.model_selection import KFold # permite generar la validacion cruzada, dividiendo el conjunto de entrenamiento y conjunto de prueba

from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix#Matriz de confucion
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from sklearn.metrics import precision_score


data=pd.read_csv(ruta, sep='&&&&&',engine='python') #se cargan los datos de archivo csv

noticias=data['noticia']# se extrae todas las noticias de la columna noticia
seccion=data['seccion']# se extraen las secciones correspondientes a cada noticia

#print (data)
#print(noticias)

vectorizer=CountVectorizer(binary=1)
X=vectorizer.fit_transform(noticias)# se extraer las caracteristicas de las noticias 
Y=seccion #Se extraen las secciones correspondientes a cada noticia


Kf=KFold(n_splits=3,random_state=1,shuffle=True)#Este metodo crea una instancia para generar la validacion  cruzada
#print(Kf)

for train_index,test_index in Kf.split(X):
	X_train,X_test=X[train_index],X[test_index]
	Y_train,Y_test=Y[train_index],Y[test_index]
	
	clf.fit(X_train,Y_train) #se crea el modelo del algoritmo, donde X es el espacio vectorial de las noticias de entrenamiento, y Y es la secciona la cula pertenece cada espacio vectoria
	
	X_resultado=clf.predict(X_test)

	accuracyP=accuracy_score(X_resultado,Y_test) # Se calcula la precicion
	accuracyN=accuracy_score(X_resultado,Y_test,normalize=False) # Se calcula la precicion
	
	
	print("numero correctas:",accuracyN,"de: ",len(X_resultado))
	print("Accuracy %: ",accuracyP)

	recall=recall_score(X_resultado,Y_test,average='macro')
	print("reacall",recall)
	
	fmeasure=f1_score(X_resultado,Y_test,average='macro')
	print("Fmeasure:",fmeasure)
	
	precision=precision_score(X_resultado,Y_test,average='macro')
	print("Precision:",precision)
	
	matrizConfusion=confusion_matrix(X_resultado,Y_test, labels=[0,1,2,3,4])
	print(matrizConfusion)

	print("")

#0-Deportes
#1-Economia
#2-Politica
#3-Cultura
#4-Ciencia y tecnologia
