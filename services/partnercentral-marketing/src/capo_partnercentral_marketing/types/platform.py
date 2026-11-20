"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#Platform``."""

from typing import Literal, TypeAlias, cast

"""Social platform a connection authorizes publishing on."""
Platform: TypeAlias = Literal[
    "FACEBOOK",
    "LINKEDIN",
    "X",
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Platform) -> str:
    return value


def deserialize_cbor(data: str) -> Platform:
    return cast(Platform, data)
