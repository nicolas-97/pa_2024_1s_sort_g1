def shell_sort(vector):
    longitud=len(vector)
    intervalo=longitud // 2 #Se necesitan divisiones enteras

    while intervalo > 0:
        for i in range(intervalo, longitud):
            valor_insert=vector[i]
            valor_index=i

            while valor_index >= intervalo and vector[valor_index-intervalo]>valor_insert:
                vector[valor_index] = vector[valor_index-intervalo]
                valor_index-=intervalo
            vector[valor_index] = valor_insert
        intervalo=intervalo//2
    return vector

def quick_sort(vector):
    if len(vector) <= 1:
        return vector
    else:
        indicador = vector[0]
        menores = [x for x in vector[1:] if x <= indicador]
        mayores = [x for x in vector[1:] if x > indicador]
    return quick_sort(menores) + [indicador] + quick_sort(mayores)
    

def merge_sort(vector):
    if len(vector) <= 1:
        return vector
    else:
        medio = len(vector) // 2
        izquierda = merge_sort(vector[:medio])
        derecha = merge_sort(vector[medio:])
        return merge(izquierda, derecha)
def merge(izquierda, derecha):
    resultado = []

    while len(izquierda) > 0 and len(derecha) > 0:
        if izquierda[0] > derecha[0]:
            resultado.append(derecha[0])
            derecha.pop(0)
        else:
            resultado.append(izquierda[0])
            izquierda.pop(0)
    while len(izquierda) > 0:
        resultado.append(izquierda[0])
        izquierda.pop(0)
    while len(derecha) > 0:
        resultado.append(derecha[0])
        derecha.pop(0)
    
    return resultado