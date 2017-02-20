## Animal is-a object
class Animal(object):
    pass

## Dog is an animal
class Dog(Animal):

    def __init__(self, name):
        ## Dog has a name
        self.name = name

# Cat is an animal
class Cat(Animal):

    def __init__(self, name):
        ## Cat has a name
        self.name = name

## Person is an object
class Person(object):

    def __init__(self, name):
        ## Person has a name

        ## Person has-a pet of some kind
        self.pet = None

## Employee is a Person
class Employee(Person):

    def __init__(self, name, salary):
        ##
        super(Employee, self).__init__(name)
        ## Employee has-a salary

## Fish is an object
class Fish(object):
    pass

## Salmon is a Fish
class Salmon(Fish):
    pass

## Halibut is a Fish
class Halibut(Fish):
    pass

## Rover is a Dog
rover = Dog("Rover")

## Satan is a Cat
satan = Cat("Satan")

## Mary is a Person
mary = Person("Mary")

## Mary has-a pet Satan
mary.pet = satan

## Frank is an Employee
frank = Employee("Frank", 120000)

## Flipper is a Fish
flipper = Fish()

## Crouse is a Salmon
crouse = Salmon()

## Harry is a Halibut
harry = Halibut()
