"""Generated from Smithy shape ``com.amazonaws.codebuild#ReportCodeCoverageSortByType``."""

from typing import Literal, TypeAlias, cast

ReportCodeCoverageSortByType: TypeAlias = Literal[
    "LINE_COVERAGE_PERCENTAGE",
    "FILE_PATH",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReportCodeCoverageSortByType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ReportCodeCoverageSortByType:
    return cast(ReportCodeCoverageSortByType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ReportCodeCoverageSortByType) -> str:
    return value


def deserialize_cbor(data: str) -> ReportCodeCoverageSortByType:
    return cast(ReportCodeCoverageSortByType, data)
