"""Generated from Smithy shape ``com.amazonaws.networkmanager#PeeringErrorCode``."""

from typing import Literal, TypeAlias, cast

PeeringErrorCode: TypeAlias = Literal[
    "TRANSIT_GATEWAY_NOT_FOUND",
    "TRANSIT_GATEWAY_PEERS_LIMIT_EXCEEDED",
    "MISSING_PERMISSIONS",
    "INTERNAL_ERROR",
    "EDGE_LOCATION_PEER_DUPLICATE",
    "INVALID_TRANSIT_GATEWAY_STATE",
    "TRANSIT_GATEWAY_ENCRYPTION_NOT_SUPPORTED",
    "CREATION_FAILED",
    "DELETION_FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: PeeringErrorCode) -> str:
    return value


def deserialize_json(data: str) -> PeeringErrorCode:
    return cast(PeeringErrorCode, data)
