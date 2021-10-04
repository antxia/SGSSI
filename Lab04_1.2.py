import hashlib, sys, shutil
import random, string

#Códigos de colores.
AMARILLO = '\033[93m'
ROJO = '\033[91m'
BLANCO = '\033[0m'

try:
	original=r"{}".format(sys.argv[1])
	copia=r"{}HEX.txt".format(sys.argv[1][:-4])
	while True:
		shutil.copyfile(original,copia)
		with open("{}HEX.txt".format(sys.argv[1][:-4]), 'a') as f:
			#Generar una secuencia aleatoria
			sec=''.join(random.choice('abcdef0123456789') for _ in range(6))
			#Guarda el documento con la línea adicional.
			f.write("{}\n".format(sec))
		with open("{}HEX.txt".format(sys.argv[1][:-4]), 'rb') as f2:
			archivo1 = f2.read()
			#Calcula el resumen
			resumen = str(hashlib.sha256(archivo1).hexdigest())
		if resumen.startswith("0000"):
			print(AMARILLO + "El documento {} se ha actualizado.".format(sys.argv[1])+BLANCO)
			exit(1)		
#Si el fichero no existe devuelve un error.
except Exception:
	print(ROJO + "No se ha podido encontrar el fichero\n" + BLANCO)
	exit(1)
