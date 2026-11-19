"""Generated from Smithy shape ``com.amazonaws.gamelift#GameSessionPlacementState``."""

from typing import Literal, TypeAlias, cast

GameSessionPlacementState: TypeAlias = Literal[
    "PENDING",
    "FULFILLED",
    "CANCELLED",
    "TIMED_OUT",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GameSessionPlacementState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> GameSessionPlacementState:
    return cast(GameSessionPlacementState, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GameSessionPlacementState) -> str:
    return value


def deserialize_cbor(data: str) -> GameSessionPlacementState:
    return cast(GameSessionPlacementState, data)
