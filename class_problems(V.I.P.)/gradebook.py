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

class Student(gecpkd):
    pass


class UG(Student):
    def __init__(self,name,classyear):
        gecpkd.__init__(self,name)
        self.year = classyear
    def getclassyear(self):
        return self.year
    def speak(self,words):
        return (self.getname() + " says " + "\n" + words) 
    

class Grad(Student):
    pass
class TransferStudent(Student):
    pass
def isStudent(obj):
    return isinstance(obj,Student)


class Grades(object):
    """
    A datastructure that contains the names of students and their grades
    """
    def __init__(self):
        """
        create an empty list and gradebook
        """
        self.students = []
        self.grades = {}
        self.isSorted = True

    def addstudent(self,student):
        """
        Add students to the list
        """
        if student in self.students:
            raise ValueError("Duplicate student")
        else:
            self.students.append(student)
            self.grades[student.getId()] = []
            self.isSorted = False
    def addGrade(self,student,grade):
        """
        Add a float number to the list of grades for a student
        """
        try:
            self.grades[student.getId()].append(grade)
        except KeyError:
            raise ValueError("Student not in gradebook")
    def getGrades(self,student):
        """
        Returns the geade list
        """
        try:
            return self.grades[student.getId()][:]
        except KeyError:
            raise ValueError("Student not in gradebook")

    def allStudents(self):
        """
        returns the list of students in the gradebook
        """
        if not self.isSorted:
            self.students.sort()
            self.isSorted = True
        return self.students[:] #returns copy of list of students

#def gradeReport(course):
    """
    Prints a report of students grades, given a specific course as input to the function.
    course is of type Grade, in fact we are calling the grade method itself.
    But since we couldn't iterate over a class we are creating a class object first and iterate over that object.
    """
#    report = []
#    for s in course.allStudents:
#        tot = 0.0
#        numGrades = 0
#        for g in course.getGrades(s):
#            tot += g
#            numGrades += 1
#        try:
 #           avg = tot/numGrades
  #          report.append(str(s) + '\'s mean grade is ' + str(avg))
   #     except ZeroDivisionError:
    #        report.append(str(s) + ' has no grades.')
     #   return '\n'.join(report)

s1 = UG("Gopi Sunder",2012)
s2 = UG("Krishna Varrier",2013)
s3 = UG("Vismay Mathews",2011)
s4 = UG("Gopi Sunder",2012)
s5 = UG("Saloman Kaloo",2013)
s6 = UG("Smruthi Mandana",2011)
s7 = UG("Ajay Krishna",2013)
s8 = UG("Ashuthosh Mohan",2011)
s9 = Grad("Kokila Vincent")
s10 = TransferStudent("Akash Menon")

CS = Grades()
CS.addstudent(s1)
CS.addstudent(s2)
CS.addstudent(s3)
CS.addstudent(s4)
CS.addstudent(s5)
CS.addstudent(s6)
CS.addstudent(s7)
CS.addstudent(s8)
CS.addstudent(s9)
CS.addstudent(s10)


CS.addGrade(s1,54)
CS.addGrade(s2,59.5)
CS.addGrade(s3,61.5)
CS.addGrade(s4,70.5)
CS.addGrade(s5,49)
CS.addGrade(s6,51.5)
CS.addGrade(s7,68)
CS.addGrade(s8,66.5)
CS.addGrade(s9,75)
CS.addGrade(s10,73.5)


for st in CS.allStudents():
    print(st)

#print(gradeReport(CS))
