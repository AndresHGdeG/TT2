#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import spacy
import pandas as pd

import sys#Permite extraer parametros de la linea de comandos

from sklearn.utils import shuffle

if len(sys.argv)<3 :
	print ("Se debe incluir <Ruta corpus> <Ruta archivo salida>")
	sys.exit(2)

ruta=sys.argv[1]
rutaSave=sys.argv[2]

noticias=pd.read_csv(ruta,sep='&&&&&',engine='python')
idNoticia=noticias['id']
titulo=noticias['titulo']
contenido=noticias['noticia']
seccion=noticias['seccion']

#contS,seccS,idS,tituS=shuffle(contenido,seccion,idNoticia,titulo,random_state=5);
idShuffle=shuffle(idNoticia,random_state=5);


#print(idS)

#print(idShuffle)
#
fileCSV=open(rutaSave,"w+")
encabezado="id&&&&&titulo&&&&&noticia&&&&&seccion\n"
fileCSV.write(encabezado)
#
##for i in range(len(contenido)):
#
for idN in idShuffle:
	idAux=str(idN)
	id=int(idAux[3:])-1
	#print(id)

	fileCSV.write(str(idNoticia[id]))
	fileCSV.write(" &&&&& ")
	#print(idNoticia[id])

	fileCSV.write(str(titulo[id]))
	fileCSV.write(" &&&&& ")

	fileCSV.write(str(contenido[id]))
	fileCSV.write(" &&&&&")
	
	fileCSV.write(str(seccion[id]))	

	fileCSV.write("\n")
	#print(str(seccion[i]))

fileCSV.close()
