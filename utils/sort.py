
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



def quick_sort(vector):
    return vector

def merge_sort(vector):
    return vector
