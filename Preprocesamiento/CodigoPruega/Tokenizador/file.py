#Programa que permite limpar tokenizar y lematizar noticias
from tkinter import *
from tkinter import filedialog
import csv
import re
from nltk.tokenize import RegexpTokenizer
import demoji

import pandas as pd
"""
    0.- Deportes
    1.- Economía
    2.- Politica
    3.- Cultura
    4.- Ciencia y tecnología
"""
def limpiarAristegui(noticia):
    # Remove Emojis
    text = demoji.replace(noticia)
    clean = re.compile('<.*?>')
    clean = re.sub(clean, '', text)
    clean = re.sub(r"\(?@\w*\)?|#\w*", " ", clean)
    clean = re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '', clean)
    clean = re.sub(r"\(?@\w*\)?|#\w*|\w+[.+]\w+[.+]\w+[/+]\w+|\w+[:+][/]+\w+.\w+[/]\w+|\\u2063|\\u200d|\\xa0", " ", clean)
    RE_EMOJI = re.compile('[\U00010000-\U0010ffff]', flags=re.UNICODE)

    return RE_EMOJI.sub(r'', clean)

def limpiarAzteca(noticia):
    text = demoji.replace(noticia)
    clean = re.compile('<.*?>')
    clean = re.sub(clean, '', text)
    clean = re.sub(r"\(?@\w*\)?|#\w*", " ", clean)
    clean = re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '', clean)
    clean = re.sub(r"\\?|\(?@\w*\)?|#\w*|\w+[.+]\w+[.+]\w+[/+]\w+|\w+[:+][/]+\w+.\w+[/]\w+", "", clean)
    RE_EMOJI = re.compile('[\U00010000-\U0010ffff]', flags=re.UNICODE)

    return RE_EMOJI.sub(r'', clean)

def limpiarElEconomista(noticia):
    text = demoji.replace(noticia)
    clean = re.compile('<.*?>')
    clean = re.sub(clean, '', text)
    clean = re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '', clean)
    clean = re.sub(r"\(?@\w*\)?|#\w*|\w+[.+]\w+[.+]\w+[/+]\w+|\w+[:+][/]+\w+.\w+[/]\w+|\\xa0|</?p+,?|</?a|href=""/\w+-\w+/\w+/\w+-\w+|</?strong|<span\sclass=[_+]\w+|\[\w+\s\w+\]|\w+-\w+=\w+|</?span|<!-- Se agrega para compatibilidad con noticias historicas --", "", clean)
    return clean

def limpiarLaJornada(noticia):
    text = demoji.replace(noticia)
    clean = re.compile('<.*?>')
    clean = re.sub(clean, '', text)
    clean = re.sub(r"\(?@\w*\)?|#\w*", " ", clean)
    clean = re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '', clean)
    clean = re.sub(r"\(?@\w*\)?|#\w*|\w+[.+]\w+[.+]\w+[/+]\w+|\w+[:+][/]+\w+.\w+[/]\w+|\\u2063|\\u200d|\\xa0", " ", clean)
    RE_EMOJI = re.compile('[\U00010000-\U0010ffff]', flags=re.UNICODE)

    return RE_EMOJI.sub(r'', clean)

def limpiarLaPrensa(noticia):
    text = demoji.replace(noticia)
    clean = re.compile('<.*?>')
    clean = re.sub(clean, '', text)
    clean = re.sub(r"\(?@\w*\)?|#\w*", " ", clean)
    clean = re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '', clean)
    clean = re.sub(r"\(?@\w*\)?|#\w*|\w+[.+]\w+[.+]\w+[/+]\w+|\w+[:+][/]+\w+.\w+[/]\w+|\\u2063|\\u200d|\\xa0", " ",clean)
    RE_EMOJI = re.compile('[\U00010000-\U0010ffff]', flags=re.UNICODE)

    return RE_EMOJI.sub(r'', clean)

def limpiarProceso(noticia):
    text = demoji.replace(noticia)
    clean = re.compile('<.*?>')
    clean = re.sub(clean, '', text)
    clean = re.sub(r"\(?@\w*\)?|#\w*", " ", clean)
    clean = re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '', clean)
    clean = re.sub(r"\(?@\w*\)?|#\w*|\w+[.+]\w+[.+]\w+[/+]\w+|\w+[:+][/]+\w+.\w+[/]\w+|\\u2063|\\u200d|\\xa0", " ",
                   clean)
    RE_EMOJI = re.compile('[\U00010000-\U0010ffff]', flags=re.UNICODE)
    return RE_EMOJI.sub(r'', clean)

