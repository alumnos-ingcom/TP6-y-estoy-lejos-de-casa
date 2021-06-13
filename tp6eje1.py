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
    texto1 = input('Ingrese palabra 1: ')
    texto2 = input('Ingrese palabra 2: ')

    cadena1 = texto1.replace(" ", "")
    cadena2 = texto2.replace(" ", "")

    resultado = anagrama(cadena1, cadena2)

    if resultado:
        print(f'{texto1} y {texto2} son un anagrama')
    else:
        print(f'{texto1} y {texto2} no son un anagrama')


if __name__ == "__main__":
    principal()
