################
# Martín René - @martinvilu
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def anagrama(cadena1, cadena2):
    palabra1 = list(cadena1.lower())
    palabra2 = list(cadena2.lower())

    palabra1.sort()
    palabra2.sort()

    if palabra1 == palabra2:
        return True
    else:
        return False


def principal():
    cadena1 = input('Ingrese texto 1: ')
    cadena2 = input('Ingrese texto 2: ')

    resultado = anagrama(cadena1, cadena2)

    if resultado:
        print(f'{cadena1} y {cadena2} son un anagrama')
    else:
        print(f'{cadena1} y {cadena2} no son un anagrama')

if __name__ == "__main__":
    principal()

