def shell_sort(vector):
    
    size=len(vector)
    interval = size//2

    while interval > 0:

        for j in range(interval,size):
            
            insert_value=vector[j] 
            insert_index = j
            

            while insert_index >= interval and vector[insert_index-interval] > insert_value:
                
                vector[insert_index]=vector[insert_index-interval]
                insert_index -= interval

            vector[insert_index]=insert_value
        interval //=2
    
    return vector

def quick_sort(vector):
    return vector

def merge_sort(vector):
    return vector