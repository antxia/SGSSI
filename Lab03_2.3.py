#Actividad 2.3: Realizar un programa que, tomando como entrada dos ficheros de texto, obtenga como salida el resultado de comprobar si
#Uno de los ficheros de texto de entrada comienza exactamente por los mismos contenidos que el otro, e incluye a continuación una línea que contiene exactamente el resumen SHA-256 (en versión hex:) del fichero original.


import hashlib, sys
import difflib

#Códigos de colores.
AMARILLO = '\033[93m'
ROJO = '\033[91m'
BLANCO = '\033[0m'

try:
	#Coge el archivo leyendo del argumento pasado.
	with open(sys.argv[1], 'rb') as f:
		archivo1 = f.read()
		#Calcula el resumen
		resumen1 = str(hashlib.sha256(archivo1).hexdigest())
	with open(sys.argv[2], 'rb') as f:
		archivo2 = f.read()
		#Calcula el resumen
		resumen2 = str(hashlib.sha256(archivo2).hexdigest())
#Si el fichero no existe devuelve un error.
except Exception:
	print(ROJO + "No se ha podido encontrar el fichero\n" + BLANCO)
	exit(1)
with open(sys.argv[1], 'r') as f:
	file_1_text = f.readlines()
with open(sys.argv[2], 'r') as f:
	file_2_text = f.readlines()
for line in difflib.unified_diff(file_1_text, file_2_text, fromfile=sys.argv[1], tofile=sys.argv[2], lineterm=''):
    if line[0]=='+' and line[1]!='+':
    	if line[1:-1]==str(resumen1) or line[1:-1]==str(resumen2):
    		print(AMARILLO + "Los archivos cumplen con la condición" + BLANCO)
    		exit(1)
print(AMARILLO + "Los archivos no cumplen con la condición" + BLANCO)
