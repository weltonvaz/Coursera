# Author: Franklin Basilio
# Data: 07/09/2013
#
 
a = float (input("Lado A? "))
b = float (input("Lado B? "))
c = float (input("Lado C? "))
 
if a <= 0 or b <= 0 or c <= 0:
    print("Valor invalido em um dos lados!")
elif a+b > c and a+c > b and b+c > a:
 
    if a==b and b==c: #transitividade a==c
        print("Triangulo Equilatero")
    elif a != b and b != c and a != c:
        if a**2 == b**2+c**2 or b**2 == a**2 + c**2 or c**2 == a**2 + b**2:
            print("Triangulo Retangulo")
        else:
            print("Triangulo Escaleno")
    elif a==b or a==c or b==c:
        print("Triangulo Isosceles")
    
else:
    print("Nao forma um Triangulo!")
 
 
