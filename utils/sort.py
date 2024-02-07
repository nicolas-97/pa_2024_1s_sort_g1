def shell_sort(vector):
    length = len(vector)
    interval = length // 2

    while interval > 0:
        # insert sort
        for i in range(interval, length):
            insert_value = vector[i] # Toma elsig. valor a ser insertado
            insert_index = i # Índice donde insertará el insert_value

            while insert_index >= interval and vector[insert_index - interval] > insert_value:
                vector[insert_index] = vector[insert_index - interval]
                insert_index -= interval


                # Insertamios el valor en su índice correspondiente:
                vector[insert_index] = insert_value

        # Actualizar interval:       
        interval //=2

    return vector

def particionado(lista):
    pivote = lista[0]
    menores = []
    mayores = []

    for i in range(1, len(lista)):
        if lista[i] < pivote:
            menores.append(lista[i])
        else:
            mayores.append(lista[i])

    return menores, pivote, mayores

def quick_sort(lista):
    if len(lista) < 2:
        return lista  # Cuando la lista es vacía o tiene un solo elemento, ya está ordenada
    else:
        menores, pivote, mayores = particionado(lista)
        return quick_sort(menores) + [pivote] + quick_sort(mayores)

def merge_sort(vector): 
    if len(vector) > 1 :
        mitad = len(vector) // 2
        primera_mitad = vector[:mitad]
        segunda_mitad = vector[mitad:]

        merge_sort(primera_mitad)
        merge_sort(segunda_mitad)
        i = 0
        j = 0
        k = 0

        while i < len(primera_mitad) and j < len(segunda_mitad):
            if primera_mitad[i] < segunda_mitad[j]:
                vector[k] = primera_mitad[i]
                i += 1
            else:
                vector[k] = segunda_mitad[j]
                j += 1
            k += 1

        while i < len(primera_mitad):
            vector[k] = primera_mitad[i]
            i += 1
            k += 1

        while j < len(segunda_mitad):
            vector[k] = segunda_mitad[j]
            j += 1
            k += 1
        return(vector)


