"""Generated from Smithy shape ``com.amazonaws.codebuild#ReportStatusType``."""

from typing import Literal, TypeAlias, cast

ReportStatusType: TypeAlias = Literal[
    "GENERATING",
    "SUCCEEDED",
    "FAILED",
    "INCOMPLETE",
    "DELETING",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReportStatusType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ReportStatusType:
    return cast(ReportStatusType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ReportStatusType) -> str:
    return value


def deserialize_cbor(data: str) -> ReportStatusType:
    return cast(ReportStatusType, data)
