import math
print("Hola, escribe tu variable x")
a= float(input())
print("Bien, ahora escribe tu variable y")
b= float(input())
print("Ya casi terminamos, solo ingresa tu variable z")
c= float(input())
dentro=((b**2)-(4*a*c))
raiz=(dentro)**(0.5)
if dentro>0:
    x1=((-b)+raiz)/(2*a)
    x2=((-b)-raiz)/(2*a)
    print("Valor de x1: " + str(x1))
    print("Valor de x2: " + str(x2))
else:
    print("Resultado indefinido, por favor, introduce otros datos")