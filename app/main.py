from app.decorators import handle_exceptions, return_type_validator


class Test:
    def __init__(self):
        self.x = 2
        self.y = 0

    def __str__(self):
        return self.__class__.__name__

    @handle_exceptions(TypeError, ValueError)
    def raise_test_exception(self, *args):
        raise ValueError("Test Exception - args: ", args)

    @return_type_validator(str)
    def getn(self, n):
        return 'n + 30'


test = Test()


if __name__ == "__main__":
    print(test.raise_test_exception('test', 'test2', 'test3', []))
    print(test.getn(1))
