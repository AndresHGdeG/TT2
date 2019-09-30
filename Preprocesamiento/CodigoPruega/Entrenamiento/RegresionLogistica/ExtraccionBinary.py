
from sklearn.feature_extraction.text import CountVectorizer#esta libreria nos permite extraer las caracteristicas de las noticias formando un espacio vectorial por cada una 
 
import pandas as pd #esta libreria nos permite extraer datos de archivos csv

from sklearn.linear_model import LogisticRegression #esta libreria nos permite entrenar el algoritmo Regresion logistica
data=pd.read_csv('../../../NoticiasPrueba/UnionPrueba.txt', sep='&&&&&',engine='python') #se cargan los datos de archivo csv

from sklearn.model_selection import KFold # permite generar la validacion cruzada, dividiendo el conjunto de entrenamiento y conjunto de prueba
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix#Matriz de confucion


noticias=data['noticia']# se extrae todas las noticias de la columna noticia
seccion=data['seccion']# se extraen las secciones correspondientes a cada noticia

#print (data)
#print(noticias)


vectorizer=CountVectorizer(binary=1)
X=vectorizer.fit_transform(noticias)# se extraer las caracteristicas de las noticias 
Y=seccion #Se extraen las secciones correspondientes a cada noticia


clf=LogisticRegression(random_state=1,solver='sag',multi_class='multinomial',max_iter=500)


Kf=KFold(n_splits=2,random_state=1,shuffle=True)#Este metodo crea una instancia para generar la validacion  cruzada
#print(Kf)
for train_index,test_index in Kf.split(X):
	X_train,X_test=X[train_index],X[test_index]
	Y_train,Y_test=Y[train_index],Y[train_index]
	
	clf.fit(X_train,Y_train) #se crea el modelo del algoritmo, donde X es el espacio vectorial de las noticias de entrenamiento, y Y es la secciona la cula pertenece cada espacio vectoria
	
	X_resultado=clf.predict(X_test)

	accuP=accuracy_score(X_resultado,Y_test) # Se calcula la precicion
	accuN=accuracy_score(X_resultado,Y_test,normalize=False) # Se calcula la precicion
	print("precicion %: ",accuP),
	print("numero correctas:",accuN,"de: ",len(X_resultado))

	matrizConfusion=confusion_matrix(X_resultado,Y_test, labels=[0,1,2,3,4])
	print(matrizConfusion)

#0-Deportes
#1-Economia
#2-Politica
#3-Cultura
#4-Ciencia y tecnologia

