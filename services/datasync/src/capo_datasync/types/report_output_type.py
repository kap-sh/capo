"""Generated from Smithy shape ``com.amazonaws.datasync#ReportOutputType``."""

from typing import Literal, TypeAlias, cast

ReportOutputType: TypeAlias = Literal[
    "SUMMARY_ONLY",
    "STANDARD",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReportOutputType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ReportOutputType:
    return cast(ReportOutputType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ReportOutputType) -> str:
    return value


def deserialize_cbor(data: str) -> ReportOutputType:
    return cast(ReportOutputType, data)
