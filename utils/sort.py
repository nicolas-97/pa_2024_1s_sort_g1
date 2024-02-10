def quick_sort(vector):
    if len(vector) <= 1:
        return vector
    pivot = vector[len(vector) // 2]
    menos = [x for x in vector if x < pivot]
    igual = [x for x in vector if x == pivot]
    mayor = [x for x in vector if x > pivot]
    return quick_sort(menos) + igual + quick_sort(mayor)


def shell_sort(vector):
    n = len(vector)
    vecdivision = n // 2

    while vecdivision > 0:
        for i in range(vecdivision, n):
            temp = vector[i]
            j = i
            while j >= vecdivision and vector[j - vecdivision] > temp:
                vector[j] = vector[j - vecdivision]
                j -= vecdivision
            vector[j] = temp
        vecdivision //= 2

    return vector

def merge_sort(vector):
    if len(vector) <= 1: 
        return vector

    def merge(izq, derecha):
        merged, izq_index, derecha_index = [], 0, 0
        while izq_index < len(izq) and derecha_index < len(derecha):
            if izq[izq_index] < derecha[derecha_index]:
                merged.append(izq[izq_index])
                izq_index += 1
            else:
                merged.append(derecha[derecha_index])
                derecha_index += 1
        merged.extend(izq[izq_index:])
        merged.extend(derecha[derecha_index:])
        return merged

    mid = len(vector) // 2
    return merge(merge_sort(vector[:mid]), merge_sort(vector[mid:]))