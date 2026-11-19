"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#RDSEstimatedMonthlyVolumeIOPsCostVariation``."""

from typing import Literal, TypeAlias, cast

RDSEstimatedMonthlyVolumeIOPsCostVariation: TypeAlias = Literal[
    "None",
    "Low",
    "Medium",
    "High",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RDSEstimatedMonthlyVolumeIOPsCostVariation) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> RDSEstimatedMonthlyVolumeIOPsCostVariation:
    return cast(RDSEstimatedMonthlyVolumeIOPsCostVariation, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RDSEstimatedMonthlyVolumeIOPsCostVariation) -> str:
    return value


def deserialize_cbor(data: str) -> RDSEstimatedMonthlyVolumeIOPsCostVariation:
    return cast(RDSEstimatedMonthlyVolumeIOPsCostVariation, data)
