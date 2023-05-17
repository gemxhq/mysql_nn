
class Person:
    def __init__(self, age, name):
        self.age = age
        self.name = name
    

if __name__ == '__main__':
    t = Person(19, "gemxhq")
    setattr(t, "age", 22)
    print(t.age)
    