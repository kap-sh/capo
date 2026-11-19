"""Generated from Smithy shape ``com.amazonaws.gamelift#LocationFilter``."""

from typing import Literal, TypeAlias, cast

LocationFilter: TypeAlias = Literal[
    "AWS",
    "CUSTOM",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LocationFilter) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> LocationFilter:
    return cast(LocationFilter, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: LocationFilter) -> str:
    return value


def deserialize_cbor(data: str) -> LocationFilter:
    return cast(LocationFilter, data)
