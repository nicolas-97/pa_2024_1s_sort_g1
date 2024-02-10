def shell_sort(vector):
    n = len(vector)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = vector[i]
            j = i 
            while j >= gap and vector[j-gap] > temp:
                vector[j] = vector[j - gap]
                j-= gap
            vector[j] = temp
        gap //= 2
    return vector

def quick_sort(vector):
    if  len(vector) <= 1:
        return vector
    pivot, *rest = vector
    pequeño = [x for x in rest if x < pivot]
    grande = [x for x in rest if x >= pivot]
    return quick_sort(pequeño) + [pivot] + quick_sort(grande)

def merge_sort(vector):
    if len(vector) <= 1:
        return vector
    mid = len(vector) // 2
    izquierda = merge_sort(vector[:mid])
    derecha = merge_sort(vector[mid:])
    return merge(izquierda, derecha)

def merge(izquierda, derecha):
    resultado = []
    izq, der = 0, 0

    while izq < len(izquierda) and der < len(derecha):
        if izquierda[izq] < derecha[der]:
            resultado.append(izquierda[izq])
            izq += 1
        else:
            resultado.append(derecha[der])
            der += 1

    resultado.extend(izquierda[izq:])
    resultado.extend(derecha[der:])
    return resultado
