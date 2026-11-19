"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#FailedReportErrorCode``."""

from typing import Literal, TypeAlias, cast

FailedReportErrorCode: TypeAlias = Literal[
    "insufficientPermissions",
    "invalidResource",
    "configurationError",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: FailedReportErrorCode) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> FailedReportErrorCode:
    return cast(FailedReportErrorCode, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: FailedReportErrorCode) -> str:
    return value


def deserialize_cbor(data: str) -> FailedReportErrorCode:
    return cast(FailedReportErrorCode, data)