def limpiarSopitas(noticia):
    text = demoji.replace(noticia)
    clean = re.compile('<.*?>')
    clean = re.sub(clean, '', text)
    clean = re.sub(r"\(?@\w*\)?|#\w*", " ", clean)
    clean = re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '', clean)
    clean = re.sub(r"\(?@\w*\)?|#\w*|\w+[.+]\w+[.+]\w+[/+]\w+|\w+[:+][/]+\w+.\w+[/]\w+|\\u2063|\\u200d|\\xa0", " ",
                   clean)
    RE_EMOJI = re.compile('[\U00010000-\U0010ffff]', flags=re.UNICODE)

    return RE_EMOJI.sub(r'', clean)

def save(titulo, noticia, archivo):
    tokenizer = RegexpTokenizer('\w+|\$[\d\,\d\.]+|\S')
    titulo = tokenizer.tokenize(titulo)
    for word in titulo:
        archivo.write(word + ' ')
    archivo.write(" &&&&& ")
    noticia = tokenizer.tokenize(noticia)
    for word in noticia:
        archivo.write(word + ' ')
    archivo.write(" &&&&& ")
    archivo.write("1")
    archivo.write('\n')

def limpiar():
    filePath = filedialog.askopenfilename()
    input_file = csv.DictReader(open(filePath))
    output_file = open("economiaCompleto.txt", "a+")
    for row in input_file:
        webSiteAux = str(row["url"])
        noticia = str(row["noticia"])
        titulo = str(row["titulo"])
        len(noticia.split())
        if(re.search("^https://aristeguinoticias.com/", webSiteAux)):
            noti = limpiarAristegui(noticia)
            if (len(noti.split()) > 20):
                save(titulo, noti, output_file)
        elif(re.search("^https://www.tvazteca.com/", webSiteAux)):
            noti = limpiarAzteca(noticia)
            if (len(noti.split()) > 60):
                save(titulo, noti, output_file)
        elif (re.search("^https://www.eleconomista.com.mx/", webSiteAux)):
            noti = limpiarElEconomista(noticia)
            if (len(noti.split()) > 60):
                save(titulo, noti, output_file)
        elif (re.search("^https://www.jornada.com.mx/", webSiteAux)):
            noti = limpiarLaJornada(noticia)
            if(len(noti.split()) > 20):
                save(titulo, noti, output_file)
        elif (re.search("^https://www.la-prensa.com.mx/", webSiteAux)):
            noti = limpiarLaPrensa(noticia)
            if (len(noti.split()) > 20):
                save(titulo, noti, output_file)
        elif (re.search("^https://www.proceso.com.mx/", webSiteAux)):
            noti = limpiarProceso(noticia)
            if(len(noti.split()) > 60):
                save(titulo, noti, output_file)
        elif (re.search("^https://www.sopitas.com/", webSiteAux)):
            noti = limpiarSopitas(noticia)
            if(len(noti.split()) > 20):
                save(titulo, noti, output_file)

    output_file.close()


def tokenizar():
    filePath = filedialog.askopenfilename()
    input_file = csv.DictReader(open(filePath))
    noticias = []
    for row in input_file:
        noticia = str(row["noticia"])
        noticias.append(noticia)

    tokenizer = RegexpTokenizer('\w+|\$[\d\,\d\.]+|\S')
    print(tokenizer.tokenize(noticias[0]))


def menu():
    raiz = Tk()
    raiz.title("Menú")

    miFrame = Frame()
    miFrame.pack()
    miFrame.config(width ="450", height="200")
    miFrame.config(bd=15)
    miFrame.config(relief="groove")

    btnUno = Button(miFrame, text="Limpiar", command=limpiar).grid(row=5, column=0, sticky="w")
    btnDos = Button(miFrame, text="Tokenizar", command = tokenizar).grid(row = 5, column = 1, sticky ="w")
    #btnTres = Button(miFrame, text="Lematizar", command=openCSV).grid(row=5, column=2, sticky="w")

    raiz.mainloop()


if __name__ == '__main__':
    menu()