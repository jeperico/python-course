# import converters
from converters import talk

class Race:
    def talk(self, message):
        print(message)


class Person(Race):
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def present(self):
        print(f"Helo, my name is {self.first_name} {self.last_name}. I'm {self.age} years old")


p1 = Person('Greg', 'Thyson', 24)
p2 = Person('George', 'Vidal', 14)
p2.present()
p1.present()
p2.talk("Oh, I can talk")
p1.talk("Me too, let's go then!")

talk("Oh... This work it")
