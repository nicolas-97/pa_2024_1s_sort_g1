def shell_sort(vector):
    gap = len(vector) // 2 

    while gap > 0: 
        for i in range(gap, len(vector)): 
            temp = vector[i] 

            j = i 

            while j >= gap and vector[j - gap] > temp: 

                vector[j] = vector[j - gap] 

                j -= gap 

            vector[j] = temp 


        gap //= 2 

    return vector

def quick_sort(vector):
    return vector
    if len (vector)<=1:
        return vector

    else:
        pivote=vector[0]

        izq=[x for x in vector[1:] if x<pivote]
        der=[x for x in vector[1:] if x>=pivote]
        return quick_sort(izq)+[pivote]+quick_sort(der)

def merge_sort(vector):
    if len(vector) > 1:
        mid = len(vector) // 2
        izq = vector[:mid]
        der = vector[mid:]

        merge_sort(izq)
        merge_sort(der)

        i, j, k = 0, 0, 0

        while i < len(izq) and j < len(der):
            if izq[i] < der[j]:
                vector[k] = izq[i]
                i += 1
            else:
                vector[k] = der[j]
                j += 1
            k += 1

        while i < len(izq):
            vector[k] = izq[i]
            i += 1
            k += 1

        while j < len(der):
            vector[k] = der[j]
            j += 1
            k += 1

    return vector