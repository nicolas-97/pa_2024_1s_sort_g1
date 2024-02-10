def shell_sort(vector):
    lenght= len(vector)
    interval= lenght//2
    while interval > 0:
        for i in range(interval, lenght):
            insert_value = vector[i]
            insert_index=i
            while insert_index >= interval and vector[insert_index - interval]>insert_value:
                vector[insert_index]=vector[insert_index-interval]
                insert_index -= interval    
            vector[insert_index]= insert_value
        interval//=2
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
    if len(vector) <= 1:
        return vector
   
    list_1 = vector[0:len(vector) // 2]
    list_2 = vector[len(vector) // 2:]
    
    ans_1 = merge_sort(list_1)
    ans_2 = merge_sort(list_2)
    
    sort_list = sort_two_list(ans_1, ans_2)
    return sort_list

def sort_two_list(list_1, list_2):
    final_list = []
    i = 0
    j = 0
    while i < len(list_1) and j < len(list_2):
        if list_1[i] <= list_2[j]:
            final_list.append(list_1[i])
            i += 1
            continue
        final_list.append(list_2[j])
        j += 1

    while i < len(list_1):
        final_list.append(list_1[i])
        i = i + 1
        
    while j < len(list_2):
        final_list.append(list_2[j])
        j = j + 1
        
    return final_list
  
    
    