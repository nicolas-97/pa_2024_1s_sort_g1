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
    pivot, *rest = vector
    pequeño = [x for x in rest if x < pivot]
    grande = [x for x in rest if x >= pivot]
    return quick_sort(pequeño) + [pivot] + quick_sort(grande)

def merge_sort(vector):
    return vector

