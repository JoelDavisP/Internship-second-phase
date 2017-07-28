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
ani1=animal(3)
ani1.set_name("Chikku")
ani1.set_age(1)
print(ani1)
