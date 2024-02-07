def shell_sort(vector):
    longitud = len(vector)
    intervalo = longitud // 2 #Se necesita una división entera

    while intervalo > 0:
        for i in range(intervalo, longitud):
            valor = vector[i]
            valor_index= i

            while valor_index >= intervalo and vector[valor_index - intervalo] > valor:
                vector[valor_index] = vector[valor_index - intervalo]
                valor_index -= intervalo

            vector[valor_index] = valor
        intervalo = intervalo//2
    return vector

def quick_sort(vector):
    return vector

def merge_sort(vector):
    return vector