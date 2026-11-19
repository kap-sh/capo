"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#RDSSavingsEstimationModeSource``."""

from typing import Literal, TypeAlias, cast

RDSSavingsEstimationModeSource: TypeAlias = Literal[
    "PublicPricing",
    "CostExplorerRightsizing",
    "CostOptimizationHub",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RDSSavingsEstimationModeSource) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> RDSSavingsEstimationModeSource:
    return cast(RDSSavingsEstimationModeSource, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RDSSavingsEstimationModeSource) -> str:
    return value


def deserialize_cbor(data: str) -> RDSSavingsEstimationModeSource:
    return cast(RDSSavingsEstimationModeSource, data)
