"""Generated from Smithy shape ``com.amazonaws.gamelift#GameServerIpProtocolSupported``."""

from typing import Literal, TypeAlias, cast

GameServerIpProtocolSupported: TypeAlias = Literal[
    "IPv4",
    "DUAL_STACK",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GameServerIpProtocolSupported) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> GameServerIpProtocolSupported:
    return cast(GameServerIpProtocolSupported, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GameServerIpProtocolSupported) -> str:
    return value


def deserialize_cbor(data: str) -> GameServerIpProtocolSupported:
    return cast(GameServerIpProtocolSupported, data)
