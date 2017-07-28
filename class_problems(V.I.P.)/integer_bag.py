class bagint(object):
    def __init__(self):
        self.val=[]
    def insert(self,i):
        if i not in self.val:
            self.val.append(i)
    def member(self,i):
        return i in self.val
    def remove(self,i):
        try:
            self.val.remove(i)
        except:
            raise ValueError(str(i) + 'not present')
    def __str__(self):
        res=''
        for i in self.val:    
            res = res + str(i) + ','
        return '{' + res[:-1] + '}'


c=bagint()
print(c)
c.insert(5)
c.insert(10)
c.insert(5)
#c.remove(10)
print(c)
c.remove(250)
print(c)
