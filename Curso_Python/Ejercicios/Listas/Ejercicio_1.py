lista = [20,50,"Curso",'Python',3.14]

print(type(lista))

#Pintar lista
print(lista)

#Pedir datos
dato1 = int(input("Introduce dato1: "))
dato2 = str(input ("Introduce dato2: "))

lista.pop(0)
lista.pop(1)

print(lista)

lista.insert(0,dato1)
lista.insert(1,dato2)

print(lista)