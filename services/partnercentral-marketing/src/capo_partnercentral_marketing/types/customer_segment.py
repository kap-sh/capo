"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#CustomerSegment``."""

from typing import Literal, TypeAlias, cast

"""The customer segment a campaign template is written for. Clients must tolerate values added later."""
CustomerSegment: TypeAlias = Literal[
    "ENTERPRISE",
    "SMB",
    "PUBLIC_SECTOR",
    "ISV",
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CustomerSegment) -> str:
    return value


def deserialize_cbor(data: str) -> CustomerSegment:
    return cast(CustomerSegment, data)
