def shell_sort(vector):
    size = len(vector)
    distance = size//2
    while distance > 0:
        for i in range(size):
            for j in range(i,0,-1):
                if(vector[j] < vector[j-1]):
                    min = vector[j]
                    vector[j] = vector[j-1]
                    vector[j-1] = min
        distance = distance//2
    return vector

def quick_sort(vector):
    size = len(vector)
    left = []
    right = []
    if size <= 1:
        return vector
    for i in vector[1:]:
        pivot = vector[0]
        if i <= pivot:
            left.append(i)
        elif i > pivot:
            right.append(i)
    return quick_sort(left) + [pivot] + quick_sort(right)

def merge_sort(vector):
    size = len(vector)
    if size < 2:
        return vector
    half = size//2
    left = merge_sort(vector[:half])
    right = merge_sort(vector[half:])
    merged_vertor = []
    i, j = 0, 0
    while (len(merged_vertor) < len(left) + len(right)):
        if left[i] < right[j]:
            merged_vertor.append(left[i])
            i+=1
        else:
            merged_vertor.append(right[j])
            j+=1
        if i == len(left) or j == len(right):
            merged_vertor.extend(left[i:] or right[j:])
            break
    return merged_vertor