import boto3
from botocore.exceptions import ClientError
from decouple import config
from werkzeug.exceptions import InternalServerError


class S3Service:
    def __init__(self):
        self.key = config("AWS_ACCESS_KEY")
        self.secret = config("AWS_SECRET")
        self.bucket = config("AWS_BUCKET")
        self.region = config("AWS_REGION")
        self.s3 = boto3.client(
            "s3",
            aws_access_key_id=self.key,
            aws_secret_access_key=self.secret,
        )

    def upload_photo(self, path, object_name):
        try:
            ext = path.split(".")[-1]
            self.s3.upload_file(
                path,
                self.bucket,
                object_name,
                ExtraArgs={"ACL": "public-read", "ContentType": f"image/{ext}"},
            )
            return f"https://{self.bucket}.s3.{self.region}.amazonaws.com/{object_name}"
        except ClientError:
            raise InternalServerError("S3 is not available at the moment")

    def delete_photo(self, object_key):
        self.s3.Object(self.bucket, object_key).delete()
