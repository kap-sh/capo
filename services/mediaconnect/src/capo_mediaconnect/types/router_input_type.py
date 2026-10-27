"""Generated from Smithy shape ``com.amazonaws.mediaconnect#RouterInputType``."""

from typing import Literal, TypeAlias, cast

RouterInputType: TypeAlias = Literal[
    "STANDARD",
    "FAILOVER",
    "MERGE",
    "MEDIACONNECT_FLOW",
    "MEDIALIVE_CHANNEL",
    "DESTINATION_ENDPOINT",
]


# --- restJson1 ser/de ---
def serialize_json(value: RouterInputType) -> str:
    return value


def deserialize_json(data: str) -> RouterInputType:
    return cast(RouterInputType, data)
