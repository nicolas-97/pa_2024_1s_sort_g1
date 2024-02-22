def shell_sort(vector):
    n = len(vector)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = vector[i]
            j = i
            while j >= gap and vector[j - gap] > temp:
                vector[j] = vector[j - gap]
                j -= gap
            vector[j] = temp
        gap //= 2
    return vector

def quick_sort(vector):
    if len(vector) <= 1:
        return vector
    else:
        pivot = vector[0]
        less_than_pivot = [x for x in vector[1:] if x <= pivot]
        greater_than_pivot = [x for x in vector[1:] if x > pivot]
        return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)

def merge_sort(vector):
    if len(vector) <= 1:
        return vector
    
   
    middle = len(vector) // 2
    left_half = vector[:middle]
    right_half = vector[middle:]
    
    
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    
   
    return merge(left_half, right_half)

def merge(left, right):
    result = []
    i, j = 0, 0
    
   
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    while i < len(left):
        result.append(left[i])
        i += 1
    
    
    while j < len(right):
        result.append(right[j])
        j += 1
    
    return result
