def shell_sort(vector):
    mitad = len(vector) // 2
    
    while mitad > 0:
        for i in range(mitad):
            opitimizar_busqueda(vector, i, mitad)
        mitad = mitad // 2
    return vector 

def opitimizar_busqueda (lista, inicio, salto):
    for i in range (inicio + salto, len(lista), salto):
        valor = lista [i]
        posicion = i

        while posicion >= salto and lista [posicion - salto] >valor:
            lista[posicion] = lista[posicion - salto]
            posicion = posicion - salto
        lista[posicion] = valor  

def quick_sort(vector):
    quick_sort_auxiliar(vector, 0, len(vector) - 1)
    return vector

def quick_sort_auxiliar(lista, inicio, fin):
    if inicio < fin:
        punto_particion = particionar(lista, inicio, fin)

        quick_sort_auxiliar(lista, inicio, punto_particion - 1)
        quick_sort_auxiliar(lista, punto_particion + 1, fin)

def particionar(lista, inicio, fin):
    pivote = lista[inicio]

    izquierda = inicio + 1
    derecha = fin
    terminado = False

    while not terminado:
        while izquierda <= derecha and lista[izquierda] <= pivote:
            izquierda += 1
        
        while lista[derecha] >= pivote and derecha >= izquierda:
            derecha -= 1
        
        if derecha < izquierda:
            terminado = True
        else:
            lista[izquierda], lista[derecha] = lista[derecha], lista[izquierda]
    
    lista[inicio], lista[derecha] = lista[derecha], lista[inicio]

    return derecha


def merge_sort(vector):
    if len(vector) > 1:
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
    return vector
