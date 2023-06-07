class IntegerList:
    def __init__(self, *args):
        self.__data = []

        for x in args:
            if type(x) == int:
                self.__data.append(x)

    def __validate_index_is_in_range(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")

    @staticmethod
    def __validate_type(item, item_type):
        type_names = {
            int: "Integer",
        }
        if not isinstance(item, item_type):
            raise ValueError(
                f"Element is not {type_names.get(item_type, default=None)}"
            )

    def get_data(self):
        return self.__data

    def add(self, element):
        self.__validate_type(element, int)
        self.get_data().append(element)
        return self.get_data()

    def remove_index(self, index):
        self.__validate_index_is_in_range(index)
        a = self.get_data()[index]
        del self.get_data()[index]
        return a

    def get(self, index):
        self.__validate_index_is_in_range(index)
        return self.get_data()[index]

    def insert(self, index, el):
        self.__validate_index_is_in_range(index)
        self.__validate_type(el, int)
        self.get_data().insert(index, el)

    def get_biggest(self):
        a = sorted(self.get_data(), reverse=True)
        return a[0]

    def get_index(self, el):
        return self.get_data().index(el)
