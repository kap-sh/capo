"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#RDSCurrentInstancePerformanceRisk``."""

from typing import Literal, TypeAlias, cast

RDSCurrentInstancePerformanceRisk: TypeAlias = Literal[
    "VeryLow",
    "Low",
    "Medium",
    "High",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RDSCurrentInstancePerformanceRisk) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> RDSCurrentInstancePerformanceRisk:
    return cast(RDSCurrentInstancePerformanceRisk, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RDSCurrentInstancePerformanceRisk) -> str:
    return value


def deserialize_cbor(data: str) -> RDSCurrentInstancePerformanceRisk:
    return cast(RDSCurrentInstancePerformanceRisk, data)
