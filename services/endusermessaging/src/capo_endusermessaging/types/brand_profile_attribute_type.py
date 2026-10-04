"""Generated from Smithy shape ``com.amazonaws.endusermessaging#BrandProfileAttributeType``."""

from typing import Literal, TypeAlias, cast

"""Type of brand profile attribute. Drives whether a value is inline (TEXT) or referenced via a presigned media upload URL."""
BrandProfileAttributeType: TypeAlias = Literal[
    "TEXT",
    "IMAGE",
    "DOCUMENT",
]


# --- restJson1 ser/de ---
def serialize_json(value: BrandProfileAttributeType) -> str:
    return value


def deserialize_json(data: str) -> BrandProfileAttributeType:
    return cast(BrandProfileAttributeType, data)
