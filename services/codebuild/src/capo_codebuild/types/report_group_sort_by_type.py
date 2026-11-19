"""Generated from Smithy shape ``com.amazonaws.codebuild#ReportGroupSortByType``."""

from typing import Literal, TypeAlias, cast

ReportGroupSortByType: TypeAlias = Literal[
    "NAME",
    "CREATED_TIME",
    "LAST_MODIFIED_TIME",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReportGroupSortByType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ReportGroupSortByType:
    return cast(ReportGroupSortByType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ReportGroupSortByType) -> str:
    return value


def deserialize_cbor(data: str) -> ReportGroupSortByType:
    return cast(ReportGroupSortByType, data)
