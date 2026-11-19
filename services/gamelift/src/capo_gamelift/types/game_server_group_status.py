"""Generated from Smithy shape ``com.amazonaws.gamelift#GameServerGroupStatus``."""

from typing import Literal, TypeAlias, cast

GameServerGroupStatus: TypeAlias = Literal[
    "NEW",
    "ACTIVATING",
    "ACTIVE",
    "DELETE_SCHEDULED",
    "DELETING",
    "DELETED",
    "ERROR",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GameServerGroupStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> GameServerGroupStatus:
    return cast(GameServerGroupStatus, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GameServerGroupStatus) -> str:
    return value


def deserialize_cbor(data: str) -> GameServerGroupStatus:
    return cast(GameServerGroupStatus, data)
