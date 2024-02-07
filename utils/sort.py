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
    if len (vector)<=1:
        return vector
    
    else:
        pivote=vector[0]
        
        izq=[x for x in vector[1:] if x<pivote]
        der=[x for x in vector[1:] if x>=pivote]
        return quick_sort(izq)+[pivote]+quick_sort(der)

def merge_sort(vector):
    tam = len(vector) - 1

    for pactual in range(0, tam):
        posicion_menor = pactual
        nmenor = vector[posicion_menor]

        for busc in range(pactual, tam):
            e_enc = vector[busc + 1]

            if nmenor > e_enc:
                mnmenor = e_enc
                posicion_menor = busc + 1

        if posicion_menor != pactual:
            nmenor = vector[posicion_menor]
            vector[posicion_menor] = vector[pactual]
            vector[pactual] = nmenor

    return vector