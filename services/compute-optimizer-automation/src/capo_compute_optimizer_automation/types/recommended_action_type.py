"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#RecommendedActionType``."""

from typing import Literal, TypeAlias, cast

"""Recommended action type enumeration"""
RecommendedActionType: TypeAlias = Literal[
    "SnapshotAndDeleteUnattachedEbsVolume",
    "UpgradeEbsVolumeType",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RecommendedActionType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> RecommendedActionType:
    return cast(RecommendedActionType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RecommendedActionType) -> str:
    return value


def deserialize_cbor(data: str) -> RecommendedActionType:
    return cast(RecommendedActionType, data)
