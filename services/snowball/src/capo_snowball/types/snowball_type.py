"""Generated from Smithy shape ``com.amazonaws.snowball#SnowballType``."""

from typing import Literal, TypeAlias, cast

SnowballType: TypeAlias = Literal[
    "STANDARD",
    "EDGE",
    "EDGE_C",
    "EDGE_CG",
    "EDGE_S",
    "SNC1_HDD",
    "SNC1_SSD",
    "V3_5C",
    "V3_5S",
    "RACK_5U_C",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SnowballType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SnowballType:
    return cast(SnowballType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: SnowballType) -> str:
    return value


def deserialize_cbor(data: str) -> SnowballType:
    return cast(SnowballType, data)
