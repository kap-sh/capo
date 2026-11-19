"""Generated from Smithy shape ``com.amazonaws.gamelift#PlayerGatewayStatus``."""

from typing import Literal, TypeAlias, cast

PlayerGatewayStatus: TypeAlias = Literal[
    "DISABLED",
    "ENABLED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PlayerGatewayStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PlayerGatewayStatus:
    return cast(PlayerGatewayStatus, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PlayerGatewayStatus) -> str:
    return value


def deserialize_cbor(data: str) -> PlayerGatewayStatus:
    return cast(PlayerGatewayStatus, data)
