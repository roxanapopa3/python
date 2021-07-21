# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age

cat1=Cat("A",20)
cat2=Cat("B",30)
cat3=Cat("C",10)


def oldest(obj1,obj2,obj3):
    return max(obj1,obj2,obj3)

if