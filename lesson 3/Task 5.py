class Nikola:
    __slots__ = ["name", "age"]
    def __init__ (self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        if self.name == 'Николай':
            print (f"Николай")
        else:
            print(f"Я не {self.name}, я Николай")

    def get_age(self):
        print(f"Мой возраст: {self.age}")

person1 = Nikola('Иван', 31)
person2 = Nikola('Николай', 14)
print(person1.get_name())
print(person2.name)
try:
    person2.surname = 'Петров'
except:
    print("Нет такого поля")