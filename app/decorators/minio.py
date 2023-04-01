import os


def connection(func):
    def decorator(*args, **kwargs):
        self = args[0]
        if not self.client.bucket_exists(self.bucket_name):
            self.client.make_bucket(self.bucket_name)
        return func(*args, **kwargs)

    return decorator


def extensions_validator(func):
    def decorator(*args, **kwargs):
        self = args[0]
        filepath = kwargs.get('filepath') or args[1]
        *_, file_extension = os.path.splitext(filepath)

        if self.extensions_accepted == '__all__' or file_extension in self.extensions_accepted:
            return func(*args, **kwargs)
        else:
            raise TypeError(f"Expected types: {self.extensions_accepted}, got: {file_extension}")
    return decorator
