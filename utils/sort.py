def shell_sort(vector):
    x = len(vector)
    y = x // 2
    while y > 0:
        for a in range(y, x):
            z = vector[a]
            b = a
            while b >= y & vector[b - y] >= z:
                vector[b] = vector[b - y]
                b - y
            vector[b] = z
        y //= 2
    return vector 

def quick_sort(vector):
    return vector

def merge_sort(vector):
    return vector