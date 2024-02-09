def shell_sort(vector):
    n = len(vector)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = vector[i]
            j = i 
            while j >= gap and vector[j-gap] > temp:
                vector[j] = vector[j - gap]
                j-= gap
            vector[j] = temp
        gap //= 2
    return vector

def quick_sort(vector):
    if  len(vector) <= 1:
        return vector
    else:
        pivot = vector.pop()
    mayor = []
    menor = []
    for  i in vector:
        if i > pivot:
            mayor.append(i)
        else:
            menor.append(i)
        return quick_sort(menor)+ [pivot]+quick_sort(mayor)  

def merge_sort(vector):
    return vector

