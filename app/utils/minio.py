from app.decorators.minio import connection, extensions_validator

from minio import Minio
from datetime import datetime, timedelta
import os


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
        self.address = address
        self.access_key = access_key
        self.secret_key = secret_key
        self.bucket_name = bucket_name
        self.extensions_accepted = extensions_accepted
        self.secure = secure
        self.client = Minio(self.address, self.access_key, self.secret_key, secure=self.secure)

    @connection
    @extensions_validator
    def save_file(self, filepath) -> str:
        filename, extension = os.path.splitext(filepath)
        filename += datetime.now().strftime('%Y%m%d%H%M%S%f') + extension
        self.client.fput_object(self.bucket_name, filename, filepath)
        return filename

    @connection
    def get_file(self, filename: str, expires_minutes: int = 1440) -> str:
        return self.client.get_presigned_url(
            'GET',
            self.bucket_name,
            filename,
            expires=timedelta(minutes=expires_minutes)
        )
