def shell_sort(vector):
    n=len(vector)
    mitad=n//2
   
    if n >= 1:
        while mitad>0:
            for i in range (mitad,n):
                j=i
                aux=vector[i]
                while j>=mitad and vector[j-mitad]>aux:
                    vector[j]=vector[j-mitad]
                    j-=mitad
                vector[j]=aux
            mitad//=2
        return vector
    else:
        return vector


def quick_sort(vector):
    if len(vector)<=1:
        return vector
    else:
        pivot=vector.pop()
        menores=[]
        mayores=[]
        for num in vector:
            if num > pivot:
                mayores.append(num)
            else:
                menores.append(num)
       
       
        return quick_sort(menores) + [pivot] + quick_sort(mayores)


def merge_sort(vector):
    if len(vector)<=1:
        return vector
    else:
        mitad=len(vector)//2
        mitad_izq=vector[:mitad]
        mitad_der=vector[mitad:]
        vector_final=[]
        merge_sort(mitad_izq)
        merge_sort(mitad_der)


        while len(mitad_izq)>i and len(mitad_der)>j:
            i=j=0
            if mitad_izq[i] > mitad_der[j]:
                vector_final.append(mitad_der[j])
                j+=1


            else:
                vector_final.append(mitad_izq[i])
                i+=1
            
        while i<len(mitad_izq):
            vector_final.append(mitad_izq[i])
            i+=1
        while j<len(mitad_der):
            vector_final.append(mitad_der[j])
            j+=1
        return vector_final
