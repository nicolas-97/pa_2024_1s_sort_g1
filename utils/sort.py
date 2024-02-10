def shell_sort(vector):
    distancia=len(vector)//2
    while distancia>0:
        for i in range(distancia,len(vector)):
            aux=vector[i]
            j=i
            while j>=distancia and vector[j-distancia]>aux:
                vector[j]=vector[j-distancia]
                j-=distancia
            vector[j]=aux  
        distancia=distancia//2

    return vector

def quick_sort(vector):
    if len(vector)<=1:
        return vector
    else:
        pivote=vector[0]
        menor=[]
        mayor=[]
        for i in vector[1:]:
            if i<pivote:
                menor.append(i)
            else:
                mayor.append(i)
        vector= quick_sort(menor)+[pivote]+quick_sort(mayor)
    return vector

def merge_sort(vector):
    if len(vector)<=1:
        return vector
    else:
        mitad=len(vector)//2
        izq=merge_sort(vector[:mitad])
        der=merge_sort(vector[mitad:])
        i=0;j=0
        vector_ordenado=[]
        while i<len(izq) and j<len(der):
            if izq[i]<der[j]:
                vector_ordenado.append(izq[i])
                i+=1
            else:
                vector_ordenado.append(der[j])
                j+=1
        while i<len(izq):
            vector_ordenado.append(izq[i])
            i+=1
        while j<len(der):
            vector_ordenado.append(der[j])
            j+=1
        vector=vector_ordenado
    return vector



