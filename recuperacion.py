from functools import reduce

#Ejercicio 1
listas1 = [[1,4,5,2],[1,5,6,3],[1,2,5,3]]
ejercicio1 = map(lambda x:[x[0],x[-1]],listas1)

#Ejercicio 2
listas2 = [1,2,3,5,6,7,8,20,288,231]
def esSuperpar(num):
    estado = True
    textNum = str(num)
    for d in textNum:
        if int(d) % 2 !=0:
            estado = estado and False
    return estado

ejercicio2 = filter(lambda x: esSuperpar(x),listas2)

#Ejercicio 3
listas3 = listas1
ejercicio3 = map(lambda x: max(x),listas3)

#Ejercicio 4

def minSuperpar(lista):
    aux = []
    for ele in lista:
        if esSuperpar(ele):
            aux.append(ele)
    return min(aux)
lista4= [[2,4,778,895,22,44],[21,4,7784,895,22,448],[1,33,45,82,88,25]]
ejercicio4 = map(lambda x: minSuperpar(x),lista4)

#Ejercicio 5
listas5 = [25,52,42,58,28,881111,25**6,25**7]
ejercicio5 = filter(lambda x: x<listas5[0]**5,listas5)


#Ejercicio 6
listas6 = [[1,2],[3,4],[4,5],[10,4],[15,6],[6,3]]
def triangular(num):
    trian = 0
    for i in range(0,num+1):
        trian = trian + i
    return trian

ejercicio6 = reduce(lambda x,y: x[0]+y[0],filter(lambda x: x[0]==triangular(x[1]),listas6))

print("Ejercicio 1")
print(ejercicio1)
print("Ejercicio 2")
print(ejercicio2)
print("Ejercicio 3")
print(ejercicio3)
print("Ejercicio 4")
print(ejercicio4)
print("Ejercicio 5")
print(ejercicio5)
print("Ejercicio 6")
print(ejercicio6)

