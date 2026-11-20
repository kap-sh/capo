"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#LayoutFormat``."""

from typing import Literal, TypeAlias, cast

"""The format of a layout preview."""
LayoutFormat: TypeAlias = Literal[
    "HTML",
    "PDF",
    "IMAGE",
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: LayoutFormat) -> str:
    return value


def deserialize_cbor(data: str) -> LayoutFormat:
    return cast(LayoutFormat, data)
