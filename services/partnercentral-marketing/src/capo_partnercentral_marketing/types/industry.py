"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#Industry``."""

from typing import Literal, TypeAlias, cast

"""Industry shape."""
Industry: TypeAlias = Literal[
    "FINANCIAL_SERVICES",
    "HEALTHCARE",
    "MANUFACTURING",
    "RETAIL",
    "MEDIA_ENTERTAINMENT",
    "ENERGY",
    "EDUCATION",
    "GOVERNMENT",
    "TELECOMMUNICATIONS",
    "AUTOMOTIVE",
    "INSURANCE",
    "OTHER",
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Industry) -> str:
    return value


def deserialize_cbor(data: str) -> Industry:
    return cast(Industry, data)
