
def shell_sort(vector):
    size=len(vector)
    distancia=size//2
    temp=0
    while distancia>1:
        for i in range(distancia):
            temp=i
            while distancia+i<size:
                if vector[distancia+i]<vector[temp]:
                    vector[distancia+i], vector[temp] = vector[temp], vector[distancia+i]
                    temp=distancia+i
                i+=distancia
                
        distancia//=2
        
    for i in range(1, len(vector)):
        temp=i
        for j in range(1, i+1):
            if vector[i-j]>vector[temp]:
                vector[i-j], vector[temp] = vector[temp], vector[i-j]
                temp=i-j
    
    return vector


'''
def quick_sort(vector):
    size=len(vector)
    pivot=size-1
    point=-1

    if size==1:
        return vector
    else:
        for i in range(size):
            if vector[i]>=vector[pivot]:
                point+=1
                vector[i], vector[point] = vector[point], vector[i]
        return vector

'''






def merge_sort(vector, inicio=0, fin=0):
    if fin==0:
        fin=len(vector)
    mid=(inicio+fin)//2

    if fin-inicio==1 or len(vector)==0:
        return vector
        
    else:
        merge_sort(vector, inicio, mid)
        merge_sort(vector, mid, fin)

        aux=[]
        der=mid
        izq=inicio

        while len(aux)<fin-inicio:

            if izq>=mid:
                aux.append(vector[der])
                der+=1
            elif der>=fin:
                aux.append(vector[izq])
                izq+=1

            elif vector[izq]<vector[der]:
                aux.append(vector[izq])
                izq+=1
            else:
                aux.append(vector[der])
                der+=1
            
        for i in range(inicio, fin):
            vector[i]=aux[i-inicio]

        return vector
