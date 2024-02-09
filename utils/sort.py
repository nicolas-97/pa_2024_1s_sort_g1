def shell_sort(vector):
    longitud = len(vector)
    espacios = longitud// 2
    while espacios > 0:
        for recorrido in range(espacios, longitud):
            buffer = vector[recorrido]
            indice = recorrido
            while indice >= espacios and vector[indice - espacios] > buffer:
                vector[indice] = vector[indice - espacios]
                indice -= espacios
            vector[indice] = buffer
        espacios = espacios // 2  

    return vector

def merge_sort(vector):
    if len(vector) > 1:
        mid = len(vector) // 2
        L = vector[:mid]
        R = vector[mid:]

        merge_sort(L)  
        merge_sort(R)  

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                vector[k] = L[i]
                i += 1
            else:
                vector[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            vector[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            vector[k] = R[j]
            j += 1
            k += 1

    return vector  

def quick_sort(vector):
    if len(vector) <= 1:
        return vector

    pivot = vector[len(vector) // 2]
    less = [x for x in vector if x < pivot]
    equal = [x for x in vector if x == pivot]
    greater = [x for x in vector if x > pivot]

    return quick_sort(less) + equal + quick_sort(greater)


