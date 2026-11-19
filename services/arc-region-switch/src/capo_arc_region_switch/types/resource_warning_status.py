"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#ResourceWarningStatus``."""

from typing import Literal, TypeAlias, cast

ResourceWarningStatus: TypeAlias = Literal[
    "active",
    "resolved",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ResourceWarningStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ResourceWarningStatus:
    return cast(ResourceWarningStatus, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ResourceWarningStatus) -> str:
    return value


def deserialize_cbor(data: str) -> ResourceWarningStatus:
    return cast(ResourceWarningStatus, data)
