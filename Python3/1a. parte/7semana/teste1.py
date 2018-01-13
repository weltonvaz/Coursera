def é_hipotenusa(a, b):
    return ((a*a) + (b*b))
 
def soma_hipotenusas(n):
    c = 1
    soma = 0
    while (c <= n):
        euclides = (c*c)      
        a = 1
        b = 1
        while (a < n):
            while (b < n):
                if (euclides == é_hipotenusa(a, b)):
                    soma = soma + c
                    a = n
                    break
                b += 1
            a += 1
            b = a
        c += 1
   
    return soma

number = int(input("Digite o numero inteiro: "))
print(soma_hipotenusas(number))