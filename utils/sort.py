def shell_sort(vector):
    size = len(vector)
    cociente=size//2

    while cociente>0:

        i=0
        while i<cociente:
            
            for j in range(cociente+i,size,cociente):
                posicion_actual=j
                valor_actual=vector[posicion_actual]
                while (posicion_actual>0) and (vector[posicion_actual-cociente]>valor_actual):
                    vector[posicion_actual]=vector[posicion_actual-cociente]
                    posicion_actual-=cociente
                vector[posicion_actual]=valor_actual
            i+=1
        
        cociente=cociente//2
        
    return vector

def quick_sort(vector):
    size=len(vector)

    if size<=1:
        return vector

    pivot=vector[0]
    menores=[]
    mayores=[]

    for i in range(1,size):
        if vector[i] < pivot:
            menores.append(vector[i])
        else:
            mayores.append(vector[i])

    return quick_sort(menores)+[pivot]+quick_sort(mayores)



def merge_sort(vector):
    size = len(vector)

    if size<=1:
        return vector
    
    mitad=size//2

    izquierda=merge_sort(vector[:mitad])
    derecha=merge_sort(vector[mitad:])

    return unir_merge(izquierda,derecha)

def unir_merge(izquierda,derecha):
    lista_a=[]

    while (len(izquierda)>0) and (len(derecha)>0):
    

        if izquierda[0]>derecha[0]:
            lista_a.append(derecha[0])
            derecha.pop(0)
        
        else:
            lista_a.append(izquierda[0])
            izquierda.pop(0)

    while (len(izquierda)>0) or (len(derecha)>0):

        if len(izquierda)==0:
            lista_a.append(derecha[0])
            derecha.pop(0)
        else:
            lista_a.append(izquierda[0])
            izquierda.pop(0)
    
    return lista_a


#lista=[1,2,3,4,5]
#lista=[5,4,3,2,1]
#lista=[3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
#print(quick_sort(lista))

#print(lista)