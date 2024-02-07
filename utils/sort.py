import math
def shell_sort(vector):
    a = len(vector)
    dis = math.floor(a/2)
    def re_do():
        for i in range(dis):
            if vector[0]> vector[dis]:
                vector[0], vector[dis] = vector[dis], vector[0]
            if vector[dis]> vector[a-1]:
                vector[dis], vector[a-1] = vector[a-1], vector[dis]
    new_dis = math.floor(dis/2)
    re_do()
    if new_dis != 1:
        re_do()
        new_dis /= 2
        math.floor(new_dis)
    for i in range(1,a,1):
        for x in range(i,0,-1): 
            if vector[x]<vector[x-1]:
                vector[x-1], vector[x] = vector[x], vector[x-1]
                
    return vector

shell_sort([2,4,5,3,9,6])

def quick_sort(vector):
    pivot = 0
    a = len(vector)
    for i in range(a):
        for x in range(a-1,0,-1):
            if vector[pivot]>vector[i]:
                vector[pivot], vector[i]=vector[i], vector[pivot]
                pivot = i
            if pivot < x:
                if vector[pivot]<vector[x]:
                    vector[pivot], vector[x]=vector[x], vector[pivot]
    return vector
print(quick_sort([12,48,5,93,3,64,2]))
def merge_sort(vector):
    return vector