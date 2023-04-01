from app.decorators.generic import handle_exceptions

from datetime import datetime, timedelta
from jose import jwt


def jwt_token_generator(
    secret_key: str = 'NotSecret',
    algorithm: str = 'HS256',
    token_type: str = 'access',
    expires_minutes: int = 1440,
    payload: dict = None
):
    data = payload.copy() if payload is not None else {}
    data.update({
        'iat': datetime.now(),
        'exp': datetime.now() + timedelta(minutes=expires_minutes),
        'type': token_type
    })
    return jwt.encode(data, secret_key, algorithm=algorithm)


@handle_exceptions(jwt.JWTError)
def jwt_token_validator(
    token: str,
    secret_key: str = 'NotSecret',
    algorithm: str = 'HS256',
):
    return jwt.decode(token, secret_key, algorithms=[algorithm])
