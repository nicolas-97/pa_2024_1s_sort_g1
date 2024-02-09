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

def quick_sort(vector):
    if len(vector) <= 1:
        return vector
    else:
        pivot = vector[0]
        menos_que_pivot = [x for x in vector[1:] if x <= pivot]
        greater_than_pivot = [x for x in vector[1:] if x > pivot]
        return quick_sort(menos_que_pivot) + [pivot] + quick_sort(greater_than_pivot)





def merge_sort(vector):
    if len(vector) <= 1:
        return vector
    else:
        mitad = len(vector) // 2
        mitad_izq = merge_sort(vector[:mitad])
        mitad_der = merge_sort(vector[mitad:])
        sorted_vectoray = []
        while len(mitad_izq) > 0 and len(mitad_der) > 0:
            if mitad_izq[0] < mitad_der[0]:
                sorted_vectoray.append(mitad_izq[0])
                mitad_izq = mitad_izq[1:]
            else:
                sorted_vectoray.append(mitad_der[0])
                mitad_der = mitad_der[1:]
        sorted_vectoray.extend(mitad_izq)
        sorted_vectoray.extend(mitad_der)
        return sorted_vectoray
