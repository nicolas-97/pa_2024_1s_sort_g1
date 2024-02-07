def shell_sort(vector):
    n=len(vector)
    salto = n//2
    while salto > 0:
        for i in range(salto,n):   
            temp = vector[i]
            j = i
            while j >= salto and vector[j - salto] > temp:
                vector[j] = vector[j - salto]
                j -= salto
            vector[j] = temp
        salto//=2

    return vector

def quick_sort(vector):
    return vector

def merge_sort(vector):
    return vector