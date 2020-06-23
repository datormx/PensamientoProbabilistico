import random

def generar_centroides(k):
    """Genera k puntos al azar

    Parámetros:
    k int > 0

    Retorna: Lista de k listas de puntos x,y [[int, int], [int, int],...]
    """
    centroids = []
    for _ in range(k):
        x = random.randint(-10, 10) #Genera puntos con coordenadas de -10 a 10
        y = random.randint(-10, 10)
        centroid = [x, y]
        centroids.append(centroid)

    print(f'Centroides originales: {centroids}')
    return centroids
    

def clusterizar(puntos, centroides):
    """Calcula la distancia de una lista de puntos designados por coordenas x,y con
    una lista de centroides con coordenadas x,y.

    Parámetros:
    puntos list [[int, int], [int, int],...]
    centroides list [[int, int], [int, int],...]

    Retorna: Lista con listas con punto, centroide_asignado, distancia_punto_centroide 
    [[[int, int], [int, int], float], [[int, int], [int, int], float], ...]
    """
    elementos_clusters = []    

    for punto in puntos:
        puntos_centroides_distancias = []
        for centroide in centroides:
            distancia_calculada = distancia(punto, centroide)
            puntos_centroides_distancias.append(distancia_calculada)
        # print(puntos_centroides_distancias)
        # print('\n')

        distancias_calculadas = []
        for el in puntos_centroides_distancias:
            distancias_calculadas.append(el[2])

        distancia_min = min(distancias_calculadas)
        
        for el in puntos_centroides_distancias:
            if el[2] == distancia_min:
                elementos_clusters.append(el)  
    
    print(f'Elementos: {elementos_clusters}')
    print(f'Cantidad elementos: {len(elementos_clusters)}')
    print('\n')
    return elementos_clusters


def distancia(punto_1, punto_2):
    """Cálcula la distancia euclidiana entre dos puntos.
    
    Parámetros:
    punto_1, punto_2 list [int, int]
    
    Retorna:
    Una lista con el punto_1, punto_2 y su distancia calculada
    [[int, int], [int, int], float]
    """
    a = punto_1[0]
    b = punto_1[1]
    c = punto_2[0]
    d = punto_2[1]

    result = ((a - c)**2 + (b - d)**2)**0.5 #Cálculo de distancia euclidiana

    return [punto_1, punto_2, result]


def calcular_nuevo_centroide(elementos_cluster, centroids, k):
    """Calcula el punto promedio de una serie de puntos relacionados para
    convertirlo en el nuevo centroide del cluster.

    Parámetros:
    elementos_cluster list [[punto, centroide, distancia], [punto, centroide, distancia], ...]
    k int > 0

    Retorna:
    Lista con los nuevos centroides calculados en forma [x, y]
    list [centroide, centroide, ...]
    """
    for i in range(k):
        puntos_centroide = []
        for el in elementos_cluster:
            if el[1] == centroids[i]:
                puntos_centroide.append(el)
        print(puntos_centroide)
        print('\n')

    

def agrupamiento_k_means(vectors, k):
    centroides = generar_centroides(k)

    elementos = clusterizar(vectors, centroides)
    nuevos_centroides = calcular_nuevo_centroide(elementos, centroides, k)


if __name__ == "__main__":
    coordenadas = [[1, 0], [3, 5], [4, 5], [-1, 1], [-2, 3], [-4, 1], [-3, 1], [-1, -4], [-3, -2], [-4, -1], [1, -3], [4, -5], [5, -3]]
    agrupamiento_k_means(coordenadas, 4)
