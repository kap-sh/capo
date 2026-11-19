"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#InstanceRecommendationFindingReasonCode``."""

from typing import Literal, TypeAlias, cast

InstanceRecommendationFindingReasonCode: TypeAlias = Literal[
    "CPUOverprovisioned",
    "CPUUnderprovisioned",
    "MemoryOverprovisioned",
    "MemoryUnderprovisioned",
    "EBSThroughputOverprovisioned",
    "EBSThroughputUnderprovisioned",
    "EBSIOPSOverprovisioned",
    "EBSIOPSUnderprovisioned",
    "NetworkBandwidthOverprovisioned",
    "NetworkBandwidthUnderprovisioned",
    "NetworkPPSOverprovisioned",
    "NetworkPPSUnderprovisioned",
    "DiskIOPSOverprovisioned",
    "DiskIOPSUnderprovisioned",
    "DiskThroughputOverprovisioned",
    "DiskThroughputUnderprovisioned",
    "GPUUnderprovisioned",
    "GPUOverprovisioned",
    "GPUMemoryUnderprovisioned",
    "GPUMemoryOverprovisioned",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InstanceRecommendationFindingReasonCode) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> InstanceRecommendationFindingReasonCode:
    return cast(InstanceRecommendationFindingReasonCode, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: InstanceRecommendationFindingReasonCode) -> str:
    return value


def deserialize_cbor(data: str) -> InstanceRecommendationFindingReasonCode:
    return cast(InstanceRecommendationFindingReasonCode, data)
