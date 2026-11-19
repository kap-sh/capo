"""Generated from Smithy shape ``com.amazonaws.codebuild#ReportType``."""

from typing import Literal, TypeAlias, cast

ReportType: TypeAlias = Literal[
    "TEST",
    "CODE_COVERAGE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReportType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ReportType:
    return cast(ReportType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ReportType) -> str:
    return value


def deserialize_cbor(data: str) -> ReportType:
    return cast(ReportType, data)
