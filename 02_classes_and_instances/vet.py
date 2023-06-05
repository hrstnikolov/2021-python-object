# Make a class named 'Vet'.
class Vet:
    # Create a class attribute named `animals` and set it to an empty list.
    animals = []
    
    # Create a class attr named `space` and set it to 5.
    space = 5

    # class Vet has-a init method that takes self and name.
    def __init__(self, name):
        # set the name attr to the value of the name param.
        self.name = name
        # set the anumals attr to an empty list.
        self.animals = []

    # class Vet has-a static method named `get_..` that takes no arguments.
    @staticmethod
    def get_space_left():
        return Vet.space - len(Vet.animals)

    def register_animal(self, animal_name):
        if self.get_space_left() <= 0:
            return "Not enough space"

        self.animals.append(animal_name)
        Vet.animals.append(animal_name)
        return f"{animal_name} registered in the clinic"

    def unregister_animal(self, animal_name):
        if animal_name not in self.animals:
            return f"{animal_name} not in the clinic"

        self.animals.remove(animal_name)
        Vet.animals.remove(animal_name)
        return f"{animal_name} unregistered successfully"

    def info(self):
        return f"{self.name} has {len(self.animals)} animals. {self.get_space_left()} space left in clinic"


peter = Vet("Peter")
george = Vet("George")
print(peter.register_animal("Tom"))
print(george.register_animal("Cory"))
print(peter.register_animal("Fishy"))
print(peter.register_animal("Bobby"))
print(george.register_animal("Kay"))
print(george.unregister_animal("Cory"))
print(peter.register_animal("Silky"))
print(peter.unregister_animal("Molly"))
print(peter.unregister_animal("Tom"))
print(peter.info())
print(george.info())
