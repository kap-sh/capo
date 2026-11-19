"""Generated from Smithy shape ``com.amazonaws.networkfirewall#ListenerPropertyType``."""

from typing import Literal, TypeAlias, cast

ListenerPropertyType: TypeAlias = Literal[
    "HTTP",
    "HTTPS",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListenerPropertyType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ListenerPropertyType:
    return cast(ListenerPropertyType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListenerPropertyType) -> str:
    return value


def deserialize_cbor(data: str) -> ListenerPropertyType:
    return cast(ListenerPropertyType, data)
