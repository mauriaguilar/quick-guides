# Este script elimina todos los branchs remotos excepto master y los de la lista BRANCHES_A_DEJAR

# 0) CONFIGURACION
# Branches o patrones de nombres que No se deben borrar
BRANCHES_A_DEJAR = [
    "release",
    "feature",
    "release/paquete_FE-2.16.1",
    "release/paquete_FE-2.11.5",
    "release/paquete_FE-2.11.47",
    "release/paquete_FE-2.14.5",
    "release/paquete_WV-2.9.1",
    "release/paquete_WV-2.10.0",
    "release/paquete_WV-2.8.4",
]
# Cantidad de branches a eliminar simultaneamente mediante confirmacion
TAMANIO_BLOQUE_COMANDOS = 30


# ---------------------------------------------------------------------
from subprocess import call

# Funcion de ejecución por consola
def run(comando):
    print(">>>"+comando+"\n")
    call(comando, shell=True)

# 1) Obtener todos los cambios
run("git stash")
run("git fetch --all")

# 2) Ubicarse en master
run("git checkout master")

# 3) Generar una lista de branches en el archivo branches.txt
run("git branch -a | grep remotes | grep -v master > branches.txt")

# 4) Guardar los branches del archivo branches.txt en la variable branches
f = open("branches.txt", "r")
branches = f.readlines()
f.close()

# 5) Creo una nueva lista excluyendo los branches importantes
branches_a_borrar = []
for branch in branches:
    agregar = True
    # Chequeo si el branch actual no es uno de los que hay que dejar
    for branch_importante in BRANCHES_A_DEJAR:
        if branch_importante in branch:
            agregar = False
    if agregar:
        branches_a_borrar.append(branch)

# 6) Eliminar branch por branch, todos los branches de la lista branches_a_borrar, de a bloques
cantidad_branches_eliminar = TAMANIO_BLOQUE_COMANDOS
contador_comandos = 0
bloque_comandos = []
contador_branches_eliminados = 0
for branch in branches_a_borrar:
    # Recorto enter y espacios de izquierda y derecha
    branch_actual = branch.strip()
    # Creo el comando para eliminar el branch
    nuevo_comando = "git push -d " + branch_actual
    # Agrego el comando a la lista
    bloque_comandos.append(nuevo_comando)
    # Incremento el contador de comandos
    contador_comandos += 1
    # Verifico si el bloque de comandos está completo
    if contador_comandos % cantidad_branches_eliminar == 0 or branch == branches_a_borrar[-1]:
        # Imprimo el bloque de comandos a ejecutar
        print("\n\nBorrar branches remotos con el bloque de comandos: ")
        for nro in range(len(bloque_comandos)):
            bloque_comandos[nro] = bloque_comandos[nro].replace("remotes/origin/", "origin ")
            print(bloque_comandos[nro])
        # Consulto al usuario si desea ejecutar la lista de comandos
        print("Ejecutar este bloque de comandos? (Enter para Confirmar, No para Omitir, S para Salir): ", end="")
        respuesta = input()
        # Chequeo la respuesta del usuario para saber si quiere Salir, Ejecutar o Omitir
        if respuesta == "s" or respuesta == "S" or respuesta == "salir":
            print("Terminado por el usuario.")
            break
        if respuesta == "" or respuesta == "si" or respuesta == "Si" or respuesta == "SI":
            for comando in bloque_comandos:
                print("->", end="")
                contador_branches_eliminados += 1
                # Elimino branch remoto
                run(comando)
        else:
            print("Bloque de comandos No ejecutado. ("+respuesta+") <-<-<-<-<-")
        # Reseteo variables ciclicas
        contador_comandos = 0
        bloque_comandos = []

print("\n\n" + str(contador_branches_eliminados) + " branchs eliminados.")
print("Fin del programa.")