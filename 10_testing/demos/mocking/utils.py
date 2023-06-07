from typing import List

from demos.mocking.validators import validate_type, TypeValidator


def my_concat(string_values: List[str]) -> str:
    # validate_type(string_values, [str])
    validator = TypeValidator()
    validator.validate(string_values, [str, ])
    result = ''
    for s in string_values:
        result += s

    return result
