class dictionary_iter:
    def __init__(self, dict_obj):
        self.dict_obj = dict_obj

    def __iter__(self):
        # return ((key, value) for (key, value) in self.dict_obj.items())
        return iter(self.dict_obj.items())


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
