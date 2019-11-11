FIRST_VALUE = 1
STEP = 2
RELATIVE_PATH = "txts"
EXTENSION_SOURCE = ".txt"
EXTENSION_DEST = ".jpg"

from os import scandir, getcwd, rename

def ls(ruta = getcwd() + "/" + RELATIVE_PATH):
    return [arch.name for arch in scandir(ruta) if arch.is_file()]

#print(ls())

CURRENT_VALUE = FIRST_VALUE
for file in ls():
   if(EXTENSION_SOURCE in file):
      new_name = str(CURRENT_VALUE)+EXTENSION_DEST
      print(file + " --> " + new_name)
      rename(RELATIVE_PATH + "/" + file,RELATIVE_PATH + "/" + new_name)
      CURRENT_VALUE += STEP
