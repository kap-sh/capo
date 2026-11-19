"""Generated from Smithy shape ``com.amazonaws.gamelift#GameServerInstanceStatus``."""

from typing import Literal, TypeAlias, cast

GameServerInstanceStatus: TypeAlias = Literal[
    "ACTIVE",
    "DRAINING",
    "SPOT_TERMINATING",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GameServerInstanceStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> GameServerInstanceStatus:
    return cast(GameServerInstanceStatus, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GameServerInstanceStatus) -> str:
    return value


def deserialize_cbor(data: str) -> GameServerInstanceStatus:
    return cast(GameServerInstanceStatus, data)
