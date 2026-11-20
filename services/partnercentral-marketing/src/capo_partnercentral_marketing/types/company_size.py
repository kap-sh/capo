"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#CompanySize``."""

from typing import Literal, TypeAlias, cast

"""CompanySize shape."""
CompanySize: TypeAlias = Literal[
    "STARTUP",
    "SMALL_BUSINESS",
    "MID_MARKET",
    "ENTERPRISE",
    "GLOBAL_ENTERPRISE",
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CompanySize) -> str:
    return value


def deserialize_cbor(data: str) -> CompanySize:
    return cast(CompanySize, data)
