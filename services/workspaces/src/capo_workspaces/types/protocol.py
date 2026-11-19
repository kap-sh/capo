"""Generated from Smithy shape ``com.amazonaws.workspaces#Protocol``."""

from typing import Literal, TypeAlias, cast

Protocol: TypeAlias = Literal[
    "PCOIP",
    "WSP",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Protocol) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Protocol:
    return cast(Protocol, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Protocol) -> str:
    return value


def deserialize_cbor(data: str) -> Protocol:
    return cast(Protocol, data)
