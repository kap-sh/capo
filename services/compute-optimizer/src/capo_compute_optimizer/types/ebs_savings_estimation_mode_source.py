"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#EBSSavingsEstimationModeSource``."""

from typing import Literal, TypeAlias, cast

EBSSavingsEstimationModeSource: TypeAlias = Literal[
    "PublicPricing",
    "CostExplorerRightsizing",
    "CostOptimizationHub",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EBSSavingsEstimationModeSource) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> EBSSavingsEstimationModeSource:
    return cast(EBSSavingsEstimationModeSource, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: EBSSavingsEstimationModeSource) -> str:
    return value


def deserialize_cbor(data: str) -> EBSSavingsEstimationModeSource:
    return cast(EBSSavingsEstimationModeSource, data)
