def shell_sort(vector):
    arreglo_size = len(vector)
    brecha = arreglo_size // 2
    while brecha > 0:
        for recorrido in range(brecha, arreglo_size):
            buffer = vector[recorrido]
            indice = recorrido
            while indice >= brecha and vector[indice - brecha] > buffer:
                vector[indice] = vector[indice - brecha]
                indice -= brecha
            vector[indice] = buffer
        brecha = brecha // 2  

    return vector 

def quick_sort(vector):
    if len(vector) <= 1:
        return vector
    else:
        pivot = vector[0]
        menos_que_pivot = [x for x in vector[1:] if x <= pivot]
        greater_than_pivot = [x for x in vector[1:] if x > pivot]
        return quick_sort(menos_que_pivot) + [pivot] + quick_sort(greater_than_pivot)





def merge_sort(vector,arrder,arrizq,arr_resultado):
    vector =[]
    while len(arrizq)>0 and len(arrder)>0:
        if arrizq[0] > arrder[0]:
            arr_resultado.append(arrder[0])
            arrder.pop(0)
        else:
            arr_resultado.append(arrizq[0])
            arrizq.pop(0)
    while len(arrizq)>0:
        arr_resultado.append(arrder[0])
        arrizq.pop(0)
    while len(arrder)>0:
        arr_resultado.append(arrizq[0])
        arrder.pop(0)

    return vector









