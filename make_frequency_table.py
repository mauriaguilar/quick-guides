# Seteo codificacion utf8 para que lea correctamente los simbolos de los archivos
# -*- coding: utf-8 -*-

# Amplio el nivel de recursividad para que ande el quicksort
import sys
limit = 8000
sys.setrecursionlimit(limit)

dir = "./textos/"
texto = ""
files = [16,23,24]
files = [16,23,24,25,36,37,40,42,45,52,55,56,58,59,60,62,69]
files = [];
with open("texto.txt", "r") as texto:
    texto = texto.readlines()
for file in files:
    print "Leyendo archivo",file,".txt"
    with open(dir+str(file)+".txt", "r") as mas_texto:
        # print "este archivo tiene: "
        # print mas_texto.readlines()
        texto += mas_texto.readlines()
#print texto
simbolos = [
            ".", ",", "+", "(", ")", ":",
            "1", "2", "3", "4", "5", "6", "7", "8", "9", "0",
            "�", "-", "−", "–", "−", "−", "_", "!", "/", "|", "", "", "",
             "[", "]", "@", "…", "⋅", "∙", "•", "●", ";", "\n", "x̂", ""
            "Δ", "θ", "ψ", "𝑃", "µ", "∝", "τ", "&", "→", "𝑥",
            "α", "ç", "õ", "α", "†", "≈", "<", ">", "", "", "", "𝐻",
            "’’", "\"", "“", "”", "◦"
            # "´", "‘", "‘̈",
            ]
def quitarSimbolos(texto):
    for sim in simbolos:
        texto = texto.replace(sim," ")
    return texto

palabras = []
for line in texto:
    # Elimino puntos, comas, comillas de la linea
    line = quitarSimbolos(line)

    # Convierto a minusculas
    line = line.lower()

    # Divido las palabras de la lineas por espacios y las guardo en un arreglo
    palabras += line.split()

tabla = []
for pal in palabras:
    # Descartar palabras de 2 o menos letras
    if len(pal) <= 3:
        # print "Descartada por pocas letras <",pal,">"
        continue
    # Si la palabra no esta en la tabla
    estaEnTabla = False
    for reg in tabla:
        if reg[0] == pal:
            # Incremento el contador
            reg[1] += 1
            estaEnTabla = True
            break
    if not estaEnTabla:
        # Agrego palabra a la tabla
        tabla.append([pal,1])

def partition(array, begin, end):
    pivot = begin
    for i in xrange(begin+1, end+1):
        if array[i][1] <= array[begin][1]:
            pivot += 1
            array[i], array[pivot] = array[pivot], array[i]
    array[pivot], array[begin] = array[begin], array[pivot]
    return pivot

def quicksort(array, begin=0, end=None):
    if end is None:
        end = len(array) - 1
    def _quicksort(array, begin, end):
        if begin >= end:
            return
        pivot = partition(array, begin, end)
        _quicksort(array, begin, pivot-1)
        _quicksort(array, pivot+1, end)
    return _quicksort(array, begin, end)

# Quitar palabras con frecuencia de 3 o menos antes de ordenar
tabla_filtrada = []
cant_palabras = 0
for reg in tabla:
    if reg[1] > 4:
        tabla_filtrada.append(reg)
        # Contar cantidad de palabras
        cant_palabras += 1
    # else:
    #     print "Palabra descartada por poca frecuencia: <",reg[1],">"

quicksort(tabla_filtrada)

resumen = ""
for reg in tabla_filtrada:
    resumen += (str(reg[0])+"\t\t\t"+str(reg[1])+"\n")

tabla_freq = open("tabla.txt","w")
tabla_freq.write(resumen)

print "Hay",cant_palabras,"palabras"
