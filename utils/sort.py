
def shell_sort(vector):
    x=len(vector)//2
    while x>0:
        for i in range(x,len(vector)):
            abc=vector[i]
            y=i
            while y>=x and vector[y-x]>abc:
                vector[y]=vector[y-x]
                y-=x
            vector[y]=abc
        x//=2
    return vector

def quick_sort(vector):
    if len(vector)<=1:
        return(vector)

    y=vector[len(vector)//2]
    izq=[x for x in vector if x<y]
    mid= [x for x in vector if x ==y]
    der=[x for x in vector if x>y]
    resultado=(quick_sort(izq)+mid+quick_sort(der))
    vector=resultado
    return vector

def merge_sort(vector):
    if len(vector)<=1:
        return vector
    mid= len(vector)//2
    izq= vector[:mid]
    der=vector[mid:]
    izq = merge_sort(izq)
    der= merge_sort(der)
    return merge(izq,der)

def merge(izq,der):
    vector=[]
    i=y=0
    while i < len(izq)and y < len(der):
        if izq[i]<der[y]:
            vector.append(izq[i])
            i+=1
        else:
            vector.append(der[y])
            y+=1
    vector+= izq[i:]
    vector+= der[y:]
        
    return vector