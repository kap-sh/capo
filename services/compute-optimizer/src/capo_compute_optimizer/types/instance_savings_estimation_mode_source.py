"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#InstanceSavingsEstimationModeSource``."""

from typing import Literal, TypeAlias, cast

InstanceSavingsEstimationModeSource: TypeAlias = Literal[
    "PublicPricing",
    "CostExplorerRightsizing",
    "CostOptimizationHub",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InstanceSavingsEstimationModeSource) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> InstanceSavingsEstimationModeSource:
    return cast(InstanceSavingsEstimationModeSource, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: InstanceSavingsEstimationModeSource) -> str:
    return value


def deserialize_cbor(data: str) -> InstanceSavingsEstimationModeSource:
    return cast(InstanceSavingsEstimationModeSource, data)
