class fraction(object):
    def __init__(self,x,y):
        self.x = x
        self.y =y
    def __str__(self):
        return str(self.x) +  '/' + str(self.y)
    def getx(self):
        return self.x
    def gety(self):
        return self.y
    def __add__(self,other):
        newx = self.getx() * other.gety() + self.gety() * other.getx()   
        newy = self.gety() * other.gety()
        return fraction(newx,newy)
    def __sub__(self,other):
        newx = self.getx() * other.gety() - self.gety() * other.getx()   
        newy = self.gety() * other.gety()
        return fraction(newx,newy)
    def convert(self):
        return self.getx() / self.gety()

c1=fraction(1,2)
c2=fraction(5,7)
c3=fraction(11,5)
c4=fraction(29,2)
c5=fraction(5,3)
c6=fraction(3,8)
c7=fraction(7,21)

print(c1)
print(c2)
print(c3)
print(c4)

print(c1+c2)
print(c3-c4)
print(c6.convert())
print(c7.convert())
