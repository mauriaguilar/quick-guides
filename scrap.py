import urllib2

letras = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
letras = ["a"]
palabras = []

for letra in letras:
    pagina = 1

    while True:

        try:
            # https://EXAMPLE.com/a?page=1
            url = "https://EXAMPLE.com/"+letra+"?page="+str(pagina)
            print "Leyendo pagina: ",url
            f = urllib2.urlopen(url)
            html = f.read().split("<")
            f.close()

            # Leer renglon por renglon y buscar la palabra
            cant_pal_en_esta_letra = 0
            for renglon in html:
                if "loadEcho" in renglon:
                    cant_pal_en_esta_letra += 1
                    #<p id="loadEcho">natricine<img src="images/speaker.png" class="result_speaker"></p>
                    palabras.append(renglon.replace("p id='loadEcho'>","").replace(" ","%20")
        except:
            print "Ocurrio un error"

        # Si no encontro palabras, pasar a la siguiente letra
        if cant_pal_en_esta_letra == 0:
            pagina = 1
            print "Letra ",letra,"terminada"
            break # Sale del while y pasa a la siguiente letra
        # Sino pasar a la siguiente pagina
        else:
            print "Letra "+letra+": Siguiente pagina"
            pagina += 1

# Ver y guardar palabras
print palabras
texto = ""
for palabra in palabras:
    texto += palabra+"\n"
f = open("palabras.txt", "a")
f.write(texto)
f.close()

# Descargar audio
ultima_palabra_descargada = "adjust"
encontre_palabra = False
for palabra in palabras:
    while not encontre_palabra:
        if palabra == ultima_palabra_descargada
            encontre_palabra = True
        continue
    try:
        # http://www.EXAMPLE.com/mp3/"+palabra+".mp3
        url = "http://www.EXAMPLE.com/mp3/"+palabra+".mp3"
        print "Leyendo pagina: ",url
        f = urllib2.urlopen(url)
        audio = open(palabra+".mp3", "w")
        audio.write( f.read() )
        audio.close()
        f.close()
    except:
        print "Ocurrio un error con el audio de",palabra
        palabras_error.append(palabra)


# Descargar audio de palabras con error
for palabra in palabras:    
    try:
        # http://www.EXAMPLE.com/mp3/"+palabra+".mp3
        url = "http://www.EXAMPLE.com/mp3/"+palabra+".mp3"
        print "Reintentando con pagina: ",url
        f = urllib2.urlopen(url)
        audio = open(palabra+".mp3", "w")
        audio.write( f.read() )
        audio.close()
        f.close()
    except:
        print "Ocurrio un error con el audio de",palabra
        f = open("palabras_error.txt", "a")
        f.write(palabra+"\n)
        f.close()

