################
# Martín René - @martinvilu
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from tp6ej1 import anagrama


def obtener_palabras(linea):
    palabra_generada1 = ""
    palabra_generada2 = ""

    cadena = linea.replace(" ", "")

    longitud_linea = len(cadena)

    for indice in range(0,longitud_linea):

        if cadena[indice] == "–":
            for i in range(indice+1,longitud_linea):
                palabra_generada2+=cadena[i]
            break
        else:
            palabra_generada1+=cadena[indice]


    palabra1 = palabra_generada1.replace("\n", "")
    palabra2 = palabra_generada2.replace("\n", "")

    return palabra1, palabra2


def principal():
	archivo = open('anagramas.txt', 'r')
	
	for linea in archivo.readlines():
		
		cadena1, cadena2 = obtener_palabras(linea)
	
		resultado = anagrama(cadena1, cadena2)
		
		if resultado:
			print(f'{cadena1} y {cadena2} son un anagrama')
		else:
			print(f'{cadena1} y {cadena2} no son un anagrama')
        

if __name__ == '__main__':
	principal()
