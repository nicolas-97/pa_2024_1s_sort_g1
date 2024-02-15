def shell_sort(my_lista):
    num=len(my_lista)//2
    my_copia=my_lista
    while(num!=0):
        num_sub=1
        while(num_sub<=num):
            subl=[]
            obj=num_sub-1
            while(obj<len(my_lista)):
                subl.append(my_lista[obj])
                obj+=num
            insercion(subl)
            #print(subl)

            obj1=num_sub-1
            i=0
            while(obj1<len(my_lista)):     
                my_copia[obj1]=subl[i]
                obj1+=num
                i+=1
            
            num_sub+=1
        
        num=num//2
    return my_lista

def quick_sort(l):
    if(len(l)==0):
        return l
    piv=l[0]
    right=[]
    left=[]
    newr=[]
    rep=[]
    if len(l)==1:
        return l
 
    for i in range(1,len(l)):
        if (l[i] < piv):
            left.append(l[i])
        elif (l[i]>piv):
            right.append(l[i])
        elif (l[i]==piv):
            rep.append(l[i])
        
    left.append(piv)
    if(len(right)>0):
        newr=quick_sort(right)

    if(len(left)>0):
        newl=quick_sort(left)
    newl+=rep
    return orden(newl,newr)

def merge_sort(vector):
    if len(vector) > 1:
        mid = len(vector) // 2
        izquierda = vector[:mid]
        derecha= vector[mid:]

        merge_sort(izquierda)
        merge_sort(derecha)
        j=0
        i=0
        k=0
        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                vector[k] = izquierda[i]
                i += 1
            else:
                vector[k] = derecha[j]
                j += 1
            k += 1

        while i < len(izquierda):
            vector[k] = izquierda[i]
            i += 1
            k += 1

        while j < len(derecha):
            vector[k] = derecha[j]
            j += 1
            k += 1
    return vector

def orden(newl,newr):
    resultado=[]
    while(len(newr)!=0 and len(newl)!=0):
        if(newl[0]>newr[0]):
            resultado.append(newr[0])
            newr.remove(newr[0])
        elif(newl[0]<newr[0]):
            resultado.append(newl[0]) 
            newl.remove(newl[0])
    while(len(newl)>0):
        resultado.append(newl[0])
        newl.remove(newl[0])
    while(len(newr)>0):
        resultado.append(newr[0])
        newr.remove(newr[0])
    return resultado

def insercion(arr):
    for i in range(1, len(arr)):
        key = arr[i]  
        j = i - 1  

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

        