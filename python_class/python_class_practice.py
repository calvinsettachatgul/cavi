

class Vehicle:
    def __init__(self, num_wheels, color, type_vehicle):
       self.num_wheels = num_wheels 
       self.color = color
       self.type_vehicle = type_vehicle


my_car = Vehicle(4, "silver", "car")
my_bike = Vehicle(2, "black", "bicycle")

# print(my_car.type_vehicle)
# print(my_car.color)
# print(my_car.num_wheels)


class Cat:
    def __init__(self, name, breed, color, age):
        self.name = name
        self.breed = breed
        self.color = color
        self.age = age

    def eat(self): 
        print("{} cat is eating".format(self.name))
        
    # nice! you can return or print printing returns None though i think
    def catToString(self):
        
        cat_string = "{} is a {} cat aged {} with color {}".format(self.name, self.breed, self.age, self.color)
#         print("{} is a {} cat aged {} with color {}".format(self.name, self.breed, self.age, self.color))
        return cat_string

meow = Cat("meow", "siamese", "black", 4) # ok printing this just says its a cat instance

print(meow.name)

# invoke it 
print(meow)

meow.eat() # this is invoking the eat method that meow object has
# ok it worked! ok I think we are done =)

print(meow.catToString())


# "{} {}".format(variable_name1, variable_name2)#  the {} are place hodlers
