"""Generated from Smithy shape ``com.amazonaws.gamelift#GameServerHealthCheck``."""

from typing import Literal, TypeAlias, cast

GameServerHealthCheck: TypeAlias = Literal["HEALTHY",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GameServerHealthCheck) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> GameServerHealthCheck:
    return cast(GameServerHealthCheck, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GameServerHealthCheck) -> str:
    return value


def deserialize_cbor(data: str) -> GameServerHealthCheck:
    return cast(GameServerHealthCheck, data)
