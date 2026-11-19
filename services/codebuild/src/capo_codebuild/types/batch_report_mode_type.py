"""Generated from Smithy shape ``com.amazonaws.codebuild#BatchReportModeType``."""

from typing import Literal, TypeAlias, cast

BatchReportModeType: TypeAlias = Literal[
    "REPORT_INDIVIDUAL_BUILDS",
    "REPORT_AGGREGATED_BATCH",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchReportModeType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> BatchReportModeType:
    return cast(BatchReportModeType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: BatchReportModeType) -> str:
    return value


def deserialize_cbor(data: str) -> BatchReportModeType:
    return cast(BatchReportModeType, data)
