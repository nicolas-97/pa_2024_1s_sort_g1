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
    if len(vector) <= 1:
        return vector
    pivot = vector[len(vector)//2]
    derecha = [x for x in vector if x < pivot]
    mitad = [x for x in vector if x == pivot]
    izquierda = [x for x in vector if x > pivot]
    return quick_sort(izquierda) + mitad + quick_sort(derecha)

def merge_sort(vector):
    return vector

