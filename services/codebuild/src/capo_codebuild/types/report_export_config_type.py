"""Generated from Smithy shape ``com.amazonaws.codebuild#ReportExportConfigType``."""

from typing import Literal, TypeAlias, cast

ReportExportConfigType: TypeAlias = Literal[
    "S3",
    "NO_EXPORT",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReportExportConfigType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ReportExportConfigType:
    return cast(ReportExportConfigType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ReportExportConfigType) -> str:
    return value


def deserialize_cbor(data: str) -> ReportExportConfigType:
    return cast(ReportExportConfigType, data)
