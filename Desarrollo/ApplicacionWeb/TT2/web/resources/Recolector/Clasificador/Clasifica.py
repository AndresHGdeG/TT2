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

if len(sys.argv)<3 :
	print ("Se debe incluir <Ruta noticias> <Modelo clasificador> ")
	sys.exit(2)


ruta=sys.argv[1]
modelo=sys.argv[2] 


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
file0=open('noticiasClasificadas_0.txt',"w+")
file1=open('noticiasClasificadas_1.txt',"w+")
file2=open('noticiasClasificadas_2.txt',"w+")
file3=open('noticiasClasificadas_3.txt',"w+")
file4=open('noticiasClasificadas_4.txt',"w+")

encabezado="id&&&&&url&&&&&titulo&&&&&autor&&&&&fecha&&&&&descripcion\n"
file0.write(encabezado)
file1.write(encabezado)
file2.write(encabezado)
file3.write(encabezado)
file4.write(encabezado)

countNoticias=0;
for i in range(len(noticia_clasificada)):
	countNoticias+=1
	if noticia_clasificada[i] ==0:
		file0.write(str(i+1))
		file0.write("&&&&&")

		file0.write(str(url[i]))
		file0.write("&&&&&")

		file0.write(str(titulo[i]))
		file0.write("&&&&&")

		file0.write(str(autor[i]))
		file0.write("&&&&&")

		file0.write(str(fecha[i]))
		file0.write("&&&&&")

		file0.write(str(descripcion[i]))
		file0.write("&&&&&")

		file0.write(str(noticia_clasificada[i]))
		file0.write("\n")

	if noticia_clasificada[i] ==1:
		file1.write(str(i+1))
		file1.write("&&&&&")

		file1.write(str(url[i]))
		file1.write("&&&&&")

		file1.write(str(titulo[i]))
		file1.write("&&&&&")

		file1.write(str(autor[i]))
		file1.write("&&&&&")

		file1.write(str(fecha[i]))
		file1.write("&&&&&")

		file1.write(str(descripcion[i]))
		file1.write("&&&&&")

		file1.write(str(noticia_clasificada[i]))
		file1.write("\n")

	if noticia_clasificada[i] ==2:
		file2.write(str(i+1))
		file2.write("&&&&&")

		file2.write(str(url[i]))
		file2.write("&&&&&")

		file2.write(str(titulo[i]))
		file2.write("&&&&&")

		file2.write(str(autor[i]))
		file2.write("&&&&&")

		file2.write(str(fecha[i]))
		file2.write("&&&&&")

		file2.write(str(descripcion[i]))
		file2.write("&&&&&")

		file2.write(str(noticia_clasificada[i]))
		file2.write("\n")
	
	if noticia_clasificada[i] ==3:
		file3.write(str(i+1))
		file3.write("&&&&&")

		file3.write(str(url[i]))
		file3.write("&&&&&")

		file3.write(str(titulo[i]))
		file3.write("&&&&&")

		file3.write(str(autor[i]))
		file3.write("&&&&&")

		file3.write(str(fecha[i]))
		file3.write("&&&&&")

		file3.write(str(descripcion[i]))
		file3.write("&&&&&")

		file3.write(str(noticia_clasificada[i]))
		file3.write("\n")

	if noticia_clasificada[i] ==4:
		file4.write(str(i+1))
		file4.write("&&&&&")

		file4.write(str(url[i]))
		file4.write("&&&&&")

		file4.write(str(titulo[i]))
		file4.write("&&&&&")

		file4.write(str(autor[i]))
		file4.write("&&&&&")

		file4.write(str(fecha[i]))
		file4.write("&&&&&")

		file4.write(str(descripcion[i]))
		file4.write("&&&&&")

		file4.write(str(noticia_clasificada[i]))
		file4.write("\n")

file0.close()
file1.close()
file2.close()
file3.close()
file4.close()

print("Se ha encotrado :",countNoticias,"noticias")
