from minio import Minio


class MinIO:
    def __init__(
            self,
            address: str,
            access_key: str,
            secret_key: str,
            bucket_name: str,
            extensions_accepted: list = '__all__',
            secure: bool = False
    ):
        self.__address = address
        self.__access_key = access_key
        self.__secret_key = secret_key
        self.__bucket_name = bucket_name
        self.__extensions_accepted = extensions_accepted
        self.__secure = secure
        self.__client = Minio(self.__address, self.__access_key, self.__secret_key, secure=self.__secure)
