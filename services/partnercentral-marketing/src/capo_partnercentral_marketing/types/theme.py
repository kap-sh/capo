"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#Theme``."""

from typing import Literal, TypeAlias, cast

"""The marketing theme of a campaign template. Clients must tolerate values added later."""
Theme: TypeAlias = Literal[
    "AI",
    "MIGRATION_MODERNIZATION",
    "SECURITY",
    "DATA_ANALYTICS",
    "AWS_TRAINING_CERTIFICATION",
    "AWS_MARKETPLACE",
    "CONNECT",
    "EVENTS",
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Theme) -> str:
    return value


def deserialize_cbor(data: str) -> Theme:
    return cast(Theme, data)
