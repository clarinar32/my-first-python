class Person:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def say_hello(self):
        print(f"Hello ,my name is {self.name} and my age is {self.age}")
person1=Person("claris",17)
person1.say_hello()
person2=Person("pavan",18)
person2.say_hello()
person3=Person("erik",30)
person3.say_hello()
# create a class called cars with the following atributes /properties
# make .model .year then create a function yhat prints make,model,year
# then create three objects

class Cars:
    def __init__(self, make, model, year):
        self.make=make
        self.model=model
        self.year=year
    def this_are_cars(self):
        print(f"This is my favourite car{self.make} {self.model} in the year {self.year}")
car1=Cars("A-class","Mercedes benz",2022)
car1.this_are_cars()
car2=Cars("A3","Audi",2023)
car2.this_are_cars()
car3=Cars("A4","Audi",2022)
car3.this_are_cars()

class Books:
    def __init__(self,name,author,publisher):
       self.name=name
       self.author=author
       self.publisher=publisher
    def my_book(self):
       print(f"kiswahili novels include{self.name} {self.author} published by{self.publisher}")
book1=Books("Chozi la heri","Asumpta K", "Kenya litrature")
book1.my_book()
book2=Books("Damu nyeusi", "Ken Walibora", "KLB")
book2.my_book()
book3=Books("Kaburi bila msalaba", "Ken Walibora", "KLB")
book3.my_book()