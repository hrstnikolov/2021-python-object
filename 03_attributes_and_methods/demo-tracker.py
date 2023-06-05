import time


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Tracker:
    def __init__(self):
        self.objects = []
        self.last_id = 0

    def add_obj(self, obj):
        self.objects.append(obj)
        setattr(obj, 'track_id', self.last_id)
        self.last_id += 1

    def track(self):
        while True:
            for obj in self.objects:
                print(getattr(obj, 'track_id', None))
            time.sleep(2)


gosho = Person('Gosho', 12)
ana = Person('Ana', 13)
tracker = Tracker()

tracker.add_obj(gosho)
tracker.add_obj(ana)

tracker.track()