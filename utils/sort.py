def shell_sort(vector):
    Longitud = len(vector)
    gap = Longitud // 2
    while gap > 0:
        j = gap
        while j < Longitud:
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
        Mid = len(vector) // 2
        Left = vector[:Mid]
        Right = vector[Mid:]
        merge_sort(Left)
        merge_sort(Right)
        i = j = k = 0
        while i < len(Left) and j < len(Right):
            if Left[i] <= Right[j]:
                vector[k] = Left[i]
                i += 1
            else:
                vector[k] = Right[j]
                j += 1
            k += 1
        while i < len(Left):
            vector[k] = Left[i]
            i += 1
            k += 1
        while j < len(Right):
            vector[k] = Right[j]
            j += 1
            k += 1
    return vector