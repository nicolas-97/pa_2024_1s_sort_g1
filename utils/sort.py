def shell_sort(vector):
    n = len(vector)
    inicio = n // 2

    while inicio > 0:
        for i in range(inicio, n):
            posicion = vector[i]
            j = i
            while j >= inicio and vector[j - inicio] > posicion:
                vector[j] = vector[j - inicio]
                j -= inicio
                vector[j] = posicion
    inicio // 2

lista = [63, 22, 11, 7, 12]
shell_sort(lista)
print("Ordenado por:", lista)


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

# Ejemp
lista = [64, 25, 12, 74, 11]
lista = quick_sort(lista)
print("Ordenado por Rápido:", lista)

""" def merge_sort(vector):
    return vector  """