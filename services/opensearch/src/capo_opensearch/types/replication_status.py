"""Generated from Smithy shape ``com.amazonaws.opensearch#ReplicationStatus``."""

from typing import Literal, TypeAlias, cast

ReplicationStatus: TypeAlias = Literal[
    "PENDING_SETUP",
    "ACTIVE",
    "SWITCHING_OVER",
    "FAILING_OVER",
    "PENDING_REMOVAL",
    "DETACHED",
    "EJECTED",
    "FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ReplicationStatus) -> str:
    return value


def deserialize_json(data: str) -> ReplicationStatus:
    return cast(ReplicationStatus, data)
