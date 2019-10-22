import sys# Libreria para recibir los argumentos de la linea de comandos
import datetime# Se obtemdra el dia en que las pruebas se hagan

from sklearn.feature_extraction.text import CountVectorizer#esta libreria nos permite extraer las caracteristicas de las noticias formando un espacio vectorial por cada una  
import pandas as pd #esta libreria nos permite extraer datos de archivos csv


from sklearn.naive_bayes import MultinomialNB #esta libreria nos permite entrenar el algoritmo Naive bayesi
from sklearn.svm import SVC # Maquinas de soporte vectorial
from sklearn.linear_model import LogisticRegression # Regresion logistica
from sklearn.ensemble import RandomForestClassifier # RandomForest


from sklearn.model_selection import GridSearchCV


#--------------------------------------FUNCIONES()-----------------------------#

def ImportarAlgoritmo(algoritmo):
	if algoritmo=="NaiveBayes":
		clf=MultinomialNB()
	
	if algoritmo=="MSV":
		clf=SVC()

	if algoritmo=="RegresionLogistica":
		clf=LogisticRegression(multi_class='auto')
	
	if algoritmo=="RandomForest":
		clf=RandomForestClassifier()
	
	return clf

def ImportarParametros(algoritmo):


	if algoritmo=="NaiveBayes":
		parameter = [
		{'alpha' : [0.5, 1, 1.5, 2]}
		]
	
	if algoritmo=="MSV":
		parameter=[
		{'kernel':['linear', 'poly', 'rbf'],'gamma' :[1e-4, 1e-5, 1e-6],'C':[1, 10, 100, 1000]}
		]

	if algoritmo=="RegresionLogistica":
		parameter=[
		{'penalty':['l1', 'l2'],'C':[1e-6, 1e-05, 1e-04, 1e-03, 1e-02, 1e-01],'solver': ['liblinear']}
		]
	
	if algoritmo=="RandomForest":
		parameter=[
		{'max_depth':[50, 100, 500, 1000],'n_estimators': [50, 100, 500, 1000]}
		]

	return parameter 


def MejoresParametros(algoritmos,clf,resultados):

	if algoritmo=="NaiveBayes":
		resultados.write("\nBest alpha:"+str(clf.best_estimator_.alpha))
		resultados.write("\nBest score:"+str(clf.best_score_))

		print('Best alpha:',clf.best_estimator_.alpha) 
	
	if algoritmo=="MSV":
		resultados.write("\nBest C:"+str(clf.best_estimator_.C))
		resultados.write("\nBest Kernel:"+str(clf.best_estimator_.kernel))
		resultados.write("\nBest Gamma:"+str(clf.best_estimator_.gamma))
		resultados.write("\nBest score:"+str(clf.best_score_))
		
		print('Best C',clf.best_estimator_.C)
		print('Best Kernel',clf.best_estimator_.kernel)
		print('Best Gamma',clf.best_estimator_.gamma)
		

	if algoritmo=="RegresionLogistica":
		resultados.write("\nBest C:"+str(clf.best_estimator_.C))
		resultados.write("\nBest Solver:"+str(clf.best_estimator_.solver))
		resultados.write("\nBest Penalty:"+str(clf.best_estimator_.penalty))
		resultados.write("\nBest score:"+str(clf.best_score_))
		
		print('Best C',clf.best_estimator_.C)
		print('Best Solver',clf.best_estimator_.solver)
		print('Best Penalty',clf.best_estimator_.penalty)

	
	if algoritmo=="RandomForest":
		
		resultados.write("\nBest max_depth:"+str(clf.best_estimator_.max_depth))
		resultados.write("\nBest n_estimators:"+str(clf.best_estimator_.n_estimators))
		resultados.write("\nBest score:"+str(clf.best_score_))
		
		print('Best max_depth :', clf.best_estimator_.max_depth) 
		print('Best n_estimators:',clf.best_estimator_.n_estimators) 


def get_process_memory():
	process=psutil.Process(os.getpid())
	return process.memory_info().rss/1000000 #Megabytes


#--------------------------------------MAIN()----------------------------------#

if len(sys.argv)<4:
	print("Se debe incluir <NombreAlgoritmo> <RutaNoticias> <Modo Binario(1)/Frecuencia(0)> enla linea de comandos")
	sys.exit(2)

algoritmo=sys.argv[1]# Es el nombre del algoritmo, NaiveBayes, RegresionLogistica,RandomForest y MSV
ruta=sys.argv[2] #Es la ruta del corpus
modoBinario=int(sys.argv[3]) #Extraccion de caracteristicas Binario/Frecuencia




data=pd.read_csv(ruta, sep='&&&&&',engine='python') #se cargan los datos de archivo csv

noticias=data['noticia']# se extrae todas las noticias de la columna noticia
seccion=data['seccion']# se extraen las secciones correspondientes a cada noticia
 


vectorizer=CountVectorizer(binary=modoBinario)

X=vectorizer.fit_transform(noticias)
Y=seccion


modelo_clasificador=ImportarAlgoritmo(algoritmo)#Se crea la instacia CLF quien genera el modelo del algoritmo
parameter=ImportarParametros(algoritmo)#Se cargan los parametros del algoritmo a probars

# Create a classifier object with the classifier and parameter candidates
particiones=5
clf = GridSearchCV(estimator=modelo_clasificador, param_grid=parameter,  cv=particiones, verbose=particiones,iid=False)

# Train the classifier on data1's feature and target data
clf.fit(X,Y)  




nombreCSV=algoritmo+"_Resumen("+str(modoBinario)+").csv"
dataframe=pd.DataFrame(data=clf.cv_results_)
dataframe.to_csv(nombreCSV,index=False)


nombreArchivo=algoritmo+"_MejoresParametros("+str(modoBinario)+").txt"
resultados=open(nombreArchivo, "w+")
resultados.write("Algoritmo:"+algoritmo)
resultados.write("\nNumero de particiones en la validacion cruzada:"+str(particiones))
resultados.write("\nNoticias de entrenamiento: "+str(len(Y)))
resultados.write("\n\nMejores Parametros\n")
best_clf=MejoresParametros(algoritmo,clf,resultados)
resultados.write("\n\nFecha de la prueba: \n:"+str(datetime.datetime.now()))
resultados.close()
#

#0-Deportes
#1-Economia
#2-Politica
#3-Cultura
#4-Ciencia y tecnologia
