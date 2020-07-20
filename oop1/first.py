mylist = [1,2,3]
mylist.append(4)
print(mylist)

class Sample():
    pass


class Dog():
    ## this is called class object attrivute
    species = "mamal"

    def __init__(self,breed="unknown",name="unknown"):
        self.breed = breed
        self.name = name

    def __str__(self):
         return self.name

mydog = Dog("lab","samy")
otherDog = Dog("Huskey","tony")
print(otherDog.species)
print(mydog.species)

print(mydog)
print(otherDog)

x = Sample()
print(type(x)


)
