import os


def handle_file_exits(func):
    def decorator(self, filepath, *args, **kwargs):
        if not os.path.isfile(filepath):
            raise FileNotFoundError(f'File {filepath} not found')
        return func(self, filepath, *args, **kwargs)
    return decorator
