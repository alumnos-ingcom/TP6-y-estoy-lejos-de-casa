################
# Martín René - @martinvilu
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# Reemplazar por las funciones del ejercicio


def principal():
    archivo1=input("Ingrese el nombre del archivo que desea copiar: ")
    archivo2=input("Ingrese el nombre del archivo al cual se copiara el contenido: ")
    f=open(archivo1, "r")
    r=open(archivo2,"r")
    contenido_f=f.read()
    contenido_r=r.read()
    r.close()
    print(f"Archivo 1 tiene: \n{contenido_f}")
    print(f"Archivo 2 tiene: \n{contenido_r}")
    
    r=open(archivo2,"a")
    r.write("\n")
    r.write(contenido_f)
    r.close()
    
    r=open(archivo2,"r")
    contenido_r=r.read()
    print(f"Ahora, archivo 2 tiene: \n{contenido_r}")
    f.close()
    r.close()
    pass

if __name__ == "__main__":
    principal()

