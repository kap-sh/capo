"""Generated from Smithy shape ``com.amazonaws.codebuild#FleetSortByType``."""

from typing import Literal, TypeAlias, cast

FleetSortByType: TypeAlias = Literal[
    "NAME",
    "CREATED_TIME",
    "LAST_MODIFIED_TIME",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FleetSortByType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FleetSortByType:
    return cast(FleetSortByType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: FleetSortByType) -> str:
    return value


def deserialize_cbor(data: str) -> FleetSortByType:
    return cast(FleetSortByType, data)
