def shell_sort(vector):
    tamano = len(vector)
    inicio = tamano // 2

    while inicio > 0:
        for i in range(inicio, tamano):
            temp = vector[i]
            posicion = i
            while posicion >= inicio and vector[posicion - inicio] > temp:
                vector[posicion] = vector[posicion - inicio]
                posicion -= inicio
            vector[posicion] = temp
        inicio //= 2

    return vector

""" lista = [64, 25, 12, 22, 11]
shell_sort(lista)
print("shell_sort:", lista) """
"""SEGUNDO"""

def quick_sort(vector): 
    if len(vector) <= 1:
        return vector
    else:
        pivot = vector.pop()
        menor = []
        mayor = []
        for element in vector:
            if element <= pivot:
                menor.append(element)
            else:
                mayor.append(element)
        return quick_sort(menor) + [pivot] + quick_sort(mayor) 

""" # Ejemplo de uso:
lista = [64, 25, 12, 74, 11]
lista = quick_sort(lista)
print("quick_sort:", lista) """

""""TERCERO"""
def merge_sort(vector):
    if len(vector) > 1:
        mid = len(vector) // 2
        mitad_izquierda = vector[:mid]
        mitad_derecha = vector[mid:]

        merge_sort(mitad_izquierda)
        merge_sort(mitad_derecha)

        i = j = k = 0

        while i < len(mitad_izquierda) and j < len(mitad_derecha):
            if mitad_izquierda[i] < mitad_derecha[j]:
                vector[k] = mitad_izquierda[i]
                i += 1
            else:
                vector[k] = mitad_derecha[j]
                j += 1
            k += 1

        while i < len(mitad_izquierda):
            vector[k] = mitad_izquierda[i]
            i += 1
            k += 1

        while j < len(mitad_derecha):
            vector[k] = mitad_derecha[j]
            j += 1
            k += 1
    return vector


""" lista = [64, 25, 12, 22, 11]
merge_sort(lista)
print("merge_sort:", lista) """