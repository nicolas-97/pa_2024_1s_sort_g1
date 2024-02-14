def shell_sort(vector):
    largo = 0
    for i in vector:
        largo += 1
    distancia = largo // 2

    while distancia > 0:
        for i in range(distancia, largo):
            val = vector[i]
            j = i
            while j >= distancia and vector[j - distancia] > val:
                vector[j] = vector[j - distancia]
                j -= distancia
            vector[j] = val
        distancia //= 2
    return vector


def quick_sort(vector, start = 0, end = None):
    if end is None:
        end = len(vector) - 1

    def quick(vector, start, end):
        if start >= end:
            return

        def particion(vector, start, end):
            pivot = vector[start]
            menor = start + 1
            mayor = end

            while True:
                while menor <= mayor and vector[mayor] >= pivot:
                    mayor = mayor - 1
                while menor <= mayor and vector[menor] <= pivot:
                    menor = menor + 1
                if menor <= mayor:
                    vector[menor], vector[mayor] = vector[mayor], vector[menor]
                else:
                    break

            vector[start], vector[mayor] = vector[mayor], vector[start]
            return mayor

        p = particion(vector, start, end)
        quick(vector, start, p-1)
        quick(vector, p+1, end)

    quick(vector, start, end)
    return vector

def merge_sort(vector):
    def merge(vector):

        def largo(vec):
                largovec = 0
                for _ in vec:
                    largovec += 1 
                return largovec
        if largo(vector) >1: 
            medio = largo(vector)//2 

            izq = vector[:medio]  
            der = vector[medio:]

            merge(izq) 
            merge(der) 

            i = j = k = 0

            while i < largo(izq) and j < largo(der): 
                if izq[i] < der[j]: 
                    vector[k] = izq[i] 
                    i+= 1
                else: 
                    vector[k] = der[j] 
                    j+= 1
                k += 1

            while i < largo(izq): 
                vector[k] = izq[i] 
                i+= 1
                k+= 1

            while j < largo(der): 
                vector[k] = der[j] 
                j+= 1
                k+= 1
    merge(vector)

    return vector

