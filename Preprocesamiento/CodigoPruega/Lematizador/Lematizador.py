#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import spacy
import pandas as pd

#-------------------------------------Funciones()---------------------------------------#
def Lematiza(text, fileCSV,nlp):
	
	doc = nlp(text)
	lemmas = [tok.lemma_.lower() for tok in doc]

	for x in range(len(lemmas)):

 		fileCSV.write(lemmas[x].encode('utf8'))
		fileCSV.write(" ")
#-------------------------------------Main()---------------------------------------------#

nlp = spacy.load('es_core_news_sm')
fileCSV=open("CorpusBalanceadoCompleto.txt","w+")

noticias=pd.read_csv("../../PrimerCorpus/corpusBalanceado.txt",sep='&&&&&',engine='python')
titulo=noticias['titulo']
contenido=noticias['noticia']
seccion=noticias['seccion']

encabezado="titulo&&&&&noticia&&&&&seccion\n"
fileCSV.write(encabezado)

for i in range(len(contenido)):
	text=unicode(str(titulo[i]),"utf8")
	Lematiza(text,fileCSV,nlp)
	fileCSV.write("&&&&&")

	text=unicode(contenido[i],"utf8")
	Lematiza(text,fileCSV,nlp)
	fileCSV.write("&&&&&")
	
	fileCSV.write(str(seccion[i]))
	fileCSV.write("\n")
#	print(str(seccion[i]))

fileCSV.close()
