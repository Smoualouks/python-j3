class Student:
    # propiété privée
    __age = 15
    first_name = ""
    last_name = ""

    # méthodes (fonction dans une classe)
    def test(self):
        print("test")
    # Accesseur (getter)
    def get_age(self):
        return self.__age
    # mutateurs ( setteurs)
    def set_age(self, age):
        self.__age = age
# instalciation :

s1 = Student()
s2 = Student()


# print(type(s1))
s1.first_name = "Toto"
print(s1.first_name)
print(s2.first_name)

# invocation d'une méthode à partir d'un objet
s1.test()
s2.test()

# print(s1.age)
s1.set_age(1)
print(s1.get_age())
print(s1)
#----------------------------------------------------------------------------------------------------
class Vehicule:
    __num_wheels = 0
    __max_speed = 100
    
    # méthodes:
    # constructeurs
    def __init__(self, num_wheels, max_speed):
       self.__num_wheels = num_wheels
       self.__max_speed = max_speed

    def get_max_speed(self):
        return self.__max_speed
    
    def get_num_wheels(self):
        return self.__num_wheels
v1 = Vehicule(2, 90)
v2 = Vehicule(4, 120)

print(v1.get_num_wheels())
print("Vitesse max du véhicule v1: ", v1.get_max_speed())
print("Vitesse max du véhicule v1: ", v2.get_max_speed())
