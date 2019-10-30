#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import spacy
import pandas as pd

import sys#Permite extraer parametros de la linea de comandos

#-------------------------------------Funciones()---------------------------------------#
def Lematiza(text, fileCSV,nlp):
	
	doc = nlp(text)
	lemmas = [tok.lemma_.lower() for tok in doc]

	for x in range(len(lemmas)):
		fileCSV.write(str(lemmas[x]))
		fileCSV.write(" ")
#-------------------------------------Main()---------------------------------------------#


if len(sys.argv)<3 :
	print("Se debe incluir <Ruta corpus> <Ruta archivo salida>")
	sys.exit(2)

nlp = spacy.load('es_core_news_sm')

ruta=sys.argv[1]
rutaSave=sys.argv[2]

noticias=pd.read_csv(ruta,sep='&&&&&',engine='python')
titulo=noticias['titulo']
contenido=noticias['noticia']
seccion=noticias['seccion']
idNoticia=noticias['id']

fileCSV=open(rutaSave,"w+")
encabezado="id&&&&&titulo&&&&&noticia&&&&&seccion\n"
fileCSV.write(encabezado)


for i in range(len(contenido)):

	fileCSV.write(str(idNoticia[i]))
	fileCSV.write("&&&&&")

	text=str(titulo[i])
	Lematiza(text,fileCSV,nlp)
	fileCSV.write("&&&&&")

	text=contenido[i]
	Lematiza(text,fileCSV,nlp)
	fileCSV.write("&&&&&")
	
	fileCSV.write(str(seccion[i]))
	fileCSV.write("\n")


fileCSV.close()
