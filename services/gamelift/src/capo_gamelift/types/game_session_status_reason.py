"""Generated from Smithy shape ``com.amazonaws.gamelift#GameSessionStatusReason``."""

from typing import Literal, TypeAlias, cast

GameSessionStatusReason: TypeAlias = Literal[
    "INTERRUPTED",
    "TRIGGERED_ON_PROCESS_TERMINATE",
    "FORCE_TERMINATED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GameSessionStatusReason) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> GameSessionStatusReason:
    return cast(GameSessionStatusReason, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GameSessionStatusReason) -> str:
    return value


def deserialize_cbor(data: str) -> GameSessionStatusReason:
    return cast(GameSessionStatusReason, data)
