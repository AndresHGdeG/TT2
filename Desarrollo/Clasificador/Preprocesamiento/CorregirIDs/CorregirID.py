#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import spacy
import pandas as pd

import sys#Permite extraer parametros de la linea de comandos


if len(sys.argv)<3 :
	print ("Se debe incluir <Ruta corpus> <Ruta archivo salida>")
	sys.exit(2)

nlp = spacy.load('es_core_news_sm')

ruta=sys.argv[1]
rutaSave=sys.argv[2]

noticias=pd.read_csv(ruta,sep='&&&&&',engine='python')
idNoticia=noticias['id']
titulo=noticias['titulo']
contenido=noticias['noticia']
seccion=noticias['seccion']


fileCSV=open(rutaSave,"w+")
encabezado="id&&&&&titulo&&&&&noticia&&&&&seccion\n"
fileCSV.write(encabezado)

for i in range(len(contenido)):
	fileCSV.write(str(i))
	fileCSV.write("&&&&& ")

	fileCSV.write(str(titulo[i]))
	fileCSV.write("&&&&& ")

	fileCSV.write(str(contenido[i]))
	fileCSV.write("&&&&&")
	
	fileCSV.write(str(seccion[i]))	

	fileCSV.write("\n")
#	print(str(seccion[i]))

fileCSV.close()
