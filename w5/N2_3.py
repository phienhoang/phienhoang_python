class Animal:
    __name = None
    __age = None
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def __str__(self):
        return self.print_animal()

class Zebra(Animal):
    __food = ""

    def __init__(self,name, age, food,height):
        super().__init__(name, age)
        self.__food = food
        self.__height = height

    def get_food(self):
        return self.__food

    def get_height(self):
        return self.__height

    def print_animal(self):
        return f"Name:{self.get_name()}  Age:{self.get_age()}  Food:{self.get_food()}  Height:{self.get_height()}"

class Dolphin(Animal):
    __color = ""

    def __init__(self,name, age, color, long):
        super().__init__(name, age)
        self.__color = color
        self.__long = long

    def get_color(self):
        return self.__color

    def get_long(self):
        return self.__long

    def print_animal(self):
        return f"Name:{self.get_name()}  Age:{self.get_age()}  Color:{self.get_color()}  Long:{self.get_long()}"


z=Zebra("Roronoa","2","Grass","1m")
print(z)
d= Dolphin("Sunny","1","White","1m")
print(d)