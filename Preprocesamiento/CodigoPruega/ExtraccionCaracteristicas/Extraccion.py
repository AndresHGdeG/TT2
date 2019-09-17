
from sklearn.feature_extraction.text import CountVectorizer 
import pandas as pd

import pickle




data=pd.read_csv('../../NoticiasPrueba/pruebaNoticias.csv')
noticias=data['noticia'][0:6]

vectorizer=CountVectorizer()
X=vectorizer.fit_transform(noticias)
#print(vectorizer.get_feature_names())
caracteristicas=str(vectorizer.get_feature_names());
#print(caracteristicas)
fCaracteristicas=open('caracteristicas.txt','w')
fCaracteristicas.write(caracteristicas)
fCaracteristicas.close()

#
f=open('vector.txt','w')
x=X.toarray()

for item in x:
	for num in item: 
		numT=str(num)
		f.write(numT)
		f.write(" ")

	f.write("\n\n")
	
	


f.close()

print(" se ha creado 2 archivos, 1 con las caracteristicas y otro con los vectores")
#print(X.toarray())

