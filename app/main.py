from app.utils.minio import MinIO


if __name__ == "__main__":
    minio = MinIO(
        address="localhost:9000",
        access_key="test",
        secret_key="test",
        bucket_name="test",
    )
