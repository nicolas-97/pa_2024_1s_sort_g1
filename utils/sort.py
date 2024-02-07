def shell_sort(vector):
    largo = 0
    
    for i in vector:
        largo += 1
    
    distancia = largo // 2
    
    while distancia > 0:
        for i in range(distancia, largo):
            val = vector[i]
            j = i
            while j >= distancia and vector[j - distancia] > val:
                vector[j] = vector[j - distancia]
                j -= distancia
            vector[j] = val
        distancia //= 2
    return vector

def quick_sort(vector):
    return vector

def merge_sort(vector):
    return vector