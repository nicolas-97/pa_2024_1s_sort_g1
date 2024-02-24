def shell_sort(vector):
    size = len(vector)
    gap = size // 2

    while gap > 0:
        for i in range(gap, size):
            temp = vector[i]
            j = i

            while j >= gap and vector[j - gap] > temp:
                vector[j] = vector[j - gap]
                j -= gap

            vector[j] = temp

        gap //= 2

    return vector


def quick_sort(vector):
        if len(vector) <= 1 :
            return vector
        
        pivot = len(vector) // 2 
        equal = [x for x in vector if x == vector[pivot]]
        left = [x for x in vector if x < vector [pivot]]
        right = [x for x in vector if x > vector[pivot]]

        return quick_sort(left) + equal  +quick_sort(right)
     
     

def merge_sort(vector):    
    if len(vector) == 1:
        return vector
    else:
        mid = len(vector) // 2
        left = vector[:mid]
        right = vector[mid:]
        
        left_sorted = merge_sort(left)
        right_sorted = merge_sort(right)
        
        return merge_sort2(left_sorted, right_sorted)

def merge_sort2(left, right):
    vector_arreglado = []
    while len(left) > 0 and len(right) > 0:
        if left[0] > right[0]:
            vector_arreglado.append(right[0])
            right.pop(0)
        else:
            vector_arreglado.append(left[0])
            left.pop(0)
                     
    while len(left) > 0:
        vector_arreglado.append(left[0])
        left.pop(0)
        
    while len(right) > 0:
        vector_arreglado.append(right[0])
        right.pop(0)
    
    return vector_arreglado
