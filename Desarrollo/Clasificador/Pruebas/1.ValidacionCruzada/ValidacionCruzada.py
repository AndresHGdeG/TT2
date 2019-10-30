from __future__ import division# permite divir numeros enteros y regrear flotanes
import sys# Libreria para recibir los argumentos de la linea de comandos
import time #Esta libreria permitira medir el timepo de ejecucion de los algoritmos
from resource import getrusage as resource_usage,RUSAGE_SELF# permite obtener el tiempo ocupado por el proceso en el sistema
import platform# permite obtener los datos de la computdora
import psutil# permite extraer el numero de CPUs
import datetime# Se obtemdra el dia en que las pruebas se hagan
import os # permite conocer la memoria consumida por el programa

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

def get_process_memory():
	process=psutil.Process(os.getpid())
	return process.memory_info().rss/1000000 #Megabytes


#--------------------------------------MAIN()----------------------------------#

if len(sys.argv)<5:
	print("Se debe incluir <NombreAlgoritmo> <RutaNoticias> <Modo Binario(1)/Frecuencia(0)> enla linea de comandos")
	sys.exit(2)

algoritmo=sys.argv[1]# Es el nombre del algoritmo, NaiveBayes, RegresionLogistica,RandomForest y MSV
ventanas=int(sys.argv[2]) #Es el numero de diviciones en la validacion cruzada
ruta=sys.argv[3] #Es la ruta del corpus
modoBinario=int(sys.argv[4])

noticiasTotales=0
noticiasCorrectas=0
accuracyPromedio=0
fmeasurePromedio=0
recallPromedio=0
precisionPromedio=0
matrizConfusionPromedio=0


modelo_clasificador=importarAlgoritmo(algoritmo)#Se crea la instacia CLF quien genera el modelo del algoritmo


data=pd.read_csv(ruta, sep='&&&&&',engine='python') #se cargan los datos de archivo csv

noticias=data['noticia']# se extrae todas las noticias de la columna noticia
seccion=data['seccion']# se extraen las secciones correspondientes a cada noticia
 
#print (data)
#print(noticias)

vectorizer=CountVectorizer(binary=modoBinario)


Kf=KFold(n_splits=ventanas,random_state=1,shuffle=True)#Este metodo crea una instancia para generar la validacion  cruzada
#print(Kf)

memoriaInicial=get_process_memory()
start_time,start_resource=time.time(),resource_usage(RUSAGE_SELF)


for train_index,test_index in Kf.split(noticias):
	noticias_train,noticias_test=noticias[train_index],noticias[test_index]
	seccion_train,seccion_test=seccion[train_index],seccion[test_index]

	
	caracteristicas_train=vectorizer.fit_transform(noticias_train) #se extraer las caracteristicas de las noticias 
	caracteristicas_test=vectorizer.transform(noticias_test)	
	
	modelo_clasificador.fit(caracteristicas_train,seccion_train) #se crea el modelo del algoritmo, donde X es el espacio vectorial de las noticias de entrenamiento, y Y es la secciona la cula pertenece cada espacio vectoria
	
	noticias_clasificadas=modelo_clasificador.predict(caracteristicas_test)

	accuracyP=accuracy_score(noticias_clasificadas,seccion_test) #Se calcula la precicion
	accuracyPromedio+=accuracyP
	accuracyN=accuracy_score(noticias_clasificadas,seccion_test,normalize=False) #Se calcula la precicion
	noticiasTotales+=len(noticias_clasificadas)
	noticiasCorrectas+=accuracyN	
	
	#print("numero correctas:",accuracyN,"de: ",len(noticias_clasificadas))
	#print("Accuracy %: ",accuracyP)

	recall=recall_score(noticias_clasificadas,seccion_test,average='macro')
	recallPromedio+=recall
	#print("reacall",recall)
	
	fmeasure=f1_score(noticias_clasificadas,seccion_test,average='macro')
	fmeasurePromedio+=fmeasure
	#print("Fmeasure:",fmeasure)
	
	precision=precision_score(noticias_clasificadas,seccion_test,average='macro')
	precisionPromedio+=precision
	#print("Precision:",precision)
	
	matrizConfusion=confusion_matrix(noticias_clasificadas,seccion_test, labels=[0,1,2,3,4])
	matrizConfusionPromedio+=matrizConfusion
	#print(matrizConfusion)

	#print("")

