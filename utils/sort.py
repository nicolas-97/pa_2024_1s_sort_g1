def shell_sort(vector):
    size = len(vector)
    subsize = size // 2
    
    while subsize > 0:
        for i in range(subsize, size):
            temp = vector[i]
            j = i
            while j >= subsize and vector[j - subsize] > temp:
                vector[j] = vector[j - subsize]
                j -= subsize
            vector[j] = temp
        subsize //= 2

    return vector

def quick_sort(vector):

    size = len(vector)
    prepiv = size // 2
    piv = vector[prepiv]
    i = 0
    j = 0
    z= size -1
    Condi1 = False  
    Condi2 = False 
    arreglo=[0,1]
    prepiv2=prepiv
    for i in range(1, prepiv2 + 1):
        while prepiv > i: 
            
            if vector[j] > piv:
                arreglo[0]=vector[j]
                Condi1 = True
                
            if vector[z] < piv:
                arreglo[1]=vector[-1]
                Condi2 = True
            if Condi1 and Condi2:
             vector[z], vector[j] = arreglo[0],arreglo[1]
            Condi1 = False  
            Condi2 = False 
            j += 1
            z -= 1
            i += 1
    prepiv2 -=1
    prepiv = prepiv//2
    return vector
       


def merge_sort(arr):
     if len(arr) > 1:
        mid = len(arr) // 2 
        left_half = arr[:mid]  
        right_half = arr[mid:]

        merge_sort(left_half) 
        merge_sort(right_half) 

        
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

       
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

     return vector
