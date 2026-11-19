"""Generated from Smithy shape ``com.amazonaws.codebuild#ReportGroupStatusType``."""

from typing import Literal, TypeAlias, cast

ReportGroupStatusType: TypeAlias = Literal[
    "ACTIVE",
    "DELETING",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReportGroupStatusType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ReportGroupStatusType:
    return cast(ReportGroupStatusType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ReportGroupStatusType) -> str:
    return value


def deserialize_cbor(data: str) -> ReportGroupStatusType:
    return cast(ReportGroupStatusType, data)
