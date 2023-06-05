def singelton(cls):
    instance = None

    def wrapper(*args, **kwargs):
        nonlocal instance
        if not instance:
            instance = cls(*args, **kwargs)
            return instance

    return wrapper


class JsonParser:
    def parse(self, obj):
        return f'json: {str(obj)}'


@singelton
class JsonParser2:
    def parse(self, obj):
        return f'json: {str(obj)}'


print(id(JsonParser()))
print(id(JsonParser()))
print(id(JsonParser()))

print(id(JsonParser2()))
print(id(JsonParser2()))
print(id(JsonParser2()))


