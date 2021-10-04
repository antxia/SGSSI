import hashlib, sys

#Códigos de colores.
AMARILLO = '\033[93m'
ROJO = '\033[91m'
BLANCO = '\033[0m'

try:
	#Coge el archivo leyendo del argumento pasado.
	with open(sys.argv[1], 'rb') as f:
		bytes = f.read()
		#Imprime el resumen.
		print(AMARILLO + "Resumen SHA256 del archivo {}: ".format(sys.argv[1]) + BLANCO + hashlib.sha256(bytes).hexdigest())
#Si el fichero no existe devuelve un error.
except Exception:
	print(ROJO + "No se ha podido encontrar el fichero\n" + BLANCO)
	exit(1)