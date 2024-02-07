def shell_sort(vector):
    size = len(vector)
    # Si el arreglo es impar usando (//) se puede hacer el inervalo entero para que se pueda manejar 
    intervalo = size // 2  

    while intervalo > 0 :
        print(f" __________Intervalo: {intervalo}__________")
        for i in range (intervalo, size):
            #print (f"Pasadas {i-1}") ## PREGUNTAR PQ
            # i esta iterando en funcion del intervalo
            insert_value = vector[i] #Toma el siguiente valor a ser insertado
            insert_index = i #Indice donde se inserta el valor

            print(f"comparación: {vector[insert_index - intervalo ]} > {insert_value}")
            while insert_index >= intervalo and [insert_index - intervalo ] > insert_value:
                #Se mueve al frente hasta encontrar un lugar adecuado o hasta el principio de la lista
                vector[insert_index] = vector[insert_index - intervalo]
                insert_index -= intervalo
            
            vector[insert_index] = insert_value #Insertamos el valor en su lugar correcto
        #Actualiza el intervalo
        intervalo //= 2
    return vector

def quick_sort(vector):
    return vector

def merge_sort(vector):
    size = len(vector)
    if size == 1:
        return [vector[0]]
    mitad = size //2
    izquierda = merge_sort(vector[:mitad])
    derecha = merge_sort(vector[mitad:])

    solve_izquierda = merge_sort(izquierda)
    solve_derecha = merge_sort(derecha)

    return Merge (solve_izquierda, solve_derecha)

def Merge(izquierda, derecha):
    final = [] #Lista abierta en donde se almacenara el arreglo organizado 
    while len(izquierda) > 0 and len(derecha) > 0: #Mientras haya elementos en ambos lados
        if izquierda[0] < derecha[0]: #Si el primer elemento
            final.append(izquierda.pop(0))
        else:
            final.append(derecha.pop(0))
        
        while  len(izquierda) != 0:
            final.append(izquierda.pop(0))

        while len(derecha) != 0:
            final.append(derecha.pop(0)) 
    return final       

