"""Generated from Smithy shape ``com.amazonaws.appstream#PreferredProtocol``."""

from typing import Literal, TypeAlias, cast

PreferredProtocol: TypeAlias = Literal[
    "TCP",
    "UDP",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PreferredProtocol) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PreferredProtocol:
    return cast(PreferredProtocol, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PreferredProtocol) -> str:
    return value


def deserialize_cbor(data: str) -> PreferredProtocol:
    return cast(PreferredProtocol, data)
