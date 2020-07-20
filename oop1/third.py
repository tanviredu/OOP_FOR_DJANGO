

### making a Base Class
class Person:
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname  = lname

    def printname(self):
        print(self.firstname,self.lastname)

class Student(Person):
    ## now all the harastics of the 
    ## Person will be inside the student
    Department = "EEE"
    pass

x1 = Person("tanvir","rahman")
x1.printname()
x2 = Student("Ornob","Rahman")
print(x2.firstname)
print(x2.lastname)
x2.printname()
print(x2.Department)


class AnotherStudent(Person):
    ## this time we add the Department 
    ## as a constructor
    ## and also call the base constructor
    ## one rule the constructor must have 
    ## the property (atleast) of the base constructor

    def __init__(self,fname,lname,dpt):
        ## calling the base constructor
        super().__init__(fname,lname)
        self.department = dpt 


    def show(self):
        print ("Name : {} ,Department: {}".format(self.printname(),self.department))


a1 = AnotherStudent("Tanvir","Rahman","EEE/CSE")
a1.show()
   

