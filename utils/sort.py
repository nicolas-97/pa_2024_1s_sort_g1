def shell_sort(vector):
    n = len(vector)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = vector[i]
            j = i - gap
            while j >= 0 and vector[j] > temp:
                vector[j] = vector[j - gap]
                j-= gap
            vector[j + gap] = temp
        gap //= 2
    return vector

def quick_sort(vector):
    return vector

def merge_sort(vector):
    return vector

