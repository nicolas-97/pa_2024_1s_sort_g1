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
   def quicksort(vector,left,right):
        partition_pos=partition(vector,left,right)
        quicksort(vector,left,partition_pos -1)
        quicksort(vector,partition_pos+1, right)
   
def partition(vector,left,right):  
    i=left
    j=right+1
    pivot= vector[right]
    while i<j:
        while i < right and vector[i] <pivot:
            i+=1
        while j > left and vector[j] >=pivot:
            j-=1
        if i<j:
            vector[i], vector[j] = vector[j], vector[i]    
    if vector[i] > pivot:
        vector[i], vector[right] = vector[right], vector[i]
    return vector

def merge_sort(vector):
    return vector

print('dejame hcer algoooo')
