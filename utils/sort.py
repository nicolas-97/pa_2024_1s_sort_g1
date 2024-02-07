def shell_sort(vector):
    return vector

def quick_sort(l):
    piv=l[0]
    right=[]
    left=[]
    newr=[]
    if len(l)==1:
        return l
    
    for i in range(1,len(l)):
        if (l[i] < piv):
            left.append(l[i])
        elif (l[i]>piv):
            right.append(l[i])
    left.append(piv)
    if(len(right)>0):
        newr=quick_sort(right)
    
    if(len(left)>0):
        newl=quick_sort(left)

    return orden(newl,newr)
    
    

def merge_sort(vector):
    if len(vector)==1:
        return vector

    mitad=len(vector)//2
    left=vector[:mitad]
    right=vector[mitad:]
    
    newl=merge_sort(left)
    newr=merge_sort(right)

    return orden(newl,newr)
    


def orden(newl,newr):
    resultado=[]
    while(len(newr)!=0 and len(newl)!=0):
        if(newl[0]>newr[0]):
            resultado.append(newr[0])
            newr.pop(0)
        elif(newl[0]<newr[0]):
            resultado.append(newl[0])  
            newl.pop(0)
    while(len(newl)>0):
        resultado.append(newl[0])
        newl.pop(0)
    while(len(newr)>0):
        resultado.append(newr[0])
        newr.pop(0)
    return resultado
