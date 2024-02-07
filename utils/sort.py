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
        Pivote_Izquierdo =[x for x in vector[1:] if x<Pivote]
        Pivote_Derecho = [x for x in vector[1:] if x>=Pivote]

        return quick_sort(Pivote_Izquierdo)+[Pivote]+quick_sort(Pivote_Derecho)

def merge_sort(vector):

    return vector