################
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def hace_etiqueta(contenido, etiqueta):
    return '<%s>%s</%s>' %(etiqueta, contenido, etiqueta)

def crear_pagina():
    body= 'body'
    encabezado = hace_etiqueta('Hola HTML', 'h1')
    encabezado2=hace_etiqueta(' Párrafo', 'p')
    parrafo = hace_etiqueta(encabezado+encabezado2, body)
    cuerpo= hace_etiqueta(parrafo,'html')
    return cuerpo
    
def control_archivo(texto,nombre):
    archivo_nuevo=open(nombre+'.html','w')
    
    archivo_nuevo.write(texto)
    
    archivo_nuevo.close()

def principal():
    nombre= input("como quiere guardar el archivo?")
    texto=crear_pagina()
    control_archivo(texto,nombre)
    
 
if __name__ == "__main__":
    principal()
        