"""Generated from Smithy shape ``com.amazonaws.directoryservice#RegionType``."""

from typing import Literal, TypeAlias, cast

RegionType: TypeAlias = Literal[
    "Primary",
    "Additional",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RegionType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RegionType:
    return cast(RegionType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RegionType) -> str:
    return value


def deserialize_cbor(data: str) -> RegionType:
    return cast(RegionType, data)
