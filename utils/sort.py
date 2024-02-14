""" lista = [64, 25, 12, 22, 11]
merge_sort(lista)
print("merge_sort:", lista) """


def shell_sort(vector):
    tamano = 0
    for i in vector:
        tamano += 1
    final = tamano // 2
    
    while final > 0:
        for i in range(final, tamano):
            val = vector[i]
            j = i
            while j >= final and vector[j - final] > val:
                vector[j] = vector[j - final]
                j -= final
            vector[j] = val
        final //= 2
    return vector

lista = [64, 25, 12, 22, 11]
shell_sort(lista)
print("shell_sort:", lista)

"""SEGUNDO"""

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

"""lista = [64, 25, 12, 74, 11]
lista = quick_sort(lista)
print("quick_sort:", lista) """

""""TERCERO"""

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
""" lista = [64, 25, 12, 22, 11]
merge_sort(lista)
print("merge_sort:", lista) """