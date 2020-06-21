def obtener_distancias(points):
    """Calcula la distancia de puntos de una lista.

    Parámetros: points list [int, int, int]

    Retorna: Lista de distancias_calculadas [int, int, int]
    """
    points_size = len(points) - 1
    distancias_calculadas = []
    position_counter = 1

    for i in range(len(points) - 1):
        for j in range(points_size):
            # print(points[i])
            # print(points[j + position_counter])
            distancias_calculadas.append(distancia(points[i], points[j + position_counter]))

        position_counter += 1 #Recorre una posición para calcular las posiciones siguientes
        points_size -= 1 #Disminuye el alcance del rango para no exceder la lista de vectores

    print(f'Distancias calculadas: {distancias_calculadas}')
    return distancias_calculadas


def obtener_distancia_mas_corta(distancias):
    """De una lista de distancias identifica la más corta.

    Parámetros: distancias list [int, int, int]

    Retorna: Lista con el valor de la distancia menor con sus identificadores de punto [int, int, int]
    """
    valores_distancias = []
    for distancia in distancias:
        valores_distancias.append(distancia[0])

    distancia_menor = min(valores_distancias)
    # print(valores_distancias)
    # print(distancia_menor)

    distancia_mas_corta = []
    for distancia in distancias:
        if distancia_menor == distancia[0]:
            distancia_mas_corta = distancia

    # print(distancia_mas_corta)
    return distancia_mas_corta


def distancia(punto_1, punto_2):
    """Calcula la distancia euclidiana entre dos puntos.

    Parámetros: punto_1, punto_2 list [int, int, int]

    Retorna: Una lista con el cálculo de la distancia y los identificadores de cada punto. [int, int, int]"""
    a = punto_1[1]
    b = punto_1[2]
    c = punto_2[1]
    d = punto_2[2]
    id_punto_1 = punto_1[0]
    id_punto_2 = punto_2[0]

    result = ((a - c)**2 + (b - d)**2)**0.5 #Cálculo de distancia euclidiana

    return [result, id_punto_1, id_punto_2]


def crear_cluster(distancia_mas_corta, vectors):
    """Agrupa dos puntos en un solo punto que está en medio de esos dos.

    Parámetros:
    distancia_mas_corta list [float, int, int]
    vectors list [list, list, ...]

    Retorna: Una lista con el cluster creado en forma de punto y los id de los puntos con los que se creó. 
    tuple (list, int, int)
    """
    # puntos_a_agrupar = []

    punto_a_agrupar_1 = vectors[distancia_mas_corta[1]]
    punto_a_agrupar_2 = vectors[distancia_mas_corta[2]]
    # puntos_a_agrupar.append(vectors[distancia_mas_corta[1]]) #Accediendo a puntos dentro de los vectors con sus id.
    # puntos_a_agrupar.append(vectors[distancia_mas_corta[2]])

    a = punto_a_agrupar_1[1]
    b = punto_a_agrupar_1[2]
    c = punto_a_agrupar_2[1]
    d = punto_a_agrupar_2[2]
    id_punto_1 = punto_a_agrupar_1[0]
    id_punto_2 = punto_a_agrupar_2[0]

    x = (a + c)/2 #Cálculo de coordenadas punto medio entre dos puntos.
    y = (b + d)/2

    id_punto = min(id_punto_1, id_punto_2)
    cluster = [id_punto, x , y]

    print(f'Cluster: {cluster}. Agrupa: {punto_a_agrupar_1}, {punto_a_agrupar_2}') #Cluster
    return (cluster, id_punto_1, id_punto_2)


def agrupamiento_jerarquico(vectors):
    while len(vectors) > 1:
        print(vectors)
        distancias = obtener_distancias(vectors)
        distancia_mas_corta = obtener_distancia_mas_corta(distancias)
        punto, eliminar_1, eliminar_2 = crear_cluster(distancia_mas_corta, vectors)

        vectors_copy = vectors.copy()
        for vector in vectors:
            if vector[0] == eliminar_1 or vector[0] == eliminar_2:
                vectors_copy.remove(vector)
        vectors_copy.append(punto)
        vectors = vectors_copy.copy()
        
        print('****'*20)

    print(f'Agrupamiento final: {vectors}')


if __name__ == "__main__":
    coordenadas = [[0, 5, 0], [1, 3, 2], [2, 4, 5], [3, 0, 4], [4, 4, 4]] #[id_punto, x, y]
    agrupamiento_jerarquico(coordenadas)