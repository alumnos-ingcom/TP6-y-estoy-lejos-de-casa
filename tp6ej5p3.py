################
# Martín René - @martinvilu
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from cesar import descifrado

class FileNotFoundError(Exception):
    pass

def decodificar(archivo, linea, rotacion):
    archivo= open(f'{archivo}.decode','a')
    texto = descifrado(linea, rotacion)
    archivo.write(texto+'\n')

    
def principal():
    nombre_archivo = input('Ingrese el nombre del archivo: ')
    try:
        archivo = open(f'{nombre_archivo}.cesar', 'r')
    except:
        raise FileNotFoundError('El archivo no existe o no es un archivo .cesar')
    
    rotacion = int(input('Ingrese cuanto debe rotar: '))

    for line in archivo.readlines():
        decodificar(nombre_archivo, line, rotacion)

    print(f'Archivo descifrado como {nombre_archivo}.decode')

if __name__ == "__main__":
    principal()