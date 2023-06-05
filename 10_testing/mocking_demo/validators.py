from abc import ABC, abstractmethod
from typing import Any, List


def validate_type(values: List[Any], types: List[Any]) -> None:
    if not any(isinstance(v, t) for v in values for t in types):
        raise TypeError('Not allowed type.')


# print(validate_type([5, 23], [int, str]))  # None
# validate_type([5, 23], [float, str])  # TypeError

class BaseValidator(ABC):
    @abstractmethod
    def validate(self):
        pass


class TypeValidator(BaseValidator):
    def validate(self, values: List[Any], types: List[Any]) -> None:
        if not any(isinstance(v, t) for v in values for t in types):
            raise TypeError('Not allowed type.')
