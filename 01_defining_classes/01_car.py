# Make class named 'Car'.
class Car:
    # Class `Car` has a init that takes self, name...
    def __init__(self, name, model, engine):
        self.name = name
        self.model = model
        self.engine = engine
    
    # Class car has a method `get_info` that takes self.
    def get_info(self):
        return f"This is {self.name} {self.model} with engine {self.engine}"


car = Car("Kia", "Rio", "1.3L B3 I4")
print(car.get_info())
