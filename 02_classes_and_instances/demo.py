d = {'one': 1, 'two': 2}
dd  = {'one': 12341, 'sd': 0}
ddd = dict.fromkeys(str(123456),'no')
print(ddd)

d.update(dd)
d.pop('three',None)
print(d)

print(d.pop('one',None))
print(d)

del d['two']
print(d)

