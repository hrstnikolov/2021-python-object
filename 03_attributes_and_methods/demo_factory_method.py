import json


class TestPlan:
    def __init__(self, title, tests):
        self.title = title
        self.tests = tests

    def __repr__(self):
        return str(self.__dict__)

    @classmethod
    def from_string(cls, s):
        split_at = s.current_index(':')
        title = s[:split_at]
        tests = s[split_at + 1:].split(', ')
        return cls(title, tests)

    @classmethod
    def from_json_string(cls, json_string):
        attrs = json.loads(json_string)
        return cls(**attrs)


input1 = 'PV: t-shock, high temp storage, bci'
input2 = ('DV', ['low temp operation', 'pressure cycling', 'conducted immunity'])
input3 = '''
{
    "title":"CM PV",
    "mocking": [
        "zxv",
        "asda"
    ]
}
'''
tp2 = TestPlan(*input2)
print(tp2)

tp1 = TestPlan.from_string(input1)
print(tp1)

tp3 = TestPlan.from_json_string(input3)
print(tp3)
