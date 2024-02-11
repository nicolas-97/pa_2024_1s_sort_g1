def shell_sort(vector):
    distancia = len(vector)//2 #Cantidad de subgrupos que saldran
    ubicacion = 0 #Indica el avance entre elementos de subgrupos
    while distancia>0: 
        while ubicacion<distancia: #No salirse del subgrupo
            for i in range(ubicacion+distancia, len(vector), distancia):
                n = i #se debe comparar el valor del vector[i] con los n vectores que lo anteceden
                while n>ubicacion:
                    n -= distancia
                    if vector[i]<vector[n]:
                        vector[i], vector[n] = vector[n], vector[i]
                        i = n
            ubicacion += 1
        distancia = distancia//2
        ubicacion = 0 #al empezar con nuevo subgrupo se reinicia ubicacion
    return vector

def quick_sort(vector):


    return vector



def merge_sort(vector):
    return vector

vect = [10,5,48,12,36,51,1]
m = shell_sort(vect)
print(m)


