"""Generated from Smithy shape ``com.amazonaws.codebuild#ReportPackagingType``."""

from typing import Literal, TypeAlias, cast

ReportPackagingType: TypeAlias = Literal[
    "ZIP",
    "NONE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReportPackagingType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ReportPackagingType:
    return cast(ReportPackagingType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ReportPackagingType) -> str:
    return value


def deserialize_cbor(data: str) -> ReportPackagingType:
    return cast(ReportPackagingType, data)
