
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
    length = len(vector)

    if length ==1:
       return vector 
    medio = length // 2 # divido el arreglo
    vector_izq = vector[:medio]
    vector_derecho = vector[medio:]

    sort1_izquierdo = merge_sort(vector_izq)#organiza el izquierdo
    sort2_derecho = merge_sort(vector_derecho)#organiza el derecho

    return merge(sort1_izquierdo, sort2_derecho) # combinar el arreglo ya ordenado 

    
def merge(izquierdo_v, derceho_v):
   lenght_derecho = len(derceho_v)
   lenght_izquierdo = len(derceho_v)
   vector_resultado = []
   while lenght_izquierdo > 0 and lenght_derecho > 0:
      if izquierdo_v[0]> derceho_v[0]:
         vector_resultado.append(derceho_v[0])
      else:
         vector_resultado.append(izquierdo_v[0])
         izquierdo_v.pop(0)

   while lenght_izquierdo > 0:
      vector_resultado.append(izquierdo_v[0])
      izquierdo_v.pop(0)

   while lenght_derecho > 0:
      vector_resultado.append(derceho_v[0])
      derceho_v.pop(0)




