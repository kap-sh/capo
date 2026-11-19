"""Generated from Smithy shape ``com.amazonaws.gamelift#FilterInstanceStatus``."""

from typing import Literal, TypeAlias, cast

FilterInstanceStatus: TypeAlias = Literal[
    "ACTIVE",
    "DRAINING",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FilterInstanceStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FilterInstanceStatus:
    return cast(FilterInstanceStatus, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: FilterInstanceStatus) -> str:
    return value


def deserialize_cbor(data: str) -> FilterInstanceStatus:
    return cast(FilterInstanceStatus, data)
