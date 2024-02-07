def shell_sort(vector):
    return vector

def quick_sort(vector):
    return vector

def merge_sort(vector):
    size = len(vector)
    if size == 1:
        return [vector[0]]
    mitad = size //2
    izquierda = merge_sort(vector[:mitad])
    derecha = merge_sort(vector[mitad:])

    solve_izquierda = merge_sort(izquierda)
    solve_derecha = merge_sort(derecha)

    return Merge (solve_izquierda, solve_derecha)

def Merge(izquierda, derecha):
    final = [] #Lista abierta en donde se almacenara el arreglo organizado 
    while len(izquierda) > 0 and len(derecha) > 0: #Mientras haya elementos en ambos lados
        if izquierda[0] < derecha[0]: #Si el primer elemento
            final.append(izquierda.pop(0))
        else:
            final.append(derecha.pop(0))
        
        while  len(izquierda) != 0:
            final.append(izquierda.pop(0))

        while len(derecha) != 0:
            final.append(derecha.pop(0)) 
    return final       

