"""Generated from Smithy shape ``com.amazonaws.networkmanager#ConnectPeerErrorCode``."""

from typing import Literal, TypeAlias, cast

ConnectPeerErrorCode: TypeAlias = Literal[
    "EDGE_LOCATION_NO_FREE_IPS",
    "EDGE_LOCATION_PEER_DUPLICATE",
    "SUBNET_NOT_FOUND",
    "IP_OUTSIDE_SUBNET_CIDR_RANGE",
    "INVALID_INSIDE_CIDR_BLOCK",
    "NO_ASSOCIATED_CIDR_BLOCK",
    "CREATION_FAILED",
    "DELETION_FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ConnectPeerErrorCode) -> str:
    return value


def deserialize_json(data: str) -> ConnectPeerErrorCode:
    return cast(ConnectPeerErrorCode, data)
