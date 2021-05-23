class Person:
    def __init__(self,name,age,male):
        self.name = name
        self.age = age
        self.male = male


a = Person('Asan',22,'man')
b = Person('Alina',20,'woman')
c = Person('Akyl',24,'man')

def display(person):
    print(f'Name:{person.name}---Age:{person.age}---Male:{person.male}')

display(a)
