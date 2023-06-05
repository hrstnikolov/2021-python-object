from project.lizard import Lizard
from project.mammal import Mammal

mammal = Mammal("Stella")
print(mammal.__class__.__bases__[0].__name__)
print(mammal.name)
print(mammal._Animal__name)
lizard = Lizard("John")
print(lizard.__class__.__bases__[0].__name__)
print(lizard.name)
print(lizard._Animal__name)

for base in lizard.__class__.__bases__:
    print(base)

print(lizard.__class__.__base__)
