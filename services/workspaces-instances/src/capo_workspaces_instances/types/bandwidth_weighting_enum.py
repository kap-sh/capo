"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#BandwidthWeightingEnum``."""

from typing import Literal, TypeAlias, cast

BandwidthWeightingEnum: TypeAlias = Literal[
    "default",
    "vpc-1",
    "ebs-1",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BandwidthWeightingEnum) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> BandwidthWeightingEnum:
    return cast(BandwidthWeightingEnum, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: BandwidthWeightingEnum) -> str:
    return value


def deserialize_cbor(data: str) -> BandwidthWeightingEnum:
    return cast(BandwidthWeightingEnum, data)
