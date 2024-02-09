def shell_sort(vector):
    longitud=len(vector)
    intervalo = longitud // 2
    while intervalo > 0:
        for i in range(intervalo, longitud):
            valor= vector[i]
            indice = i
            while indice >= intervalo and vector[indice - intervalo] > valor:
                vector[indice] = vector[indice - intervalo]
                indice -= intervalo
                vector[indice] = valor
                
        intervalo //= 2
    return vector

def quick_sort(vector):
    if len(vector) <=1:
        return vector
    pivot =vector[len(vector) //2]
    left =[x for x in vector if x < pivot]
    middle = [x for x in vector if x == pivot ]
    right = [x for x in vector  if x > pivot]
    return quick_sort(left) +middle +quick_sort(right)

def merge_sort(vector):

    if len(vector) > 1:
        derecho =vector[len(vector)//2:]
        izquierdo =vector[:len(vector)//2]
        
        merge_sort(izquierdo)
        merge_sort(derecho)

        i = 0
        j = 0
        m = 0

        while i < len(izquierdo) and j < len(derecho):
            if izquierdo[i] < derecho[j]:
                vector[m] =izquierdo[i]
                i +=1
            else:
                vector[m]=derecho[j]
                j +=1
            m+=1
        while i < len(izquierdo):
            vector[m]=izquierdo[i]
            i +=1
            m +=1
        
        while j < len(derecho):
            vector[m]= derecho[j]
            j +=1
            m +=1

    return vector
