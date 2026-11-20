"""Generated from Smithy prelude shape ``smithy.api#Blob``."""

import base64


# --- restJson1 ser/de ---
def serialize_json(value: bytes) -> str:
    return base64.b64encode(value).decode("ascii")


def deserialize_json(data: str) -> bytes:
    return base64.b64decode(data)
