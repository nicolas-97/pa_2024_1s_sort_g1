def shell_sort(vector):
    n = len(vector)
    brecha = n // 2

    while brecha > 0:
        for i in range(brecha, n):
            temp = vector [i]
            j = i
            while j >= brecha and vector[j - brecha] > temp:
                vector [j] = vector[j - brecha]
                j -= brecha
            vector [j] = temp
        brecha //= 2

    return vector

import time

#

def quick_sort(vector):

    if len(vector) <= 1:
        return vector

    pivot = vector[len(vector) // 2]
    left = [x for x in vector if x < pivot]
    middle = [x for x in vector if x == pivot]
    right = [x for x in vector if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)

vector = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
sorted_vector = quick_sort(vector)
print(sorted_vector)


strat_time=time.time()
quick_sort(vector)
end_time=time.time()

def merge_sort(vector):
    if len(vector) <= 1:
        return vector

    izquierda = merge_sort(vector[:len(vector)//2])
    derecha = merge_sort(vector[len(vector)//2:])

    i=0 # L index
    j=0 # R index
    k=0 # index vector sorted

    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] < derecha[j]:
            vector[k] = izquierda[i]
            i += 1
        else:
            vector[k] = derecha[j]
            j += 1
        k += 1

    while i < len(izquierda):
        vector[k] = izquierda[i]
        i += 1
        k += 1

    while j < len(derecha):
        vector[k] = derecha[j]
        j += 1
        k += 1

    return vector