import hashlib, sys, shutil

#Códigos de colores.
AMARILLO = '\033[93m'
ROJO = '\033[91m'
BLANCO = '\033[0m'

try:
	#Coge el archivo leyendo del argumento pasado.
	with open(sys.argv[1], 'rb') as f:
		bytes = f.read()
		#Calcula el resumen
		resumen=hashlib.sha256(bytes).hexdigest()
	#Crear copia del archivo
	original=r"{}".format(sys.argv[1])
	copia=r"{}SHA.txt".format(sys.argv[1][:-4])
	shutil.copyfile(original,copia)
	with open("{}SHA.txt".format(sys.argv[1][:-4]), 'a') as f:
		#Guarda el documento con la línea adicional.
		f.write("{}\n".format(resumen))
		#Imprime que la operación se ha realizado con éxito:
		print(AMARILLO + "El documento {} se ha actualizado con el resumen SHA256 del contenido original.".format(sys.argv[1])+BLANCO)
	#Si el fichero no existe devuelve un error.
except Exception:
	print(ROJO + "No se ha podido encontrar el fichero\n" + BLANCO)
	exit(1)
