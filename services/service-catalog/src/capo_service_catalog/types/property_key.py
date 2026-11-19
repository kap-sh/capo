"""Generated from Smithy shape ``com.amazonaws.servicecatalog#PropertyKey``."""

from typing import Literal, TypeAlias, cast

PropertyKey: TypeAlias = Literal[
    "OWNER",
    "LAUNCH_ROLE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PropertyKey) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PropertyKey:
    return cast(PropertyKey, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PropertyKey) -> str:
    return value


def deserialize_cbor(data: str) -> PropertyKey:
    return cast(PropertyKey, data)
