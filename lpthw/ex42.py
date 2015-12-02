##Animal is-a object
class Animal(object):
	pass

class Dog(Animal):
	def __init__(self, name):
		self.name = name

class Cat(Animal):
	def __init__(self, name):
		self.name = name

class Person(object):
	def __init__(self, name):
		self.name = name

	##Person has-a pet 
		self.pet = None

class Employee(Person):

	def __init__(self, name, salary):
	 	
	 	##trial
	 	super(Employee, self).__init__(name)

	 	self.salary = salary

class Fish(object):
	pass
class Salmon(Fish):
	pass

class Halibut(Fish):
	pass

#rover is a dog

rover = Dog("Rover")

sataa = Cat("Sataa")

mary = Person("Mary")

mary.pet = sataa

frank = Employee("Frank", 120000)

frank.pet = rover

flipper = Fish()

crouse = Salmon()

harry = Halibut()