end_resource,end_time=resource_usage(RUSAGE_SELF),time.time()
memoriaFinal=get_process_memory()

# print 'real',end_time-start_time
# print 'user',end_resource.ru_utime-start_resource.ru_utime
# print 'sys',end_resource.ru_stime-start_resource.ru_stime


matrizConfusionPromedio=matrizConfusionPromedio/ventanas
accuracyPromedio/=ventanas
fmeasurePromedio/=ventanas
recallPromedio/=ventanas
precisionPromedio/=ventanas

# print "Matriz confusion promedio: ",matrizConfusionPromedio
# print "Memoria usada: ",memoriaFinal-memoriaInicial,"  MB"
# print "Accuracy Promedio:",accuracyPromedio
# print "Fmeasure promedio:",fmeasurePromedio
# print "Recall promedio:",recallPromedio
# print "precision promedio:",precisionPromedio

nombreArchivo=algoritmo+"_"+"Div("+str(ventanas)+")_SelCaract("+str(modoBinario)+").txt"
resultados=open(nombreArchivo, "w+")
resultados.write("Algoritmo:"+algoritmo)
resultados.write("\nNumero de ventanas:"+str(ventanas))
resultados.write("\nNoticias de entrenamiento: "+str(len(train_index)))
resultados.write("\nNoticias de test: "+str(len(test_index)))

if modoBinario:
	resultados.write("\nseleccion de caracteristicas: Modo binario")
else:
	resultados.write("\nseleccion de caracteristicas: Por frecuencia")

resultados.write("\n\nNoticias clasificadas correctamente:"+str(noticiasCorrectas)+" de:"+str(noticiasTotales))
resultados.write("\nAccuracy promedio:"+str(accuracyPromedio))
resultados.write("\nFmeasure promedio:"+str(fmeasurePromedio))
resultados.write("\nRecall promedio:"+str(recallPromedio))
resultados.write("\nPrecision promedio:"+str(precisionPromedio))
resultados.write("\n\nMatriz de confucion promedio\n")

resultados.write(str(matrizConfusionPromedio.round()))
resultados.write("\n\nOrden de etiquetas:\n 0 1 2 3 4")
resultados.write("\nDonde \n0:Deportes\n1:Economia\n2:Politica\n3:Cultura\n4:Ciencia y tecnologia")

resultados.write("\n\nCorpus ocupado para validacion cruzada")
resultados.write("\n"+ruta)

resultados.write("\n\nInformacion de cada division en la validacion cruzada")
resultados.write("\nMemoria ocupada(Megabytes):"+str((memoriaFinal-memoriaInicial)/ventanas)+" MB")
resultados.write("\nTiempo real de ejecucion(segundos):"+str((end_time-start_time)/ventanas)+" s")
resultados.write("\nTiempo ocupado por el usuario(segundos):"+str((end_resource.ru_utime-start_resource.ru_utime)/ventanas)+" s")
resultados.write("\nTiempo promedio ocupado en el sistema/CPU (segundos):"+str((end_resource.ru_stime-start_resource.ru_stime)/ventanas)+" s")

resultados.write("\n\nInformacion total del proceso de validacion cruzada")
resultados.write("\nMemoria ocupada(Megabytes):"+str(memoriaFinal-memoriaInicial)+" MB")
resultados.write("\nTiempo real de ejecucion(segundos):"+str(end_time-start_time)+" s")
resultados.write("\nTiempo ocupado por el usuario(segundos):"+str(end_resource.ru_utime-start_resource.ru_utime)+" s")
resultados.write("\nTiempo ocupado en el sistema/CPU (segundos):"+str(end_resource.ru_stime-start_resource.ru_stime)+" s")

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
