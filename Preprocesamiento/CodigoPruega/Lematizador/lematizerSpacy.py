e#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import spacy
nlp = spacy.load('es_core_news_sm')
text = "Soy un texto que pide a gritos que lo procesen. Por eso yo canto, tú cantas, ella canta, nosotros cantamos, cantáis, cantan, 3423.23 10/02/2019"
text2="corriendo, correr, corrí, corremos, corre, jugando, jugaré, jugamos, jugaste, juguemos,"
text3="salto, saltas, salta, saltamos, saltáis, saltan, saltaba, saltabas, saltaba, saltábamos, saltabais, saltaban, saltaré, saltarás, saltará, saltaremos, saltaréis, saltarán, saltado"
text4="El otro dia estaba comiendo cuando una pelota me pegó en la cara, las niñas se rrieron de mi"

doc = nlp(text)
lemmas = [tok.lemma_.lower() for tok in doc]

print "\n"
print text
print "\n"

for x in range(len(lemmas)):
	print (lemmas[x]),
print "\n"



#python -m spacy download es_core_news_md

#h