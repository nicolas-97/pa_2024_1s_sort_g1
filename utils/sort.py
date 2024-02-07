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
    return vector

def merge_sort(vector):
    return vector
