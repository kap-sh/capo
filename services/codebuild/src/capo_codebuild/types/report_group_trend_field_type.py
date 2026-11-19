"""Generated from Smithy shape ``com.amazonaws.codebuild#ReportGroupTrendFieldType``."""

from typing import Literal, TypeAlias, cast

ReportGroupTrendFieldType: TypeAlias = Literal[
    "PASS_RATE",
    "DURATION",
    "TOTAL",
    "LINE_COVERAGE",
    "LINES_COVERED",
    "LINES_MISSED",
    "BRANCH_COVERAGE",
    "BRANCHES_COVERED",
    "BRANCHES_MISSED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReportGroupTrendFieldType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ReportGroupTrendFieldType:
    return cast(ReportGroupTrendFieldType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ReportGroupTrendFieldType) -> str:
    return value


def deserialize_cbor(data: str) -> ReportGroupTrendFieldType:
    return cast(ReportGroupTrendFieldType, data)
