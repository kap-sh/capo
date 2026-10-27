"""Generated from Smithy shape ``com.amazonaws.mediaconnect#EndpointEncryptionType``."""

from typing import Literal, TypeAlias, cast

EndpointEncryptionType: TypeAlias = Literal[
    "SECRETS_MANAGER",
    "AUTOMATIC",
]


# --- restJson1 ser/de ---
def serialize_json(value: EndpointEncryptionType) -> str:
    return value


def deserialize_json(data: str) -> EndpointEncryptionType:
    return cast(EndpointEncryptionType, data)
