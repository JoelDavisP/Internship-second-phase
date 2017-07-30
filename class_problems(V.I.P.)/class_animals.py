class animal(object):
    def __init__(self,age):
        self.age = age
        self.name = None
    def get_age(self):
        return self.age
    def get_name(self):
        return self.name
    def set_age(self,new_age):
        self.age = new_age
    def set_name(self,new_name=""):
        self.name = new_name
    def __str__(self):
        return "animal: " + str(self.name)+ " have " + str(self.age) + " years old"
    
class Cat(animal):
    def speak(self):
        print("Meow")
    def __str__(self):
        return "Cat: " + str(self.name) + " have  " + str(self.age) + " years old. " 

class Rabbit(animal):
    tag = 1
    def __init__(self,age):
        self.age = age
        self.RID = Rabbit.tag
        Rabbit.tag += 1
    def speak(self):
        print("Meep")
    def __str__(self):
        return "Rabbit: " + str(self.name) + " have  " + str(self.age) + " years old " + " and tag is: " + str(self.RID) 


class person(animal):
    def __init__(self,name,age):
        animal.__init__(self,age)
        animal.set_name(self,name)
        self.friends = []
    def get_friends(self):
        print("Friends of ", self.get_name(), " are: ")
        for i in self.friends:
            print(i)
    def add_friend(self,friend):
        if friend not in self.friends:
            self.friends.append(friend)
    def speak(self):
        print("Hello Joel")
    def age_diff(self,other):
        diff = self.get_age() - other.get_age()
        if diff > 0:
            print(self.get_name(), " is ", diff, " years older than ", other.get_name() )
        else:
                
            print(self.get_name(), " is ", diff, " years younger than ", other.get_name() )

    def __str__(self):
        return "Person: " + str(self.get_name()) + " : " + str(self.get_age())


ani1=animal(3)
ani1.set_name("Chikku")
ani1.set_age(1)
print(ani1)

ani2 = Cat(2)
ani2.set_name("Tommy")
print(ani2)
ani2.speak()

ani3 = Rabbit(0)
ani3.set_name("Mikky")
print(ani3)
ani3.speak()

ani10 = Rabbit(2)
ani10.set_name("Minny")
print(ani10)
ani10.speak()


ani11 = Rabbit(1)
ani11.set_name("Mitty")
print(ani11)
ani11.speak()

ani4=person("Joel",23)
ani5=person("Maya",22)
ani6=person("Mahipal",23)
ani7=person("Vishnu",23)
ani8=person("Nakku",23)
ani9=person("Divss",23)
ani4.speak()
ani4.add_friend(ani5)
ani4.add_friend(ani6)
ani4.add_friend(ani7)
ani4.add_friend(ani8)
ani4.add_friend(ani9)
ani4.age_diff(ani5)
print(ani4)
ani4.get_friends()
