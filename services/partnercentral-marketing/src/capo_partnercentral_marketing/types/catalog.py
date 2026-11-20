"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#Catalog``."""

from typing import Literal, TypeAlias, cast

"""Catalog shape."""
Catalog: TypeAlias = Literal[
    "AWS",
    "Sandbox",
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Catalog) -> str:
    return value


def deserialize_cbor(data: str) -> Catalog:
    return cast(Catalog, data)
