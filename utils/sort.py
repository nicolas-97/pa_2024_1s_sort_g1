
def shell_sort(vector):
    lenght = len(vector)
    interval = lenght // 2 # con la doble diagonal se convierte a la parte entera 

    while interval > 0:

     for i in range(interval, lenght):

        insert_value = vector[i]
        insert_index = i
       
        while insert_index >= interval and vector[insert_index - interval] > insert_value:
            vector[insert_index] = vector[insert_index-interval]
            insert_index = insert_index - interval

        vector[insert_index] = insert_value
        
     interval //= 2
    
    return vector

def quick_sort(vector):
    if len(vector) <= 1:
         return vector
    pivot = vector[len(vector) // 2]

    left = [x for x in vector if x < pivot]

    middle = [x for x in vector if x == pivot] #funciona igual
    
    right = [x for x in vector if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def merge_sort(vector):
    if len(vector) <= 1:
        return vector

    def merge(left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    middle = len(vector) // 2
    left = merge_sort(vector[:middle])
    right = merge_sort(vector[middle:])
    return merge(left, right)




