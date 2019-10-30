#Programa que  permite limpar tokenizar y lematizar noticias
from __future__ import unicode_literals
import spacy
import pandas as pd
import tkinter
from tkinter import *
from tkinter import filedialog
import csv
import re
from nltk.tokenize import RegexpTokenizer
import demoji
import nltk
from os import remove
words = set(nltk.corpus.words.words())
import sys 
"""
Secciones
    0.- Deportes
    1.- Economia
    2.- Politica
    3.- Cultura
    4.- Ciencia y tecnologia
IDs periodicos
    100.- Aristegui
    200.- TVAZTECA
    300.- El Economista
    400.- La jornada
    500.- La prensa
    500.- La prensa
    600.- Proceso
    700.- Sopitas
"""
#----------------------------Funciones limpiar texto()----------------------------------#
def limpiarAristegui(noticia):
    # Remove Emojis
    text = demoji.replace(noticia)
    clean = re.compile('<.*?>')
    clean = re.sub(clean, '', text)
    clean = re.sub(r"\(?@\w*\)?|#\w*|\w* \d*, \d{4}|\d{2}/\d{2} – \d{2}h\d{2}| \\ U000e0067 | \\ U000e0062 | \\ U000e006e | \\ U000e0067 | \\ U000e007f  | \\ U000e0073 | \\ U000e0063 | \\ U000e0074 | \\ U000e0065", " ", clean)
    clean = re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '', clean)
    clean = re.sub(r'\d* de \w* de \d{4}','',clean)
    clean = re.sub(r'CIUDAD DE MÉXICO \d* de \w* \d{4} \(\w*\)', '', clean)
    clean = re.sub(r"\(?@\w*\)?|#\w*|\w+[.+]\w+[.+]\w+[/+]\w+|\w+[:+][/]+\w+.\w+[/]\w+|\\u2063|\\u200d|\\xa0| \| Video| \\u27A1| \\uFE0F | � | ➔ | —", " ", clean)
    RE_EMOJI = re.compile('[\U00010000-\U0010ffff]', flags=re.UNICODE)

    return RE_EMOJI.sub(r'', clean)

def limpiarAzteca(noticia):
    text = demoji.replace(noticia)
    clean = re.compile('<.*?>')
    clean = re.sub(clean, '', text)
    clean = re.sub(r"\(?@\w*\)?|#\w*|�|\w* \d*, \d{4}| \\U000E0067 | \\U000E0062 | \\U000E0065 | \\U000E006E | \\U000E0067  | \\U000E007F | \d{2}/\d{2} – \d{2}h\d{2}", " ", clean)
    clean = re.sub(r'\d* de \w* de \d{4}', '', clean)
    clean = re.sub(r'CIUDAD DE MÉXICO \d* de \w* \d{4} \(\w*\)', '', clean)
    clean = re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '', clean)
    clean = re.sub(r"\\?|\(?@\w*\)?|#\w*|\w+[.+]\w+[.+]\w+[/+]\w+|\w+[:+][/]+\w+.\w+[/]\w+ | \| Video | \\u2794", "", clean)
    RE_EMOJI = re.compile('[\U00010000-\U0010ffff]', flags=re.UNICODE)

    return RE_EMOJI.sub(r'', clean)

def limpiarElEconomista(noticia):
    text = demoji.replace(noticia)
    clean = re.compile('<.*?>')
    clean = re.sub(clean, '', text)
    clean = re.sub(r'\d* de \w* de \d{4} | \d{2}/\d{2} – \d{2}h\d{2}', '', clean)
    clean = re.sub(r'CIUDAD DE MÉXICO \d* de \w* \d{4} \(\w*\)', '', clean)
    clean = re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '', clean)
    clean = re.sub(r"\(?@\w*\)?|#\w*|\w+[.+]\w+[.+]\w+[/+]\w+|\w+[:+][/]+\w+.\w+[/]\w+|\\xa0|</?p+,?| � |</?a|href=""/\w+-\w+/\w+/\w+-\w+|</?strong|<span\sclass=[_+]\w+|\[\w+\s\w+\]|\w+-\w+=\w+|</?span| \| Video | \\u2794|<!-- Se agrega para compatibilidad con noticias historicas --| \\u000e0067 | \\u000E0067 | \\u000E0062 | \\u000E0065 | \\u000E006E | \\u000E0067  | \\u000E007F", "", clean)
    return clean

def limpiarLaJornada(noticia):
    text = demoji.replace(noticia)
    clean = re.compile('<.*?>')
    clean = re.sub(clean, '', text)
    clean = re.sub(r'\d* de \w* de \d{4}|\w* \d*, \d{4}', '', clean)
    clean = re.sub(r'CIUDAD DE MÉXICO \d* de \w* \d{4} \(\w*\)', '', clean)
    clean = re.sub(r"\(?@\w*\)?|#\w*", " ", clean)
    clean = re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '', clean)
    clean = re.sub(r"\(?@\w*\)?|#\w*|\w+[.+]\w+[.+]\w+[/+]\w+|\w+[:+][/]+\w+.\w+[/]\w+| � |\\u2063|\\u200d|\\xa0| \| Video| \\u2794 | \\U000E0067 | \\U000E0062 | \\U000E0065 | \\U000E006E | \\U000E0067  | \\U000E007F | \d{2}/\d{2} – \d{2}h\d{2}", " ", clean)
    RE_EMOJI = re.compile('[\U00010000-\U0010ffff]', flags=re.UNICODE)

    return RE_EMOJI.sub(r'', clean)

