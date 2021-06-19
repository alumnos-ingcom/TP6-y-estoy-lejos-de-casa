################
# Martín René - @martinvilu
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from cesar import cifrado

class FileNotFoundError(Exception):
    pass

def codificar(archivo, linea, rotacion):
    archivo_cifrado = open(f'{archivo}.cesar','a')
    texto_cifrado = cifrado(linea, rotacion)
    archivo_cifrado.write(texto_cifrado+'\n')

    
def principal():
    nombre_archivo = input('Ingrese el nombre del archivo: ')
    try:
        archivo = open(f'{nombre_archivo}.txt', 'r')
    except:
        raise FileNotFoundError('El archivo especificado no existe en el directorio.')
    
    rotacion = int(input('Ingrese la rotacion: '))

    for line in archivo.readlines():
        codificar(nombre_archivo, line, rotacion)

    print(f'Archivo cifrado y copiado en {nombre_archivo}.cesar')

if __name__ == "__main__":
    principal()