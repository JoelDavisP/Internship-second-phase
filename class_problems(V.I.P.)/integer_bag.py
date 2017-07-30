class intSet(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self""" 
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes e is an integer
           Returns True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
           Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'

    def intersect(self,other):
        inew = intSet()
        try:
            for i in self.vals:
                if i in other.vals:
                    inew.insert(i)
            return inew
        except:
            raise ValueError("No common elements found")
            
    def __len__(self):
        return len(self.vals)            





c=intSet()
c.insert(5)
c.insert(10)
c.insert(55)

d=intSet()
d.insert(5)
d.insert(50)
d.insert(90)
d.insert(55)

e=intSet()
e.insert(500)
e.insert(540)
e.insert(920)
d.insert(55)
print(c.intersect(d))
print(d.intersect(e))
print(len(c))
print(len(d))
print(len(e))
