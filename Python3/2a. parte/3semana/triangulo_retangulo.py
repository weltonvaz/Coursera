class Triangulo():
    
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
    
    def retangulo(self):
        if self.a <= 0 or self.b <= 0 or self.c <= 0:
            return False
        elif (self.a + self.b) > self.c and (self.a + self.c) > self.b and self.b + self.c > self.a:
            return False
        elif self.a == self.b and self.b == self.c: #transitividade a==c
            return False
        elif self.a != self.b and self.b != self.c and self.a != self.c:
            return False                
        elif (self.a ** 2) == (self.b ** 2) + (self.c ** 2) or (self.b ** 2) == (self.a ** 2) + (self.c ** 2) or (self.c ** 2) == (self.a ** 2) + (self.b ** 2):
            return True
        elif self.a == self.b or self.a == self.c or self.b == self.c:
            return False
        else:
            return False
    
    def semelhantes(self, t2):
        if t1 == t2:
            return True
        else:
            return False
        