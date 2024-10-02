lista = [1,2,3,4,5,6,7,8,9,10]

print(lista)

l4 = lista[3]*2
l7 = lista[6]*2
l9 = lista[8]*2

print(l4,l7,l9)

lista.pop(3)
lista.insert(3,l4)

lista.pop(6)
lista.insert(6,l7)

lista.pop(8)
lista.insert(8,l9)

print(lista)