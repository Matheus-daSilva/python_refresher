class ClassTest:
    def instance_method(self):
        print(f"Called instance_method of {self}")

    @classmethod
    def class_method(cls): #cls representa a própria classe
        print(f"Called class_method of {cls}")
    
    @staticmethod
    def static_method(): # método usado quando não vai receber nenhum método da classe
        print("Called static_method")

ClassTest.class_method() #o classmethod permite chamar um método sem a necessidade de instanciar a classe

# --------------------------------------------------------

class Book:
    TYPES = ("harcover", "paperback")

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self):
        return f"<Book {self.name}, {self.book_type}, weighing {self.weight}g>"
    
    @classmethod
    def hardcover(cls, name, page_weight):
        return cls(name, cls.TYPES[0], page_weight) # também pode ser Book.TYPES[0] ao invés de cls.TYPES[0]
    
    @classmethod
    def paperback(cls, name, page_weight):
        return cls(name, cls.TYPES[1], page_weight)
    


book = Book.hardcover("Harry Potter", 1500)
light = Book.paperback("Python 101", 600)

print(Book.TYPES)
print(book)
print(light)
