def shell_sort(vector):
    n = len(vector)
    brecha = n // 2

    while brecha > 0:
        for i in range(brecha, n):
            temp = vector [i]
            j = i
            while j >= brecha and vector[j - brecha] > temp:
                vector [j] = vector[j - brecha]
                j -= brecha
            vector [j] = temp
        brecha //= 2

    return vector





def merge_sort(vector):
    
    return vector