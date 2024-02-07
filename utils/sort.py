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

    return vector

def merge_sort(vector):
    return vector