def limpiarLaPrensa(noticia):
    text = demoji.replace(noticia)
    clean = re.compile('<.*?>')
    clean = re.sub(clean, '', text)
    clean = re.sub(r'\w* \d*, \d{4}|\d* de \w* de \d{4}', '', clean)
    clean = re.sub(r'CIUDAD DE MÉXICO \d* de \w* \d{4} \(\w*\)', '', clean)
    clean = re.sub(r"\(?@\w*\)?|#\w*", " ", clean)
    clean = re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '', clean)
    clean = re.sub(r"\(?@\w*\)?|#\w*|\w+[.+]\w+[.+]\w+[/+]\w+|\w+[:+][/]+\w+.\w+[/]\w+| � |\\u2063|\\u200d|\\xa0| \| Video| \\u2794 | \\U000E0067 | \\U000E0062 | \\U000E0065 | \\U000E006E | \\U000E0067  | \\U000E007F | \d{2}/\d{2} – \d{2}h\d{2}", " ",clean)
    RE_EMOJI = re.compile('[\U00010000-\U0010ffff]', flags=re.UNICODE)

    return RE_EMOJI.sub(r'', clean)

def limpiarProceso(noticia):
    text = demoji.replace(noticia)
    clean = re.compile('<.*?>')
    clean = re.sub(clean, '', text)
    clean = re.sub(r'\d* de \w* de \d{4}', '', clean)
    clean = re.sub(r'CIUDAD DE MÉXICO \d* de \w* \d{4} \(\w*\)', '', clean)
    clean = re.sub(r"\(?@\w*\)?|#\w*", " ", clean)
    clean = re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '', clean)
    clean = re.sub(r"\(?@\w*\)?|#\w*|\w+[.+]\w+[.+]\w+[/+]\w+|\w+[:+][/]+\w+.\w+[/]\w+| � | \\u2063|\\u200d|\\xa0| \| Video| \\u2794 | \\u000e0067 | \\u000e0062 | \\u000e0065 | \\u000e006e | \\u000e0067 | \\u000e007f | \d{2}/\d{2} – \d{2}h\d{2}", " ",
                   clean)
    RE_EMOJI = re.compile('[\U00010000-\U0010ffff]', flags=re.UNICODE)
    return RE_EMOJI.sub(r'', clean)

def limpiarSopitas(noticia):
    text = demoji.replace(noticia)
    clean = re.compile('<.*?>')
    clean = re.sub(clean, '', text)
    clean = re.sub(r'\d* de \w* de \d{4}', '', clean)
    clean = re.sub(r'CIUDAD DE MÉXICO \d* de \w* \d{4} \(\w*\)', '', clean)
    clean = re.sub(r"\(?@\w*\)?|#\w*", " ", clean)
    clean = re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '', clean)
    clean = re.sub(r"\(?@\w*\)?|#\w*|\w+[.+]\w+[.+]\w+[/+]\w+|\w+[:+][/]+\w+.\w+[/]\w+| � |\\u2063|\\u200d|\\xa0| \| Video| \\u2794 | \\u000e0067 | \\u000e0062 | \\u000e0065 | \\u000e006e | \\u000e0067 | \\u000e007f | \d{2}/\d{2} – \d{2}h\d{2}", " ",
                   clean)
    RE_EMOJI = re.compile('[\U00010000-\U0010ffff]', flags=re.UNICODE)

    return RE_EMOJI.sub(r'', clean)

#----------------------------Funciones guarda archivo()----------------------------------#
def save(titulo, noticia, archivo,periodico, id):
    tokenizer = RegexpTokenizer('\w+|\$[\d\,\d\.]+|\S')
    archivo.write(periodico+str(id))
    archivo.write(" &&&&& ")
    titulo = tokenizer.tokenize(titulo)
    for word in titulo:
        archivo.write(word + ' ')
    archivo.write(" &&&&& ")
    noticia = tokenizer.tokenize(noticia)
    for word in noticia:
        archivo.write(word + ' ')
    archivo.write(" &&&&&")
    archivo.write("0")
    archivo.write('\n')

