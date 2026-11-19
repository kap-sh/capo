"""Generated from Smithy shape ``com.amazonaws.workspaces#AGAPreferredProtocolForWorkSpace``."""

from typing import Literal, TypeAlias, cast

AGAPreferredProtocolForWorkSpace: TypeAlias = Literal[
    "TCP",
    "NONE",
    "INHERITED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AGAPreferredProtocolForWorkSpace) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AGAPreferredProtocolForWorkSpace:
    return cast(AGAPreferredProtocolForWorkSpace, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AGAPreferredProtocolForWorkSpace) -> str:
    return value


def deserialize_cbor(data: str) -> AGAPreferredProtocolForWorkSpace:
    return cast(AGAPreferredProtocolForWorkSpace, data)
