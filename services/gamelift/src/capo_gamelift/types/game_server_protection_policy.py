"""Generated from Smithy shape ``com.amazonaws.gamelift#GameServerProtectionPolicy``."""

from typing import Literal, TypeAlias, cast

GameServerProtectionPolicy: TypeAlias = Literal[
    "NO_PROTECTION",
    "FULL_PROTECTION",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GameServerProtectionPolicy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> GameServerProtectionPolicy:
    return cast(GameServerProtectionPolicy, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GameServerProtectionPolicy) -> str:
    return value


def deserialize_cbor(data: str) -> GameServerProtectionPolicy:
    return cast(GameServerProtectionPolicy, data)
