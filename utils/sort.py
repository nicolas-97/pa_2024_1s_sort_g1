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
        menor = [x for x in vector[1:] if x <= pivot]
        mayor = [x for x in vector[1:] if x > pivot]
    return quick_sort(menor) + [pivot] + quick_sort(mayor)
    

def merge_sort(vector):
    if len(vector) > 1:
        mid = len(vector) // 2
        left_half = vector[:mid]
        right_half = vector[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                vector[k] = left_half[i]
                i += 1
            else:
                vector[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            vector[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            vector[k] = right_half[j]
            j += 1
            k += 1
    return vector