#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import pandas as pd

import sys#Permite extraer parametros de la linea de comandos


if len(sys.argv)<2 :
	print ("Se debe incluir <Ruta corpus>")
	sys.exit(2)


ruta=sys.argv[1]

noticias=pd.read_csv(ruta,sep='&&&&&',engine='python')
idNoticia=noticias['id']
titulo=noticias['titulo']
contenido=noticias['noticia']
seccion=noticias['seccion']

idAnterior=0


for i in range(len(contenido)):
	text=contenido[i]
	#print(text.split())
	if len(text.split())<180:
		print("Longitud",len(text.split()))
		print("id noticia:",idNoticia[i])



#	print(str(seccion[i]))


