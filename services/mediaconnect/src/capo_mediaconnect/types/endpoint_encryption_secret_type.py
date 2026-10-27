"""Generated from Smithy shape ``com.amazonaws.mediaconnect#EndpointEncryptionSecretType``."""

from typing import Literal, TypeAlias, cast

EndpointEncryptionSecretType: TypeAlias = Literal[
    "AES_128_KEY",
    "AES_192_KEY",
    "AES_256_KEY",
    "SRT_PASSPHRASE",
]


# --- restJson1 ser/de ---
def serialize_json(value: EndpointEncryptionSecretType) -> str:
    return value


def deserialize_json(data: str) -> EndpointEncryptionSecretType:
    return cast(EndpointEncryptionSecretType, data)
