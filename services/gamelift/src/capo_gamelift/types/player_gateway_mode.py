"""Generated from Smithy shape ``com.amazonaws.gamelift#PlayerGatewayMode``."""

from typing import Literal, TypeAlias, cast

PlayerGatewayMode: TypeAlias = Literal[
    "DISABLED",
    "ENABLED",
    "REQUIRED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PlayerGatewayMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PlayerGatewayMode:
    return cast(PlayerGatewayMode, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PlayerGatewayMode) -> str:
    return value


def deserialize_cbor(data: str) -> PlayerGatewayMode:
    return cast(PlayerGatewayMode, data)
