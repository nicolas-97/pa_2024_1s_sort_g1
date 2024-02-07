def shell_sort(vector):
    distancia = len(vector)//2
    tamaño = len(vector)
    while distancia > 0 :
        vector = insercion(vector, distancia)
        distancia = distancia//2    
    return print(vector)

def insercion(vector, distancia):
    for i in range(distancia, len(vector)-1): #Posicion del elemento con el cual empezamos a comparar
                for j in range(i+1, len(vector)): #Posicion del elemento con el cual comparamos i 
                    if vector[i] > vector[j]:
                        vector[i], vector[j] = vector[j], vector[i]
                        if i != 0: #Vamos a comparar si el elemento en i es menor a elementos anteriores
                            dato = vector[i]
                            for veces in range(distancia, len(vector[:i])):
                                n = vector.index(dato) #n = Posicion actual del dato que antes estaba en i.
                                if vector[n-1] > vector[n]:
                                    vector[n-1], vector[n] = vector[n], vector[n-1]
                                else:
                                    continue
                    i += 1
    return vector

def quick_sort(vector):
    return vector

def merge_sort(vector):
    return vector

vect = [30,3,565,8,3,7,2]
m = shell_sort(vect)




















def ordenamiento_insercion(vector,longitud_vector): #Ordenamiento que compara los elementos por parejas y los reubica a la posición favorable. 
    #Este ordenamiento en la comparación tambien revisa si el antecesor del elemento que estamos comparando es menor y de ser asi intercambia posiciones.
    for i in range(longitud_vector-1): #Posicion del elemento con el cual empezamos a comparar
        for j in range(i+1, longitud_vector): #Posicion del elemento con el cual comparamos i 
            if vector[i] > vector[j]:
                vector[i], vector[j] = vector[j], vector[i]
                if i != 0: #Vamos a comparar si el elemento en i es menor a elementos anteriores
                    dato = vector[i]
                    for veces in range(len(vector[:i])):
                        n = vector.index(dato) #n = Posicion actual del dato que antes estaba en i.
                        if vector[n-1] > vector[n]:
                            vector[n-1], vector[n] = vector[n], vector[n-1]
                        else:
                            continue
            i += 1
    return print(f'vector ordenada : {vector}')