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
    def quicksort(vector,menor,mayor):
        menor=0
        mayor=len(vector)-1
        if menor < mayor:
            valor = partition(vector, menor, mayor)
            quicksort(vector, menor, valor - 1)
            quicksort(vector, valor + 1, mayor)
    
    def partition(vector, menor, mayor):  
        pivot = vector[mayor]
        i = menor - 1
        for j in range(menor, mayor):
            if vector[j] <= pivot:
                i = i + 1
                (vector[i], vector[j]) = (vector[j], vector[i])
        (vector[i + 1], vector[mayor]) = (vector[mayor], vector[i + 1])
         
        return i+1    
    return vector




def merge_sort(vector):
    return vector


