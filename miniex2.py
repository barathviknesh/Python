class Person:
    def __init__(self, name):
        self.name = name
    def talk(self):
        print("TALKING..!")

john = Person("john smith")
print(john.name)
john.talk()