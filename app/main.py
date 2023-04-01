from app.utils.jwt import JWT


if __name__ == "__main__":
    payload = {'user_id': 1, 'username': 'admin'}
    jwt = JWT()
    tkn = jwt.get_token(payload)
