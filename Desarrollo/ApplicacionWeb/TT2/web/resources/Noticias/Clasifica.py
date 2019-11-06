import pandas as pd #Libreria ocupada para leer los archivos CSV
import sys#Permite extraer parametros de la linea de comandos
import spacy

from sklearn.feature_extraction.text import CountVectorizer#esta libreria nos permite extraer las caracteristicas de las noticias formando un espacio vectorial por cada una  
import pickle

#-------------------------------------Funciones()---------------------------------------#
def TokenizaLematiza(text,nlp):
	
	doc = nlp(text)
	lemmas = [tok.lemma_.lower() for tok in doc]
	noticiaTokLe=''

	for x in range(len(lemmas)):
		noticiaTokLe+=str(lemmas[x])+" "
	return noticiaTokLe
		
#-------------------------------------Main()---------------------------------------------#

if len(sys.argv)<4 :
	print ("Se debe incluir <Ruta noticias> <Modelo clasificador> <Seccion> ")
	sys.exit(2)


ruta=sys.argv[1]
modelo=sys.argv[2] 
seccion=int(sys.argv[3])

#--------Lectura del archivo csv----------------#
noticias_totales=pd.read_csv(ruta)

url=noticias_totales['url']
titulo=noticias_totales['titulo']
autor=noticias_totales['autor']
fecha=noticias_totales['fecha']
descripcion=noticias_totales['descripcion']
noticia=noticias_totales['noticia']



#--------Procesar texto, tokenizar lematizar------#
nlp = spacy.load('es_core_news_sm')
for i in range(len(noticia)):

	noticia[i]=TokenizaLematiza(str(noticia[i]),nlp)
	#print(noticia[i])

#-----Lectura del modelo clasificador----#

vectorizer,clf=pickle.load(open(modelo,'rb'))#Se crea la instacia CLF quien genera el modelo del algoritmo

#-----Extracion de características ----#
caracteristicas=vectorizer.transform(noticia) #se extraer las caracteristicas de las noticias 

#-----Clasificación de noticias--------#
noticia_clasificada=clf.predict(caracteristicas)

#print(noticia_clasificada)

#-----Guardar noticias de la seccion seleccionada-------#
file=open('noticiasClasificadas.txt',"w+")
encabezado="id&&&&&url&&&&&titulo&&&&&autor&&&&&fecha&&&&&descripcion\n"
file.write(encabezado)

countNoticias=0;
for i in range(len(noticia_clasificada)):
	if noticia_clasificada[i] ==seccion:
		countNoticias+=1
		#print(noticia_clasificada[i])

		file.write(str(i+1))
		file.write("&&&&&")

		file.write(str(url[i]))
		file.write("&&&&&")

		file.write(str(titulo[i]))
		file.write("&&&&&")

		file.write(str(autor[i]))
		file.write("&&&&&")

		file.write(str(fecha[i]))
		file.write("&&&&&")

		file.write(str(descripcion[i]))
		file.write("&&&&&")

		file.write(str(noticia_clasificada[i]))
		file.write("\n")

file.close()

print("Se ha encotrado :",countNoticias,"noticias")
