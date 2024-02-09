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
    return vector

def merge_sort(vector):
    return vector

