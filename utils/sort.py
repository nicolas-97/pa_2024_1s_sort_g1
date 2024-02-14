def shell_sort(vector):
    n = len(vector)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = vector[i]
            j = i
            while j >= gap and vector[j - gap] > temp:
                vector[j] = vector[j - gap]
                j -= gap
            vector[j] = temp
        gap //= 2
    return vector

def quick_sort(vector):
    if  len(vector) <= 1:
        return vector
    pivote, *rest = vector
    small = [x for x in rest if x < pivote]
    big = [x for x in rest if x >= pivote]
    return quick_sort(small) + [pivote] + quick_sort(big)

def merge_sort(vector):
    if len(vector)>1:
        mitad = len(vector)//2
        mitadIzquierda = vector[:mitad]
        mitadDerecha = vector[mitad:]
        merge_sort(mitadIzquierda)
        merge_sort(mitadDerecha)
        i=0
        j=0
        k=0
        while i < len(mitadIzquierda) and j < len(mitadDerecha):
            if mitadIzquierda[i] < mitadDerecha[j]:
                vector[k]=mitadIzquierda[i]
                i=i+1
            else:
                vector[k]=mitadDerecha[j]
                j=j+1
            k=k+1
        while i < len(mitadIzquierda):
            vector[k]=mitadIzquierda[i]
            i=i+1
            k=k+1
        while j < len(mitadDerecha):
            vector[k]=mitadDerecha[j]
            j=j+1
            k=k+1
    return vector