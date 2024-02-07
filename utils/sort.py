def shell_sort(vector):
    size=len(vector)
    interval = size//2

    while interval > 0:

        for j in range(interval,size):
            
            actual=vector[j]
            index_actual = j
            
            compare_value = j-interval
            while index_actual >= interval and vector[compare_value] > actual:
                vector[j]=vector[compare_value]
                index_actual -= interval
            vector[compare_value]=actual
        interval //=2
    
    return vector

def quick_sort(vector):
    return vector

def merge_sort(vector):
    return vector