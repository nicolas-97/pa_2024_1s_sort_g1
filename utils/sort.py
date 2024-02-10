def shell_sort(vector):
    
    size=len(vector)
    interval = size//2

    while interval > 0:

        for j in range(interval,size):
            
            insert_value=vector[j] 
            insert_index = j
    
            while insert_index >= interval and vector[insert_index-interval] > insert_value:

                vector[insert_index]=vector[insert_index-interval]
                insert_index -= interval

            vector[insert_index]=insert_value
        interval //=2
    
    return vector

def quick_sort(vector):

    return vector

def merge_sort(vector):

    size=len(vector)

    #Comprobamos si la lista contiene un solo elemento y lo retornamos
    if size == 1:
        return vector
    # En caso de que el vector tenga más de 1 elemento
    
    mitad = size//2 #Encontramos su medio
    vector_izq = vector[:mitad] #Almacenamos los datos izq del vector hasta su medio
    vector_der = vector[mitad:] #Almacenamos los datos der del vector desde su medio hasta el final

    #recursividad para volver a ordenar la sublistas
    vector_izq_ord = merge_sort(vector_izq) 
    vector_der_ord = merge_sort(vector_der)

    resultado = []

    while len(vector_izq_ord) > 0 and len(vector_der_ord) > 0: #Comprobamos que ambos vectores ordenados tengan una longitud mayor a 0 para poder compararlos
        #Si el primer dato del sub-arreglo ordenado izq es menor que el primer dato del sub-arreglo ordenado der entonces
        #agrega ese dato en la lista resultado y lo elimina de su sub-lista original
        if vector_izq_ord[0] < vector_der_ord[0]: 
            resultado = resultado + [vector_izq_ord[0]]
            vector_izq_ord = [i for i in vector_izq_ord if i != vector_izq_ord[0]]
        #caso contrario de lo anterior
        else:
            resultado = resultado + [vector_der_ord[0]]
            vector_der_ord = [i for i in vector_der_ord if i != vector_der_ord[0]]
    
    #evalua si la longitud es mayor a 0 para verificar si ese elemento fue el primero en agregarse antes y asi 
    #que el siguiente elemento del sub-arreglo derecho se inserte ya que queda como restante
    while len(vector_izq_ord) > 0:
        resultado = resultado + [vector_izq_ord[0]] #agregamos el dato 
        vector_izq_ord = [i for i in vector_izq_ord if i != vector_izq_ord[0]]
    
    while len(vector_der_ord) > 0:
        resultado = resultado + [vector_der_ord[0]]
        vector_der_ord = [i for i in vector_der_ord if i != vector_der_ord[0]]
    
    return resultado