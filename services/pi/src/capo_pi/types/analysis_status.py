"""Generated from Smithy shape ``com.amazonaws.pi#AnalysisStatus``."""

from typing import Literal, TypeAlias, cast

AnalysisStatus: TypeAlias = Literal[
    "RUNNING",
    "SUCCEEDED",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AnalysisStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AnalysisStatus:
    return cast(AnalysisStatus, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AnalysisStatus) -> str:
    return value


def deserialize_cbor(data: str) -> AnalysisStatus:
    return cast(AnalysisStatus, data)
