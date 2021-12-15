import base64

from werkzeug.exceptions import BadRequest


def decode_photo(encoded_photo, path):
    with open(path, "wb") as file:
        try:
            file.write(base64.b64decode(encoded_photo.encode("utf-8")))
        except Exception:
            raise BadRequest("Invalid photo encoding")
