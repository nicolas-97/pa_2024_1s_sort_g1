def shell_sort(vector):
    n=len(vector)
    intervalo=n//2
    while intervalo>0:
        j=intervalo
        while j<n:
            m=j-intervalo
            while m>=0:
                if vector[m+intervalo]>vector[m]:
                    break
                else:
                    vector[m+intervalo],vector[m]=vector[m],vector[m+intervalo]
                m=m-intervalo
            j+=1
        intervalo=intervalo//2        
    return vector

def quick_sort(vector):
    if len(vector)<=1:
        return vector
    intervalo_1=vector[len(vector)//2]
    iz=[x for x in vector if x<intervalo_1]
    mi=[x for x in vector if x==intervalo_1]
    de=[x for x in vector if x>intervalo_1]
    return quick_sort(iz)+mi+quick_sort(de)
    
    

def merge_sort(vector):
    if len(vector<=1):
        return vector
    if len(vector)>1:
        mid=len(vector)//2
        s1=vector[:mid]
        s2=vector[mid:]
    s1=merge_sort(s1)
    s2=merge_sort(s2)
    return merge(s1,s2)
def merge(left,right):
    merged=[]
    left_1=0
    right_1=0
    while left_1<len(left) and right_1<len(right):
        if left[left_1]<right[right_1]:
            merged.append(left[left_1])
            left_1+=1
        else:
            merged.append(right[right_1])
            right_1+=1
    merged+=left[left_1:]
    merged+=right[right_1:] 
    return merged   


