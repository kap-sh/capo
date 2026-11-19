"""Generated from Smithy shape ``com.amazonaws.appstream#UsageReportExecutionErrorCode``."""

from typing import Literal, TypeAlias, cast

UsageReportExecutionErrorCode: TypeAlias = Literal[
    "RESOURCE_NOT_FOUND",
    "ACCESS_DENIED",
    "INTERNAL_SERVICE_ERROR",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UsageReportExecutionErrorCode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> UsageReportExecutionErrorCode:
    return cast(UsageReportExecutionErrorCode, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: UsageReportExecutionErrorCode) -> str:
    return value


def deserialize_cbor(data: str) -> UsageReportExecutionErrorCode:
    return cast(UsageReportExecutionErrorCode, data)
