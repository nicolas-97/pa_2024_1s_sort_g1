def shell_sort(lista):
    grupo = len(lista) // 2
    
    while grupo > 0:
        for i in range(grupo, len(lista)):
            temp = lista[i]
            j = i
            
            while j >= grupo and lista[j - grupo] > temp:
                lista[j] = lista[j - grupo]
                j -= grupo
            
            lista[j] = temp
        
        grupo //= 2
    
    return lista

def quick_sort(vector):
    if len(vector) <= 1:
        return vector
    pivot = vector[0]
    menor = [x for x in vector[1:] if x <= pivot]
    mayor = [x for x in vector[1:] if x > pivot]

    sorted_menor = quick_sort(menor)
    sorted_mayor = quick_sort(mayor)

    return sorted_menor + [pivot] + sorted_mayor

def merge_sort(vector):

    return vector


