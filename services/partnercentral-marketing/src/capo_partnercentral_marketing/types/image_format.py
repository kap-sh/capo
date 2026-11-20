"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#ImageFormat``."""

from typing import Literal, TypeAlias, cast

"""An accepted image format."""
ImageFormat: TypeAlias = Literal[
    "PNG",
    "JPEG",
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ImageFormat) -> str:
    return value


def deserialize_cbor(data: str) -> ImageFormat:
    return cast(ImageFormat, data)
