#Actividad 1.2: A partir del programa desarrollado en la Actividad 1.1, realizar un nuevo programa que tomando como entrada un fichero de texto, obtenga como salida un nuevo fichero con las siguientes características
#El fichero de texto de salida debe:
#-Comenzar exactamente por los mismos contenidos del fichero de entrada
#-Incluir a continuación una línea adicional con una secuencia de 8 caracteres en hexadecimal (se utilizará la representación en minúsculas de las letras a-z)
#-El resumen SHA-256 del fichero debe comenzar por por la secuencia de 0s más larga que se pueda obtener en un minuto de ejecución del programa


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
			sec=''.join(random.choice('abcdef0123456789') for _ in range(8))
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
