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
    if len(vector)>1:
        mid=len(vector)//2
        s1=vector[:mid]
        s2=vector[mid:]
        merge_sort(s1)
        merge_sort(s2)
        a=0
        b=0
        c=0
    while a<len(s1) and b<len(s2):
        if s1[a]<s2[b]:
            vector[c]=s1[a]
            a+=1
        else:
            vector[c]=s2[b]
            b+=1
        c+=1
    while a<len(s1):
        vector[c]=s1[a]
        a+=1
        c+=1
    while b<len(s2):
        vector[c]=s2[b]
        b+=1
        c+=1
    return vector
    

 