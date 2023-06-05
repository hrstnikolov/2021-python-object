'''
Task: Write two parse classes. One shall parse in json format, the other - csv.
Each class has a parse method.
Create a class Person and an instance. Test the parsers with the instance.

'''
import json
from abc import ABC, abstractmethod


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class JsonParser:
    def parse(self, obj):
        return json.dumps(obj.__dict__)


class CsvParser:
    def parse(self, obj):
        result = [
            ', '.join(str(x) for x in obj.__dict__.keys()),
            ', '.join(str(x) for x in obj.__dict__.values()),
        ]
        return result


alan = Person('Alan', 23)


# # Initial
# format = input()
# if format == 'json':
#     result = JsonParser().parse(alan)
# elif format == 'csv':
#     result = CsvParser().parse(alan)
#
# print(result)


# # Better: use factory method design pattern
# class StringParser:
#     def parse(self, obj):
#         return str(obj)
#
#
# def get_parser(format):
#     if format == 'json':
#         return JsonParser()
#     elif format == 'csv':
#         return CsvParser()
#     else:
#         return StringParser()
#
# format = input('format: ')
# parser = get_parser(format)
# result = parser.parse(alan)
# print(result)d


# # Even better: make real method (not function as above)
# class Parser(ABC):
#     @abstractmethod
#     def parse(self):
#         pass
#
# class ParsersFactory:
#     def get(self, format) -> Parser:
#         # if ... return ...