
def ganancia(seguidos, entrenamiento):
    """
    Calcula la ganancia obtenida por un jugador en un entrenamiento en base a su energia.
    """
    if seguidos<entrenamiento:
        return seguidos
    return entrenamiento


def max(n1, n2):
    """
    Devuelve el maximo entre dos numeros.
    """
    if n1>n2:
        return n1
    return n2


def creacion_listas(ruta):
    """
    Leemos el archivo y armamos dos listas, una con la energia de los jugadores "e_jugadores" y otra con la energia
    requerida en cada entrenamiento "e_entrenamientos".
    """
    archivo = open(ruta)
    n = int(archivo.readline().rstrip("\n"))  #Cantidad de elementos que tendran ambas listas.
    entrenamientos = lector(archivo, n)
    seguidos = lector(archivo, n)
    archivo.close()

    return seguidos, entrenamientos

def lector(archivo, n):
    """
    Lee las n lineas del archivo pasado por parametro y las guarda en una lista.
    """
    lista = []
    for i in range(n):
        lista.append(int(archivo.readline().rstrip("\n")))
    return lista


def maxElemLista(lista):
    """
    Dada una lista devuelve el elemento mas grande de los n primeros digitos.
    """
    max = 0
    for i in range(len(lista)):
        if lista[i]>max:
            max=lista[i]

    return max


def obtenerResultado(matriz):
    """
    Obtiene la ganancia maxima a partir de los datos de la matriz.
    """
    n = len(matriz)-1
    return maxElemLista(matriz[n])



def obtenerRecorrido(matriz):
    """
    Devuelve el recorrido de la matriz
    """
    lista = []

    i = 1
    while i != len(matriz):
        maximo = maxElemLista(matriz[len(matriz)-i])
        idx_max = matriz[len(matriz)-i].index(maximo)
        i += idx_max
        
        while idx_max!=0:
            idx_max-=1
            lista.append("Entreno")
            
        
        if i!=len(matriz):
            lista.append("No entreno")
            i+=1


    lista.reverse()
    lista.append("Entreno") #Siempre entrena en el ultimo dia.

    return lista


def matriz(ruta):
    """
    Creamos una matriz con las columnas siendo el dia en el que estamos (columna 0 = dia 0, columna 1 = dia 1, ...)
    y las filas siendo la cantidad de dias seguidos entrenados (fila 0 = 0 entrenamientos seguidos, fila 1 = 1 entrenamiento
    seguido, ....)
    """
    seguidos, entrenamientos = creacion_listas(ruta)
    n = len(entrenamientos)
    matriz = []

    for i in range(len(entrenamientos)):
        lista = []
        for j in range(i+1):
            lista.append(0)
        matriz.append(lista)
            
    resultado = []
    d_entrenamiento = []
    matriz[0][0] = ganancia(seguidos[0],entrenamientos[0])

    matriz[1][0] = ganancia(seguidos[0],entrenamientos[1])
    matriz[1][1] = matriz[0][0] + ganancia(seguidos[1],entrenamientos[1])
    
    for i in range(2,n):                    #Columnas --> energia entrenamiento
        for j in range(len(matriz[i])):     #Filas --> energia jugador
            matriz[i][j]
            if j == 0:
                matriz[i][j] = maxElemLista(matriz[i-2]) + ganancia(seguidos[0],entrenamientos[i])

            else:
                matriz[i][j] = matriz[i-1][j-1] + ganancia(seguidos[j],entrenamientos[i])

    resultado = obtenerResultado(matriz)
    dias = obtenerRecorrido(matriz)

    print(resultado)
    print(dias)
    
