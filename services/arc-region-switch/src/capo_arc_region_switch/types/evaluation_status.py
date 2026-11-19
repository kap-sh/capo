"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#EvaluationStatus``."""

from typing import Literal, TypeAlias, cast

EvaluationStatus: TypeAlias = Literal[
    "passed",
    "actionRequired",
    "pendingEvaluation",
    "unknown",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EvaluationStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> EvaluationStatus:
    return cast(EvaluationStatus, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: EvaluationStatus) -> str:
    return value


def deserialize_cbor(data: str) -> EvaluationStatus:
    return cast(EvaluationStatus, data)
