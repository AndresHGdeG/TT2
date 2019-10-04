import sys# Libreria para recibir los argumentos de la linea de comandos
import time #Esta libreria permitira medir el timepo de ejecucion de los algoritmos
import platform# permite obtener los datos de la computdora
import psutil# permite extraer el numero de CPUs
import datetime# Se obtemdra el dia en que las pruebas se hagan

from sklearn.feature_extraction.text import CountVectorizer#esta libreria nos permite extraer las caracteristicas de las noticias formando un espacio vectorial por cada una  
import pandas as pd #esta libreria nos permite extraer datos de archivos csv

from sklearn.model_selection import KFold # permite generar la validacion cruzada, dividiendo el conjunto de entrenamiento y conjunto de prueba

from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix#Matriz de confucion
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from sklearn.metrics import precision_score

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

if len(sys.argv)<2:
	print "Se debe incluir <NombreAlgoritmo> <RutaNoticias> enla linea de comandos"
	sys.exit(2)

algoritmo=sys.argv[1]# Es el nombre del algoritmo, NaiveBayes, RegresionLogistica,RandomForest y MSV
ventanas=int(sys.argv[2]) #Es el numero de diviciones en la validacion cruzada
ruta=sys.argv[3] #Es la ruta del corpus

modoBinario=1

noticiasTotales=0
noticiasCorrectas=0
accuracyPromedio=0
fmeasurePromedio=0
recallPromedio=0
precisionPromedio=0



clf=importarAlgoritmo(algoritmo)#Se crea la instacia CLF quien genera el modelo del algoritmo


data=pd.read_csv(ruta, sep='&&&&&',engine='python') #se cargan los datos de archivo csv

noticias=data['noticia']# se extrae todas las noticias de la columna noticia
seccion=data['seccion']# se extraen las secciones correspondientes a cada noticia
 
#print (data)
#print(noticias)

vectorizer=CountVectorizer(binary=modoBinario)
X=vectorizer.fit_transform(noticias) #se extraer las caracteristicas de las noticias 
Y=seccion #Se extraen las secciones correspondientes a cada noticia


Kf=KFold(n_splits=ventanas,random_state=1,shuffle=True)#Este metodo crea una instancia para generar la validacion  cruzada
#print(Kf)


tiempoInicio=time.time()# inicio del tiempo

for train_index,test_index in Kf.split(X):
	X_train,X_test=X[train_index],X[test_index]
	Y_train,Y_test=Y[train_index],Y[test_index]
	
	clf.fit(X_train,Y_train) #se crea el modelo del algoritmo, donde X es el espacio vectorial de las noticias de entrenamiento, y Y es la secciona la cula pertenece cada espacio vectoria
	
	X_resultado=clf.predict(X_test)

	accuracyP=accuracy_score(X_resultado,Y_test) #Se calcula la precicion
	accuracyPromedio+=accuracyP
	accuracyN=accuracy_score(X_resultado,Y_test,normalize=False) #Se calcula la precicion
	noticiasTotales+=len(X_resultado)
	noticiasCorrectas+=accuracyN	
	
	#print("numero correctas:",accuracyN,"de: ",len(X_resultado))
	#print("Accuracy %: ",accuracyP)

	recall=recall_score(X_resultado,Y_test,average='macro')
	recallPromedio+=recall
	#print("reacall",recall)
	
	fmeasure=f1_score(X_resultado,Y_test,average='macro')
	fmeasurePromedio+=fmeasure
	#print("Fmeasure:",fmeasure)
	
	precision=precision_score(X_resultado,Y_test,average='macro')
	precisionPromedio+=precision
	#print("Precision:",precision)
	
	matrizConfusion=confusion_matrix(X_resultado,Y_test, labels=[0,1,2,3,4])
	#print(matrizConfusion)

	#print("")
tiempoFinal=time.time()

accuracyPromedio/=ventanas
fmeasurePromedio/=ventanas
recallPromedio/=ventanas
precisionPromedio/=ventanas

print "tiempo de ejecucion",tiempoFinal-tiempoInicio," segundos"
	
print "Accuracy Promedio:",accuracyPromedio
print "Fmeasure promedio:",fmeasurePromedio
print "Recall promedio:",recallPromedio
print "precision promedio:",precisionPromedio

nombreArchivo="Resul_"+algoritmo+"_"+str(ventanas)+".txt"
resultados=open(nombreArchivo, "w+")
resultados.write("Algoritmo:"+algoritmo)
resultados.write("\nNumero de ventanas:"+str(ventanas))

if modoBinario:
	resultados.write("\nseleccion de caracteristicas: Modo binario")
else:
	resultados.write("\nseleccion de caracteristicas: Por frecuencia")

resultados.write("\nTiempo de ejecucion:"+str(tiempoFinal-tiempoInicio))
resultados.write("\n\nClasificadas correctamente:"+str(noticiasCorrectas)+" de:"+str(noticiasTotales))
resultados.write("\nAccuracy promedio:"+str(accuracyPromedio))
resultados.write("\nFmeasure promedio:"+str(fmeasurePromedio))
resultados.write("\nRecall promedio:"+str(recallPromedio))
resultados.write("\nPrecision promedio:"+str(precisionPromedio))
resultados.write("\n\nMatriz de confucion\n")
resultados.write(str(matrizConfusion))
resultados.write("\n\nOrden de etiquetas:\n 0 1 2 3 4")
resultados.write("\nDonde \n0:Deportes\n1:Economia\n2:Politica\n3:Cultura\n4:Ciencia y tecnologia")

resultados.write("\n\nInformacion del equipo")
resultados.write("\nSystem OS:"+platform.system())
resultados.write("\nProcesador:"+platform.processor())
resultados.write("\nNumero de CPUs:"+str(psutil.cpu_count()))
resultados.write("\nNumero de CPUs fisicos:"+str(psutil.cpu_count(logical=False)))
resultados.write("\nVersion:"+platform.version())

resultados.write("\n\nFecha de la prueba: \n:"+str(datetime.datetime.now()))
resultados.close()


#0-Deportes
#1-Economia
#2-Politica
#3-Cultura
#4-Ciencia y tecnologia
