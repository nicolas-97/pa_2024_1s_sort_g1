def shell_sort(vector):
    long = len(vector)
    division = long // 2
    while division > 0:
        x = division
        while x < long:
            y = x - division
            while y >= 0:
                if vector[y + division] > vector[y]:
                    break
                else:
                    vector[y + division], vector[y] = vector[y], vector[y + division]
                y = y - division
            x += 1
        division = division // 2
    return vector

def quick_sort(vector):
    if len(vector) <= 1:
        return vector
    pivot = vector[len(vector) // 2]
    less = [i for i in vector if i < pivot]
    equal = [i for i in vector if i == pivot]
    high = [i for i in vector if i > pivot]
    return quick_sort(less) + equal + quick_sort(high)

def merge_sort(vector):
    if len(vector) > 1:
        mitad = len(vector) // 2
        mitad_izq, mitad_der = vector[:mitad], vector[mitad:]
        merge_sort(mitad_izq)
        merge_sort(mitad_der)
        i = j = k = 0
        while i < len(mitad_izq) and j < len(mitad_der):
            if mitad_izq[i] < mitad_der[j]:
                vector[k] = mitad_izq[i]
                i += 1
            else:
                vector[k] = mitad_der[j]
                j += 1
                
            k += 1
        while i < len(mitad_izq):
            vector[k] = mitad_izq[i]
            i += 1
            k += 1
        while j < len(mitad_der):
            vector[k] = mitad_der[j]
            j += 1
            k += 1
    return vector