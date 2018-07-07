class Animal(object):
    def run(self):
        print 'Animal is running...'
class Dog(Animal):
    def run(self):
        print 'Dog is running...'
    def eat(self):
        print 'Eating meat...'
    pass
class Cat(Animal):
    def run(self):
        print 'Cat is running...'
    pass
def run_twice(animal):
    animal.run()
    animal.run()

dog = Dog()
dog.run()
cat = Cat()
cat.run()

run_twice(Dog())
