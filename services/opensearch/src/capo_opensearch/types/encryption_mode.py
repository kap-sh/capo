"""Generated from Smithy shape ``com.amazonaws.opensearch#EncryptionMode``."""

from typing import Literal, TypeAlias, cast

"""<p>The type of encryption at rest applied to a domain's data: <code>DISK</code> for volume-level encryption or <code>NATIVE</code> for engine-native, index-level encryption.</p>"""
EncryptionMode: TypeAlias = Literal[
    "DISK",
    "NATIVE",
]


# --- restJson1 ser/de ---
def serialize_json(value: EncryptionMode) -> str:
    return value


def deserialize_json(data: str) -> EncryptionMode:
    return cast(EncryptionMode, data)
