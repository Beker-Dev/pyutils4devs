import bcrypt


class Encrypt:
    def __init__(self, salt: bytes = bcrypt.gensalt()):
        self.salt = salt

    def encrypt_password(self, pw: bytes) -> bytes:
        return bcrypt.hashpw(pw, self.salt)

    def check_password(self, pw: bytes, hashed_string: bytes) -> bool:
        return bcrypt.checkpw(pw, hashed_string)
