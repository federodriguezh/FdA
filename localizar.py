import sys # Importamos la libreria.

# Importamos el tipo DependenciaJudicial. 
from dependencia_judicial import DependenciaJudicial

# Definimos una funcion que cargue las dependencias judiciales del archivo que se le pasa como argumento. 
def cargar_dependencias(archivo):
    dependencias = [] # Creamos una lista vacía para guardar cada una de las dependencias.
    archivo = open(archivo, encoding='latin-1') # Abrimos el archivo que el usuario pasa como argumento.
    # Cargamos solo los atributos que consideramos necesarios para la resolución de este ejercicio.
    for linea in archivo:
        atributos = linea.split(";")
        numero = atributos[0]
        # Hacemos un if para que la fila que indica el nombre de la columna no se guarde.
        if numero != "Número":
            fuero = atributos[1]
            nombre = atributos[2]
            direccion = atributos[4]
            localidad = atributos[5]
            latitud = float(atributos[8].replace(',','.'))
            longitud = float(atributos[9].replace(',','.'))
            dependencia = DependenciaJudicial(linea)
            dependencias.append(dependencia)
    archivo.close()
    return dependencias

# Cargo el archivo que le paso despues de python en la consola y lo guardo en dependencias:
dependencias = cargar_dependencias(sys.argv[1])

# Le indico que luego del archivo le paso la latitud y la longitud en la consola 
# y lo guardo en latitud y longitud respectivamente:
latitud = sys.argv[2]
longitud = sys.argv[3]

# Creo un diccionario para almacenar las dependencias en funcion de las distancias:
distancias = dict()

# Creo una lista para almacenar las distancias:
min_distancia = []

# Itero en las dependencias y para cada distancias (clave) le asigno el valor de la dependencia.
# Ademas guardo las dependencias en una lista.
for dependencia in dependencias:
    distancias[dependencia.distancia(latitud, longitud)] = dependencia
    min_distancia.append(dependencia.distancia(latitud, longitud))
    
# Ordeno las distancias:
min_distancia.sort()

# Devuelvo la dependencia asociada a la menor distancia:
print(distancias[min_distancia[0]])
