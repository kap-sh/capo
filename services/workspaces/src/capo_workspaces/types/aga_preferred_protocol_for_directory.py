"""Generated from Smithy shape ``com.amazonaws.workspaces#AGAPreferredProtocolForDirectory``."""

from typing import Literal, TypeAlias, cast

AGAPreferredProtocolForDirectory: TypeAlias = Literal[
    "TCP",
    "NONE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AGAPreferredProtocolForDirectory) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AGAPreferredProtocolForDirectory:
    return cast(AGAPreferredProtocolForDirectory, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AGAPreferredProtocolForDirectory) -> str:
    return value


def deserialize_cbor(data: str) -> AGAPreferredProtocolForDirectory:
    return cast(AGAPreferredProtocolForDirectory, data)
