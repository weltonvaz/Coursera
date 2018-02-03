def floatEquals(f1, f2, tol = 0.000000001):
    return abs(f1-f2) <= tol
    

class Triangulo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        
        
    def similar(self, t2):
        sides1 = sorted([self.a, self.b, self.c])
        sides2 = sorted([t2.a, t2.b, t2.c])
        isSimilar = True
        ratio = None
        for i in range(0, len(sides1)):
            newRatio = sides1[i]/sides2[i]
            if ratio != None and not floatEquals(newRatio, ratio):
                isSimilar = False
                break
            ratio = newRatio
        return isSimilar