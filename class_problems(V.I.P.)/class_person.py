import datetime
class Person(object):
    def __init__(self,name):
        """
        Create a person called name
        """
        self.name= name
        self.birthday= None
        self.lastname= name.split(' ')[-1]
    def getLastname(self):
        """
        return the last name of person
        """
        return self.lastname
    
    def setBirthday(self,month,day,year):
        """
        set the birthday of that person
        """
        self.birthday = datetime.date(year,month,day)
    def getAge(self):
        """
        return current age in days
        """
        if self.birthday == None:
            raise ValueError
        return (datetime.date.today() - self.birthday).days

    
    def __lt__(self,other):
        """
        return True if the person's last name is 
        lexicographically less than other's last name"""
        if self.lastname == other.lastname:
            return self.name < other.name
        else:
            return self.lastname < other.lastname

    def __str__(self):
        """
        return the object in a systematic way
        """
        return str(self.name) +  " born on " +  str(self.birthday)




class gecpkd(Person):
    ID = 1000
    def __init__(self,name):
        Person.__init__(self,name)
        self.ID = gecpkd.ID    
        gecpkd.ID += 1
    def getId(self):
        return self.ID
    def getname(self):
        return str(self.name)
    def __gt__(self,other):
        """
        Return True if self has larger ID than other
        """
        return self.ID > other.ID
    def speak(self, words):
        return (self.getname() + " says " + "\n" + words) 

class UG(gecpkd):
    def __init__(self,name,classyear):
        gecpkd.__init__(self,name)
        self.year = classyear
    def getclassyear(self):
        return self.year
    def speak(self,words):
        return (self.getname() + " says " + "\n" + words) 
    

class Grad(gecpkd):
    pass
    def isStud(obj):
        return isinstance(obj,UG) or isinstance(obj,Grad)
    



class Professor(gecpkd):
    def __init__(self,name,department):
        gecpkd.__init__(self,name)
        self.department = department
    def speak(self,words):
        new = "In the course " + self.department + " we say "
        return gecpkd.speak(self,new + words)
    def lecture(self,topic):
        return self.speak(" Today we gonna discuss about" + topic)





pr = Professor("Irshadh KP", "Science")






p1 = Person("Joel Davis")
p1.setBirthday(1,17,1995)

p2 = Person("Mark Zukkur")
p2.setBirthday(5,6,1984)
p3 = Person("John Senna")
p3.setBirthday(12,10,1990)
p4 = Person("Mary Raphael")
p4.setBirthday(6,1,1978)
p5 = Person("Simon Doull")
p5.setBirthday(12,7,1936)
p6 = Person("Mohan Lal")
p6.setBirthday(11,3,1954)

persons = [p1,p2,p3,p4,p5,p6]
persons.sort()
for e in persons:
    print(e)



t1 = gecpkd("Eric Drisson")
Person.setBirthday(t1,11,3,1999)
t2 = gecpkd("Gimm Dessinson")
Person.setBirthday(t2,7,9,1965)

tutors = [t1,t2]
tutors.sort()





s1 = UG("Kumar Varma",2015)
s2= UG("Vijay Shankar",2014)
s3 = UG("Sudheep Mishra",2014)
s4 = Grad("Leanardo Daa Vincchi")

