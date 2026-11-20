"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#SendMode``."""

from typing import Literal, TypeAlias, cast

"""When a sendable asset (`EMAIL`, `SOCIAL_POST`) sends. See `UpdateCampaignAssetRequest$SendMode`."""
SendMode: TypeAlias = Literal[
    "ON_ACTIVATION",
    "SCHEDULED",
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: SendMode) -> str:
    return value


def deserialize_cbor(data: str) -> SendMode:
    return cast(SendMode, data)
