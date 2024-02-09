def shell_sort(vector):
    n=len(vector)
    salto = n//2
    while salto > 0:
<<<<<<< HEAD
        for i in range(salto,n):   
=======
        for i in range(salto,n):  
>>>>>>> ae3aa79022544a2f955382eb3eb00bda117b892b
            temp = vector[i]
            j = i
            while j >= salto and vector[j - salto] > temp:
                vector[j] = vector[j - salto]
                j -= salto
            vector[j] = temp
        salto//=2
<<<<<<< HEAD
=======

>>>>>>> ae3aa79022544a2f955382eb3eb00bda117b892b
    return vector

def quick_sort(vector):
    if len (vector)<=1:
        return vector
    else:
        pivote=vector[0]
<<<<<<< HEAD
    
    izq=[x for x in vector[1:] if x< pivote]
=======

    izq=[x for x in vector[1:] if x<pivote]
>>>>>>> ae3aa79022544a2f955382eb3eb00bda117b892b
    der=[x for x in vector[1:] if x>=pivote]
    return quick_sort(izq)+[pivote]+quick_sort(der)

def merge_sort(vector):
    if len(vector) > 1:
        med = len(vector) // 2
        izq = vector[:med]
        der = vector[med:]
        
        merge_sort(izq)
        merge_sort(der)
        
        i, j, k = 0, 0, 0
        while i < len(izq) and j < len(der):
            if izq[i] < der[j]:
                vector[k] = izq[i]
                i += 1
            else:
                vector[k] = der[j]
                j += 1
            k += 1
        
        while i < len(izq):
            vector[k] = izq[i]
            i += 1
            k += 1
        
        while j < len(der):
            vector[k] = der[j]
            j += 1
            k += 1
    
    return vector