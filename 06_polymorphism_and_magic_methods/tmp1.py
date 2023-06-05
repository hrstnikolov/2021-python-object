from typing import Any, List


class MyList:
    def __init__(self, data: List[Any]) -> None:
        self.data = data

    def __getitem__(self, key):
        return self.data[key]

    def __setitem__(self, key, value):
        self.data[key] = value

    def __iter__(self):
        return iter(self.data)
    

my_list = MyList(['First', 'Second',])
print(my_list[0])  # Calls getitem
my_list[1] = 'Updated'  # Calls setitem
for item in my_list:  # Calls iter and next
    print(item)

