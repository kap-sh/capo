"""Generated from Smithy shape ``com.amazonaws.gamelift#GameSessionStatus``."""

from typing import Literal, TypeAlias, cast

GameSessionStatus: TypeAlias = Literal[
    "ACTIVE",
    "ACTIVATING",
    "TERMINATED",
    "TERMINATING",
    "ERROR",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GameSessionStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> GameSessionStatus:
    return cast(GameSessionStatus, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GameSessionStatus) -> str:
    return value


def deserialize_cbor(data: str) -> GameSessionStatus:
    return cast(GameSessionStatus, data)
