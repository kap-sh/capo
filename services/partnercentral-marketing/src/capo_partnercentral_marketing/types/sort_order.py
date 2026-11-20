"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#SortOrder``."""

from typing import Literal, TypeAlias, cast

"""A sort direction."""
SortOrder: TypeAlias = Literal[
    "ASCENDING",
    "DESCENDING",
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: SortOrder) -> str:
    return value


def deserialize_cbor(data: str) -> SortOrder:
    return cast(SortOrder, data)
