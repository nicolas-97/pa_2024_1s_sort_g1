'''
Natalia Osejo Hincapie
'''

def shell_sort(vector):
    distancia = len(vector)//2 #Cantidad de subgrupos que saldran
    ubicacion = 0 #Indica el avance entre elementos de subgrupos
    while distancia>0: 
        while ubicacion<distancia: #No salirse del subgrupo
            for i in range(ubicacion+distancia, len(vector), distancia):
                n = i #se debe comparar el valor del vector[i] con los n vectores que lo anteceden
                while n>ubicacion:
                    n -= distancia
                    if vector[i]<vector[n]:
                        vector[i], vector[n] = vector[n], vector[i]
                        i = n
            ubicacion += 1
        distancia = distancia//2
        ubicacion = 0 #al empezar con nuevo subgrupo se reinicia ubicacion
    return vector

#----------------------------------


def quick_sort(vector):
    if len(vector) <= 1: #caso base
        return vector
    
    pivote = vector[0] #Primer elemento seleccionado como pivote
    menores = [] #subgrupos de mayores y menores
    mayores = []
    for i in range(1, len(vector)):
        if vector[i]<pivote:
            menores.append(vector[i])
        elif vector[i]>pivote:
            mayores.append(vector[i])
        else:
            menores.append(vector[i]) #Si es igual al pivote se agrega a menores
    
    menores = quick_sort(menores) #recursividad hasta llegar a caso base
    mayores = quick_sort(mayores)
    
    return quick(menores, pivote, mayores) #se acomodan los resultados

def quick(menores, pivote, mayores):
    vector_ordenado = []
    for i in range(len(menores)): #se agregan menores
        vector_ordenado.append(menores[i])
    vector_ordenado.append(pivote) #se agrega el pivote
    for i in range(len(mayores)): #se agregan mayores
        vector_ordenado.append(mayores[i])
    return vector_ordenado

#----------------------------------


def merge_sort(vector):
    if len(vector) <= 1: #caso base
        return vector
    
    longitud = len(vector)//2
    vector_der = vector[longitud:] #se crean dos subgrupos
    vector_iz = vector[:longitud]

    vector_der_orden = merge_sort(vector_der) #recursividad para llevar a todos los subgrupos al caso base
    vector_iz_orden = merge_sort(vector_iz)

    return merge(vector_der_orden, vector_iz_orden) #se retorna el array ordenado

def merge(vector_der, vector_iz):
    vector_ordenado = []
    while len(vector_der) > 0 and len(vector_iz) > 0: #Ver que no esten vacios
        if vector_der[0] > vector_iz[0]: #añadir al vector final el valor más bajo
            vector_ordenado.append(vector_iz[0])
            vector_iz.pop(0) #Se elimina del array el vector añadido al resultado
        else:
            vector_ordenado.append(vector_der[0])
            vector_der.pop(0)
    
    #El último y más grande valor se agrega
    while len(vector_der) > 0:
        vector_ordenado.append(vector_der[0])
        vector_der.pop(0)

    while len(vector_iz) > 0:
        vector_ordenado.append(vector_iz[0])
        vector_iz.pop(0)

    return vector_ordenado
