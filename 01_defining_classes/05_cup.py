class Cup:
    def __init__(self, size, quantity):
        self.size = size
        self.quantity = quantity

    def get_free_volume(self):
        return self.size - self.quantity

    def fill(self, milliliters):
        if milliliters > self.get_free_volume():
            return

        self.quantity += milliliters

    def status(self):
        return self.get_free_volume()


cup = Cup(100, 50)
cup.fill(50)
cup.fill(10)
print(cup.status())
