def shell_sort(vector):
    n = len(vector)
    gap = n // 2
    while gap > 0:
        j = gap
        while j < n:
            i = j - gap
            while i >= 0:
                if vector[i + gap] > vector [i]:
                    break
                else:
                    vector[i + gap], vector[i] = vector[i], vector[i + gap]
                i = i - gap
            j += 1
        gap = gap//2
    return vector

def quick_sort(vector):
    if len(vector) <= 1:
        return vector
    pivot = vector[len(vector) // 2]
    left = [x for x in vector if x < pivot]
    middle = [x for x in vector if x == pivot]
    right = [x for x in vector if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def merge_sort(vector):
    if len(vector) > 1:
        mid = len(vector) // 2
        L = vector[:mid]
        R = vector[mid:]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                vector[k] = L[i]
                i += 1
            else:
                vector[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            vector[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            vector[k] = R[j]
            j += 1
            k += 1
    return vector