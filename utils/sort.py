def shell_sort(vector):
    x = len(vector)
    y = x // 2
    while y > 0:
       a = y
       while a < x:
          b = a - y
          while b >= 0:
            if vector[b + y] > vector [b]:
                break
            else:
                vector[b + y], vector[b] = vector[b], vector[b + y]
                b= b-y
            a += 1
    y = y //2
    return vector 

def quick_sort(vector):

     return vector
   

def merge_sort(vector):
    return vector