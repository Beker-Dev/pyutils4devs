from app.generators.secrets import secret_key_generator
from app.generators.jwt import jwt_token_generator, jwt_token_validator


if __name__ == "__main__":
    payload = {'user_id': 1, 'username': 'admin'}
    tkn = jwt_token_generator(payload=payload)
    print(jwt_token_validator(tkn))
