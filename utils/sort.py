
def shell_sort(vector):
    size=len(vector)
    distancia=size//2
    temp=0

    while True:
        for i in range(distancia):
            temp=i
            while distancia+i<size:
                if vector[distancia+i]<vector[temp]:
                    vector[distancia+i], vector[temp] = vector[temp], vector[distancia+i]
                    temp=distancia+i
                i+=distancia
                
        if distancia==1:
            break
        distancia//=2
        
    return vector



def quick_sort(vector):
    return vector

def merge_sort(vector):
    return vector
