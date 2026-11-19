"""Generated from Smithy shape ``com.amazonaws.datasync#LocationFilterName``."""

from typing import Literal, TypeAlias, cast

LocationFilterName: TypeAlias = Literal[
    "LocationUri",
    "LocationType",
    "CreationTime",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LocationFilterName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> LocationFilterName:
    return cast(LocationFilterName, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: LocationFilterName) -> str:
    return value


def deserialize_cbor(data: str) -> LocationFilterName:
    return cast(LocationFilterName, data)
