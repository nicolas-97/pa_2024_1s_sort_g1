def shell_sort(vector):
    tamaño=len(vector)//2
    while tamaño>0:
        for i in range (tamaño):
           tamañodos(vector,i,tamaño)

        tamaño=tamaño//2   
    return vector

def tamañodos(vector,iniciar,saltar):
    for j in range(iniciar+saltar,len(vector),saltar):
        numero=vector[j]
        posicion=j

        while posicion >= saltar and vector[posicion-saltar]>numero:
           vector[posicion]=vector[posicion-saltar]
           posicion=posicion-saltar
        vector[posicion]=numero

def gap(vector):
    pivot = vector[0]
    subarray = []
    subarray2 = []

    for i in range(1, len(vector)):
        if vector[i] < pivot:
            subarray.append(vector[i])
        else:
            subarray2.append(vector[i])

    return subarray, pivot, subarray2

def quick_sort(vector):
    if len(vector) < 2:
        return vector 
    else:
        subarray, pivot, subarray2 = gap(vector)
        return quick_sort(subarray) + [pivot] + quick_sort(subarray2)



def merge_sort(vector):
    if len(vector)>1:
        mitad=len(vector)//2
        primera=vector[:mitad]
        segunda=vector[mitad:]

        merge_sort(primera)
        merge_sort(segunda)
        i=0
        j=0
        k=0
        
        while i<len(primera)and j<len(segunda):
            if primera[i]<segunda[j]:
                vector[k]=primera[i]
                i+=1 
            else:
                vector[k]=segunda[j]
                j+=1
            k+=1

        while i <len(primera): 
            vector[k]=primera[i]
            i+=1
            k+=1

        while j<len(segunda):
            vector[k]=segunda[j]
            j+=1
            k+=1
    return vector
