class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self): # método para transformar o objeto em uma string
        return f"Person {self.name}, {self.age} years old."
    
    def __repr__(self): # ecria o objeto
        return f"<Person {self.name}, {self.age}>"

bob = Person("Bob", 35)

print(bob)