from abc import abstractmethod, ABC


class Shape(ABC):
    @abstractmethod
    def draw_rectangle(self):
        raise NotImplementedError

    @abstractmethod
    def draw_circle(self):
        raise NotImplementedError


class