"""Generated from Smithy shape ``com.amazonaws.fms#DestinationType``."""

from typing import Literal, TypeAlias, cast

DestinationType: TypeAlias = Literal[
    "IPV4",
    "IPV6",
    "PREFIX_LIST",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DestinationType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DestinationType:
    return cast(DestinationType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DestinationType) -> str:
    return value


def deserialize_cbor(data: str) -> DestinationType:
    return cast(DestinationType, data)
