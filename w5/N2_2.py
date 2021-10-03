class Mother:
    def __init__(self, name):
        self.__name = name

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def __str__(self):
        return "Name:{}".format(self.__name)

class Daughter(Mother):
    def __init__(self, name, age, job):
        super().__init__(name)
        self.__age = age
        self.__job = job
    def set_age(self, age):
        self.__age = age

    def get_age(self):
        return self.__age

    def set_job(self, job):
        self.__job = job

    def get_job(self):
        return self.__job

    def __str__(self):
        return "Name:{}  Age:{}  Job:{}".format(self.get_name(),self.get_age(), self.get_job())

print(Mother('Misa'))
print(Daughter('Phien','21','student'))