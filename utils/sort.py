def shell_sort(vector):
    n = len(vector)
    salto = n // 2
    while salto > 0:
        j = salto
        while j < n:
            i = j - salto
            while i >= 0:
                if vector[i + salto] > vector [i]:
                    break
                else:
                    vector[i + salto], vector[i] = vector[i], vector[i + salto]
                i = i - salto
            j += 1
        salto = salto//2
    return vector

def quick_sort(vector):
    if len(vector) <= 1:
        return vector
    pivote = vector[len(vector) // 2]
    left = [x for x in vector if x < pivote]
    middle = [x for x in vector if x == pivote]
    right = [x for x in vector if x > pivote]
    return quick_sort(left) + middle + quick_sort(right)

def merge_sort(vector):
    if len(vector) > 1:
        mitad = len(vector) // 2
        IZQ = vector[:mitad]
        DER = vector[mitad:]
        merge_sort(IZQ)
        merge_sort(DER)
        i = j = k = 0
        while i < len(IZQ) and j < len(DER):
            if IZQ[i] <= DER[j]:
                vector[k] = IZQ[i]
                i += 1
            else:
                vector[k] = DER[j]
                j += 1
            k += 1
        while i < len(IZQ):
            vector[k] = IZQ[i]
            i += 1
            k += 1
        while j < len(DER):
            vector[k] = DER[j]
            j += 1
            k += 1
    return vector