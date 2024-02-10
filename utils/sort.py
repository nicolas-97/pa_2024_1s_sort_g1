def opitimizar_busqueda (lista, inicio, salto):
    for i in range (inicio + salto, len(lista, salto)):
        valor = lista [i]
        posicion = i

        while posicion >= salto and lista [posicion - salto] >valor:
            lista[posicion] = lista[posicion - salto]
            posicion = posicion - salto
        lista[posicion] = valor  

def shell_sort(vector):
    mitad = len(vector) // 2

    while mitad > 0:
        for i in range(mitad):
            opitimizar_busqueda(vector, i, mitad)
        mitad = mitad // 2
    return vector 

def quick_sort(vector):
    return vector

def merge_sort(vector):
    return vector