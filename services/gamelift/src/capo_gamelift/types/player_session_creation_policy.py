"""Generated from Smithy shape ``com.amazonaws.gamelift#PlayerSessionCreationPolicy``."""

from typing import Literal, TypeAlias, cast

PlayerSessionCreationPolicy: TypeAlias = Literal[
    "ACCEPT_ALL",
    "DENY_ALL",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PlayerSessionCreationPolicy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PlayerSessionCreationPolicy:
    return cast(PlayerSessionCreationPolicy, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PlayerSessionCreationPolicy) -> str:
    return value


def deserialize_cbor(data: str) -> PlayerSessionCreationPolicy:
    return cast(PlayerSessionCreationPolicy, data)
