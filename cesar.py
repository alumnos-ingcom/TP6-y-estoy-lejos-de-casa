################
# Martín René - @martinvilu
# UNRN Andina - Introducción a la Ingenieria en Computación
################


def cifrado(palabra, desplazamiento):
    cifrado = ''

    for x in palabra:
        if x.islower() is True:
            posX = ord(x) - 97
            Ord = (posX + desplazamiento)%26 + 97
            Xcifrado = chr(Ord)
            cifrado+=Xcifrado
        elif x.isupper() is True:
            posX = ord(x) - 65
            Ord = (posX + desplazamiento)%26 + 65
            Xcifrado = chr(Ord)
            cifrado+=Xcifrado
        
    return cifrado

def descifrado(palabra, desplazamiento):
    descifra = ''

    for x in palabra:
        if x.islower() is True:
            posX = ord(x) - 97
            Ord = (posX - desplazamiento)%26 + 97
            Xdescifrado = chr(Ord)
            descifra+=Xdescifrado
        elif x.isupper() is True:
            posX = ord(x) - 65
            Ord = (posX - desplazamiento)%26 + 65
            Xdescifrado = chr(Ord)
            descifra+=Xdescifrado

    return descifra