def limpiar():
    num = int(input("Ingresa el numero de palabras noticias: "))
    name = "DeportesTokenizado.txt"
    #remove(name)
    id = 1
    idNumNot = 1
    urls = []

    #filePath = filedialog.askopenfilename()
   # filePath = "CulturaCompleto_1067.csv"
    filePath= sys.argv[1]
    input_file = csv.DictReader(open(filePath))
    output_file = open(name, "w+")
    for row in input_file:
        if id <=3000 and str(row["url"]) not in urls:
            urls.append(str(row["url"]))
            webSiteAux = str(row["url"])
            noticia = str(row["noticia"])
            titulo = str(row["titulo"])
            len(noticia.split())
            if(re.search("^https://aristeguinoticias.com/", webSiteAux)):
                noti = limpiarAristegui(noticia)
                titu = limpiarAristegui(titulo)
                if (len(noti.split()) > num):
                    save(titu, noti, output_file,'100',id)
                    id += 1
                else:
                    idNumNot += 1
            elif(re.search("^https://www.tvazteca.com/", webSiteAux)):
                noti = limpiarAzteca(noticia)
                titu = limpiarAzteca(titulo)
                if (len(noti.split()) > num):
                    save(titu, noti, output_file,'200',id)
                    id += 1
                else:
                    idNumNot += 1
            elif (re.search("^https://www.eleconomista.com.mx/", webSiteAux)):
                noti = limpiarElEconomista(noticia)
                titu = limpiarElEconomista(titulo)
                if (len(noti.split()) > num):
                    save(titu, noti, output_file,'300',id)
                    id += 1
                else:
                    idNumNot += 1
            elif (re.search("^https://www.jornada.com.mx/", webSiteAux)):
                noti = limpiarLaJornada(noticia)
                titu = limpiarLaJornada(titulo)
                if (len(noti.split()) > num):
                    save(titu, noti, output_file,'400',id)
                    id += 1
                else:
                    idNumNot += 1
            elif (re.search("^https://www.la-prensa.com.mx/", webSiteAux)):
                noti = limpiarLaPrensa(noticia)
                titu = limpiarLaPrensa(titulo)
                if (len(noti.split()) > num):
                    save(titu, noti, output_file,'500',id)
                    id += 1
                else:
                    idNumNot += 1
            elif (re.search("^https://www.elsoldemexico.com.mx/", webSiteAux)):
                noti = limpiarLaPrensa(noticia)
                titu = limpiarLaPrensa(titulo)
                if (len(noti.split()) > num):
                    save(titu, noti, output_file,'500',id)
                    id += 1
                else:
                    idNumNot += 1
            elif (re.search("^https://www.proceso.com.mx/", webSiteAux)):
                noti = limpiarProceso(noticia)
                titu = limpiarProceso(titulo)
                if (len(noti.split()) > num):
                    save(titu, noti, output_file,'600',id)
                    id += 1
                else:
                    idNumNot += 1
            elif (re.search("^https://www.sopitas.com/", webSiteAux)):
                noti = limpiarSopitas(noticia)
                titu = limpiarSopitas(titulo)
                if (len(noti.split()) > num):
                    save(titu, noti, output_file,'700',id)
                    id += 1
                else:
                    idNumNot += 1
        else:
            print(str(row["url"]))
            idNumNot += 1
    print(idNumNot)
    output_file.close()


# -------------------------------------Función Lematizar()---------------------------------------#
def Lematiza(text, fileCSV, nlp):
    doc = nlp(text)
    lemmas = [tok.lemma_.lower() for tok in doc]

    for x in range(len(lemmas)):
        fileCSV.write(lemmas[x])
        fileCSV.write(" ")

#----------------------------Funciones lematizar texto()----------------------------------#
def lematizar():
    nlp = spacy.load('es_core_news_sm')
    filePath = filedialog.askopenfilename()
    #input_file = csv.DictReader(open(filePath))
    fileCSV = open("CorpusBalanceadoCompleto.txt", "w+")

    print(filePath)
    noticias = pd.read_csv(filePath, sep='&&&&&', engine='python')

    id = noticias['id']
    titulo = noticias['titulo']
    contenido = noticias['noticia']
    seccion = noticias['seccion']

    encabezado = "id&&&&&titulo&&&&&noticia&&&&&seccion\n"
    fileCSV.write(encabezado)

    for i in range(len(contenido)):
        fileCSV.write(str(id))
        fileCSV.write(" &&&&& ")
        text = str(titulo[i])
        Lematiza(text, fileCSV, nlp)
        fileCSV.write("&&&&&")

        text = str(contenido[i])
        Lematiza(text, fileCSV, nlp)
        fileCSV.write("&&&&&")

        fileCSV.write(str(seccion[i]))
        fileCSV.write("\n")
    #	print(str(seccion[i]))
    print("Finalizado")

    fileCSV.close()

def menu():
#    raiz = Tk()
#    raiz.title("Menú")
#
#    miFrame = Frame()
#    miFrame.pack()
#    miFrame.config(width ="450", height="200")
#    miFrame.config(bd=15)
#    miFrame.config(relief="groove")
#
#    btnUno = Button(miFrame, text="Limpiar", command=limpiar).grid(row=5, column=0, sticky="w")
#    btnDos = Button(miFrame, text="Lematizar", command = lematizar).grid(row = 5, column = 1, sticky ="w")
    limpiar()
    #raiz.mainloop()

if __name__ == '__main__':
    menu()