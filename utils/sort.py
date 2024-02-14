def shell(lista):
    medio=len(lista)//2

    while medio>=1:
        for k in range(medio):
            for i in range(k+medio,len(lista),medio):
                numero = lista[i]
                while i >= medio and lista[i-medio]>numero:
                    lista[i]=lista[i-medio]
                    i=i-medio
                lista[i]=numero

        medio=medio//2

#####
        
def particion(lista):
    pivote=lista[0]
    mayores=[]
    menores=[]

    for i in range(1,len(lista)):
        if lista[i]<pivote:
            menores.append(lista[i])
        else:
            mayores.append(lista[i])
    
    return menores, pivote, mayores

def quick_sort(lista):
    if len(lista)<2:
        return lista
    
    menores, pivote, mayores = particion(lista)
    
    return quick_sort(menores)+[pivote]+quick_sort(mayores)

#####

def merge_sort(vector):
    if len(vector)<=1:
        return vector
    else:
        mitad=len(vector)//2
        lista1=merge_sort(vector[:mitad])
        lista2=merge_sort(vector[mitad:])
        return merge(lista1,lista2)

#funcion que hace la mezcla de las dos listas divididas
def merge(lista1,lista2):
    lista=[]
    #indice i para lista 1, indice j para lista 2
    i=0
    j=0
    #comparando los numeros de las dos listas entre ellas
    while i<len(lista1) and j<len(lista2):
        if lista1[i]<lista2[j]:
            lista.append(lista1[i])
            i+=1
        else:
            lista.append(lista2[j])
            j+=1

    #si la lista 1 se acaba 
    if i==len(lista1):
        for k in range(j,len(lista2)):
            lista.append(lista2[k])
    
    #si la lista 2 se acaba
    if j==len(lista2):
        for k in range(i,len(lista1)):
            lista.append(lista1[k]) 

    return lista