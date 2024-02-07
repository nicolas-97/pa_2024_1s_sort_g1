def shell_sort(vector):
    size = len(vector)
    distance = size//2
    while distance > 0:
       for i in range(size):
        for j in range(i,0,-1):
            if(vector[j] < vector[j-1]):
                minimum = vector[j]
                vector[j]= vector[j-1]
                vector[j-1]= minimum
        distance = distance//2
    return vector  

def quick_sort(vector):
    size = len(vector)
    pivot = vector[0]
    for i in range(size):
        for j in range(pivot, size-1):
            if pivot > vector[j]:
                vector[j] = pivot
            else:
                 vector[0] = vector[j]
            
            
def quick_sort(vector):
    if len(vector) <= 1:
        return vector
    else:
        left, right = [],[]
        pivot = vector[0]
        for n in vector[1:]:
            if n < pivot:
                left.append(n)
            else:
                right.append(n)
        sub_v_left = quick_sort(left) 
        sub_v_right = quick_sort(right)
        return sub_v_left + [pivot] + sub_v_right
 
def merge_sort(vector):
    size = len(vector)
    if size < 2:
        return vector
    half = size//2
    left = merge_sort(vector[:half])
    right = merge_sort(vector[half:])
    merged_vector = []
    i, j = 0, 0
    while (len(merged_vector) < len(left) + len(right)):
        if left[i] < right[j]:
            merged_vector.append(left[i])
            i+= 1
        else:
            merged_vector.append(right[j])
            j+= 1
        if i == len(left) or j == len(right):
            merged_vector.extend(left[i:] or right[j:])
            break
    return merged_vector