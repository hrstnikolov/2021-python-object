class Glass:
    # Set the class attr `capacity` to 250.
    capacity = 250

    def __init__(self):
        self.content = 0

    def get_space_left(self):
        return Glass.capacity - self.content

    def empty(self):
        self.content = 0
        return "Glass is now empty"

    def fill(self, ml):
        if self.get_space_left() < ml:
            return f"Cannot add {ml} ml"

        self.content += ml
        return f"Glass filled with {ml} ml"

    def info(self):
        return f"{self.get_space_left()} ml left"


glass = Glass()
print(glass.fill(100))
print(glass.fill(200))
print(glass.empty())
print(glass.fill(200))
print(glass.info())
