def shell_sort(vector):
    Longitud= len(vector) // 2
    while Longitud > 0:
        for i in range(Longitud, len(vector)):
            valor = vector[i]
            j = i
            while j >= Longitud and vector[j - Longitud] > valor:
                vector[j] = vector[j - Longitud]
                j -= Longitud
                vector[j] = valor
                Longitud //= 2
    return vector
   
def quick_sort(vector):
    Longitud =len(vector)
    if Longitud<=1:
        return vector
    else :
        Pivote =vector[0]
        Pivote_izquierdo =[x for x in vector[1:] if x<Pivote]
        Pivote_derecho = [x for x in vector[1:] if x>=Pivote]

        return quick_sort(Pivote_izquierdo)+[Pivote]+quick_sort(Pivote_derecho)

def merge_sort(vector):
    if len(vector) > 1:
        Medio = len(vector) // 2
        Left = vector[:Medio]
        Right = vector[Medio:]

        merge_sort(Left)
        merge_sort(Right)

        i, j, k = 0, 0, 0

        while i < len(Left) and j < len(Right):
            if Left[i] < Right[j]:
                vector[k] = Left[i]
                i += 1
        else:
            vector[k] = Right[j]
            j += 1
            k += 1

            while i < len(Left):
                vector[k] = Left[i]
                i += 1
                k += 1

                while j < len(Right):
                    vector[k] = Right[j]
                    j += 1
                    k += 1

    return vector