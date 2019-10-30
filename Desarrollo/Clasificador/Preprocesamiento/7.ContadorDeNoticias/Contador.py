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

contadorDeportes=0
contadorEconomia=0
contadorCienciaT=0
contadorCultura=0
contadorPolitica=0

contaristegui=0
conttvAzteca=0
contelEconomista=0
contlaJornada=0
contlaPrensa=0
contproceso=0
contsopitas=0

for i in range(len(idNoticia)):
	idAux=str(idNoticia[i])
	id=int(idAux[0:3])
	seccAux=int(seccion[i])

	if seccAux==0:
		contadorDeportes+=1
	if seccAux==1:
		contadorEconomia+=1
	if seccAux==2:
		contadorPolitica+=1
	if seccAux==3:
		contadorCultura+=1
	if seccAux==4:
		contadorCienciaT+=1

	if id==100:
		contaristegui+=1
	if id==200:
		conttvAzteca+=1
	if id==300:
		contelEconomista+=1
	if id==400:
		contlaJornada+=1
	if id==500:
		contlaPrensa+=1
	if id==600:
		contproceso+=1
	if id==700:
		contsopitas+=1

print("Secciones\n")
print ("Deportes: ",contadorDeportes)
print("Economia: ",contadorEconomia)
print("CienciaT: ",contadorCienciaT)
print("Cultura: ",contadorCultura)
print("Politica: ",contadorPolitica)


print("\nPeriodicos\n")
print("aristegui: ",contaristegui)
print("tvAzteca: ",conttvAzteca)
print("elEconomista: ",contelEconomista)
print("laJornada: ",contlaJornada)
print("laPrensa: ",contlaPrensa)
print("proceso: ",contproceso)
print("sopitas: ",contsopitas)


fileCSV.write("Secciones\n")
fileCSV.write ("\nDeportes: " + str(contadorDeportes))
fileCSV.write("\nEconomia: " + str(contadorEconomia))
fileCSV.write("\nCienciaT: " + str(contadorCienciaT))
fileCSV.write("\nCultura: " + str(contadorCultura))
fileCSV.write("\nPolitica: " + str(contadorPolitica))
fileCSV.write("\n\nPeriodicos\n")
fileCSV.write("\naristegui: " + str(contaristegui))
fileCSV.write("\ntvAzteca: " + str(conttvAzteca))
fileCSV.write("\nelEconomista: " + str(contelEconomista))
fileCSV.write("\nlaJornada: " + str(contlaJornada))
fileCSV.write("\nlaPrensa: " + str(contlaPrensa))
fileCSV.write("\nproceso: " + str(contproceso))
fileCSV.write("\nsopitas: " + str(contsopitas))




















#	print(str(seccion[i]))

fileCSV.close()
