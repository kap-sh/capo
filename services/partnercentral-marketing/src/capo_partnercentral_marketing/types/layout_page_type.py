"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#LayoutPageType``."""

from typing import Literal, TypeAlias, cast

"""Which page of a multi-page layout a preview serves."""
LayoutPageType: TypeAlias = Literal[
    "FORM",
    "CONFIRMATION",
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: LayoutPageType) -> str:
    return value


def deserialize_cbor(data: str) -> LayoutPageType:
    return cast(LayoutPageType, data)
