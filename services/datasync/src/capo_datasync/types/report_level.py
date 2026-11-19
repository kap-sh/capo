"""Generated from Smithy shape ``com.amazonaws.datasync#ReportLevel``."""

from typing import Literal, TypeAlias, cast

ReportLevel: TypeAlias = Literal[
    "ERRORS_ONLY",
    "SUCCESSES_AND_ERRORS",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReportLevel) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ReportLevel:
    return cast(ReportLevel, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ReportLevel) -> str:
    return value


def deserialize_cbor(data: str) -> ReportLevel:
    return cast(ReportLevel, data)
