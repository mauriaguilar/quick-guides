import urllib.request as urllib2
from datetime import date
from datetime import datetime

class Producto:
    def __init__(self, nombre, url):
        self.nombre = nombre
        self.url = url
        self.precio = 0
        self.precio_dcto = 0
        self.dcto = 0

# Leo productos de bd productos
f = open("productos.csv")
listado_productos = f.readlines()
f.close()
print(listado_productos[0].split(",")[1])

# Guardar productos en un arreglo
productos = []
for item in listado_productos:
    productos.append(Producto(item.split(",")[0], item.split(",")[1]))

# Buscar nuevos precios
clave = "ASDASDASD"
separador_inicio = "<span"
separador_fin = "</span>"
eliminar1 = "<span class=\"price-tag-fraction\">"
eliminar2 = "</span>"
for producto in productos:
    try:
        # Obtener pagina
        print("Leyendo pagina: ",producto.url)
        f = urllib2.urlopen(producto.url)
        html = str(f.read())
        f.close()
        #print(html)

        # Inserto palabras claves donde necesito recortar
        html = html.replace(separador_inicio, clave + separador_inicio)
        html = html.replace(separador_fin, separador_fin + clave)
        # Recorto el html por palabras claves
        html = html.split(clave)

        # Leer renglon por renglon y buscar la palabra
        for renglon in html:
            #if len(renglon) < 50 and "price-tag" in renglon:
            #    print("renglon::: "+renglon+"\n")
            if "price-tag-fraction" in renglon:
                renglon = renglon.replace(eliminar1,"")
                renglon = renglon.replace(eliminar2,"")
                renglon = renglon.replace(".","")
                producto.precio = renglon
                print("  Precio "+producto.nombre+": "+producto.precio)
    except Exception as e:
        print("Ocurrio un error: "+str(e))

# Guardar precios
fecha_hoy = date.today()
ahora = datetime.now()
for producto in productos:
    f = open("precios_" + producto.nombre + ".csv", "a")
    f.write(str(ahora) + "," + str(fecha_hoy) + "," + str(ahora.hour) + "," + str(producto.precio) + "\n")
    f.close()

print("finalizadoo---")